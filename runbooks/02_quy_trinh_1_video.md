# Single Video Workflow

## 1. Create the video folder
Create a new video directory with a clear identifier.

## 2. Prepare inputs
- Fill in `channels/{{TARGET_CHANNEL}}/00_channel_seed.json`
- Run Step 00 to generate all profiles
- Fill in `channels/{{TARGET_CHANNEL}}/videos/{{TARGET_VIDEO}}/01_video_intake.json`

## 3. Script source rule
- Default source: `06_script_canonical.json`
- Use `06B_script_canonical.json` only when `01_project_manifest.json` explicitly sets `script_source_of_truth`
- Steps 07A, 07, 08, 09, and 10 must use the same source

## 4. Run prompts step by step
Run in order:
00 → 01 → 02 → 03 → 04 → 05 → 06 → 07A → 07 → 08 → 09 → 10

## 5. Save outputs to the correct locations
- Save pipeline artifacts in `channels/{{TARGET_CHANNEL}}/videos/{{TARGET_VIDEO}}/`
- Final 3-column file is `09_final_three_column.csv`
- Title / thumbnail / description / shorts package is `10_publication_package.json` and `10_publication_package.md`

## 6. Only publish when all 3 conditions are met
- `09_export_qc_report.md` has no blocking errors
- Publication package includes title, thumbnail, description, and keywords
- 2 Shorts derivatives are ready to drive traffic to the long-form video
