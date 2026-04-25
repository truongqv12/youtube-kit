# STEP 06C — Host Character Lock

## Purpose
Create or verify the channel-level host identity sheet before image and video prompt generation.

This step exists because consistent characters need persistent state, not only repeated prompt wording.

## Target Context
User MUST supply `TARGET_CHANNEL` (e.g. kenh_2). Stop and ask if not provided.

## Required reads
Read exactly these paths. DO NOT use global workspace search for abstract filenames to prevent cross-channel configuration contamination.
- `core/system_principles.md`
- `core/character_identity_lock_standard.md`
- `bootstrap/00_host_character_sheet.template.json`
- `channels/{{TARGET_CHANNEL}}/00_channel_seed.json`
- `channels/{{TARGET_CHANNEL}}/00_visual_profile.json`

## Optional reads
- `channels/{{TARGET_CHANNEL}}/00_host_character_sheet.json`
- `channels/{{TARGET_CHANNEL}}/assets/host_reference/*`

## Required outputs
- `00_host_character_sheet.json`
- short operator note describing missing or available reference images

## Hard rules
- Character identity is channel state, not per-video state.
- Preserve the existing host design if `00_host_character_sheet.json` already exists.
- Do not invent a celebrity likeness or real person's identity.
- If no reference images exist, produce a stable text-only character sheet and tell the operator which reference images to generate or upload.
- If reference images exist, the sheet must point to the approved files and keep the identity packet consistent with them.
