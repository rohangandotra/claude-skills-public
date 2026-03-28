# Claude Code Skills Pack

Free, production-ready Claude Code skills for content creators, marketers, and solopreneurs.

**8 skills. 0 coding required. Just install and go.**

---

## What Are Skills?

Skills are instruction folders that teach Claude Code how to do specific tasks. Drop them into your project and Claude automatically discovers and uses them when relevant.

## Quick Install

```bash
# Clone the repo
git clone https://github.com/rohangandotra/claude-skills-public.git

# Copy any skill into your project's .claude/skills/ directory
cp -r claude-skills-public/skills/hook-generator /your-project/.claude/skills/
```

Or install the full pack:
```bash
cp -r claude-skills-public/skills/* /your-project/.claude/skills/
```

## Skills Included

### Content & Marketing
| Skill | What It Does |
|---|---|
| **content-repurposer** | Takes one video transcript and generates 10+ platform-specific posts (IG captions, tweet threads, LinkedIn posts, YouTube descriptions) |
| **hook-generator** | Generates scroll-stopping hooks in 6 proven viral formats, ranked by real engagement data |
| **social-media-poster** | Automates cross-posting to 7+ platforms with platform-specific formatting and scheduling |
| **competitor-analyzer** | Scrapes and analyzes competitor content to find winning patterns, topics, and hooks |

### Video Production
| Skill | What It Does |
|---|---|
| **reel-editor** | Full video editing pipeline: silence removal, jump cuts, vertical crop with face tracking, captions, color correction, audio mastering |
| **reel-from-script** | Generates animated video reels from text scripts using Remotion — kinetic typography, hook sequences, CTA end cards |

### Automation & Building
| Skill | What It Does |
|---|---|
| **landing-page-builder** | Builds a complete landing page from a one-line description — responsive, conversion-optimized |
| **overnight-agent** | Sets up autonomous Claude Code agents that work while you sleep — research, content planning, data processing |

## Skill Details

### content-repurposer
Turn one piece of content into 10+. Give it a video transcript or blog post, and it generates platform-ready posts for Instagram, TikTok, Twitter/X, LinkedIn, and YouTube — each formatted for that platform's style and algorithm.

### hook-generator
Based on analysis of 100+ viral AI content videos, this skill generates hooks using the 6 formats that actually work:
1. Opinion/Hot Take (175K avg views)
2. Engagement Bait (104K avg views)
3. Personal Story (67K avg views)
4. Replacement/Killer (51K avg views)
5. News/Breaking (31K avg views)
6. Bold Claim (15K avg views)

### reel-editor
Takes raw footage and produces polished short-form reels. The full pipeline:
- Silence detection & removal (jump cuts)
- Whisper transcription with word-level timestamps
- Vertical crop (9:16) with OpenCV face tracking
- Color correction (warm talking-head preset)
- Audio mastering (highpass, EQ, compression, loudness normalization)
- Auto-generated captions burned in
- Hook text overlay for first 3 seconds
- Batch processing & hook variation exports

Dependencies: ffmpeg, python3, openai-whisper, opencv-python-headless

### reel-from-script
Generates animated video reels programmatically using Remotion (React). No filming required. Give it a script and pick a style:
- **Bold** — large text, scale + fade animations, accent color highlights
- **Kinetic** — text flies in from different directions, spring physics
- **Terminal** — typewriter effect, code editor aesthetic, syntax highlighting
- **Minimal** — clean, elegant, lots of whitespace

Also generates overlays for filmed content: hook intros, lower thirds, CTA end cards.

Dependencies: Node.js 18+, Remotion (`npx create-video@latest`)

### landing-page-builder
One prompt. One landing page. Generates a complete, responsive landing page with copy, layout, and styling. Optimized for conversion with hero section, social proof, features, and CTA.

### overnight-agent
Configure Claude Code to run autonomously on long-running tasks. Uses loops, file logging, and structured output so you wake up to organized results. Perfect for research, content planning, and data processing.

### social-media-poster
Formats and schedules content across 7+ platforms from a single input. Handles character limits, hashtag strategies, image sizing, and optimal posting times per platform.

### competitor-analyzer
Give it competitor profile URLs and it pulls their content, ranks by engagement, extracts hooks and topics, and gives you a report on what's working and what isn't. Uses Apify for data collection.

## Recommended Skills (By Others)

These are excellent skills by other creators that pair well with this pack:

| Skill | Author | What It Does |
|---|---|---|
| [**Remotion**](https://github.com/remotion-dev/remotion/tree/main/packages/skills) | Remotion (Official) | Best practices for programmatic video creation in React. Our `reel-from-script` skill builds on top of this. Install: `npx skills add remotion-dev/skills` |
| [**caption-clip**](https://github.com/kwindla/skill-caption-clip) | kwindla | Download YouTube clips, transcribe with Deepgram, burn styled captions |
| [**ButterCut**](https://github.com/barefootford/buttercut) | barefootford | Full video editing with Claude — generates timelines for Final Cut Pro, Premiere, and DaVinci Resolve |
| [**Anthropic Official Skills**](https://github.com/anthropics/skills) | Anthropic | Official skills for documents (xlsx, pptx, docx, pdf), design, and development |
| [**awesome-claude-skills**](https://github.com/travisvn/awesome-claude-skills) | travisvn | Curated directory of 1000+ community skills across all categories |

## Creating Your Own Skills

Every skill is just a folder with a `SKILL.md` file:

```
your-skill-name/
  SKILL.md          # Required — instructions for Claude
  scripts/          # Optional — Python tools
  references/       # Optional — supporting docs
```

See `template/SKILL.md` for a starter template.

## Want More?

This is the free pack. For premium skills, advanced setups, live workshops, and a community of AI builders:

**[Join the community →](YOUR_SKOOL_LINK)**

## License

MIT — use these however you want.
