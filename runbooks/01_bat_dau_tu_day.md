# Getting Started

## Goal
This file explains how to run the pipeline manually, following the v3 process.

## Important rules
- Operator guides are written in English
- Execution prompts are kept in English
- `*_vi.md` files in `compiled_prompts/` are reading companions only, not for execution
- New artifacts are the source of truth
- Do not trust that an AI has read a file just because it claims to have
- Any step with `Required reads` requires all listed files to be pasted before execution
- Always require the AI to return `Preflight` first
- Each channel only requires filling one file: `00_channel_seed.json`

## Short workflow
1. Fill in `00_channel_seed.json`
2. Run Step 00 to build all profiles
3. Fill in `01_video_intake.json`
4. Run Step 01 intake
5. Run Step 02 topic strategy
6. Run Step 03 mandatory research
7. Run Step 04 policy gate
8. Run Step 05 outline
9. Run Step 06 script canonical
10. Run Step 07 image prompt
11. Run Step 08 video prompt
12. Run Step 09 export + minimal QA
13. Run Step 10 publication package

## Operational notes
- Do not start by finding a competitor video to follow.
- If the topic angle is still vague, pause at Step 02 before proceeding to research.
- If the script still sounds robotic, go back to Step 06 instead of manually editing at Step 09.
