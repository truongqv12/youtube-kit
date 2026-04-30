from __future__ import annotations

import argparse
from pathlib import Path

from prompt_checkpoint_common import (
    add_common_arguments,
    build_row_map,
    canonical_units,
    read_csv_rows,
    read_json,
    video_dir,
    write_csv_rows,
)
from validate_prompt_checkpoints import format_result, validate_checkpoint_files

FINAL_COLUMNS = ["script_text", "prompt_img_nano", "prompt_video_veo3"]


def load_export_rows(base_dir: Path) -> list[dict[str, str]]:
    units = canonical_units(read_json(base_dir / "06_script_canonical.json"))
    image_by_index = build_row_map(read_csv_rows(base_dir / "07_image_prompt_table.csv"))
    video_by_index = build_row_map(read_csv_rows(base_dir / "08_video_prompt_table.csv"))
    rows: list[dict[str, str]] = []
    for index, script_text in enumerate(units):
        rows.append(
            {
                "script_text": script_text,
                "prompt_img_nano": image_by_index[index]["prompt_img_nano"],
                "prompt_video_veo3": video_by_index[index]["prompt_video_veo3"],
            }
        )
    return rows


def write_qc_report(base_dir: Path, validation_text: str, row_count: int) -> None:
    content = "\n".join(
        [
            "# Step 09 Export QC Report",
            "",
            "## Source checkpoints",
            "",
            "- `06_script_canonical.json`",
            "- `07_image_prompt_table.csv` - checkpoint",
            "- `08_video_prompt_table.csv` - checkpoint",
            "",
            "## Final artifact",
            "",
            "- `09_final_three_column.csv` - production prompt table",
            "- Columns: `script_text,prompt_img_nano,prompt_video_veo3`",
            f"- Rows exported: {row_count}",
            "",
            "## Validation summary",
            "",
            "```text",
            validation_text,
            "```",
            "",
        ]
    )
    (base_dir / "09_export_qc_report.md").write_text(content, encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Export Step 09 final three-column production CSV.")
    add_common_arguments(parser)
    args = parser.parse_args()
    try:
        base_dir = video_dir(args.channel, args.video)
        result = validate_checkpoint_files(base_dir)
        validation_text = format_result(result)
        print(validation_text)
        if not result.passed:
            print("ERROR: checkpoint validation failed; final export refused")
            return 1
        rows = load_export_rows(base_dir)
        write_csv_rows(base_dir / "09_final_three_column.csv", FINAL_COLUMNS, rows)
        write_qc_report(base_dir, validation_text, len(rows))
        print(f"Exported 09_final_three_column.csv with {len(rows)} rows")
        return 0
    except Exception as exc:
        print(f"ERROR: {exc}")
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
