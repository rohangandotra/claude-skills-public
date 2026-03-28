#!/usr/bin/env python3
"""Transcribe video audio using OpenAI Whisper with word-level timestamps."""

import whisper
import json
import sys


def transcribe(input_file, output_json):
    """Transcribe audio and output word-level timestamps."""
    print(f"Loading Whisper model (base)...")
    model = whisper.load_model("base")

    print(f"Transcribing: {input_file}")
    result = model.transcribe(input_file, word_timestamps=True)

    # Extract word-level timestamps
    words = []
    for segment in result["segments"]:
        for word_info in segment.get("words", []):
            words.append({
                "word": word_info["word"].strip(),
                "start": round(word_info["start"], 3),
                "end": round(word_info["end"], 3),
            })

    output = {
        "text": result["text"],
        "segments": [
            {
                "id": seg["id"],
                "start": round(seg["start"], 3),
                "end": round(seg["end"], 3),
                "text": seg["text"].strip(),
            }
            for seg in result["segments"]
        ],
        "words": words,
    }

    with open(output_json, "w") as f:
        json.dump(output, f, indent=2)

    print(f"Transcription saved to {output_json}")
    print(f"Total segments: {len(output['segments'])}")
    print(f"Total words: {len(output['words'])}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} INPUT.mp4 OUTPUT.json")
        sys.exit(1)
    transcribe(sys.argv[1], sys.argv[2])
