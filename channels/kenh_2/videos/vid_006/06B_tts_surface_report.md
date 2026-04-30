# 06B TTS Surface Normalization Report

## Project
- **project_id:** kenh_2_vid_006
- **channel_id:** kenh_2
- **pipeline_step:** 06B_tts_surface_normalizer
- **generated_at:** 2026-04-30T15:44:00+07:00

## Source Metrics (Pre-Normalization)
| Metric | Value |
|---|---|
| Total chars | 3581 |
| Total units | 116 |
| Estimated duration | 11.2 min |
| Duration status | PASS |

## Output Metrics (Post-Normalization)
| Metric | Value |
|---|---|
| Total chars | 3563 |
| Total units | 116 |
| Estimated duration | 11.1 min |
| Duration status | PASS |
| Char delta | −18 |

## Summary
| Category | Count |
|---|---|
| Units changed | 22 |
| Units kept as-is | 94 |
| Splits | 0 |
| Merges | 0 |
| Row order changes | 0 |

## Change Log

### A. Numeral → Kanji Spoken Form (Reading Stability — Rule D)

| Line | Before | After | Reason |
|---|---|---|---|
| 42 | `6つ` | `六つ` | `6つ` can wobble between ろくつ/むっつ on some engines |
| 45 | `1回にコップ半分から1杯` | `一回にコップ半分から一杯` | Arabic-kanji mix risks inconsistent reading |
| 47 | `1日...1000ミリリットルから1500ミリリットル` | `一日...千ミリリットルから千五百ミリリットル` | Large Arabic numerals have high reading variance |
| 57 | `30度` | `三十度` | Consistent kanji numeral reading |
| 61 | `28度以下...50パーセントから60パーセント` | `二十八度以下...五十パーセントから六十パーセント` | Multi-numeral line, all converted for consistency |
| 63 | `28度` | `二十八度` | Consistency with surrounding context |
| 64 | `28度...2度、3度` | `二十八度...二度、三度` | Eliminate mixed numeral styles |
| 65 | `26度` | `二十六度` | Consistency |
| 72 | `2時間や3時間` | `二時間や三時間` | Reading stability for counter expressions |
| 81 | `コップ1杯` | `コップ一杯` | Consistency |
| 89 | `コップ1杯` | `コップ一杯` | Consistency |
| 93 | `28度` | `二十八度` | Consistency |

**Note:** `3つ` (lines 5, 17, 70, 86, 101, 109) retained as-is because `3つ` is universally stable as みっつ across all major Japanese TTS engines. `57パーセント` and `65歳` (line 14) also retained — these are spoken statistics where Arabic numerals + パーセント/歳 are standard and stable.

### B. Quote Stabilization (Rule C — Quote-Fragment)

| Line | Before | After | Reason |
|---|---|---|---|
| 31 | `「いつもの疲れかな」と思いがちですが` | `いつもの疲れかなと思いがちですが` | Inner-quote fragment creates TTS pause artifact |
| 39 | `色だけで「大丈夫」と判断しないほうが` | `色だけで大丈夫と判断しないほうが` | Single-word quote disrupts spoken flow |
| 44 | `「飲み忘れ」がぐっと減ります` | `飲み忘れがぐっと減ります` | Unnecessary quote around common phrase |
| 51 | `「エアコンもつけてるし、部屋にいるから大丈夫」と思いがちですよね` | `エアコンもつけてるし部屋にいるから大丈夫と思いがちですよね` | Long inner-quote, removed for smoother reading + reduced comma inside |
| 57 | `「それほど暑くない」と思っていても` | `それほど暑くないと思っていても` | Single-phrase quote removed for flow |

### C. Comma Reduction (Rule B — Comma-Chain)

| Line | Before | After | Reason |
|---|---|---|---|
| 13 | `これは、体の自然な変化なので` | `これは体の自然な変化なので` | Unnecessary comma after これは |
| 15 | `そして、発生場所で` | `そして発生場所で` | Unnecessary comma after そして |
| 16 | `室内で過ごしているから安心、とは限らない` | `室内で過ごしているから安心とは限らない` | Comma creates unnatural pause |
| 29 | `これは、着替えるとき` | `これは着替えるとき` | Unnecessary comma |
| 50 | `部屋の中にいるのに暑い、ということ` | `部屋の中にいるのに暑いということ` | Comma before ということ is page-style |
| 85 | `夜の環境も、少し気にかけて` | `夜の環境も少し気にかけて` | Unnecessary comma |
| 95 | `お茶でも、お水でも` | `お茶でもお水でも` | Micro-comma in conversational list |
| 108 | `こうした相談先を、元気なうちに` | `こうした相談先を元気なうちに` | Page-style comma removed |
| 76 | `朝のだるさや頭のぼんやり感、じつは` | `朝のだるさや頭のぼんやり感は、じつは` | Added は to create proper topic marker landing instead of dangling comma |
| 103 | `だるさが続いたり、食欲がないと` | `だるさが続いたり食欲がないと` | Unnecessary comma in たり construction |

### D. Landing Stability (Rule A — Suspended Endings)

No suspended endings found in source. All 116 units land as complete thoughts. **No changes needed.**

### E. Mimetic Density (Rule E)

`カサカサ` (line 26) and `じわじわ` (line 73) retained — both are semantically essential and stable across engines. No excessive mimetic density detected. **No changes needed.**

## Safety Preservation Check

| Softener | Status | Note |
|---|---|---|
| SF01 (effectiveness softener) | ✅ Preserved | 目安, かもしれません, 変わることがあります — all intact |
| SF02 (consult clinician) | ✅ Preserved | かかりつけ医 references in S03, S07 intact |
| SF03 (numbers qualified) | ✅ Preserved | 一般的な目安, 望ましいとされています intact |
| SF04 (chronic condition) | ✅ Preserved | 心臓や腎臓に持病がある方 → かかりつけ医 intact |
| SF05 (closing safety) | ✅ Preserved | 急がなくても大丈夫です intact |

## Engine-Agnostic Compliance

| Check | Status |
|---|---|
| SSML notation | None |
| Phoneme tags | None |
| Kana-control syntax | None |
| Vendor dictionary format | None |
| AquesTalk notation | None |
| Ruby/furigana markup | None |
| Engine-specific hacks | None |
| **Overall** | **PASS — fully engine-agnostic** |

## Final Status

All normalization passes complete. Script updated in-place in `06_script_canonical.json`, `06_script_full.md`, and `06_script_metrics.json`. No meaning drift, no policy weakening, no new claims introduced. Script remains warm, natural, and suited to older listeners.
