from __future__ import annotations

import argparse
import csv
import json
import re
from dataclasses import dataclass, field
from pathlib import Path

SAFE_NAME_PATTERN = re.compile(r"^[A-Za-z0-9_-]+$")


@dataclass
class ValidationIssue:
    level: str
    message: str


@dataclass
class ValidationResult:
    script_count: int = 0
    image_count: int = 0
    video_count: int = 0
    issues: list[ValidationIssue] = field(default_factory=list)

    @property
    def errors(self) -> list[ValidationIssue]:
        return [issue for issue in self.issues if issue.level == "ERROR"]

    @property
    def warnings(self) -> list[ValidationIssue]:
        return [issue for issue in self.issues if issue.level == "WARN"]

    @property
    def passed(self) -> bool:
        return not self.errors

    def add_error(self, message: str) -> None:
        self.issues.append(ValidationIssue("ERROR", message))

    def add_warning(self, message: str) -> None:
        self.issues.append(ValidationIssue("WARN", message))


def repo_root() -> Path:
    return Path(__file__).resolve().parents[2]


def validate_safe_name(value: str, label: str) -> str:
    if not value or not SAFE_NAME_PATTERN.fullmatch(value):
        raise ValueError(f"{label} invalid: use only letters/digits/_/-")
    if ".." in value or "/" in value or "\\" in value:
        raise ValueError(f"{label} must not contain path segments")
    return value


def video_dir(channel: str, video: str) -> Path:
    safe_channel = validate_safe_name(channel, "channel")
    safe_video = validate_safe_name(video, "video")
    root = repo_root()
    target = (root / "channels" / safe_channel / "videos" / safe_video).resolve()
    videos_root = (root / "channels" / safe_channel / "videos").resolve()
    try:
        target.relative_to(videos_root)
    except ValueError as exc:
        raise ValueError("Video path escapes repository") from exc
    return target


def read_json(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as file:
        return json.load(file)


def read_csv_rows(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as file:
        return list(csv.DictReader(file))


def write_csv_rows(path: Path, fieldnames: list[str], rows: list[dict[str, str]]) -> None:
    with path.open("w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames, quoting=csv.QUOTE_MINIMAL)
        writer.writeheader()
        writer.writerows(rows)


def canonical_units(script: dict) -> list[str]:
    units = script.get("canonical_script_units")
    if not isinstance(units, list) or not all(isinstance(unit, str) for unit in units):
        raise ValueError("06_script_canonical.json missing canonical_script_units string list")
    return units


def require_columns(rows: list[dict[str, str]], columns: list[str], label: str, result: ValidationResult) -> None:
    if not rows:
        result.add_error(f"{label} has no data rows")
        return
    missing = [column for column in columns if column not in rows[0]]
    if missing:
        result.add_error(f"{label} missing columns: {', '.join(missing)}")


def parse_unit_indexes(rows: list[dict[str, str]], label: str, result: ValidationResult) -> list[int]:
    indexes: list[int] = []
    seen: set[int] = set()
    for row_number, row in enumerate(rows, start=2):
        raw_index = (row.get("unit_index") or "").strip()
        if not raw_index.isdigit():
            result.add_error(f"{label} row {row_number}: unit_index is not numeric")
            continue
        index = int(raw_index)
        if index in seen:
            result.add_error(f"{label} row {row_number}: duplicate unit_index {index}")
        seen.add(index)
        indexes.append(index)
    if indexes and indexes != list(range(len(indexes))):
        result.add_error(f"{label}: unit_index is not contiguous from 0")
    return indexes


def build_row_map(rows: list[dict[str, str]]) -> dict[int, dict[str, str]]:
    return {int(row["unit_index"]): row for row in rows}


def add_common_arguments(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("--channel", required=True, help="Channel id, for example kenh_2")
    parser.add_argument("--video", required=True, help="Video id, for example vid_006")
