# seniorhealth_pipeline_topic_first_v3

This folder is a refactored pipeline package built from the repomix snapshot.

## Main changes
- one manual channel seed file: `bootstrap/00_channel_seed.template.json`
- new Step 00 builds all legacy profiles
- every compiled prompt now has a Vietnamese reading companion `*_vi.md`
- old QA step and operator-review step are deprecated
- Step 09 now exports 3 columns and runs minimum QC
- publication package is now Step 10
- script writer is upgraded for rhythm, breath groups, and less AI-sounding Japanese narration
- image prompts are line-context locked for Nano Banana
- Veo prompts are motion-only and i2v-safe

## Recommended operator flow
1. fill `00_channel_seed.json`
2. run Step 00
3. fill `01_video_intake.json`
4. run Steps 01 → 10 in order

## Notes
- legacy files are kept where helpful for backward reference
- `*_vi.md` files are for reading only, not execution
