# STEP 08 — Video Prompt Builder Veo 3 i2v (Non-Dialogue)

## Goal
Turn each still image prompt into one Veo 3 image-to-video motion prompt.

## New key rule
Prompt này là motion-only.
Không mô tả lại full image.
Không tự thêm text mới.
Không implied speech nếu non-dialogue mode đang bật.

## Must decide per row
- i2v_mode
- motion_strategy
- recommended_duration_sec
- prompt_video_veo3

## Output
- `08_video_prompt_table.csv`
