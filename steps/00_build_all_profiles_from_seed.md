# STEP 00 — Build All Profiles From Seed

## Purpose
From `00_channel_seed.json`, generate all legacy-format profile files that downstream pipeline steps depend on:
- `00_channel_config.json`
- `00_editorial_profile.json`
- `00_publication_profile.json`
- `00_visual_profile.json`
- `00_language_profile.json`
- `00_profile_inference_report.md`

## Target Context
User MUST supply `TARGET_CHANNEL` (e.g. kenh_2). Stop and ask if not provided.

## Required reads
Read exactly these paths. DO NOT use global workspace search for abstract filenames to prevent cross-channel configuration contamination.
- `channels/{{TARGET_CHANNEL}}/00_channel_seed.json`
- `bootstrap/*.template.json`
- `knowledge/japanese/*`
- `knowledge/visual/*`

## Required outputs
- All legacy profile files listed above
- `00_profile_inference_report.md`

## Key rules
- The seed's 6 fields are the only manual input per channel
- All other profiles are derived state
- Must maintain backward compatibility for downstream steps
