import json
import csv

# Read Canonical
with open("06_script_canonical.json", "r", encoding="utf-8") as f:
    units = json.load(f)["canonical_script_units"]

# Read 07
with open("07_image_prompt_table.csv", "r", encoding="utf-8") as f:
    s07_rows = list(csv.DictReader(f))

# Read 08
with open("08_video_prompt_table.csv", "r", encoding="utf-8") as f:
    s08_rows = list(csv.DictReader(f))

# Read full md
with open("06_script_full.md", "r", encoding="utf-8") as f:
    full_lines = [l.strip() for l in f if l.strip()]

out_07 = []
out_08 = []

pointer_old = 0
for i, can_unit in enumerate(units):
    can_clean = can_unit.replace(" ", "").replace("　", "")
    
    start_idx = pointer_old
    cur_text = ""
    
    while pointer_old < len(full_lines):
        line = full_lines[pointer_old].replace(" ", "").replace("　", "")
        cur_text += line
        pointer_old += 1
        if can_clean == cur_text or cur_text in can_clean:
            if can_clean == cur_text:
                break
        elif can_clean.startswith(cur_text):
            continue
        else:
            # Over or mismatch, break to avoid infinite loop
            break
            
    if start_idx < len(s07_rows):
        row07 = s07_rows[start_idx].copy()
        row07["unit_index"] = i + 1
        out_07.append(row07)
        
        row08 = s08_rows[start_idx].copy()
        row08["unit_index"] = i + 1
        out_08.append(row08)
    else:
        # Fallback
        row07 = s07_rows[-1].copy()
        row07["unit_index"] = i + 1
        out_07.append(row07)
        
        row08 = s08_rows[-1].copy()
        row08["unit_index"] = i + 1
        out_08.append(row08)

# Write out fixed files
with open("07_image_prompt_table.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=list(out_07[0].keys()))
    writer.writeheader()
    writer.writerows(out_07)

with open("08_video_prompt_table.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=list(out_08[0].keys()))
    writer.writeheader()
    writer.writerows(out_08)

print(f"Alignment fixed! 07 rows: {len(out_07)}, 08 rows: {len(out_08)}")
