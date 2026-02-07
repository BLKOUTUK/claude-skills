# BLKOUT Claude Skills

Custom AI skills for BLKOUT — a community-owned liberation platform for and by Black queer men in the UK.

These skills encode organisational knowledge, brand voice, and design patterns so that multiple people can produce consistent, on-brand work using Claude across platforms (Claude Code CLI, claude.ai, Claude Desktop).

## Installation

### Claude Code (CLI)
```bash
git clone https://github.com/BLKOUTUK/claude-skills.git ~/.claude/skills
```

### Claude.ai (Web)
Upload individual `SKILL.md` files via Settings > Skills.

### Claude Desktop
Copy skill directories to your Claude Desktop skills location.

## Active Skills

### Visual Identity & Design

| Skill | Purpose | Triggers on |
|-------|---------|-------------|
| **blkout-brand** | Official brand guidelines — colours, typography, messaging, logo usage | Any BLKOUT material needing brand consistency |
| **blkout-themes** | 5 themed palettes (Revolutionary Red, Community Gold, Liberation Teal, Trans Joy, Abolition Dark) | Styling BLKOUT presentations, documents, web artifacts |
| **community-web-design** | Web page patterns for community organising — landing pages, dashboards, interactive tools | Building websites for community orgs, campaigns, membership portals |

### Funding & Sustainability

| Skill | Purpose | Triggers on |
|-------|---------|-------------|
| **uk-community-funding** | Learning-oriented grant writing — tracks applications, captures funder feedback, evolves with each cycle | Writing grant applications, EOIs, funding proposals, funder conversations |

### Content Production

| Skill | Purpose | Triggers on |
|-------|---------|-------------|
| **blkout-community-media** | Podcast and video production — briefings, consent, transcription, storyboarding, video generation | Podcast production, recording, transcription, video storyboard, participant briefing, media consent |

### Planned Skills

| Skill | Purpose | Status |
|-------|---------|--------|
| **blkout-voice** | Writing voice and tone — the sound equivalent of blkout-brand | Planned |

## Design Principles

Skills earn their place when they encode something that:

1. **Claude gets wrong by default** — UK context, Black queer community voice, cooperative framing
2. **Repeats across contexts** — theory of change used in grants, board papers, newsletters, pitches
3. **Has a quality bar humans can't easily maintain at speed** — consistent voice across 17 grant apps

Skills should not be so general they add nothing over base Claude, nor so specific they're used once.

## Structure

```
skills/
├── README.md
├── blkout-brand/
│   ├── SKILL.md              # Brand guidelines
│   ├── DOCUMENT-TEMPLATES.md  # Document templates
│   ├── IDENT-IMPLEMENTATION.md
│   ├── LOGO-IDENT.md
│   └── UK-CONTEXT.md
├── blkout-themes/
│   ├── SKILL.md              # Theme collection
│   └── themes/
│       └── revolutionary-red.md
├── community-web-design/
│   ├── SKILL.md              # Core skill (adapted from ui-ux-pro-max-skill)
│   └── references/
│       ├── patterns-interactive.md  # Surveys, quizzes, directories
│       ├── patterns-landing.md      # Campaigns, coalitions, investor pages
│       └── visual-systems.md        # Colour, typography, spacing, components
├── uk-community-funding/
│   ├── SKILL.md              # Learning-oriented grant writing
│   ├── applications/          # Log of what we've submitted
│   └── feedback/              # Funder feedback (the most valuable part)
├── blkout-community-media/
│   ├── SKILL.md              # Podcast & video production
│   ├── references/            # Consent, copyright, producer checklist, repurposing
│   ├── templates/             # Briefings (4 formats) + email templates
│   └── scripts/               # Python: transcribe, edit, storyboard, video gen
└── for-claude-ai/             # Paste-ready exports with sync headers
    ├── UPDATE-HEADER.md       # How the sync protocol works
    ├── blkout-brand.md
    ├── blkout-themes.md
    ├── community-web-design.md
    ├── uk-community-funding.md
    └── blkout-community-media.md
```

## Attribution

`community-web-design` is adapted from [ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) by Next Level Builder, customised for community organising and BLKOUT contexts.

## Contributing

These skills are maintained by BLKOUT community. To propose changes:
1. Open an issue or PR
2. Changes to brand/voice skills go through community governance
3. Pattern and reference additions welcome from any contributor

## License

Community-governed. See BLKOUT governance structure for decision-making processes.
