# STEP 01 — Video Intake

## Purpose
Merge state của kênh (được Step 00 sinh ra) với `01_video_intake.json` để tạo intake spec và project manifest.

## Target Context
User MUST supply `TARGET_CHANNEL` (e.g. kenh_2) and `TARGET_VIDEO` (e.g. vid_001). Stop and ask if not provided.

## Required reads
Read exactly these paths. DO NOT use global workspace search for abstract filenames to prevent cross-channel configuration contamination.
- channels/{{TARGET_CHANNEL}}/00_channel_config.json
- channels/{{TARGET_CHANNEL}}/00_language_profile.json
- channels/{{TARGET_CHANNEL}}/00_visual_profile.json
- channels/{{TARGET_CHANNEL}}/00_editorial_profile.json
- channels/{{TARGET_CHANNEL}}/00_publication_profile.json
- channels/{{TARGET_CHANNEL}}/videos/{{TARGET_VIDEO}}/01_video_intake.json

## Required outputs
- 01_intake_spec.json
- 01_project_manifest.json
