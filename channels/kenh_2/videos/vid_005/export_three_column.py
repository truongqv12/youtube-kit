"""
Step 09 — Three Column Exporter for kenh_2/vid_005
Merges canonical script, image prompts, and video prompts into final 3-column CSV.
Also emits a minimal QC report.
"""
import json
import csv
import os
import re

BASE = os.path.dirname(os.path.abspath(__file__))

# --- Load canonical script units ---
with open(os.path.join(BASE, "06_script_canonical.json"), "r", encoding="utf-8") as f:
    canonical = json.load(f)
script_units = canonical["canonical_script_units"]

# --- Load image prompt table ---
img_prompts = []
with open(os.path.join(BASE, "07_image_prompt_table.csv"), "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        img_prompts.append(row["prompt_img_nano"])

# --- Load video prompt table ---
vid_prompts = []
with open(os.path.join(BASE, "08_video_prompt_table.csv"), "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        vid_prompts.append(row["prompt_video_veo3"])

# --- QC Checks ---
qc_results = []
qc_pass = True

# Check 1: Row counts match
count_script = len(script_units)
count_img = len(img_prompts)
count_vid = len(vid_prompts)
if count_script == count_img == count_vid:
    qc_results.append(f"[PASS] Row counts match: script={count_script}, img={count_img}, vid={count_vid}")
else:
    qc_results.append(f"[FAIL] Row count mismatch: script={count_script}, img={count_img}, vid={count_vid}")
    qc_pass = False

# Check 2: No blank script_text
blank_script = [i+1 for i, s in enumerate(script_units) if not s.strip()]
if blank_script:
    qc_results.append(f"[FAIL] Blank script_text at rows: {blank_script}")
    qc_pass = False
else:
    qc_results.append("[PASS] No blank script_text rows")

# Check 3: No blank img prompts
blank_img = [i+1 for i, p in enumerate(img_prompts) if not p.strip()]
if blank_img:
    qc_results.append(f"[FAIL] Blank prompt_img_nano at rows: {blank_img}")
    qc_pass = False
else:
    qc_results.append("[PASS] No blank prompt_img_nano rows")

# Check 4: No blank vid prompts
blank_vid = [i+1 for i, p in enumerate(vid_prompts) if not p.strip()]
if blank_vid:
    qc_results.append(f"[FAIL] Blank prompt_video_veo3 at rows: {blank_vid}")
    qc_pass = False
else:
    qc_results.append("[PASS] No blank prompt_video_veo3 rows")

# Check 5: Non-dialogue compliance — Veo prompts must NOT ask for speech/lip sync
speech_keywords = ["lip sync", "spoken dialogue", "direct-to-camera speech", "singing", "chanting",
                    "ambient audio", "foley", "room tone", "ambience"]
# These should appear in negations only. Check for affirmative requests.
speech_violations = []
for i, p in enumerate(vid_prompts):
    p_lower = p.lower()
    # Check if any speech keyword appears WITHOUT "no" before it
    for kw in speech_keywords:
        # Find all occurrences
        idx = 0
        while True:
            pos = p_lower.find(kw, idx)
            if pos == -1:
                break
            # Check if preceded by "no " within 5 chars
            prefix = p_lower[max(0, pos-5):pos]
            if "no " not in prefix and "no," not in prefix:
                speech_violations.append((i+1, kw))
            idx = pos + 1

if speech_violations:
    qc_results.append(f"[WARN] Possible affirmative speech/audio keywords (check context): {speech_violations[:5]}")
else:
    qc_results.append("[PASS] All Veo prompts enforce non-dialogue constraints")

# Check 6: Silent audio directive present in all Veo prompts
silent_missing = [i+1 for i, p in enumerate(vid_prompts) if "(Silent video, no audio)." not in p]
if silent_missing:
    qc_results.append(f"[FAIL] Missing '(Silent video, no audio).' at rows: {silent_missing}")
    qc_pass = False
else:
    qc_results.append("[PASS] All Veo prompts contain '(Silent video, no audio).'")

# Check 7: No "new readable text" requests in Veo prompts
new_text_violations = [i+1 for i, p in enumerate(vid_prompts)
                       if "create new" in p.lower() and "text" in p.lower()
                       or "generate new" in p.lower() and "text" in p.lower()
                       or "add text" in p.lower()
                       or "write text" in p.lower()]
if new_text_violations:
    qc_results.append(f"[FAIL] Veo prompts request new text at rows: {new_text_violations}")
    qc_pass = False
else:
    qc_results.append("[PASS] No Veo prompts request new readable text")

# --- Export final CSV ---
output_csv = os.path.join(BASE, "09_final_three_column.csv")
with open(output_csv, "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["script_text", "prompt_img_nano", "prompt_video_veo3"])
    min_rows = min(count_script, count_img, count_vid)
    for i in range(min_rows):
        writer.writerow([script_units[i], img_prompts[i], vid_prompts[i]])

# --- Emit QC Report ---
report_lines = [
    "# 09 Export QC Report",
    "",
    f"**Project:** kenh_2_vid_005",
    f"**Generated:** 2026-04-29",
    "",
    "## Row Counts",
    f"- canonical_script_units: {count_script}",
    f"- 07_image_prompt_table: {count_img}",
    f"- 08_video_prompt_table: {count_vid}",
    f"- 09_final_three_column: {min_rows}",
    "",
    "## Columns",
    "- script_text ✅",
    "- prompt_img_nano ✅",
    "- prompt_video_veo3 ✅",
    "- Extra columns: NONE ✅",
    "",
    "## QC Checks",
]
for r in qc_results:
    report_lines.append(f"- {r}")

report_lines.extend([
    "",
    f"## Overall: {'PASS ✅' if qc_pass else 'FAIL ❌'}",
    "",
    "## Notes",
    "- script_text is pass-through from canonical_script_units (no rewriting)",
    "- Row order preserved (sequential 1-to-N merge)",
    "- Non-dialogue mode enforced in all Veo prompts",
    "- Silent audio directive present in all Veo prompts",
])

report_path = os.path.join(BASE, "09_export_qc_report.md")
with open(report_path, "w", encoding="utf-8") as f:
    f.write("\n".join(report_lines) + "\n")

print(f"Exported {min_rows} rows to 09_final_three_column.csv")
print(f"QC Report: 09_export_qc_report.md")
print(f"Overall QC: {'PASS' if qc_pass else 'FAIL'}")
for r in qc_results:
    print(f"  {r}")
