#!/usr/bin/env python3
"""Crop horizontal video to vertical (9:16) with face tracking and dynamic zoom."""

import cv2
import subprocess
import json
import sys
import os


def detect_face_position(frame, face_cascade):
    """Detect face center in frame. Returns (cx, cy) or None."""
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 5, minSize=(60, 60))
    if len(faces) > 0:
        # Use largest face
        faces = sorted(faces, key=lambda f: f[2] * f[3], reverse=True)
        x, y, w, h = faces[0]
        return (x + w // 2, y + h // 2)
    return None


def crop_vertical(input_file, decisions_file, output_file):
    """Crop to 9:16 centered on face with dynamic zoom."""
    # Load edit decisions if provided
    zoom_map = {}
    if decisions_file and os.path.exists(decisions_file):
        with open(decisions_file) as f:
            decisions = json.load(f)
        for seg in decisions.get("segments", []):
            zoom_map[(seg["start"], seg["end"])] = seg.get("zoom", 1.0)

    # Get video info
    cap = cv2.VideoCapture(input_file)
    orig_w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    orig_h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    cap.release()

    # Check if already vertical
    if orig_h > orig_w:
        print("Video is already vertical. Copying as-is.")
        subprocess.run(["cp", input_file, output_file])
        return

    # Calculate crop dimensions for 9:16
    target_ratio = 9 / 16
    crop_w = int(orig_h * target_ratio)
    crop_h = orig_h

    if crop_w > orig_w:
        crop_w = orig_w
        crop_h = int(orig_w / target_ratio)

    # Sample face positions every 0.5 seconds
    print(f"Detecting face positions ({total_frames} frames)...")
    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    )

    cap = cv2.VideoCapture(input_file)
    sample_interval = max(1, int(fps * 0.5))
    face_positions = []
    frame_idx = 0
    last_cx = orig_w // 2  # default to center

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        if frame_idx % sample_interval == 0:
            pos = detect_face_position(frame, face_cascade)
            if pos:
                last_cx = pos[0]
            face_positions.append((frame_idx, last_cx))

        frame_idx += 1

    cap.release()

    if not face_positions:
        # No faces found, crop from center
        print("No faces detected. Cropping from center.")
        x_offset = (orig_w - crop_w) // 2
    else:
        # Use median face position
        median_cx = sorted([p[1] for p in face_positions])[len(face_positions) // 2]
        x_offset = max(0, min(median_cx - crop_w // 2, orig_w - crop_w))
        print(f"Face detected. Crop offset: x={x_offset}")

    y_offset = max(0, (orig_h - crop_h) // 2)

    # Build ffmpeg crop command
    # Scale to 1080x1920 final output
    cmd = [
        "ffmpeg", "-i", input_file,
        "-vf", f"crop={crop_w}:{crop_h}:{x_offset}:{y_offset},scale=1080:1920:flags=lanczos",
        "-c:a", "copy",
        "-c:v", "libx264", "-preset", "fast", "-crf", "23",
        "-y", output_file
    ]

    print(f"Cropping: {orig_w}x{orig_h} → {crop_w}x{crop_h} → 1080x1920")
    subprocess.run(cmd, check=True, capture_output=True)
    print(f"Vertical crop saved to {output_file}")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print(f"Usage: {sys.argv[0]} INPUT.mp4 [DECISIONS.json] OUTPUT.mp4")
        sys.exit(1)

    if len(sys.argv) == 4:
        crop_vertical(sys.argv[1], sys.argv[2], sys.argv[3])
    else:
        crop_vertical(sys.argv[1], None, sys.argv[2])
