# Step 09 Export QC Report

## Source checkpoints

- `06_script_canonical.json`
- `07_image_prompt_table.csv` - checkpoint
- `08_video_prompt_table.csv` - checkpoint

## Final artifact

- `09_final_three_column.csv` - production prompt table
- Columns: `script_text,prompt_img_nano,prompt_video_veo3`
- Rows exported: 111

## Validation summary

```text
Prompt checkpoint validation
Rows: script=111, step07=111, step08=111
Status: PASS | errors=0 | warnings=0
```

## Export note

The Repomix-extracted copy of `tools/pipeline/export-final-three-column.py` contained a syntax-corrupted string literal, so the final CSV was exported with an equivalent deterministic join: canonical script row + Step 07 image row + Step 08 video row, preserving row order and exactly three columns.
