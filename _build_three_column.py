"""
Step 09 — Three Column Exporter + Minimal QA
Merges:
  - 06_script_canonical.json  → script_text (pass-through)
  - 07_image_prompt_table.csv → prompt_img_nano
  - 08_video_prompt_table.csv → prompt_video_veo3
into 09_final_three_column.csv (exactly 3 columns, no metadata).
Also emits 09_export_qc_report.md.
"""
import json
import csv
import re
import sys
from pathlib import Path

BASE = Path("channels/kenh_3/videos/vid_001")

# ── Load canonical script units ──
with open(BASE / "06_script_canonical.json", encoding="utf-8") as f:
    script_data = json.load(f)
script_units = script_data["canonical_script_units"]

# ── Load image prompts ──
img_rows = []
with open(BASE / "07_image_prompt_table.csv", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        img_rows.append(row)

# ── Load video prompts ──
vid_rows = []
with open(BASE / "08_video_prompt_table.csv", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        vid_rows.append(row)

# ── QA checks ──
errors = []

# 1. Row count match
n_script = len(script_units)
n_img = len(img_rows)
n_vid = len(vid_rows)

if n_script != n_img:
    errors.append(f"ROW_MISMATCH: script={n_script}, image_prompts={n_img}")
if n_script != n_vid:
    errors.append(f"ROW_MISMATCH: script={n_script}, video_prompts={n_vid}")
if n_img != n_vid:
    errors.append(f"ROW_MISMATCH: image_prompts={n_img}, video_prompts={n_vid}")

# Use the minimum to avoid index errors, but report the mismatch
n_rows = min(n_script, n_img, n_vid)

# 2. Check for blank prompts
blank_img = []
blank_vid = []
for i in range(n_rows):
    if not img_rows[i].get("prompt_img_nano", "").strip():
        blank_img.append(i)
    if not vid_rows[i].get("prompt_video_veo3", "").strip():
        blank_vid.append(i)

if blank_img:
    errors.append(f"BLANK_IMG_PROMPT: rows {blank_img}")
if blank_vid:
    errors.append(f"BLANK_VID_PROMPT: rows {blank_vid}")

# 3. Check for blank script lines
blank_script = [i for i in range(n_rows) if not script_units[i].strip()]
if blank_script:
    errors.append(f"BLANK_SCRIPT: rows {blank_script}")

# 4. Non-dialogue check: Veo prompts must not ASK FOR speech (ignore negative constraints)
speech_patterns = [
    r'(?<!\bno\s)lip\s*sync',
    r'(?<!\bno\s)spoken\s+dialogue',
    r'(?<!\bno\s)direct.to.camera\s+speech',
    r'(?<!\bno\s)singing',
    r'(?<!\bno\s)chanting',
    r'\bsays?\s',
    r'\bspeaking\b(?!\s*pose)',
    r'\btalks?\s+to\s+camera',
]
speech_violations = []
for i in range(n_rows):
    prompt = vid_rows[i].get("prompt_video_veo3", "").lower()
    for pat in speech_patterns:
        if re.search(pat, prompt):
            speech_violations.append((i, pat))
            break

if speech_violations:
    errors.append(f"SPEECH_IN_VEO: {speech_violations}")

# 5. Check Veo prompts don't request new readable text
new_text_violations = []
for i in range(n_rows):
    prompt = vid_rows[i].get("prompt_video_veo3", "").lower()
    if "generate text" in prompt or "create text" in prompt or "write text" in prompt or "add text" in prompt:
        new_text_violations.append(i)

if new_text_violations:
    errors.append(f"NEW_TEXT_IN_VEO: rows {new_text_violations}")

# 6. Check silent audio directive present in every Veo prompt
missing_silent = []
for i in range(n_rows):
    prompt = vid_rows[i].get("prompt_video_veo3", "")
    if "(Silent video, no audio)." not in prompt:
        missing_silent.append(i)

if missing_silent:
    errors.append(f"MISSING_SILENT_DIRECTIVE: rows {missing_silent}")

# 7. Row order preserved (unit_index must match 0..n-1)
order_violations = []
for i in range(n_rows):
    img_idx = int(img_rows[i].get("unit_index", -1))
    vid_idx = int(vid_rows[i].get("unit_index", -1))
    if img_idx != i or vid_idx != i:
        order_violations.append((i, img_idx, vid_idx))

if order_violations:
    errors.append(f"ORDER_VIOLATION: {order_violations}")

# ── Determine pass/fail ──
qc_pass = len(errors) == 0

# ── Write 09_final_three_column.csv ──
output_csv = BASE / "09_final_three_column.csv"
with open(output_csv, "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["script_text", "prompt_img_nano", "prompt_video_veo3"])
    for i in range(n_rows):
        writer.writerow([
            script_units[i],
            img_rows[i]["prompt_img_nano"],
            vid_rows[i]["prompt_video_veo3"]
        ])

# ── Write 09_export_qc_report.md ──
report_lines = []
report_lines.append("# 09 Export QC Report")
report_lines.append("")
report_lines.append(f"**Channel:** kenh_3")
report_lines.append(f"**Video:** vid_001")
report_lines.append(f"**Generated:** 2026-04-28T21:07:00+07:00")
report_lines.append("")
report_lines.append("## Row Counts")
report_lines.append(f"- canonical_script_units: {n_script}")
report_lines.append(f"- image_prompt_table rows: {n_img}")
report_lines.append(f"- video_prompt_table rows: {n_vid}")
report_lines.append(f"- final_three_column rows: {n_rows}")
report_lines.append("")
report_lines.append("## QA Checks")
report_lines.append("")
report_lines.append(f"| Check | Result |")
report_lines.append(f"|---|---|")
report_lines.append(f"| Row count match (06=07=08) | {'✅ PASS' if n_script == n_img == n_vid else '❌ FAIL'} |")
report_lines.append(f"| No blank script_text | {'✅ PASS' if not blank_script else '❌ FAIL'} |")
report_lines.append(f"| No blank prompt_img_nano | {'✅ PASS' if not blank_img else '❌ FAIL'} |")
report_lines.append(f"| No blank prompt_video_veo3 | {'✅ PASS' if not blank_vid else '❌ FAIL'} |")
report_lines.append(f"| No speech in Veo prompts | {'✅ PASS' if not speech_violations else '❌ FAIL'} |")
report_lines.append(f"| No new text in Veo prompts | {'✅ PASS' if not new_text_violations else '❌ FAIL'} |")
report_lines.append(f"| Silent directive present | {'✅ PASS' if not missing_silent else '❌ FAIL'} |")
report_lines.append(f"| Row order preserved | {'✅ PASS' if not order_violations else '❌ FAIL'} |")
report_lines.append(f"| Exactly 3 columns | ✅ PASS |")
report_lines.append(f"| script_text is pass-through | ✅ PASS |")
report_lines.append("")
report_lines.append(f"## Overall Result")
report_lines.append("")
report_lines.append(f"**{'✅ ALL CHECKS PASSED' if qc_pass else '❌ SOME CHECKS FAILED'}**")

if errors:
    report_lines.append("")
    report_lines.append("## Error Details")
    for e in errors:
        report_lines.append(f"- {e}")

report_lines.append("")

with open(BASE / "09_export_qc_report.md", "w", encoding="utf-8") as f:
    f.write("\n".join(report_lines))

print(f"=== Export complete ===")
print(f"  CSV: {output_csv} ({n_rows} data rows)")
print(f"  QC:  {'PASS' if qc_pass else 'FAIL'}")
if errors:
    for e in errors:
        print(f"  [WARN] {e}")
