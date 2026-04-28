import csv

data = []
with open("07_image_prompt_table.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for i, row in enumerate(reader):
        idx = int(row["unit_index"])
        arch = row["scene_archetype"]
        img_prompt = row["prompt_img_nano"].lower()
        
        mode = "first_frame_only"
        
        # Determine duration
        if arch == "object_focus":
            dur = 4
        elif arch == "environment_bridge":
            dur = 8
        else:
            dur = 6

        neg_base = "No lip sync, no direct-to-camera speech, no spoken dialogue, no singing, no chanting, no mouth-performance acting, no ambient audio requests."

        # Determine motion strategy
        if arch == "host_anchor":
            strat = "host_gentle_push" if i % 2 == 0 else "host_listening_drift"
            cam = "Gentle slow camera push." if i % 2 == 0 else "Subtle sideways camera drift."
            sub = "The subject blinks naturally, presenting a warm reassuring postural adjustment." if i % 2 == 0 else "The subject tilts their head slightly in a soft affirmative motion."
            env = "Background elements remain still."
            mood = "Preserve the warm conversational mood, exact identity, and wardrobe."
            neg = neg_base
            
        elif arch == "everyday_example":
            strat = "daily_action_follow" if i % 2 == 0 else "daily_pause_observe"
            cam = "Subtle observational follow drift." if i % 2 == 0 else "Slow camera pan revealing the scene."
            sub = "The subject executes a slow, deliberate everyday movement, while clothing shifts gently." if "woman" in img_prompt else "The subject adjusts their posture deliberately."
            env = "Mild air currents visible in the sunlight."
            mood = "Preserve the practical domestic mood and exact human identity."
            neg = neg_base + " No fast dramatic action."
            
        elif arch == "object_focus":
            strat = "object_inspection_push" if i % 2 == 0 else "object_in_use_micro"
            cam = "Slight slow macro push." if i % 2 == 0 else "Gentle tilt downward towards the object."
            sub = "The specific object remains steadily in focus."
            env = "Subtle air currents drift around the highlighted area."
            mood = "Preserve the educational clarity and exact placement of the item."
            neg = neg_base + " No disruptive camera shakes, no new readable text."
            
        elif arch == "process_metaphor":
            strat = "process_layer_drift" if i % 2 == 0 else "process_signal_pulse"
            cam = "Controlled parallax drift across the graphic elements." if i % 2 == 0 else "Subtle breathing push into the scene."
            sub = "Abstract elements float or pulse very gently for educational emphasis."
            env = "Background and foreground layers separate slightly."
            mood = "Preserve the symbolic explanation and graphic clarity exactly as-is."
            neg = neg_base + " No chaotic physics, no scene redesign, no new readable text."
            
        else: # environment_bridge
            strat = "environment_breathing_pan" if i % 2 == 0 else "environment_observe_tilt"
            cam = "Slow breathing pan across the serene room." if i % 2 == 0 else "Subtle tilt upward towards the ceiling."
            sub = "No human action."
            env = "Curtains or distant foliage drift gently in the summer breeze, light beams move slowly."
            mood = "Preserve the calm time-of-day lighting and peaceful domestic mood."
            neg = neg_base + " No fast pan, no lighting changes."

        # Add text preservation if policy requires
        text_pres = "Preserve any existing visible text exactly as-is." if row.get("visible_text_policy") != "no_readable_text" else ""
        
        # Inject specific features based on the image prompt content
        if "stove" in img_prompt:
            env += " Gentle steam or heat haze is visible near the stove."
        if "water" in img_prompt or "glass" in img_prompt:
            sub += " Water elements hold stable structure."
        if "refrigerator" in img_prompt:
            env += " Keep refrigerator items exactly as arranged without morphing."
        if "sponge" in img_prompt:
            sub += " Sponge texture and moisture remain crisp."
        if "fire" in img_prompt or "flame" in img_prompt:
            sub += " Flame or heat indicators flicker very softly and educationally."

        audio = "(Silent video, no audio)."
        
        prompt_parts = [cam, sub, env, mood, text_pres, audio, neg]
        prompt = " ".join([p for p in prompt_parts if p])

        data.append({
            "unit_index": idx,
            "i2v_mode": mode,
            "motion_strategy": strat,
            "recommended_duration_sec": dur,
            "prompt_video_veo3": prompt
        })

with open("08_video_prompt_table.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["unit_index", "i2v_mode", "motion_strategy", "recommended_duration_sec", "prompt_video_veo3"])
    writer.writeheader()
    for d in data:
        writer.writerow(d)
        
print("Generated 08_video_prompt_table.csv")
