# Single Video Workflow

## 1. Create the video folder
Create a new video directory with a clear identifier.

## 2. Prepare inputs
- Fill in `channels/{{TARGET_CHANNEL}}/00_channel_seed.json`
- Run Step 00 to generate all profiles
- Fill in `channels/{{TARGET_CHANNEL}}/videos/{{TARGET_VIDEO}}/01_video_intake.json`

## 3. Script source rule
- Source: `06_script_canonical.json`
- If Step 06B is run, it normalizes `06_script_canonical.json`, `06_script_full.md`, and `06_script_metrics.json` in place
- Steps 07A, 07, 08, 09, and 10 always use the `06_*` artifacts

## 4. Run prompts step by step
Run in order:
00 → 01 → 02 → 03 → 04 → 05 → 06 → 07A → 07 → 08 → 09 → 10

## 5. Save outputs to the correct locations
- Save pipeline artifacts in `channels/{{TARGET_CHANNEL}}/videos/{{TARGET_VIDEO}}/`
- Final 3-column file is `09_final_three_column.csv`
- Title / thumbnail / description / shorts package is `10_publication_package.json` and `10_publication_package.md`

## 6. Validate checkpoints and export production CSV

Step 07/08 CSVs are checkpoint artifacts for resume/debug/QC. Use Step 09 CSV as the only production prompt table.

```bash
python tools/pipeline/validate-prompt-checkpoints.py --channel kenh_2 --video vid_006
python tools/pipeline/export-final-three-column.py --channel kenh_2 --video vid_006
```

Windows examples:

```powershell
powershell -ExecutionPolicy Bypass -File tools/pipeline/validate-prompt-checkpoints.ps1 -Channel kenh_2 -Video vid_006
powershell -ExecutionPolicy Bypass -File tools/pipeline/export-final-three-column.ps1 -Channel kenh_2 -Video vid_006
```

Do not ask the AI agent to write temporary Python/CMD scripts for standard Step 07/08/09 validation or export. Use `tools/pipeline` scripts.

## 7. Only publish when all 3 conditions are met
- `09_export_qc_report.md` has no blocking errors
- Publication package includes title, thumbnail, description, and keywords
- 2 Shorts derivatives are ready to drive traffic to the long-form video
