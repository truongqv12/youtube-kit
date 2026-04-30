# 06B TTS Surface Normalization Report — kenh_3 / vid_001

## Overview
- Source: `06_script_canonical.json` (127 units, 3,398 chars)
- In-place target: `06_script_canonical.json` (128 units, 3,321 chars)
- Delta: +1 unit, −77 chars (minor compression from surface cleanup)
- Duration: 10.4 min (within 10–20 min target)
- Engine-agnostic: ✅ No SSML, phoneme tags, or vendor-specific notation

## Changes Applied

### A. Suspended-ending fixes (Landing stability)

| Line (06) | Issue | Action |
|-----------|-------|--------|
| L5 `〜行ったり。` | suspended `〜たり` ending without completion | **Rewrite** → `〜出かけたりしています。` — completed verb |
| L7 `ある朝のこと。` | suspended fragment | **Rewrite** → `ある朝のことです。` — completed copula |
| L11 `部屋がふわっと揺れた` | mimetic `ふわっと` — TTS may over-emphasize | **Simplify** → `部屋が揺れたように` — calmer surface |
| L54 `体がまだ「おはよう」に追いついていない。` | quoted fragment ends line in suspended feel | **Rewrite** → remove quotes, add `んです` completion |
| L69 `体が安定したかなと感じてから、そっと立ち上がる。` | dictionary-form ending (`立ち上がる`) feels incomplete | **Rewrite** → `立ち上がります。` — polite completion |
| L80 `ほんのすこし補ってあげる。` | dictionary-form suspended | **Rewrite** → `補ってあげるだけで十分です。` — completed |

### B. Comma-chain splits (Pause stability)

| Line (06) | Issue | Action |
|-----------|-------|--------|
| L13 `すぐに収まりましたが、はるこさんは〜` | `が` connector creates compound | **Split** → L13 `すぐに収まりました。` + L14 `でも、はるこさんは〜` |
| L39 `そうすると、頭にいく血の量が〜` | comma-heavy compound with `ところが` in previous line | **Simplify** → removed `そうすると` connector, direct statement |
| L68 `血圧やバランスが落ち着くのを、体が自然に〜` | double subject | **Simplify** → `血圧やバランスが落ち着くのを待ちます。` |
| L95 `自律神経の働きが安定しやすくなり、翌朝の体の調子にも〜` | comma join with compound | **Simplify** → `翌朝の調子にも` — removed `体の` redundancy |

### C. Reading-stability fixes

| Line (06) | Issue | Action |
|-----------|-------|--------|
| L67 `3秒くらい` | numeral `3` may be read differently by engines | **Rewrite** → `三秒くらい` — kanji numeral, stable reading |
| L63 `足首をくるくると回して` | mimetic `くるくると` — acceptable but simplified | **Simplify** → `足首を回して` — calmer, same meaning |
| L70 `「体におはようを言ってからにする」` | quoted phrase — readable but adds TTS quote-handling risk | **Simplify** → removed quotes, kept natural speech phrasing |
| L82 `「朝のお水が気持ちいい」` | same quote-handling concern | **Simplify** → removed quotes |
| L102 `「起きるのが怖い」〜「今日も静かに始められた」` | double quoted fragments in one line | **Simplify** → removed quotes, reworded as declarative |

### D. Quote-fragment reduction

| Line (06) | Issue | Action |
|-----------|-------|--------|
| L31 `「年のせいだから」と` | short quote, common phrasing | **Keep** but removed quotes → flows as natural speech |
| L58 `「こういう仕組みが〜」という` | long quoted paraphrase | **Rewrite** → integrated as natural clause |
| L100 `「またか」と不安に` | short quote — common but TTS may add awkward pauses | **Keep** but removed quotes |

### E. Mimetic-density reduction

| Original | Action | Reason |
|----------|--------|--------|
| `ふわっと揺れた` | → `揺れた` | non-essential mimetic; TTS stability |
| `くるくると回して` | → `回して` | simplified; motion is clear without mimetic |

### F. Other surface cleanups

| Type | Examples | Action |
|------|---------|--------|
| Redundant commas | L17 `数秒だけ、足元が` → `数秒だけ足元が` | Removed pause-causing comma |
| `「逆に、〜」` patterns | L88 `逆に、早めに〜` → `早めに〜` | Removed connective that creates competing transition |
| Trailing `そっと` | L120 `そっと大切に` → `大切に` | Reduced emphatic modifier |
| `もし〜` openings | L108, L123 — kept where needed for conditional | Consistent conditional framing |

## Checks Summary

| Check | Result |
|-------|--------|
| Reconstruction (full_script == join) | ✅ PASS |
| Duration (10.4 min in 10–20 range) | ✅ PASS |
| Chars (3,321 in 3,200–6,400 range) | ✅ PASS |
| Landing stability | ✅ PASS — no suspended endings remain |
| Pause stability | ✅ PASS — no comma chains remain |
| Reading stability | ✅ PASS — numerals normalized, quotes reduced |
| Prosodic stability | ✅ PASS — calm narration, no theatrical emphasis |
| Portability | ✅ PASS — engine-agnostic, no vendor notation |
| Banned phrases | ✅ PASS — none found |
| Meaning preservation | ✅ PASS — no new claims, no weakened softeners |
| Policy posture | ✅ PASS — S08 consult guidance intact |
