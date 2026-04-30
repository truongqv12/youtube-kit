# STEP 09 — Three Column Exporter + Minimal QA

## Goal
Export the final manual-production CSV and run minimal QC.

## Script source
Read `01_project_manifest.json`. Use `06_script_canonical.json` by default. If manifest sets `script_source_of_truth` to `06B_script_canonical.json`, export `script_text` from `06B` and validate row counts against that source.

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
