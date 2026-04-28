=== PREFLIGHT START ===

## 1. files_read
- core/system_principles.md ✅
- core/output_conventions.md ✅
- core/canonical_script_unit_standard.md ✅
- channels/kenh_3/videos/vid_001/06_script_canonical.json ✅
- channels/kenh_3/videos/vid_001/07_image_prompt_table.csv ✅
- channels/kenh_3/videos/vid_001/08_video_prompt_table.csv ✅

## 2. rules_extracted_by_file

### system_principles.md
- narration-support pipeline: final export is operator-facing, one row per keyframe
- one canonical unit = one keyframe = one row
- script_text is pass-through from canonical_script_units (no rewriting)

### output_conventions.md
- exactly 3 columns: script_text, prompt_img_nano, prompt_video_veo3
- forbidden columns: id, source, duration, notes, scene, policy flag, scene_archetype, visible_text_policy, visible_text_exact, motion_strategy, line_context_frame
- script_text must be TTS-safe spoken line
- prompt_video_veo3 must be motion-only, must not re-describe full image
- non_dialogue_mode → no spoken dialogue, lip sync, direct-to-camera speech in Veo prompts
- row order preserved
- must emit 09_export_qc_report.md

### canonical_script_unit_standard.md
- script_text comes directly from canonical_script_units array
- no later step may rewrite script_text
- TTS-safe: plain spoken language, one thought per line, max 2 clauses

## 3. column_names_required
- script_text
- prompt_img_nano
- prompt_video_veo3

## 4. allowed_to_proceed
✅ YES — all required files read, column contract understood, merge validated.

=== PREFLIGHT END ===

=== ARTIFACT: 09_final_three_column.csv ===
File: channels/kenh_3/videos/vid_001/09_final_three_column.csv
Row count: 127 data rows (header + 127 data rows)
Columns: script_text, prompt_img_nano, prompt_video_veo3
=== END ARTIFACT ===

=== ARTIFACT: 09_export_qc_report.md ===
File: channels/kenh_3/videos/vid_001/09_export_qc_report.md
Result: ALL CHECKS PASSED ✅
=== END ARTIFACT ===
