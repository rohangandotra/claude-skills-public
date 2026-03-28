# Claude Code Skills Pack

Free, production-ready Claude Code skills for content creators, marketers, and solopreneurs.

**6 skills. 0 coding required. Just install and go.**

---

## What Are Skills?

Skills are instruction folders that teach Claude Code how to do specific tasks. Drop them into your project and Claude automatically discovers and uses them when relevant.

## Quick Install

```bash
# Clone the repo
git clone https://github.com/YOUR_USERNAME/claude-skills-public.git

# Copy any skill into your project's .claude/skills/ directory
cp -r claude-skills-public/skills/hook-generator /your-project/.claude/skills/
```

Or install the full pack:
```bash
cp -r claude-skills-public/skills/* /your-project/.claude/skills/
```

## Skills Included

| Skill | What It Does |
|---|---|
| **content-repurposer** | Takes one long-form video transcript and generates 10+ platform-specific posts (IG captions, tweet threads, LinkedIn posts, YouTube descriptions) |
| **hook-generator** | Analyzes your best-performing content and generates scroll-stopping hooks in 6 proven formats |
| **landing-page-builder** | Builds a complete landing page from a one-line description using Claude Code |
| **overnight-agent** | Sets up an autonomous Claude Code agent that works while you sleep — researches, organizes, and reports back |
| **social-media-poster** | Automates cross-posting to multiple platforms with platform-specific formatting |
| **competitor-analyzer** | Scrapes and analyzes competitor content to find winning patterns, topics, and hooks |

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

### landing-page-builder
One prompt. One landing page. Generates a complete, responsive landing page with copy, layout, and styling. Optimized for conversion with hero section, social proof, features, and CTA.

### overnight-agent
Configure Claude Code to run autonomously on long-running tasks. Uses loops, file logging, and structured output so you wake up to organized results. Perfect for research, content planning, and data processing.

### social-media-poster
Formats and schedules content across 7+ platforms from a single input. Handles character limits, hashtag strategies, image sizing, and optimal posting times per platform.

### competitor-analyzer
Give it competitor profile URLs and it pulls their content, ranks by engagement, extracts hooks and topics, and gives you a report on what's working and what isn't. Uses Apify for data collection.

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
