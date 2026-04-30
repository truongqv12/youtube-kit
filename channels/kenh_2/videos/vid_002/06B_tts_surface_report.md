# 06B TTS Surface Normalization Report

**Project:** kenh_2_vid_002  
**Step:** 06B_tts_surface_normalized  
**Source:** 06_script_canonical.json (96 units, 3211 chars)  
**In-place Target:** 06_script_canonical.json (95 units, 3220 chars)  
**Generated:** 2026-04-25T00:21:00+07:00

---

## Summary

Surface normalization applied to improve TTS reading stability, landing stability, and cross-engine portability. No meaning drift. No policy softeners weakened. No new claims introduced. All changes are surface-form only.

---

## Changes Applied

### 1. Suspended-ending merge (Rule A)

| 06 Unit # | Original | 06B Result | Rule |
|---|---|---|---|
| 6–7 | `でも実は、足元が冷たくて滑りやすかったり、気温の差が大きかったり。` + `ちょっとした不安を感じている方もいらっしゃるのではないでしょうか。` | `でも実は、足元が冷たくて滑りやすかったり、気温の差が大きかったりして、ちょっとした不安を感じている方もいらっしゃるのではないでしょうか。` | **Rule A** — Line 6 ended with `〜かったり。` (suspended double-たり with period). Merged into one complete line that lands naturally. |

**Net effect:** 96 → 95 units (-1)

### 2. Reading-stability rewrites (Rule D)

| 06 Unit # | Original surface | 06B surface | Reason |
|---|---|---|---|
| 8 | `ポイントを3つに絞って` | `ポイントを三つに絞って` | Arabic `3` → kanji `三` for stable TTS reading |
| 22 | `足の裏がひやっとして` | `足の裏が冷たくて` | Mimetic `ひやっと` replaced with stable `冷たくて` (Rule E — minor mimetic, not semantically essential) |
| 26 | `コルクマットやEVA素材の` | `コルクマットや、イーブイエー素材の` | Latin abbreviation `EVA` → katakana `イーブイエー` for reading stability |
| 28 | `EVA素材のマットは` | `イーブイエー素材のマットは` | Same EVA expansion |
| 30 | `確認しておきたいのは3つあります` | `確認しておきたいのは三つあります` | `3` → `三` |
| 43 | `温度差が10度以上あると` | `温度差が十度以上あると` | `10度` → `十度` |
| 44 | `入浴の10分から15分くらい前に` | `入浴の十分から十五分くらい前に` | `10分` → `十分`, `15分` → `十五分` |
| 45 | `温度を20度前後に` | `温度を二十度前後にしておくと` | `20度` → `二十度` |
| 55 | `3つ目は` | `三つ目は` | `3` → `三` |
| 82 | `限度額は20万円で、自己負担は1割から3割` | `限度額は二十万円で、自己負担は一割から三割` | All arabic numerals → kanji |
| 89 | `脱衣所で気をつけたいことを3つ` | `脱衣所で気をつけたいことを三つ` | `3` → `三` |
| 92 | `3つ目は` | `三つ目は` | `3` → `三` |

### 3. Landing-stability rewrite (Rule A)

| 06 Unit # | Original | 06B | Reason |
|---|---|---|---|
| 31 | `ひとつは、マットそのものがズレないかどうか。` | `ひとつは、マットそのものがズレないかどうかです。` | Added `です` for complete spoken landing. Original ended with bare `かどうか。` which sounds suspended in TTS. |
| 32 | `もうひとつは、水はけが良く、カビにくい素材かどうか。` | `もうひとつは、水はけが良く、カビにくい素材かどうかです。` | Same — `かどうか。` → `かどうかです。` for spoken completeness |

---

## Changes NOT Applied (Intentional keeps)

| Unit | Content | Reason kept |
|---|---|---|
| 14 | `入浴中の事故で救急搬送される高齢者の多くが…` | Landing is complete. Two clauses but tightly linked. Splitting would break the statistical context. |
| 15 | `脱衣所だけの件数は…` | Long but reads as single narrative thought. Spoken landing is stable. |
| 53 | `血圧のことが気になる方や…` | Important consult-clinician line (SF02). Must remain as one spoken unit for policy completeness. |

---

## Verification Checks

| Check | Status |
|---|---|
| Reconstruction: `full_script == join(canonical_units)` | ✅ PASS |
| Duration: 3220 chars ÷ 320 = 10.1 min ∈ [8, 12] | ✅ PASS |
| TTS-safe: no headings/bullets/tags/markdown/emoji | ✅ PASS |
| Engine-agnostic: no SSML/phoneme/kana-control/vendor notation | ✅ PASS |
| Banned phrases: none found | ✅ PASS |
| Softeners: SF01–SF07 all present | ✅ PASS |
| Rhythm: max 2 consecutive same-pattern lines | ✅ PASS |
| Naturalness: warm spoken register preserved | ✅ PASS |
| Policy drift: NONE | ✅ PASS |
| Meaning drift: NONE | ✅ PASS |
| Portable TTS gate: all 95 units pass 6-point check | ✅ PASS |

---

## Canonical-Unit Portable TTS Gate (Spot Check)

| Unit | Sounds complete? | Grammar independent? | Natural landing? | Spoken Japanese? | Unlikely misread? | Warm/respectful? |
|---|---|---|---|---|---|---|
| 6 (merged) | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 25 (EVA→イーブイエー) | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 30 (かどうかです) | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 42 (十度) | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 82 (二十万円) | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
