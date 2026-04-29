# 09 Export QC Report

**Project:** kenh_2_vid_005
**Generated:** 2026-04-29

## Row Counts
- canonical_script_units: 95
- 07_image_prompt_table: 95
- 08_video_prompt_table: 95
- 09_final_three_column: 95

## Columns
- script_text ✅
- prompt_img_nano ✅
- prompt_video_veo3 ✅
- Extra columns: NONE ✅

## QC Checks
- [PASS] Row counts match: script=95, img=95, vid=95
- [PASS] No blank script_text rows
- [PASS] No blank prompt_img_nano rows
- [PASS] No blank prompt_video_veo3 rows
- [PASS] All Veo prompts enforce non-dialogue constraints
- [PASS] All Veo prompts contain '(Silent video, no audio).'
- [PASS] No Veo prompts request new readable text

## Overall: PASS ✅

## Notes
- script_text is pass-through from canonical_script_units (no rewriting)
- Row order preserved (sequential 1-to-N merge)
- Non-dialogue mode enforced in all Veo prompts
- Silent audio directive present in all Veo prompts
