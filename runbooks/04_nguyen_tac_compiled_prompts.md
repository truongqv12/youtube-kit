# Compiled Prompts Principles

## What this directory is for
Contains the execution prompt files for each pipeline step.

## v3 rules
- The primary execution prompts are kept in English
- Vietnamese companion files `*_vi.md` are allowed in the same directory
- `*_vi.md` files are for operator reading comprehension only
- Do not use `*_vi.md` files for pipeline execution

## Rationale
Operators may need to understand the logic without being required to read specialized English, but the actual execution prompts must remain stable in English.
