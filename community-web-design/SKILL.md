---
name: community-web-design
description: Design and build web pages for community organising, coalition building, and social enterprise. Use for landing pages, campaign funnels, membership portals, dashboards, interactive tools (surveys, quizzes, directories, sign-up forms), subject briefings, content showcases, and documentation. Triggers on requests involving community websites, advocacy campaigns, manifesto sites, investor attraction pages, member dashboards, or any web design for organisations serving marginalised communities. Produces HTML/Tailwind by default; React for interactive tools requiring state management.
---

# Community Web Design

Build web pages that earn trust, honour community, and move people to action.

## Core Principles

These aren't style preferences—they're how the design earns trust:

- **Trust the people** → No manipulation, no dark patterns. Clear information, honest CTAs
- **Move at the speed of trust** → Progressive disclosure over overwhelming. Let relationships deepen
- **Small is good, small is all** → Quality over scale. 10 committed people > 1000 passive clicks
- **Critical connections > critical mass** → Design for depth of engagement, not vanity metrics
- **Less prep, more presence** → Pages should feel human, not corporate. Warmth over polish

## Stack Decision

**Default to HTML/Tailwind** for:
- Landing pages, campaign pages, content showcases
- Subject briefings, documentation, guides
- Sign-up forms (simple), directories (static)

**Use React artifacts** for:
- Dashboards with state management
- Surveys, quizzes, competitions (multi-step, scoring)
- Interactive tools with calculations or filtering

## Page Types

### Landing Pages & Campaign Funnels

Journey: Awareness → Understanding → Connection → Action

1. **Hook** - One clear statement of who this is for and why it matters
2. **Context** - The situation that makes this necessary
3. **Invitation** - What you're asking people to join/support/do
4. **Social proof** - Community voices. "Who else is here?"
5. **Action** - Single clear next step per viewport

Avoid: Countdown timers, fake scarcity, manipulation tactics.

### Coalition Building Pages

Pattern: Multiple organisations, shared purpose, distributed ownership

1. **Shared frame** - What brings us together
2. **Partner presence** - Equal visual weight, alphabetical or rotating
3. **Collective asks** - "We" language, shared positions
4. **Multiple entry points** - Different actions for different capacities
5. **Resource commons** - Shared assets, briefings, toolkits

### Membership Portals & Dashboards

Pattern: Belonging, not access. Relationship, not transaction.

1. **Welcome** - Personal, name-based, acknowledges contribution
2. **Community pulse** - What's happening, who's active
3. **Your journey** - Engagement history, suggested actions
4. **Resources** - Tools relevant to their role
5. **Connection** - Ways to reach others

### Interactive Tools

**Surveys:**
1. Purpose statement - Why asking, what happens with answers
2. Progress indicator - Always show position
3. Conditional logic - Skip irrelevant questions
4. Immediate value - Show something useful mid-survey
5. Gratitude close - Acknowledge contribution

**Directories:**
1. Search/filter first
2. Consent-based profiles
3. Connection facilitation
4. Reciprocity prompt - Invite viewers to add themselves

### Subject Briefings

1. **TL;DR** - One paragraph summary up front
2. **Why this matters** - Stakes and context
3. **Key points** - Scannable, clearly headed
4. **Deeper reading** - Expandable or linked
5. **Action bridge** - "Now you know this, here's what you can do"

### Content Showcases

1. **The work first** - Video/image/content as hero
2. **Context layer** - Who made this, why it matters
3. **Engagement invitation**
4. **Related threads**
5. **Creator presence**

## Visual Identity Modes

### BLKOUT UK / Black queer contexts

**Core aesthetic principle:** Boldness and masculinity, disrupted by beauty and vulnerability.

This is not "either/or" but "both/and" — strength AND softness, bold AND vulnerable, masculine AND beautiful. The tension between these creates the BLKOUT aesthetic.

**Three-layer structure:**

1. **Foundation (the people at heart)**
   - Black bodies, faces looking directly at camera
   - Not decorative — the ground everything stands on
   - Presence, witnessing, being witnessed
   - Hero imagery should show joy, power, vulnerability in equal measure
   - 20-30% opacity when used as background layer

2. **Protective shell (the structure)**
   - Bold typography: Work Sans 900 weight, uppercase, tight tracking
   - Dark backgrounds: deep blacks (#1a1a2e), purples (#4a1942)
   - Heavy borders: 4-8px gold (#d4af37) borders as power statements
   - No rounded corners — sharp edges
   - Chunky titles: 5xl-7xl sizes
   - This shell "holds the sound of the sea" — contains the movement

3. **Disruption (beauty/vulnerability breaking through)**
   - Tender language: "You, Beloved", "We receive you either way"
   - Italic moments of softness breaking the uppercase
   - Colorful elements at higher opacity (30%+) — not hidden
   - Gradients (purple/gold fades) softening hard edges
   - Mix of uppercase commands and lowercase intimacy
   - Phrases acknowledging vulnerability: "We know this work is vulnerable"

**Typography:**
- Headlines: Work Sans Black (900), uppercase, tracking-tight
- Commands without shouting — weight carries authority, not aggression
- Body: Work Sans Regular/Medium (400-500)
- Disruption moments: italic, lowercase, softer weight

**Colour:**
- Deep purples, golds, black as power (the shell)
- RGB shifts, gradients as beauty (the disruption)
- Generous space — room to exist and breathe

**Imagery:**
- Centre joy AND struggle
- Black queer men claiming space
- Faces looking at lens — direct witness
- Bodies in motion and stillness

**In practice:**
- No emojis (use typography weight and color for emphasis)
- Gold em-dashes (—) for lists, not bullets
- Moments of breath between bold sections
- The aesthetic develops through iteration, not prescription

### Coalition / collaborative contexts
- Neutral base allowing partner brands to coexist
- Flexible colour system for multiple identities
- Accessible typography, no single imposed voice

### Investor / enterprise contexts
- Sophistication without stuffiness
- Nature-forward imagery (for eco contexts)
- Confidence and groundedness
- Clear value proposition without hype

## Typography

**Headlines:** DM Serif Display, Fraunces, Playfair Display (warmth)
**Body:** Work Sans, Source Sans Pro, Atkinson Hyperlegible (accessibility)
**Avoid:** Inter, Roboto for body—feels corporate

## Implementation

**HTML/Tailwind:**
- Mobile-first always
- Custom colours in config for brand consistency
- WCAG AA contrast minimum
- Semantic HTML, focus states

**React:**
- Functional components with hooks
- localStorage for draft saves where appropriate
- Tailwind for styling consistency

## Context-Specific References

For detailed pattern databases, see `references/` folder:
- `patterns-landing.md` - Landing page structures by context
- `patterns-interactive.md` - Survey, quiz, directory patterns
- `visual-systems.md` - Colour, typography, spacing guidance
