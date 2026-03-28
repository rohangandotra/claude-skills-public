---
name: landing-page-builder
description: Builds a complete, responsive landing page from a one-line description. Use when the user wants to create a landing page, website, sales page, or opt-in page. Generates HTML, CSS, and copy optimized for conversion.
---

# Landing Page Builder

## Overview
Generates a complete, production-ready landing page from a single prompt. Outputs clean HTML + CSS with conversion-optimized copy and layout.

## When to Activate
- User says "build me a landing page" or "create a website"
- User wants a sales page, opt-in page, or Skool landing page
- User mentions needing a page for their product/service/community

## Process

### Step 1: Gather Requirements
If not provided, ask for:
- What is this page for? (product, service, community, lead magnet)
- Who is the target audience?
- What's the primary CTA? (sign up, buy, join, download)
- Any brand colors or style preferences?

If the user gives minimal input, make smart defaults and build it.

### Step 2: Generate the Page

Every landing page MUST include these sections in order:

#### 1. Hero Section
- Headline: Bold, benefit-driven, under 10 words
- Subheadline: One sentence expanding on the promise
- CTA button: High contrast, action verb ("Join Now", "Get Started", "Download Free")
- Social proof snippet: "Join 1,000+ members" or similar

#### 2. Problem Section
- 3 pain points the target audience has
- Use "You" language, not "We"
- Short, punchy sentences

#### 3. Solution Section
- What the product/service does
- 3 key features with icons or visual markers
- Keep it scannable — bullet points or cards

#### 4. Social Proof
- Testimonials (generate realistic placeholder ones, marked as examples)
- Logos, numbers, or stats if applicable

#### 5. Pricing/Offer (if applicable)
- Clear pricing with what's included
- Highlight the best value option
- Remove friction: "Cancel anytime", "No credit card required"

#### 6. FAQ
- 4-5 common objections answered
- Keep answers to 1-2 sentences

#### 7. Final CTA
- Repeat the main CTA
- Add urgency if appropriate
- Include the primary button again

### Step 3: Technical Requirements
- Single HTML file with inline CSS (easy to deploy anywhere)
- Fully responsive (mobile-first)
- Clean, modern design with good whitespace
- System fonts (no external dependencies)
- Fast-loading (no external scripts unless requested)
- Accessible: proper heading hierarchy, alt texts, contrast ratios

### Step 4: Color and Style
Default palette (override if user provides brand colors):
- Background: #fafafa
- Text: #1a1a1a
- Accent: #2563eb (blue) or #d97706 (orange)
- CTA button: High contrast against background
- Typography: System font stack, large headings (48-64px), readable body (18px)

## Output
- Complete HTML file ready to save and open in a browser
- Explanation of the layout decisions
- Suggestions for what to customize (headlines, testimonials, colors)
