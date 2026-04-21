# Visual Strategy

Default visual philosophy:
- narration-support visuals, not acted film scenes
- one canonical script unit = one keyframe = one motion beat
- semantic lock: each visual prompt must visualize the exact meaning of its line, not a generic topic illustration
- continuity: carry forward 2 to 4 anchors across adjacent related rows such as host identity, location family, prop family, wardrobe family, or time-of-day
- reference-first when host imagery is used
- locale fidelity: scenery, signage, props, wardrobe, packaging, architecture, and public-space cues must fit the target country or region
- readable text should be avoided by default and only used when the line truly needs it
- style must be resolved from `visual_style_id` and `visual_substyle_id`, never from a vague label like `manga-style`
- motion defaults to calm, explanatory, non-dialogue support for external TTS
- Veo prompts must use `(Silent video, no audio).` — do not request ambience, foley, or room tone; audio is handled entirely by external TTS