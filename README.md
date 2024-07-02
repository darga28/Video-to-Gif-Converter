# Video to Segmented GIFs with Captions

This Python script extracts captions from a video, splits them into segments, and generates GIFs with captions overlaid on each segment. It uses the MoviePy library for video processing and Whisper for automatic transcription.

## Introduction

This script automates the process of creating segmented GIFs with captions from a video file. It's useful for scenarios where you want to highlight specific segments of a video with accompanying text, ideal for social media snippets, educational purposes, or storytelling through visual media.

### Features

- **Automatic Caption Extraction:** Utilizes Whisper for automatic transcription to extract captions from the video.
- **Segmentation:** Splits captions into segments ensuring each segment contains full sentences.
- **Customizable Parameters:** Adjust segment duration, language for transcription, FPS for GIFs, and more.
- **Text Rendering:** Option to overlay captions on GIFs for enhanced readability.

## Requirements

- Python 3.6+
- moviepy (install via `pip install moviepy`)
- whisper (install via `pip install whisper`)
- OpenCV (install via `pip install opencv-python`)

## Parameters

- `video_path`: Path to the input video file.
- `output_dir`: Directory where GIF segments with captions will be saved.
- `segment_duration`: Duration (in seconds) of each GIF segment.
- `language`: Language code for transcription (default: "en").
- `fps`: Frames per second for the output GIFs.
- `text_extraction`: Method for text extraction ("whisper" for automatic transcription).
- `text_rendering`: Method for text rendering ("overlay" for overlaying captions on GIFs).
- `resize_factor`: Factor by which to resize the frames (default: 1.0, no resize).

### How It Works

- **Video Loading and Preparation**: Initially, the script uses `moviepy.editor` to load the input video file (`video_path`). Optionally, it can resize the video frames using the `resize_factor` parameter to reduce file size or adjust display dimensions. It sets up the video clip for further processing.

- **Text Extraction and Segmentation**: The script utilizes the Whisper library (`whisper`) to extract captions from the video. Whisper transcribes spoken words into text, providing segments of text along with their start and end times. These segments are split into smaller segments (`segment_duration`), ensuring each segment contains complete sentences. This is crucial for maintaining readability and coherence in the generated GIFs.

- **GIF Creation with Caption Overlay**: For each segmented caption, the script extracts the corresponding video segment, adjusts its duration, and optionally resizes it. It then overlays the extracted caption text onto the frames using OpenCV (`cv2`). The text is rendered onto each frame, centered near the bottom. Finally, each modified segment is saved as a GIF file (`segment_path`) in the specified output directory (`output_dir`). This process repeats for each segment, resulting in a series of GIFs that visually represent different sections of the original video with synchronized captions.

## Acknowledgments

- [MoviePy](https://github.com/Zulko/moviepy) - Video editing with Python
- [Whisper](https://github.com/CrowdCurio/whisper) - Automatic speech recognition library
- [OpenCV](https://opencv.org/) - Computer vision library
