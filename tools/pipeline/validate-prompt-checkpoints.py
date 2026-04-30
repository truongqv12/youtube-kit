from __future__ import annotations

import argparse

from prompt_checkpoint_common import add_common_arguments, video_dir
from validate_prompt_checkpoints import format_result, validate_checkpoint_files


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate Step 07/08 prompt checkpoint CSV files.")
    add_common_arguments(parser)
    parser.add_argument("--report", action="store_true", help="Write 09_export_qc_report.md with validation result")
    args = parser.parse_args()
    try:
        base_dir = video_dir(args.channel, args.video)
        result = validate_checkpoint_files(base_dir)
        output = format_result(result)
        print(output)
        if args.report:
            (base_dir / "09_export_qc_report.md").write_text(output + "\n", encoding="utf-8")
        return 0 if result.passed else 1
    except Exception as exc:
        print(f"ERROR: {exc}")
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
