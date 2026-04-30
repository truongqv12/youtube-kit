# STEP 09 — Three Column Exporter + Minimal QA

## Goal
Export the final manual-production CSV and run minimal QC.

## Script source
Read `01_project_manifest.json`. Always export `script_text` from `06_script_canonical.json` and validate row counts against that source. Step 06B normalizes this artifact in place when used.

## Required final columns
- script_text
- prompt_img_nano
- prompt_video_veo3

## Additional output
- `09_export_qc_report.md`

## Retention QC
- Read `07A_retention_visual_plan.json` when present.
- Confirm opening visual overrides stay within allowed rows.
- Confirm `prompt_video_veo3` includes attention targets for retention-aware rows.
- Strip all Step 07A metadata from `09_final_three_column.csv`.
