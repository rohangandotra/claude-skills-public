---
name: reel-from-script
description: Generates animated short-form video reels from a text script using Remotion (React-based programmatic video). Creates hook sequences, text animations, kinetic typography, lower thirds, intro/outro sequences, and B-roll overlays. Use when the user wants to create an animated reel, generate a video from text, build an intro sequence, or make kinetic typography content without filming.
---

# Reel From Script

## Overview
Takes a video script (hook, body, CTA) and generates a polished animated reel using Remotion. Produces platform-ready 9:16 vertical video with animated text, transitions, background visuals, and optional audio.

Built on top of the official [Remotion skill](https://github.com/remotion-dev/remotion). Requires Remotion to be installed.

## Prerequisites

- Node.js 18+
- Remotion (install with `npx create-video@latest`)
- Remotion Agent Skills (`npx skills add remotion-dev/skills`)

## When to Activate

- User provides a script and wants a video without filming
- User wants animated text reels, kinetic typography, or motion graphics
- User wants intro/outro sequences for their filmed content
- User says "make a reel from this script", "animate this", "text-to-video"

## Setup (First Time Only)

```bash
# Create a Remotion project if one doesn't exist
npx create-video@latest reel-project --template blank
cd reel-project
npm install

# Install Remotion agent skills for best practices
npx skills add remotion-dev/skills
```

## Input Format

The user provides a script object:

```json
{
  "hook": "Stop scrolling. This will change how you use AI.",
  "body": [
    "Most people use ChatGPT like a search engine.",
    "But Claude Code can build entire apps.",
    "In 3 minutes. From one prompt."
  ],
  "cta": "Comment BUILD and I'll send you the setup",
  "style": "bold",
  "duration_seconds": 30,
  "background": "dark"
}
```

## Video Styles

### Style: "bold" (Default — Best for Hot Takes)
- Dark background (#0a0a0a)
- Large white text, centered
- Words animate in with scale + fade
- Key words highlighted in accent color (#3b82f6)
- One sentence at a time, full screen

### Style: "kinetic" (Best for Lists/Steps)
- Text flies in from different directions
- Each point stacks or replaces the previous
- Numbers/bullets animate with spring physics
- High energy, fast transitions

### Style: "terminal" (Best for Tech/Claude Code Content)
- Simulated terminal/code editor background
- Text types in character by character (typewriter effect)
- Monospace font, green or white on black
- Cursor blink animation
- Code syntax highlighting for any code snippets

### Style: "minimal" (Best for Personal Stories)
- Clean white or cream background
- Elegant serif or sans-serif font
- Subtle fade transitions
- Lots of whitespace
- Calm, premium feel

## Remotion Component Structure

Generate these React components:

```
src/
  compositions/
    Reel/
      index.tsx          # Main composition
      HookSequence.tsx   # First 3 seconds — the hook
      BodySequence.tsx   # Middle section — each body point
      CTASequence.tsx    # Last 3-5 seconds — call to action
      TextAnimation.tsx  # Reusable animated text component
      Background.tsx     # Animated background
  Root.tsx               # Register composition
```

### Key Remotion Patterns

```tsx
// Use spring animations for natural movement
import { spring, useCurrentFrame, useVideoConfig } from "remotion";

const TextAnimation: React.FC<{ text: string; delay: number }> = ({ text, delay }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  const opacity = spring({ frame: frame - delay, fps, config: { damping: 20 } });
  const scale = spring({ frame: frame - delay, fps, config: { damping: 15, mass: 0.5 } });

  return (
    <div style={{
      opacity: Math.min(1, opacity),
      transform: `scale(${0.8 + 0.2 * Math.min(1, scale)})`,
    }}>
      {text}
    </div>
  );
};
```

### Composition Config

```tsx
// Always register at 9:16 for short-form
<Composition
  id="Reel"
  component={Reel}
  durationInFrames={duration * 30}  // 30fps
  fps={30}
  width={1080}
  height={1920}
/>
```

## Timing

For a 30-second reel:
- **Hook**: frames 0-90 (0-3 seconds)
- **Body point 1**: frames 90-240 (3-8 seconds)
- **Body point 2**: frames 240-420 (8-14 seconds)
- **Body point 3**: frames 420-600 (14-20 seconds)
- **Pause/transition**: frames 600-720 (20-24 seconds)
- **CTA**: frames 720-900 (24-30 seconds)

Adjust proportionally for different durations.

## Rendering

```bash
# Preview in browser
npm run dev

# Render to MP4
npx remotion render Reel output/reel.mp4

# Render specific duration
npx remotion render Reel output/reel.mp4 --frames=0-900
```

## Hook Variation Exports

To create multiple versions with different hooks:

1. Parameterize the hook text as an input prop
2. Render once per hook variation:

```bash
npx remotion render Reel output/reel_hookA.mp4 --props='{"hook":"Hook A text"}'
npx remotion render Reel output/reel_hookB.mp4 --props='{"hook":"Hook B text"}'
```

## Combining with Filmed Footage

This skill can also generate components to overlay on filmed footage:

### Hook Intro Overlay (first 3 seconds)
Generate an animated text intro that goes OVER the filmed video:
- Animated hook text with background blur
- Transitions out to reveal the speaker

### Lower Thirds
Generate animated name/title cards:
- Slide-in animation from left
- Name + title/handle
- Auto-dismiss after 3 seconds

### CTA End Card
Generate an animated end card:
- "Comment SKILLS" with animated pointing hand
- Profile handle with follow button animation
- Background: blurred/darkened last frame of video

## Output
- MP4 file at 1080x1920, 30fps, H.264
- Ready to upload directly to Instagram Reels, TikTok, YouTube Shorts
- Multiple hook variation exports if requested
