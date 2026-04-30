# Output Conventions

## Response envelope
Use this response envelope in every compiled prompt when the execution environment cannot write files directly:
- `=== PREFLIGHT START ===`
- `=== PREFLIGHT END ===`
- `=== ARTIFACT: filename.ext ===`
- `=== END ARTIFACT ===`

## File-first output mode
When the execution environment can write files directly, every compiled prompt MUST write each artifact to its target path instead of pasting full artifact bodies into chat.

Chat output should contain only:
- preflight result
- files written with relative paths
- short validation summary
- unresolved questions, if any

Do not paste full JSON, CSV, or Markdown artifact content into chat unless the operator explicitly asks for inline output.
If direct file writing is unavailable, fall back to the response envelope above.

## Artifact roles
- Checkpoint artifact: resumable intermediate output for debug, QC, and safe resume. It may contain helper metadata.
- Production artifact: operator-facing final deliverable for external production use.
- `07_image_prompt_table.csv` is a Step 07 checkpoint artifact.
- `08_video_prompt_table.csv` is a Step 08 checkpoint artifact.
- `09_final_three_column.csv` is the only production prompt table.
- `09_export_qc_report.md` must list source checkpoints and row alignment status.

## Final export
Exactly 3 columns:
- `script_text`
- `prompt_img_nano`
- `prompt_video_veo3`

## Hard rules
- `script_text` must come directly from the source-of-truth `canonical_script_units`.
- Script source is always `06_script_canonical.json`; Step 06B normalizes this artifact in place when used.
- `script_text` must remain a TTS-safe spoken line with no formatting cleanup required.
- `prompt_img_nano` is the still-image keyframe prompt.
- `prompt_img_nano` must stay semantically locked to the current line, except bounded opening rows approved by `07A_retention_visual_plan.json`.
- retention metadata and Step 07A fields must stay in sidecar/intermediate artifacts, never in final export.
- `prompt_video_veo3` is the image-to-video motion prompt.
- `prompt_video_veo3` must stay motion-only and must not re-describe the full image.
- If visible text is needed inside the image, it must be exact, short, and correct for `channel_language`.
- If `non_dialogue_mode=true` or `voiceover_mode=narration_only`, `prompt_video_veo3` must forbid spoken dialogue, lip sync, and direct-to-camera speech.
- The final exporter must preserve row order.
- Step 09 must also emit `09_export_qc_report.md`.

## Forbidden in final export
- id
- source
- duration
- notes
- scene
- policy flag
- scene_archetype
- visible_text_policy
- visible_text_exact
- motion_strategy
- line_context_frame
- retention_beat_type
- attention_target
- visual_hook_override_used
- opening_strategy
- motion_intent
