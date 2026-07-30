from PIL import Image

def create_gif_vertical(input_path, output_path, frames, fps, frame_height=30):
    img = Image.open(input_path)
    w, h = img.size
    
    gif_frames = []
    for i in range(frames):
        top = i * frame_height
        bottom = top + frame_height
        cropped = img.crop((0, top, w, bottom))
        gif_frames.append(cropped)
        
    duration = int(1000 / fps)
    
    gif_frames[0].save(
        output_path,
        save_all=True,
        append_images=gif_frames[1:],
        duration=duration,
        loop=0
    )

create_gif_vertical('CHI_fully_under_control_animated.png', r'c:\Users\Kimina\.gemini\antigravity-ide\brain\eb8f3218-93b3-4f7a-9f64-738e60391cd2\scratch\CHI_fully_under_control_animated_new.gif', 40, 40)
create_gif_vertical('CHI_warning_enemy_present_animated.png', r'c:\Users\Kimina\.gemini\antigravity-ide\brain\eb8f3218-93b3-4f7a-9f64-738e60391cd2\scratch\CHI_warning_enemy_present_animated_new.gif', 72, 40)
