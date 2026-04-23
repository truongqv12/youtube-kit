# Export QC Report & Preflight

## Preflight Data
- **files_read**: 
  - `core/system_principles.md`
  - `core/output_conventions.md`
  - `core/canonical_script_unit_standard.md`
  - `06_script_canonical.json`
  - `07_image_prompt_table.csv`
  - `08_video_prompt_table.csv`
- **rules_extracted_by_file**:
  - `canonical_script_unit_standard.md`: `script_text` must come directly from `canonical_script_units` untouched.
  - `09_run_three_column_exporter.md`: Final export must contain exactly 3 columns (`script_text`, `prompt_img_nano`, `prompt_video_veo3`). Row order must be strictly preserved.
- **column_names_required**: `script_text`, `prompt_img_nano`, `prompt_video_veo3`
- **allowed_to_proceed**: YES

## Quality Control (QC) Checks
- [x] **Row count match:** Confirmed. All sources have exactly 116 units.
- [x] **`script_text` is pass-through:** Confirmed. Text mapped cleanly from `06_script_canonical.json` without any markdown cleanup.
- [x] **Blank rows check:** Confirmed. 0 blank prompt rows.
- [x] **Audio/Speech compliance (non-dialogue mode):** Confirmed. No Veo row asks for lip sync, direct-to-camera speech, singing, or ambient audio. Every single row includes the `(Silent video, no audio).` constraint.
- [x] **New readable text generation check:** Confirmed. No prompt implies or asks for generation of *new* readable text. Existing text (`ポイント1`, `介護保険`, etc.) is explicitly locked as "exactly as-is".
- [x] **Column count:** Confirmed exactly 3 columns in `09_final_three_column.csv`.
- [x] **Row order preserved:** Confirmed. Rows `0` to `115` mapped exactly via direct index pairing.

## Conclusion
Quality gate passed. The 3-column operator output file is verified safe for pipeline execution, TTS alignment, and generation.
