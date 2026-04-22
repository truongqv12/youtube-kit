# Visual Strategy

Default visual philosophy:
- narration-support visuals, not acted film scenes
- one canonical script unit = one keyframe = one motion beat
- semantic lock: each visual prompt must visualize the exact meaning of its line, not a generic topic illustration
- continuity: carry forward 2 to 4 anchors across adjacent related rows such as host identity, location family, prop family, wardrobe family, or time-of-day
- reference-first when host imagery is used
- locale fidelity: scenery, signage, props, wardrobe, packaging, architecture, and public-space cues must fit the target country or region
- readable text should be avoided by default and only used when the line truly needs it
- style must be resolved into a concrete style lock with explicit prompt phrases, render medium, line treatment, color system, and composition bias — either by matching a known family in the style registry, or by deriving directly from the seed's `image_style` description. Seed-driven locks must preserve the raw value in `style_lock.seed_image_style_raw`. Never use a vague label like `manga-style` without a resolved lock.
- motion defaults to calm, explanatory, non-dialogue support for external TTS
- Veo prompts must use `(Silent video, no audio).` — do not request ambience, foley, or room tone; audio is handled entirely by external TTS