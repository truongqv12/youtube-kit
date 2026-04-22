# Style Registry

## Resolution rule
Every visual profile must resolve `visual_style_id` and `visual_substyle_id` into a concrete style lock.
Two valid approaches:
1. **Registry-based:** Match the seed's `image_style` to a known family below, then use the family's pre-defined lock.
2. **Seed-driven:** When `image_style` does not match any registry family, derive `visual_style_id` and `visual_substyle_id` directly from the seed description and build a custom style lock. The raw `image_style` value must be preserved in `style_lock.seed_image_style_raw`.

Never stop at vague labels such as `manga-style`, `anime-style`, or `watercolor-style`.
A valid style lock (whether registry-based or seed-driven) must specify:
- family prompt phrase
- substyle prompt phrase
- render medium
- line treatment
- color system
- texture or screentone behavior (if applicable)
- composition bias
- emotion ceiling
- style drift to avoid (if applicable)

## Family: manga_editorial_clean
Base lock:
- family_prompt_phrase: editorial manga illustration
- render_medium: clean editorial manga illustration
- line_treatment: clean ink line art, controlled line weight, restrained screentone
- color_system: flat soft colors, low-saturation neutrals, gentle warm accents
- composition_bias: panel-like clarity, readable anatomy, low clutter, negative space for narration support
- emotion_ceiling: calm, reassuring, observant, informative
- style_drift_to_avoid: battle manga exaggeration, chibi proportions, slapstick faces, glossy poster rendering

### Substyle: seinen_soft_educational
- substyle_prompt_phrase: seinen soft educational style
- extra_anchors: mature proportions, health-magazine explainer tone, restrained expressions, practical everyday realism
- best_for: senior health, finance explainers, calm social commentary

### Substyle: shonen_dynamic_explainer
- substyle_prompt_phrase: shonen dynamic explainer style
- extra_anchors: stronger contrast, sharper motion lines, energetic clarity, still readable and informative
- best_for: sports science, productivity, educational action breakdowns
- avoid: combat posing, screaming faces, heroic power-up cliches

### Substyle: josei_warm_lifestyle
- substyle_prompt_phrase: josei warm lifestyle style
- extra_anchors: gentle domestic warmth, elegant daily-life realism, soft fashion cues
- best_for: lifestyle explainers, home routines, relationships, wellness
- avoid: romance-drama melodrama, idol glamour styling

## Family: anime_editorial
Base lock:
- family_prompt_phrase: anime editorial illustration
- render_medium: polished anime editorial illustration
- line_treatment: clean contour lines with selective soft shading
- color_system: controlled contemporary palette with magazine-feature contrast
- composition_bias: cover-story clarity, expressive but not theatrical
- emotion_ceiling: present, articulate, composed
- style_drift_to_avoid: idol-poster gloss, over-rendered fantasy spectacle, mascot cuteness

### Substyle: magazine_feature_clean
- substyle_prompt_phrase: magazine feature clean anime style
- extra_anchors: article-illustration clarity, contemporary fashion realism, restrained gradients

### Substyle: infographic_character_clean
- substyle_prompt_phrase: infographic character clean anime style
- extra_anchors: simplified shapes, didactic readability, symbolic object emphasis

## Family: ghibli_inspired_pastoral
Base lock:
- family_prompt_phrase: Ghibli-inspired pastoral illustration
- render_medium: hand-painted pastoral anime illustration
- line_treatment: soft pencil contour with painterly edges
- color_system: natural greens, sky blues, sun-warmed earth tones
- composition_bias: breathing space, lived-in environments, gentle environmental storytelling
- emotion_ceiling: tender, curious, quietly hopeful
- style_drift_to_avoid: fantasy overload, theme-park whimsy, caricature comedy

### Substyle: gentle_rural_observational
- substyle_prompt_phrase: gentle rural observational substyle
- extra_anchors: wind, foliage, domestic craft detail, observational pacing

## Family: watercolor_documentary
Base lock:
- family_prompt_phrase: watercolor documentary illustration
- render_medium: watercolor documentary field-note illustration
- line_treatment: ink contour with soft watercolor wash
- color_system: muted natural pigments, paper texture, selective accent color
- composition_bias: field-note clarity, factual observation, low clutter
- emotion_ceiling: reflective, trustworthy, humane
- style_drift_to_avoid: greeting-card sentimentality, abstract wash chaos, decorative excess

### Substyle: ink_wash_field_notes
- substyle_prompt_phrase: ink wash field-notes substyle
- extra_anchors: notebook realism, observational annotation feel without infographic clutter