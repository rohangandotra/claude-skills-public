#!/usr/bin/env python3
"""Generate SRT caption file from Whisper transcript JSON."""

import json
import sys


def format_timestamp(seconds):
    """Convert seconds to SRT timestamp format (HH:MM:SS,mmm)."""
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    secs = int(seconds % 60)
    millis = int((seconds % 1) * 1000)
    return f"{hours:02d}:{minutes:02d}:{secs:02d},{millis:03d}"


def generate_srt(transcript_json, output_srt, max_words_per_line=6):
    """Generate SRT from transcript with readable line lengths."""
    with open(transcript_json) as f:
        data = json.load(f)

    words = data.get("words", [])
    if not words:
        # Fallback to segments
        segments = data.get("segments", [])
        with open(output_srt, "w") as f:
            for i, seg in enumerate(segments, 1):
                start = format_timestamp(seg["start"])
                end = format_timestamp(seg["end"])
                f.write(f"{i}\n{start} --> {end}\n{seg['text']}\n\n")
        print(f"Generated {len(segments)} caption segments from segments.")
        return

    # Group words into caption lines
    captions = []
    current_words = []
    current_start = None

    for word in words:
        if current_start is None:
            current_start = word["start"]

        current_words.append(word["word"])

        if len(current_words) >= max_words_per_line:
            captions.append({
                "start": current_start,
                "end": word["end"],
                "text": " ".join(current_words),
            })
            current_words = []
            current_start = None

    # Flush remaining words
    if current_words:
        captions.append({
            "start": current_start,
            "end": words[-1]["end"],
            "text": " ".join(current_words),
        })

    # Write SRT
    with open(output_srt, "w") as f:
        for i, cap in enumerate(captions, 1):
            start = format_timestamp(cap["start"])
            end = format_timestamp(cap["end"])
            # Capitalize first word of each line
            text = cap["text"]
            if text:
                text = text[0].upper() + text[1:]
            f.write(f"{i}\n{start} --> {end}\n{text}\n\n")

    print(f"Generated {len(captions)} caption lines → {output_srt}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} TRANSCRIPT.json OUTPUT.srt")
        sys.exit(1)
    generate_srt(sys.argv[1], sys.argv[2])
