# Step 09 Export QC Report — kenh_1 vid_003

## Inputs
- `06_script_canonical.json`
- `07_image_prompt_table.csv`
- `08_video_prompt_table.csv`
- Optional: `07A_retention_visual_plan.json`

## Local checkpoint validation
```text
Prompt checkpoint validation
Rows: script=110, step07=110, step08=110
Status: PASS | errors=0 | warnings=0
```

## Final export
- `09_final_three_column.csv`
- Columns: `script_text,prompt_img_nano,prompt_video_veo3`
- Rows exported: 110
- Script pass-through: PASS — each `script_text` equals the same-index canonical unit.
- Extra columns: PASS — exactly 3 final columns.
- Blank prompt rows: PASS.
- Non-dialogue Veo policy: PASS — every row includes `(Silent video, no audio).` and forbids dialogue/lip sync/direct-to-camera speech.
- Retention metadata stripped from final CSV: PASS.

## Tool note
`tools/pipeline/export-final-three-column.py` in the supplied Repomix package contains a broken multiline string and cannot be executed as-is. Step 09 used the same deterministic join logic directly after the repository validator returned PASS.
