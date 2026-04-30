# Artifact Contracts

## Artifact roles
- Checkpoint artifact = resumable intermediate for resume/debug/QC; it may include helper metadata.
- Production artifact = operator-facing final deliverable.
- `07_image_prompt_table.csv` and `08_video_prompt_table.csv` are checkpoint artifacts.
- `09_final_three_column.csv` is the only production prompt table.
- `09_export_qc_report.md` records source checkpoints, row counts, alignment, warnings, and errors.

## Hard contracts
- external research required before script when topic requires it
- `full_script == "\n".join(canonical_script_units)`
- every `canonical_script_unit` must be TTS-safe spoken narration
- final export exact 3 columns
- downstream script source is always `06_script_canonical.json`; Step 06B normalizes this artifact in place when used
- `script_text` rows == source-of-truth `canonical_script_units` in order
- final export columns are:
  - script_text
  - prompt_img_nano
  - prompt_video_veo3
- `07A_retention_visual_plan.json` is an intermediate sidecar for retention strategy; it must never add columns to final export
- retention metadata is forbidden in `09_final_three_column.csv`
- `prompt_img_nano` must stay semantically locked to each line, except bounded opening rows approved by `07A_retention_visual_plan.json`
- non-linear visual hook rows are allowed only for first 1-3 rows / first 10-15 seconds and must not rewrite script text
- `prompt_video_veo3` must stay motion-only for image-to-video
- visible text must follow `channel_language` and locale governance
- compiled prompts require mandatory file reads + preflight extraction