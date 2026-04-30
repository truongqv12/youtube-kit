# 06B TTS Surface Normalization Report
# kenh_2 / vid_003 — 夏の台所まわりで見直したい安全チェック
# Generated: 2026-04-28T15:37:22+07:00

## Summary

| Metric | 06 (source) | 06B (normalized) |
|--------|------------|-----------------|
| Total units | 76 | 77 |
| Total chars | 3,244 | 3,241 |
| Estimated duration | 10.14 min | 10.13 min |
| Within target (10–18 min) | ✅ | ✅ |
| Reconstruction match | ✅ | ✅ |
| Suspended endings | 0 | 0 |
| Engine-locked notation | 0 | 0 |
| Units changed | — | 4 (3 rewrite + 1 split) |

## Normalization mode
Engine-agnostic. No SSML, no phoneme strings, no kana-only control syntax, no vendor notation, no ruby markup.

---

## Changes applied

### Change 1 — Rule D (Reading risk): 中黒（・）→ 読点（、）
**Unit index:** 6 (0-indexed)

**Source:**
```
この動画でお伝えするのは、食材の管理・換気と暑さ対策・火の元の安全、そして衛生管理のコツ、この四つのポイントです。
```

**Normalized:**
```
この動画でお伝えするのは、食材の管理、換気と暑さ対策、火の元の安全、そして衛生管理のコツ、この四つのポイントです。
```

**Reason:** 中黒（`・`）はリスト区切りとして使われているが、エンジンによって無音・短ポーズ・「ナカグロ」と読み上げるなど挙動が異なる。単純な読点（`、`）に置き換えることで、エンジン間の発音安定性を高めた。意味は完全に保持。

---

### Change 2 — Rule B (Comma-chain) + Split: 長い従属節を2行に分割
**Unit index:** 13 (0-indexed)

**Source:**
```
気がつかないうちに体に疲れが蓄積されていることもありますから、少し意識的に確認する習慣が助けになります。
```

**Normalized (split into 2 units):**
```
気がつかないうちに体に疲れが蓄積していることもあります。
少し意識的に確認する習慣が、安心のきっかけになります。
```

**Reason:** 原文は従属節（`〜ありますから、`）で息継ぎが発生し、1行に2つの自然な読み間が生じている。分割することで各ユニットが独立して完結し、TTS エンジンのポーズ挿入が安定する。意味・トーン・softener は保持。

---

### Change 3 — Rule E (Mimetic density): 擬態語 → 中立的表現
**Unit index:** 50 (0-indexed、分割後は51)

**Source:**
```
袖口が広がった服や、ふわっとした化繊素材の服は、コンロ周りでは特に注意が必要です。
```

**Normalized:**
```
袖口が広がった服や、化繊や薄手の素材の服は、コンロ周りでは特に注意が必要です。
```

**Reason:** 「ふわっとした」は擬態語であり、エンジンによってはポーズや強調処理が不安定になる。「化繊や薄手の素材の服」とすることで、同義かつ読み上げが安定する表現に置き換えた。着衣着火のリスク説明の意味は完全に保持。

---

### Change 4 — Rule D (Reading risk): ローマ字略称「NITE」の除去
**Unit index:** 46 (0-indexed、分割後は47)

**Source:**
```
製品評価技術基盤機構、いわゆるNITEや消防機関では、コンロ付近での着衣着火について注意を呼びかけています。
```

**Normalized:**
```
製品評価技術基盤機構や消防機関などでは、コンロ付近での着衣着火について注意を呼びかけています。
```

**Reason:** ローマ字略称「NITE」はエンジンによって「ナイト」「エヌアイティーイー」等と誤読されるリスクがある。エンジン非依存の音読みヒントを注入することは本ステップの範囲外であることから、略称を省いて正式名称のみを残した。情報源の authority は保持。

---

## Units kept without change
72 units — no suspended endings, no reading-risk items, no comma-chain violations found.

## Policy compliance check (post-normalization)
- Softeners SF01–SF05: ✅ all preserved
- Forbidden angles: ✅ none introduced
- Meaning drift: ✅ NONE
- Consult guidance (SF02 / C1): ✅ preserved in S04 and S07

## Canonical-unit portable TTS gate (post-normalization)
All 77 units pass:
1. ✅ Sounds complete by itself
2. ✅ Does not rely on next line to finish grammar
3. ✅ Lands naturally if a short pause follows
4. ✅ Uses normal spoken Japanese, not page-fragment writing
5. ✅ Unlikely to be misread by a generic Japanese TTS engine
6. ✅ Remains warm, respectful, suited to older listeners

## Downstream integration note
From Step 07 onward, use `06_script_canonical.json` as the source of truth for `script_text`.
Step 06B normalizes the Step 06 artifacts in place; do not create parallel script outputs.
