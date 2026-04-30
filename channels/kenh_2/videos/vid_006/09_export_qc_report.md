# 09 Export QC Report — kenh_2 / vid_006

## Checkpoint Validation

| Check | Result |
|-------|--------|
| `validate-prompt-checkpoints.py` | ✅ PASS (0 errors, 0 warnings) |
| `export-final-three-column.py` | ✅ PASS (116 rows exported) |

## Row Counts

| Source | Count |
|--------|-------|
| `06_script_canonical.json` canonical_script_units | 116 |
| `07_image_prompt_table.csv` | 116 |
| `08_video_prompt_table.csv` | 116 |
| `09_final_three_column.csv` | 116 |

## Column Proof

| # | Column | Present |
|---|--------|---------|
| 1 | `script_text` | ✅ |
| 2 | `prompt_img_nano` | ✅ |
| 3 | `prompt_video_veo3` | ✅ |

No extra columns detected.

## QA Checks

| Check | Status |
|-------|--------|
| Row count matches across all steps | ✅ |
| `script_text` is pass-through from canonical units (not rewritten) | ✅ |
| No blank `prompt_img_nano` rows | ✅ (0 blanks) |
| No blank `prompt_video_veo3` rows | ✅ (0 blanks) |
| No Veo prompt asks for speech or lip sync | ✅ |
| All Veo prompts end with `(Silent video, no audio).` | ✅ |
| No Veo prompt requests ambient audio, foley, or room tone | ✅ |
| Opening rows (0-2) have concrete visual overrides from 07A | ✅ |
| Non-linear visual overrides stay within 07A `allowed_non_linear_rows` [1,2,3] | ✅ |
| No retention metadata in final CSV | ✅ |
| No extra columns beyond 3 | ✅ |
| Row order preserved (matches canonical unit order) | ✅ |
| Host rows use `reference_first_locked` with age preservation rule | ✅ |
| All image prompts include style lock prefix | ✅ |
| All image prompts include demographic aging cues for human characters | ✅ |
| Locale governance: Japan domestic interiors | ✅ |
| `visible_text_policy=no_readable_text` enforced (no numbers/text in prompts) | ✅ |

## Issues Found and Fixed During QC

1. **Host rows had `generate_locked` instead of `reference_first_locked`** — Fixed by updating `prompt_mode` and prompt prefix for all 21 host rows.
2. **16 reference-first host rows missing age preservation rule** — Fixed by appending "The character MUST appear the SAME age as the reference. NO youth reduction." to affected prompts.
3. **UTF-8 BOM in CSV files** — Fixed by rewriting both checkpoint CSVs without BOM before export.

## Files Written

- `09_final_three_column.csv` (116 rows, 3 columns)
- `09_export_qc_report.md` (this file)
