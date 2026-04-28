import json
import csv
import sys

def main():
    try:
        # Load step 06
        with open("06_script_canonical.json", "r", encoding="utf-8") as f:
            s06 = json.load(f)
            units = s06["canonical_script_units"]

        # Load step 07
        s07 = []
        with open("07_image_prompt_table.csv", "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                s07.append(row["prompt_img_nano"])

        # Load step 08
        s08 = []
        with open("08_video_prompt_table.csv", "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                s08.append(row["prompt_video_veo3"])

        # QA constraints
        assert len(units) == len(s07) == len(s08), f"Row count mismatch: 06={len(units)}, 07={len(s07)}, 08={len(s08)}"

        qc_errors = []

        final_data = []
        for i in range(len(units)):
            text = units[i]
            img = s07[i]
            vid = s08[i]
            
            if not img.strip():
                qc_errors.append(f"Row {i+1}: Blank prompt_img_nano")
            if not vid.strip():
                qc_errors.append(f"Row {i+1}: Blank prompt_video_veo3")
                
            # Check for unwanted speech verbs in Veo, making sure to avoid triggering on our own negative prompts
            vid_lower = vid.lower()
            # remove our standard negative base from the check to avoid false positives
            vid_stripped = vid_lower.replace("no direct-to-camera speech", "").replace("no spoken dialogue", "").replace("no speech", "").replace("no talking", "").replace("no lip sync", "")
            if any(w in vid_stripped for w in ["speak", "talk", "says", "lipsync", "lip sync", "vocal"]):
                qc_errors.append(f"Row {i+1}: Potential speech embedded in non-dialogue prompt")

            final_data.append({
                "script_text": text,
                "prompt_img_nano": img,
                "prompt_video_veo3": vid
            })

        # Write the final CSV
        with open("09_final_three_column.csv", "w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=["script_text", "prompt_img_nano", "prompt_video_veo3"])
            writer.writeheader()
            for d in final_data:
                writer.writerow(d)

        qc_report = f"""# Export QC Report

## Row Counts
- Step 06 Rows: {len(units)}
- Step 07 Rows: {len(s07)}
- Step 08 Rows: {len(s08)}
- Final Export Rows: {len(final_data)}

## Checks
- Row counts match: {'PASS' if len(units) == len(s07) == len(s08) else 'FAIL'}
- Blank rows detected: {'FAIL' if any('Blank' in e for e in qc_errors) else 'PASS'}
- Speech/New text in non-dialogue: {'FAIL' if any('Potential speech' in e for e in qc_errors) else 'PASS'}
- `script_text` passes through directly: PASS
- Extra columns: PASS
- Row order preserved: PASS

## Errors
"""
        if not qc_errors:
            qc_report += "None.\n"
        else:
            for e in qc_errors:
                qc_report += f"- {e}\n"

        with open("09_export_qc_report.md", "w", encoding="utf-8") as f:
            f.write(qc_report)

        print("Export finished and QC report generated.")
        
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
