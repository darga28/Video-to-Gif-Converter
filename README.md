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

## Usage

1. **Clone the repository:**

   ```bash
   git clone https://github.com/darga28/Video-to-Gif-Converter.git
   cd your_repository
   ```

2. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the script:**

   ```bash
   python video_to_segmented_gifs_with_captions.py
   ```

   Make sure to modify `video_path`, `output_dir`, and other parameters according to your requirements within the script.

## Parameters

- `video_path`: Path to the input video file.
- `output_dir`: Directory where GIF segments with captions will be saved.
- `segment_duration`: Duration (in seconds) of each GIF segment.
- `language`: Language code for transcription (default: "en").
- `fps`: Frames per second for the output GIFs.
- `text_extraction`: Method for text extraction ("whisper" for automatic transcription).
- `text_rendering`: Method for text rendering ("overlay" for overlaying captions on GIFs).
- `resize_factor`: Factor by which to resize the frames (default: 1.0, no resize).

## Acknowledgments

- [MoviePy](https://github.com/Zulko/moviepy) - Video editing with Python
- [Whisper](https://github.com/CrowdCurio/whisper) - Automatic speech recognition library
