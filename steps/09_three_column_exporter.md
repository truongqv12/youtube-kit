# STEP 09 — Three Column Exporter + Minimal QA

## Goal
Export the final manual-production CSV and run minimal QC. Step 07/08 CSVs are checkpoint inputs; `09_final_three_column.csv` is the only production prompt table.

## Standard tools
Run validation/export with reviewed repo scripts when local tools are available:

```bash
python tools/pipeline/validate-prompt-checkpoints.py --channel {{TARGET_CHANNEL}} --video {{TARGET_VIDEO}}
python tools/pipeline/export-final-three-column.py --channel {{TARGET_CHANNEL}} --video {{TARGET_VIDEO}}
```

Do not create per-video scripts for standard Step 07/08/09 validation/export.

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
- If absent in legacy videos, continue without retention-specific QC.
- Confirm opening visual overrides stay within allowed rows when Step 07A exists.
- Confirm `prompt_video_veo3` includes attention targets for retention-aware rows when Step 07A exists.
- Strip all Step 07A metadata from `09_final_three_column.csv`.
