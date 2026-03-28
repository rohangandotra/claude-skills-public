---
name: social-media-poster
description: Automates formatting and posting content across multiple social media platforms from a single input. Use when the user wants to post to multiple platforms, cross-post content, schedule posts, or automate their social media distribution.
---

# Social Media Poster

## Overview
Takes one piece of content and formats it for 7+ platforms, handling character limits, hashtag strategies, image sizing, and platform-specific conventions. Can generate posting scripts for automation.

## When to Activate
- User wants to post to multiple platforms at once
- User says "cross-post", "post everywhere", "distribute this content"
- User wants a posting automation setup

## Platform Specs

### Instagram
- Caption: Max 2,200 chars, first 125 visible in preview
- Hashtags: 20-30, mix of sizes (under 100K, 100K-1M, 1M+)
- Image: 1080x1350 (4:5 portrait) for feed, 1080x1920 (9:16) for Reels
- Best times: 11am-1pm, 7-9pm (user's timezone)
- Notes: Line breaks for readability, emoji sparingly, CTA at end

### TikTok
- Caption: Max 4,000 chars (but shorter is better, aim for under 300)
- Hashtags: 3-5 max, trending + niche
- Video: 1080x1920 (9:16)
- Best times: 7-9am, 12-3pm, 7-9pm
- Notes: Casual tone, can use slang, trending sounds referenced in caption

### Twitter/X
- Single post: Max 280 chars
- Thread: 280 chars per tweet, 5-10 tweets ideal
- Image: 1600x900 (16:9) or 1080x1080 (1:1)
- Best times: 8-10am, 12-1pm
- Notes: No hashtags in thread body (looks spammy), 1-2 in last tweet only

### LinkedIn
- Post: Max 3,000 chars, first 210 visible before "see more"
- Image: 1200x627 or 1080x1080
- Best times: 7-8am, 12pm, 5-6pm Tue-Thu
- Notes: Professional but not corporate, single-sentence paragraphs, ask a question at end

### YouTube Shorts
- Title: Max 100 chars
- Description: Max 5,000 chars but keep under 200 for Shorts
- Video: 1080x1920 (9:16), under 60 seconds
- Tags: 5-10 relevant keywords
- Notes: Title is the hook, description is for SEO

### Threads
- Post: Max 500 chars
- Image: 1080x1350
- Notes: Conversational, no hashtags needed, reply-chain format for longer content

### Bluesky
- Post: Max 300 chars
- Image: Standard aspect ratios
- Notes: Similar to early Twitter, text-first, minimal hashtags

## Process

### Step 1: Take Input
Accept any of:
- Raw text / caption
- Video transcript
- Blog post excerpt
- Previous social media post to reformat

### Step 2: Generate Platform Versions
For each target platform, rewrite the content following that platform's specs above. Don't just truncate — actually rewrite for the platform's tone and format.

### Step 3: Generate CTA Variations
For platforms that support it, add a "Comment [WORD]" CTA:
- Rotate the keyword: SETUP, SKILLS, BUILD, FREE, GUIDE, LINK
- Match the keyword to the content topic

### Step 4: Hashtag Research
Generate hashtags in 3 tiers:
- **Small** (under 100K posts): Niche, high relevance, lower competition
- **Medium** (100K-1M posts): Balanced reach and competition
- **Large** (1M+ posts): Broad reach, high competition

### Step 5: Posting Automation (Optional)
If the user wants to automate posting, generate a script using one of:

#### Option A: Repurpose.io Integration
Provide instructions for connecting platforms and setting up auto-posting rules.

#### Option B: Custom Python Script
```python
# Uses platform APIs where available
# Instagram: Instagram Graph API (requires Business account)
# Twitter: Twitter API v2
# LinkedIn: LinkedIn API
# Others: Manual or third-party tools
```

#### Option C: Buffer/Later Integration
Provide CSV format for bulk upload to scheduling tools.

## Output Format

```
## CROSS-PLATFORM POST PACK
Topic: [topic]
Platforms: [list]

### Instagram
**Caption:**
[formatted caption with line breaks]

**Hashtags:**
[hashtag block]

**Best posting time:** [time]

### TikTok
**Caption:**
[caption]

### Twitter/X
**Tweet 1:** [hook]
**Tweet 2:** [point 1]
...

### LinkedIn
**Post:**
[formatted post]

### YouTube Shorts
**Title:** [title]
**Description:** [description]
**Tags:** [tags]

### Posting Schedule
| Time | Platform | Content |
|------|----------|---------|
| Mon 11am | Instagram | Post 1 |
| Mon 12pm | Twitter | Thread 1 |
...
```
