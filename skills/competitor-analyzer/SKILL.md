---
name: competitor-analyzer
description: Analyzes competitor social media content to find winning patterns, topics, hooks, and posting strategies. Use when the user wants to analyze competitors, find viral content patterns, reverse-engineer what's working, or research other creators in their niche.
---

# Competitor Analyzer

## Overview
Takes competitor profile data (from Apify or manual input) and produces a detailed analysis of what's working: top content, hook patterns, topic clusters, posting frequency, and engagement rates.

## When to Activate
- User says "analyze competitor", "what's working for [creator]", "reverse engineer"
- User provides Apify JSON data or scraped social media content
- User wants to understand why certain content goes viral

## Input Formats Accepted

### Option A: Apify JSON Export
User provides JSON from Apify Instagram Scraper with fields:
- `caption`, `likesCount`, `commentsCount`, `videoPlayCount`, `timestamp`, `type`

### Option B: Manual List
User provides a list of videos with:
- Caption/title
- View count
- Like count
- Comment count
- Date posted

### Option C: Profile URLs
If user just provides profile URLs, guide them through Apify setup:
1. Go to apify.com (free tier works)
2. Use Instagram Reel Scraper
3. Enter profile URL
4. Export as JSON
5. Paste or provide file path

## Analysis Process

### Step 1: Data Cleaning
- Filter to requested time period (default: last 30 days)
- Remove posts with missing data
- Calculate engagement rate per post: (likes + comments) / views * 100

### Step 2: Profile Overview
For each competitor, calculate:
- Total posts in period
- Total views, likes, comments
- Average views per post
- Average engagement rate
- Posting frequency (posts per day)
- Active days vs inactive days

### Step 3: Top Content Ranking
Rank all posts by views (primary) and engagement rate (secondary).
List top 10 with full captions.

### Step 4: Hook Analysis
Categorize every post's hook into one of these formats:
1. **Opinion/Hot Take** — contains "imo", "honestly", "I think", controversial statement
2. **Engagement Bait** — contains "comment", "tag", "save this"
3. **Personal Story** — starts with "I", "my", shares personal experience
4. **Replacement/Killer** — "X killed Y", "replaced", "replaces"
5. **News/Breaking** — "just dropped", "new feature", "just launched"
6. **Bold Claim** — strong declarative statement
7. **How-To/Tutorial** — "how to", "step by step", "guide"

Calculate average views and engagement per hook type.
Rank hook types by performance.

### Step 5: Topic Clustering
Group posts by topic keywords. Common clusters:
- Tool comparisons (vs, killed, replaced)
- Building/creating (built, build, create, vibe code)
- Business/money (revenue, clients, paid, business)
- Automation (agent, automate, overnight, loop)
- Skills/setup (skill, setup, CLAUDE.md, config)
- Content/growth (content, posting, viral, followers)

Calculate average views per topic cluster.

### Step 6: Timing Analysis
- Which days of the week get the most views?
- Any patterns in posting time vs performance?
- How does posting frequency correlate with per-post performance?

### Step 7: Recommendations
Based on the analysis, provide:
1. Top 5 topics to create content about (highest avg views)
2. Top 3 hook formats to use (highest engagement)
3. Recommended posting frequency
4. Specific content ideas inspired by top performers
5. Gaps in competitor content that you could fill

## Output Format

```
## COMPETITOR ANALYSIS REPORT
Period: [date range]
Profiles analyzed: [list]

### Overview
| Creator | Posts | Avg Views | Avg Engagement | Frequency |
|---------|-------|-----------|----------------|-----------|
| @handle | XX    | XX,XXX    | X.X%           | X.X/day   |

### Top 10 Posts (All Creators)
| # | Creator | Views | Eng% | Caption |
|---|---------|-------|------|---------|
| 1 | @handle | XXX,XXX | X.X% | [caption] |
...

### Hook Type Performance
| Hook Type | Count | Avg Views | Avg Engagement |
|-----------|-------|-----------|----------------|
| Opinion/Hot Take | XX | XXX,XXX | X.X% |
...

### Topic Performance
| Topic | Count | Avg Views | Total Views |
|-------|-------|-----------|-------------|
| Vibe Coding | XX | XXX,XXX | X,XXX,XXX |
...

### Timing Patterns
[day-of-week and frequency insights]

### Recommendations
1. **Topics to target:** [list]
2. **Hook formats to use:** [list]
3. **Posting frequency:** [recommendation]
4. **Content gaps to fill:** [list]
5. **Specific video ideas:** [5 ideas with hooks]
```
