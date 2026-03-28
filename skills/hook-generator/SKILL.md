---
name: hook-generator
description: Generates scroll-stopping hooks for short-form video content (Reels, TikTok, Shorts) based on 6 proven viral formats. Use when the user needs hooks, opening lines, video intros, or wants to make their content more engaging. Also use when the user wants to analyze or improve existing hooks.
---

# Hook Generator

## Overview
Generates hooks based on data from 100+ viral AI content videos. Every hook follows one of 6 proven formats ranked by average performance.

## Hook Formats (Ranked by Average Views)

### 1. Opinion/Hot Take (175K avg views, 2.9% engagement)
Pattern: State a controversial or contrarian opinion with casual confidence.
- "Vibe coding is not a real skill — here's what actually is"
- "Everyone's using ChatGPT wrong. Here's what works."
- "I think [popular tool] is completely overrated and here's why"
Key: Use words like "honestly", "imo", "unpopular opinion" — casual authority tone.

### 2. Engagement Bait (104K avg views, 3.9% engagement)
Pattern: Direct the viewer to take an action in the comments.
- "Comment [WORD] and I'll send you the full setup"
- "Tag someone who needs to see this"
- "Save this before it gets taken down"
Key: The CTA IS the hook. Put it at the start, not the end.

### 3. Personal Story (67K avg views, 2.5% engagement)
Pattern: Share a personal result or experience that creates curiosity.
- "I went to sleep. Claude didn't. Here's what happened."
- "This is cooking me" / "This is ruining my life" (hyperbole)
- "I've been doing [X] for 6 months and just discovered this"
Key: Make it about YOUR experience, not a tutorial.

### 4. Replacement/Killer (51K avg views, 3.9% engagement)
Pattern: Claim one thing has killed/replaced another.
- "I just replaced an entire ads team with 4 Claude skills"
- "Claude Code officially killed [tool] today"
- "I used to pay $4,000/month. Now I pay $20."
Key: Specific numbers make it believable. Dollar amounts are strongest.

### 5. News/Breaking (31K avg views, 3.5% engagement)
Pattern: Announce something new that just happened.
- "Claude skills V2 just dropped and they are insane"
- "[Tool] dropped a new feature last night"
- "This just changed everything about [topic]"
Key: Urgency + recency. Must feel like RIGHT NOW.

### 6. Bold Claim (15K avg views, 2.5% engagement)
Pattern: Make a strong, specific statement.
- "You need to be using overnight agents"
- "This is the only skill that matters in 2026"
- "MCP servers waste tokens"
Key: Confidence without hedging. No "I think" or "maybe."

## Instructions

When generating hooks:

1. Ask or determine the VIDEO TOPIC
2. Generate 3 hooks per format (18 total) ranked by predicted performance
3. For each hook, specify:
   - The hook text (what appears on screen / what they say first)
   - Which format it uses
   - A suggested CTA to pair with it
   - Whether it needs a visual element (screen recording, text overlay, etc.)

4. Recommend the top 3 hooks overall with reasoning

## Rules
- Every hook must work with SOUND OFF (assume text on screen)
- Keep hooks under 15 words for on-screen text
- The spoken hook can be longer but the first 3 seconds must deliver the core message
- Never use "In this video I'll show you" — that's a tutorial opener, not a hook
- Never start with a question unless it's rhetorical and provocative
- Always pair a hook with a matching CTA format

## Output Format

```
## HOOKS FOR: [topic]

### Top 3 Recommended
1. "[hook text]" (Format: [type]) — CTA: "[cta]"
2. "[hook text]" (Format: [type]) — CTA: "[cta]"
3. "[hook text]" (Format: [type]) — CTA: "[cta]"

### All Hooks by Format

#### Opinion/Hot Take
1. "[hook]" — CTA: "[cta]"
2. "[hook]" — CTA: "[cta]"
3. "[hook]" — CTA: "[cta]"

#### Engagement Bait
...

[continue for all 6 formats]
```
