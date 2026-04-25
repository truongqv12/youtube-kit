# STEP 08 — Video Prompt Builder Veo 3 i2v (Non-Dialogue)

## Goal
Turn each still image prompt into one Veo 3 image-to-video motion prompt.
The clip must support external TTS narration for YouTube, not generate its own performance or audio.

## New key rule
This prompt is motion-only.
Do not re-describe the full image.
Do not add new text.
Do not imply speech if non-dialogue mode is enabled.
Do not add ambience, foley, room tone, soundscape, music, voice, or any audio cue.
For host rows, preserve the exact character identity from the source image and approved subject references.

## Must decide per row
- i2v_mode
- motion_strategy
- recommended_duration_sec
- prompt_video_veo3

## Host video rule
If the source image contains the channel host, the video prompt must preserve identity:
- exact face and hair silhouette
- visible age cues
- wardrobe family
- body posture
- illustration style

The video prompt must not redesign the character.

## Output
- `08_video_prompt_table.csv`
