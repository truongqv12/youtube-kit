# Duration Control Standard

- target_min_chars = target_duration_min * tts_chars_per_min
- target_max_chars = target_duration_max * tts_chars_per_min
- Script must be inside target range before passing.
- Outline-like or underdeveloped scripts do not pass.
- Artificially inflating line count with tiny empty units does not pass.
- Extreme monotony does not pass:
  - too many equally short units in a row
  - too many equally long units in a row
  - obvious filler lines added only to hit duration
- Duration should feel earned through clear, useful spoken content.
