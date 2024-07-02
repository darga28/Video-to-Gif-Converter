import moviepy.editor as mp
import whisper
import cv2
import numpy as np
import os

def calculate_duration(start_time, end_time):
    return end_time - start_time

def split_captions_into_segments(segments, segment_duration):
    caption_segments = []
    current_segment = ""

    for segment in segments:
        start_time = segment['start']
        end_time = segment['end']
        caption_text = segment['text']

        # Calculate the duration of this caption segment
        duration = calculate_duration(start_time, end_time)

        # Split the caption text into sentences
        sentences = caption_text.split(". ")

        for sentence in sentences:
            if len(current_segment) + len(sentence) + 1 <= segment_duration:
                current_segment += sentence + " " 
            else:
                if current_segment.strip():
                    caption_segments.append(current_segment.strip())
                current_segment = sentence + " "  # Start new segment

    # Add the last segment if there's any remaining text
    if current_segment.strip():
        caption_segments.append(current_segment.strip())

    return caption_segments


def video_to_segmented_gifs_with_captions(video_path, output_dir, segment_duration=2, language="en", fps=10, text_extraction="whisper", text_rendering="overlay", resize_factor=1.0):
    """Transcribes a video, segments it into GIFs with captions, and saves them to an output directory."""

    # Load video clip
    clip = mp.VideoFileClip(video_path)

    # Resize frames if requested
    if resize_factor != 1.0:
        clip = clip.resize(resize_factor)

    # Extract captions using Whisper
    if text_extraction == "whisper":
        model = whisper.load_model("base") 
        result = model.transcribe(video_path, language=language)
        segments = result['segments']
    else:
        raise ValueError("Invalid text extraction method: {}".format(text_extraction))

    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Split captions into segments
    caption_segments = split_captions_into_segments(segments, segment_duration)

    # Create and save GIF segments with captions
    num_segments = len(caption_segments)

    for i in range(num_segments):
        caption = caption_segments[i]

        # Determine start and end times for this segment
        start_time = i * segment_duration
        end_time = min(start_time + segment_duration, clip.duration)

        subclip = clip.subclip(start_time, end_time).set_fps(fps)

        if text_rendering == "overlay":
            def add_caption(get_frame, t):
                frame = get_frame(t)
                frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

                # Calculate text size and position
                text = caption
                font = cv2.FONT_HERSHEY_SIMPLEX
                font_scale = 1.5
                font_thickness = 2
                text_size = cv2.getTextSize(text, font, font_scale, font_thickness)[0]
                text_x = int((frame.shape[1] - text_size[0]) / 2)  # Centered horizontally
                text_y = frame.shape[0] - 50  # Positioned near the bottom

                # Add text to frame
                cv2.putText(frame, text, (text_x, text_y), font, font_scale, (255, 255, 255), font_thickness, cv2.LINE_AA)

                return cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            subclip = subclip.fl(add_caption)

        segment_path = f"{output_dir}/segment_{i:03d}.gif"
        subclip.write_gif(segment_path)

script_dir = os.path.dirname(os.path.abspath(__file__))  # Directory of the current script
video_path = os.path.join(script_dir, "samplevideo.mp4")
output_dir = "output_gifs"
segment_duration = 2 
language = "en"
fps = 10
resize_factor = 0.5 

video_to_segmented_gifs_with_captions(video_path, output_dir, segment_duration, language, fps, resize_factor=resize_factor)







