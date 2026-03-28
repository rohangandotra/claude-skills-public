---
name: reel-editor
description: Edits raw video footage into polished short-form reels (Instagram, TikTok, YouTube Shorts). Handles silence removal, jump cuts, vertical cropping with face tracking, captions, color correction, audio mastering, and hook text overlays. Use when the user wants to edit a video, create a reel, add captions, remove silence, make jump cuts, or process raw footage into short-form content.
---

# Reel Editor

## Overview
Takes raw video footage and produces polished, platform-ready short-form reels. The full pipeline: silence removal → transcription → jump cuts → vertical crop with face tracking → color correction → audio mastering → captions → hook text overlay → export.

## Dependencies
- ffmpeg (required)
- python3 with: openai-whisper, opencv-python-headless (required)
- All scripts located in this skill's `scripts/` directory

## When to Activate
- User provides a video file and wants it edited into a reel
- User says "edit this", "make a reel", "add captions", "cut this down"
- User has raw footage from a batch recording session

## Pipeline Steps

Run each step sequentially. Always confirm the input file exists before starting.

### Step 1: Silence Detection & Removal

Detect silence longer than 0.5 seconds and trim to 0.3 seconds:

```bash
ffmpeg -i INPUT.mp4 -af silencedetect=n=-35dB:d=0.5 -f null - 2>&1 | grep "silence_"
```

Parse the silence timestamps, then use ffmpeg to cut them out:

```bash
python3 SKILL_DIR/scripts/remove_silence.py INPUT.mp4 output_no_silence.mp4
```

This creates a version with dead air removed — the foundation of jump cuts.

### Step 2: Transcription

Transcribe the audio using Whisper:

```bash
python3 SKILL_DIR/scripts/transcribe.py output_no_silence.mp4 transcript.json
```

Output: `transcript.json` with word-level timestamps.

### Step 3: Editorial Decisions

Read the transcript and categorize segments:
- **Normal** (60%): Standard delivery, 1x zoom
- **Emphasis** (30%): Key points, bold claims, numbers — 1.25x zoom
- **Critical** (10%): The hook, the punchline, the CTA — 1.5x zoom

Write these decisions to `edit_decisions.json`.

### Step 4: Vertical Crop with Face Tracking

Crop from horizontal to vertical (9:16) keeping the face centered:

```bash
python3 SKILL_DIR/scripts/crop_vertical.py output_no_silence.mp4 edit_decisions.json output_cropped.mp4
```

This script:
1. Detects face position using OpenCV's Haar cascade
2. Crops to 1080x1920 (9:16) centered on the face
3. Applies zoom levels from edit_decisions.json
4. Smooths zoom transitions over 0.3 seconds

If the input is already vertical (9:16), skip cropping but still apply zoom levels.

### Step 5: Color Correction

Apply a warm talking-head preset:

```bash
ffmpeg -i output_cropped.mp4 \
  -vf "eq=contrast=1.05:brightness=0.03:saturation=1.1,curves=m='0/0 0.25/0.27 0.5/0.52 0.75/0.77 1/1'" \
  -c:a copy output_color.mp4
```

### Step 6: Audio Mastering

Run a mastering chain:

```bash
ffmpeg -i output_color.mp4 \
  -af "highpass=f=80,equalizer=f=3000:t=q:w=1.5:g=3,acompressor=threshold=-20dB:ratio=3:attack=5:release=50,loudnorm=I=-14:LRA=7:TP=-1" \
  -c:v copy output_mastered.mp4
```

This applies:
- Highpass at 80Hz (removes rumble)
- Presence boost at 3kHz (clarity)
- Compression (evens out volume)
- Loudness normalization to -14 LUFS (Instagram/TikTok standard)

### Step 7: Generate & Burn Captions

Generate SRT from the transcript:

```bash
python3 SKILL_DIR/scripts/generate_srt.py transcript.json captions.srt
```

Burn captions with bold, readable styling:

```bash
ffmpeg -i output_mastered.mp4 \
  -vf "subtitles=captions.srt:force_style='FontSize=22,FontName=Avenir Next Bold,PrimaryColour=&H00FFFFFF,OutlineColour=&H00000000,BorderStyle=1,Outline=2,Shadow=0,MarginV=60,MarginL=30,MarginR=30,Alignment=2'" \
  -c:a copy output_captioned.mp4
```

Style: White text, black outline, bottom-center, large enough to read on mobile.

### Step 8: Hook Text Overlay (Optional)

If the user provides hook text, burn it into the first 3 seconds:

```bash
ffmpeg -i output_captioned.mp4 \
  -vf "drawtext=text='HOOK TEXT HERE':fontfile=/System/Library/Fonts/Helvetica.ttc:fontsize=56:fontcolor=white:borderw=3:bordercolor=black:x=(w-text_w)/2:y=h*0.35:enable='between(t,0,3)'" \
  -c:a copy output_final.mp4
```

### Step 9: Export

Rename to final output:
```bash
mv output_final.mp4 REEL_[topic]_[date].mp4
```

Clean up intermediate files (ask user first).

Report: duration, file size, and preview command:
```bash
open REEL_[topic]_[date].mp4  # macOS
```

## Batch Processing

When the user has multiple raw recordings from a batch session:

1. List all video files in the input directory
2. Process each one through the full pipeline
3. Name outputs sequentially: `reel_01_[topic].mp4`, `reel_02_[topic].mp4`, etc.
4. Generate a summary with durations and file sizes

```bash
for f in raw_footage/*.mp4; do
  echo "Processing: $f"
  # Run full pipeline on each file
done
```

## Hook Variation Exports

For each video, if the user wants multiple hook variations:
1. Take the final captioned video
2. For each hook variation, burn different text in the first 3 seconds
3. Export as separate files: `reel_01_hookA.mp4`, `reel_01_hookB.mp4`

This turns 10 recordings into 20-30 unique posts.

## Platform Export Presets

### Instagram Reels
- Resolution: 1080x1920
- Codec: H.264, AAC
- Max duration: 90 seconds
- Max file size: 250MB

### TikTok
- Resolution: 1080x1920
- Codec: H.264, AAC
- Max duration: 10 minutes
- Max file size: 287MB

### YouTube Shorts
- Resolution: 1080x1920
- Codec: H.264, AAC
- Max duration: 60 seconds

Export command for all platforms:
```bash
ffmpeg -i FINAL.mp4 -c:v libx264 -preset medium -crf 23 -c:a aac -b:a 128k -movflags +faststart -y OUTPUT.mp4
```
