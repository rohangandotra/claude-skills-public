#!/usr/bin/env python3
"""Remove silence from video, keeping 0.3s of natural pause."""

import subprocess
import sys
import re
import tempfile
import os


def detect_silence(input_file, noise_db=-35, duration=0.5):
    """Detect silent segments in video."""
    cmd = [
        "ffmpeg", "-i", input_file,
        "-af", f"silencedetect=n={noise_db}dB:d={duration}",
        "-f", "null", "-"
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    output = result.stderr

    silences = []
    starts = re.findall(r"silence_start: ([\d.]+)", output)
    ends = re.findall(r"silence_end: ([\d.]+)", output)

    for start, end in zip(starts, ends):
        silences.append((float(start), float(end)))

    return silences


def get_duration(input_file):
    """Get video duration."""
    cmd = [
        "ffprobe", "-v", "error",
        "-show_entries", "format=duration",
        "-of", "default=noprint_wrappers=1:nokey=1",
        input_file
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    return float(result.stdout.strip())


def remove_silence(input_file, output_file, keep_duration=0.3):
    """Remove silence, keeping keep_duration seconds of natural pause."""
    silences = detect_silence(input_file)
    total_duration = get_duration(input_file)

    if not silences:
        print("No silence detected. Copying file as-is.")
        subprocess.run(["cp", input_file, output_file])
        return

    # Build list of segments to keep
    segments = []
    prev_end = 0.0

    for silence_start, silence_end in silences:
        # Keep content before silence
        if silence_start > prev_end:
            segments.append((prev_end, silence_start))

        # Keep a small portion of silence for natural feel
        if keep_duration > 0:
            pad_start = silence_start
            pad_end = min(silence_start + keep_duration, silence_end)
            segments.append((pad_start, pad_end))

        prev_end = silence_end

    # Keep content after last silence
    if prev_end < total_duration:
        segments.append((prev_end, total_duration))

    # Create filter complex for concatenation
    filter_parts = []
    for i, (start, end) in enumerate(segments):
        filter_parts.append(
            f"[0:v]trim=start={start}:end={end},setpts=PTS-STARTPTS[v{i}];"
            f"[0:a]atrim=start={start}:end={end},asetpts=PTS-STARTPTS[a{i}];"
        )

    concat_v = "".join(f"[v{i}]" for i in range(len(segments)))
    concat_a = "".join(f"[a{i}]" for i in range(len(segments)))
    filter_parts.append(
        f"{concat_v}concat=n={len(segments)}:v=1:a=0[outv];"
        f"{concat_a}concat=n={len(segments)}:v=0:a=1[outa]"
    )

    filter_complex = "".join(filter_parts)

    cmd = [
        "ffmpeg", "-i", input_file,
        "-filter_complex", filter_complex,
        "-map", "[outv]", "-map", "[outa]",
        "-c:v", "libx264", "-preset", "fast", "-crf", "23",
        "-c:a", "aac", "-b:a", "128k",
        "-y", output_file
    ]

    print(f"Found {len(silences)} silent segments. Keeping {len(segments)} content segments.")
    subprocess.run(cmd, check=True, capture_output=True)

    orig_dur = get_duration(input_file)
    new_dur = get_duration(output_file)
    print(f"Duration: {orig_dur:.1f}s → {new_dur:.1f}s (removed {orig_dur - new_dur:.1f}s of silence)")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} INPUT.mp4 OUTPUT.mp4")
        sys.exit(1)
    remove_silence(sys.argv[1], sys.argv[2])
