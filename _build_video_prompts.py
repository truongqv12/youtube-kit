import csv

input_file = "channels/kenh_3/videos/vid_001/07_image_prompt_table.csv"
output_file = "channels/kenh_3/videos/vid_001/08_video_prompt_table.csv"

def generate_video_prompt(row):
    archetype = row["scene_archetype"]
    host_usage = row["host_usage"]
    
    i2v_mode = "first_frame_only"
    
    if archetype == "host_anchor":
        motion_strategy = "host_gentle_push"
        duration = 6
        camera = "Very slow, subtle push-in camera motion."
        subject = "The elderly Japanese narrator breathes gently, eyes blinking naturally, maintaining a warm, steady, reassuring expression."
        env = "Soft ambient light shifts almost imperceptibly."
        mood = "The atmosphere is warm, reassuring, and calm."
        negative = "No rapid movement, no speech, no lip movement, no vocalization, no mouth-open acting."
    elif archetype == "everyday_example":
        motion_strategy = "daily_action_follow"
        duration = 6
        camera = "Gentle, observing static shot with a very subtle pan."
        subject = "The elderly woman moves with slow, deliberate micro-movements, her hands shifting slightly and posture adjusting naturally."
        env = "Dust motes drift softly in the warm light; subtle fabric movement."
        mood = "The atmosphere is serene, lived-in, and peaceful."
        negative = "No sudden movements, no speech, no lip sync, no dramatic falls or action."
    elif archetype == "environment_bridge":
        motion_strategy = "environment_breathing_pan"
        duration = 4
        camera = "Slow, atmospheric pan across the quiet Japanese space."
        subject = "The scene remains still."
        env = "Dust motes dance softly in the warm shafts of light; a faint breeze barely stirs a curtain."
        mood = "The atmosphere is quiet, contemplative, and still."
        negative = "No fast pans, no sudden changes, no character presence."
    elif archetype == "process_metaphor":
        motion_strategy = "process_layer_drift"
        duration = 6
        camera = "Slow, subtle parallax drift camera motion."
        subject = "The educational symbolic elements gently float or pulse with a soft, slow rhythm."
        env = "The abstract background softly shifts to provide depth."
        mood = "The atmosphere is clean, educational, and non-alarming."
        negative = "No rapid pulsing, no flashing, no medical horror, no jarring motion."
    elif archetype == "comparison_pair":
        motion_strategy = "comparison_parallax_hold"
        duration = 6
        camera = "Static observing shot with a very gentle push-in."
        subject = "The split-screen elements hold their positions while exhibiting slow, isolated micro-movements."
        env = "Soft, continuous ambient light on both sides."
        mood = "The atmosphere is analytical and calmly educational."
        negative = "No fast transitions, no erratic movement."
    elif archetype == "object_focus":
        motion_strategy = "object_inspection_push"
        duration = 4
        camera = "Slow, intimate push-in camera motion on the object."
        subject = "The object remains still while fulfilling its purpose."
        env = "Subtle light reflections shift slowly across the object's surface."
        mood = "The atmosphere is quiet and focused."
        negative = "No erratic movement, no character action."
    else:
        motion_strategy = "daily_action_follow"
        duration = 6
        camera = "Slow gentle camera movement."
        subject = "Subtle, natural micro-movements."
        env = "Soft ambient light."
        mood = "The atmosphere is calm."
        negative = "No rapid movement, no speech."

    audio = "(Silent video, no audio)."
    
    prompt = f"{camera} {subject} {env} {mood} {audio} {negative}"
    
    return [row["unit_index"], i2v_mode, motion_strategy, str(duration), prompt]

with open(input_file, mode='r', encoding='utf-8') as infile, \
     open(output_file, mode='w', encoding='utf-8', newline='') as outfile:
    
    reader = csv.DictReader(infile)
    writer = csv.writer(outfile)
    
    # Write header
    writer.writerow(["unit_index", "i2v_mode", "motion_strategy", "recommended_duration_sec", "prompt_video_veo3"])
    
    for row in reader:
        writer.writerow(generate_video_prompt(row))

print("Video prompt table generated successfully.")
