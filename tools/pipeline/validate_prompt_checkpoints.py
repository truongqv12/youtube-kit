from __future__ import annotations

import re
from collections import Counter
from pathlib import Path

from prompt_checkpoint_common import (
    ValidationResult,
    build_row_map,
    canonical_units,
    parse_unit_indexes,
    read_csv_rows,
    read_json,
    require_columns,
)

IMAGE_COLUMNS = [
    "unit_index",
    "scene_group_id",
    "scene_archetype",
    "host_usage",
    "visible_text_policy",
    "visible_text_exact",
    "prompt_mode",
    "prompt_img_nano",
]
VIDEO_COLUMNS = [
    "unit_index",
    "i2v_mode",
    "motion_strategy",
    "recommended_duration_sec",
    "motion_role",
    "attention_target",
    "prompt_video_veo3",
]
AUDIO_TERMS = ["sound effect", "music", "narration", "voiceover"]
EXPLICIT_TEXT_PATTERN = re.compile(
    r"\b(reads?|showing|display(?:s|ing)?|label(?:ed)?|checklist)\b[^.]{0,40}\d|\d+\s*(degrees?|percent|ml)|\d+\s*(ミリリットル|パーセント|度)",
    re.IGNORECASE,
)
DISPLAY_CONTEXT_PATTERN = re.compile(r"display|remote|thermo|hygrometer|meter|screen|monitor|温度|湿度", re.IGNORECASE)
THERMAL_CONTEXT_PATTERN = re.compile(r"water|tea|glass|cup|kettle|steam|hot|thermal|condensation|汗|水|茶", re.IGNORECASE)
AGE_RULE_PATTERN = re.compile(r"same age|no youth|age as the reference|年齢", re.IGNORECASE)


def validate_required_files(base_dir: Path, result: ValidationResult) -> dict[str, Path]:
    paths = {
        "script": base_dir / "06_script_canonical.json",
        "image": base_dir / "07_image_prompt_table.csv",
        "video": base_dir / "08_video_prompt_table.csv",
    }
    for path in paths.values():
        if not path.exists():
            result.add_error(f"Missing required file: {path.name}")
    return paths


def validate_rows(script_units: list[str], image_rows: list[dict[str, str]], video_rows: list[dict[str, str]], result: ValidationResult) -> None:
    result.script_count = len(script_units)
    result.image_count = len(image_rows)
    result.video_count = len(video_rows)
    if len(image_rows) != len(script_units):
        result.add_error(f"Step 07 row count {len(image_rows)} != script units {len(script_units)}")
    if len(video_rows) != len(script_units):
        result.add_error(f"Step 08 row count {len(video_rows)} != script units {len(script_units)}")
    expected = list(range(len(script_units)))
    if parse_unit_indexes(image_rows, "Step 07", result) != expected:
        result.add_error("Step 07 unit_index does not align canonical units")
    if parse_unit_indexes(video_rows, "Step 08", result) != expected:
        result.add_error("Step 08 unit_index does not align canonical units")


def validate_image_rows(image_rows: list[dict[str, str]], result: ValidationResult) -> None:
    for row in image_rows:
        index = row.get("unit_index", "?")
        prompt = row.get("prompt_img_nano", "")
        policy = row.get("visible_text_policy", "")
        visible_text = row.get("visible_text_exact", "").strip()
        if row.get("host_usage") == "host" and row.get("prompt_mode") != "reference_first_locked":
            result.add_error(f"Step 07 row {index}: host_usage=host requires reference_first_locked")
        if row.get("prompt_mode") == "reference_first_locked" and not AGE_RULE_PATTERN.search(prompt):
            result.add_error(f"Step 07 row {index}: reference-first prompt missing age preservation rule")
        if policy == "no_readable_text" and EXPLICIT_TEXT_PATTERN.search(prompt):
            result.add_error(f"Step 07 row {index}: no_readable_text conflicts with explicit text/number/display")
        if policy == "exact_visible_text" and not visible_text:
            result.add_error(f"Step 07 row {index}: exact_visible_text missing visible_text_exact")


def validate_video_rows(image_rows: list[dict[str, str]], video_rows: list[dict[str, str]], result: ValidationResult) -> None:
    image_by_index = build_row_map(image_rows)
    prompts = [row.get("prompt_video_veo3", "") for row in video_rows]
    for prompt, count in Counter(prompts).items():
        if prompt and count > 1:
            result.add_error(f"Step 08 duplicate exact prompt: {count} times")
    first_sentences = [prompt.split(".", 1)[0].strip() for prompt in prompts if prompt]
    for sentence, count in Counter(first_sentences).items():
        if sentence and count > 2:
            result.add_warning(f"Step 08 repeats first motion sentence {count} times: {sentence}")
    for row in video_rows:
        index = row.get("unit_index", "?")
        prompt = row.get("prompt_video_veo3", "")
        lower_prompt = prompt.lower()
        if "(silent video, no audio)." not in lower_prompt:
            result.add_error(f"Step 08 row {index}: missing exact silent rule")
        for term in AUDIO_TERMS:
            if term in lower_prompt and f"no {term}" not in lower_prompt:
                result.add_error(f"Step 08 row {index}: invalid audio request: {term}")
        image_prompt = image_by_index.get(int(index), {}).get("prompt_img_nano", "") if str(index).isdigit() else ""
        if "display numbers" in lower_prompt and not DISPLAY_CONTEXT_PATTERN.search(image_prompt):
            result.add_warning(f"Step 08 row {index}: display numbers but image lacks display/remote/thermo context")
        if re.search(r"steam|condensation", lower_prompt) and not THERMAL_CONTEXT_PATTERN.search(image_prompt):
            result.add_warning(f"Step 08 row {index}: steam/condensation but image lacks liquid/thermal context")


def validate_checkpoint_files(base_dir: Path) -> ValidationResult:
    result = ValidationResult()
    paths = validate_required_files(base_dir, result)
    if result.errors:
        return result
    script_units = canonical_units(read_json(paths["script"]))
    image_rows = read_csv_rows(paths["image"])
    video_rows = read_csv_rows(paths["video"])
    require_columns(image_rows, IMAGE_COLUMNS, "Step 07", result)
    require_columns(video_rows, VIDEO_COLUMNS, "Step 08", result)
    validate_rows(script_units, image_rows, video_rows, result)
    if result.errors:
        return result
    validate_image_rows(image_rows, result)
    validate_video_rows(image_rows, video_rows, result)
    return result


def format_result(result: ValidationResult) -> str:
    lines = [
        "Prompt checkpoint validation",
        f"Rows: script={result.script_count}, step07={result.image_count}, step08={result.video_count}",
        f"Status: {'PASS' if result.passed else 'FAIL'} | errors={len(result.errors)} | warnings={len(result.warnings)}",
    ]
    lines.extend(f"{issue.level}: {issue.message}" for issue in result.issues)
    return "\n".join(lines)
