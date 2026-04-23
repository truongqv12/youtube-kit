# Single Video Workflow

## 1. Create the video folder
Create a new video directory with a clear identifier.

## 2. Prepare inputs
- Fill in `profile/00_channel_seed.json`
- Run Step 00 to generate all profiles
- Fill in `inputs/01_video_intake.json`

## 3. Run prompts step by step
Run in order:
00 → 01 → 02 → 03 → 04 → 05 → 06 → 07 → 08 → 09 → 10

## 4. Save outputs to the correct locations
- Research goes into `research/`
- Pipeline artifacts go into `artifacts/`
- Final 3-column file goes into `exports/`
- Title / thumbnail / description / shorts notes go into `publication/`

## 5. Only publish when all 3 conditions are met
- `09_export_qc_report.md` has no blocking errors
- Publication package includes title, thumbnail, description, and keywords
- 2 Shorts derivatives are ready to drive traffic to the long-form video
