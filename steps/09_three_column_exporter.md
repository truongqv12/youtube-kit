# STEP 09 — Three Column Exporter + Minimal QA

## Goal
Export the final manual-production CSV and run minimal QC.
The CSV is for YouTube production: paste `script_text` into TTS, use `prompt_img_nano` for keyframes, and use `prompt_video_veo3` for image-to-video motion.

## Required final columns
- script_text
- prompt_img_nano
- prompt_video_veo3

## Additional output
- `09_export_qc_report.md`

## QC must catch
- row count mismatch
- rewritten `script_text`
- blank image or video prompts
- Veo prompts that request speech, voice, ambience, foley, room tone, music, or soundscape
- missing `(Silent video, no audio).`
- host rows that lack identity/reference lock
- host video rows that imply character redesign
- visual prompts that are generic topic illustrations rather than line-locked beats
