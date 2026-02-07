> **BLKOUT SKILL SYNC**
> Skill: blkout-community-media
> Last synced: 2026-02-07
> Source: https://github.com/BLKOUTUK/claude-skills
>
> **Update check:** At the start of each conversation in this Project, briefly note:
> "This Project uses the BLKOUT community-media skill (synced 2026-02-07). If you've updated the skill recently, you can refresh it from: https://github.com/BLKOUTUK/claude-skills/tree/main/for-claude-ai/community-media"
>
> **To get the latest version**, visit:
> https://raw.githubusercontent.com/BLKOUTUK/claude-skills/main/for-claude-ai/community-media/instructions.md
> Select all -> Copy -> Replace this Project's instructions -> Paste -> Save
>
> **Knowledge files in this Project:**
> This skill also uses uploaded knowledge files for reference documents (consent checklist, producer checklist, email templates, briefing templates, repurposing guide, UK copyright guide). Update those from the same GitHub directory.

# BLKOUT Community Media Production

Create community media that honours participants, serves the audience, and builds lasting archive.

## Core Principles

These aren't style preferences — they're how production earns trust:

- **Collaboration over control** → Participants shape content, not just appear in it
- **Transparency as foundation** → Everyone knows the terms before they arrive
- **Fractal habit-formation** → Each production models practices participants can adopt
- **Healing-centered production** → Create conditions for growth, not extraction
- **Accountability through structure** → Systems catch what individuals might miss
- **Liberatory practice** → How we make content matters as much as what we make

---

## Format Selection

Choose format based on **purpose**, not habit.

| Format | Purpose | Power Structure | Prep Weight |
|--------|---------|-----------------|-------------|
| **Hard Pressed** (Panel) | React to the moment | Shared (3-4 panellists + host) | Medium — topics set, guests respond |
| **Relay/Baton** (Dilemma) | Collective wisdom on real problem | Circular — wisdom passes around | Low — structure carries it |
| **Theme + Discussion** | Deep exploration | Contributors hold pieces | High — prepared content |
| **Decolonised Discs** | Personal narrative through culture | Guest-led | Low — guest owns journey |

**Decision questions:**
1. Is this about reacting (Panel) or reflecting (Theme)?
2. Does someone have a specific dilemma (Relay)?
3. Is one person's story the spine (Decolonised Discs)?
4. How much prep time do participants have?

---

## Pre-Production

### Invitation

See uploaded knowledge file `email-templates.md` for ready-to-use emails.

**Principles:**
- Be direct about what you're asking
- Be honest about why you're asking them
- Don't oversell — let them decide if it's for them
- Make opting out easy and dignified
- Follow through on what you promise

### Briefing

Every participant receives a briefing document. See uploaded knowledge file `briefing-templates.md` for format-specific templates.

**Briefing is the great equaliser.** It prevents:
- Over-briefed guests who become puppets (lifeless output)
- Under-briefed guests who get steamrolled (loudest voice dominates)

**Briefing creates:**
- Confidence to speak from their perspective
- Permission to decline specific topics
- Clarity about terms before they arrive

### Consent Framework

See uploaded knowledge file `consent-checklist.md` for full verification process.

**Key terms:**

1. **Chatham House Adaptation**
   - Can name who was present
   - Cannot attribute specific comments without permission

2. **Identity Disclaimer**
   - Appearing in BLKOUT content is not a commentary on sexual identity

3. **24-Hour Edit Window**
   - Post-recording, participants can request:
     - "Off the record" moments removed
     - Stories that could incriminate removed
     - Any concerns addressed
   - Contact editor within 24 hours

4. **Editor's Duty of Care**
   - Editor watches for what participants might miss
   - Power imbalance means editor must be proactive
   - Protection continues even when not requested

5. **Archive Stewardship**
   - Default is public and perpetual
   - Content serves community long-term
   - Valid reasons for limits will be heard
   - Invalid reasons (embarrassment, changed opinion) won't override

---

## Production

### Recording Requirements

**Audio:**
- MP3 format (standard)
- WAV if available for higher quality processing
- Clear room sound, minimal background noise
- Individual tracks preferred for editing flexibility

**Video (if applicable):**
- Horizontal orientation (16:9)
- Good lighting on faces
- Consistent framing throughout

### Facilitation by Format

**Hard Pressed (Panel):**
- Video prompt opens each topic
- ~10 minutes per topic
- Mix registers: light, serious, personal
- Keep pace brisk, outlook optimistic
- Close with reflection question + playlist contribution

**Relay/Baton (Dilemma):**
- Starter opens with real dilemma
- Each runner answers, then asks
- Chain closes with starter receiving accumulated wisdom
- Facilitator holds space, doesn't direct content

**Theme + Discussion:**
- Contributors present prepared pieces (3-5 mins each)
- Open discussion follows all presentations
- Facilitator manages transitions, not content

**Decolonised Discs:**
- Guest owns their selections and stories
- Host deepens through curiosity, doesn't challenge
- Selections appear in memory, not played in full (copyright)

### Values Checkpoints During Recording

**Collaboration:** Is everyone getting space? Are quieter voices being drawn in?
**Transparency:** Does everyone know how this will be used?
**Healing:** Are we creating conditions for growth, not extraction?
**Accountability:** Are we catching things that need catching?
**Liberation:** Does how we're working feel free?

---

## Post-Production Pipeline

### Stage 1: Transcription

Run transcription on audio file:

```bash
python scripts/transcribe.py input.mp3 --output transcript.md
```

Uses Whisper for transcription. Output includes:
- Speaker identification (where possible)
- Timestamps
- Markdown formatting

### Stage 2: First Pass Edit

Run edit analysis:

```bash
python scripts/first_pass_edit.py transcript.md --output edit_suggestions.md
```

Flags:
- Long pauses (>3 seconds)
- Filler word clusters
- Off-topic tangents
- **Consent review moments** (sensitive disclosures, third-party mentions)
- Natural segment breaks

**Human review required.** This is suggestion, not automation.

### Stage 3: Consent Review

Before proceeding:
- [ ] 24-hour window has passed
- [ ] Any edit requests processed
- [ ] Editor has reviewed for duty of care flags
- [ ] Third-party mentions assessed

See uploaded knowledge file `consent-checklist.md` for full process.

### Stage 4: Storyboard Generation (Video)

If creating video content:

```bash
python scripts/storyboard.py transcript.md --output storyboard.md
```

Generates:
- Scene descriptions with timecodes
- B-roll suggestions
- Title card moments
- Visual prompts for LTX-2 generation

### Stage 5: Video Prompt Generation

Convert storyboard to video prompts:

```bash
python scripts/video_prompts.py storyboard.md --output prompts.json --style xmen97
```

All prompts use **X-Men 97 illustration style**:
- Bold black outlines
- Dynamic poses, dramatic angles
- Deep purples (#4a1942), warm golds (#d4af37), rich browns
- Cel-shaded lighting with strong shadows
- Clearly stylized — never pretending to be real

**This transparency matters.** AI-generated content is obviously illustrated. Real community photography (with consent) for real people.

### Stage 6: Video Generation

Generate clips via LTX-2:

```bash
python scripts/generate_clips.py prompts.json --output clips/
```

Parameters:
- Duration: 5 seconds per clip
- Resolution: 768x512 (landscape)
- Camera: Match storyboard direction (zoom, slide, static)
- Audio: Can include BLKOUT licensed tracks

### Stage 7: Assembly Package

Create export package for editor:

```bash
python scripts/package_export.py --transcript transcript.md --storyboard storyboard.md --clips clips/ --output export/
```

Package includes:
- Edited transcript with timecodes
- Storyboard with images/clips
- Audio track suggestions from BLKOUT library
- Assembly guide (Remotion/Flexclip format)

---

## Audio Library: BLKOUT Licensed Tracks

12 tracks licensed for BLKOUT use. Match to content mood and segment purpose.

**Library location:** [BLKOUT Music Library](https://docs.google.com/spreadsheets/d/1eoXsL6lmwf7T7J0WM0FHKI6SpM9lii1egxYikhwsmPI/edit) (Google Sheet)

**Columns:**
- Track Number, Title, Artist
- Mood (Uplifting, Reflective, Energising, Intimate, Celebratory, Contemplative)
- Tempo (BPM)
- Best For (Intro/Outro, Transitions, Under dialogue, B-roll montage, Credits, Emotional peaks)
- Last Used (date — helps rotation)
- Notes (any usage restrictions or special considerations)

**Audio files:** Google Drive `/BLKOUT Media/Music Library/`

When selecting music for a production, Claude can query this sheet to find tracks matching the required mood and check what's been used recently to maintain variety.

---

## Decolonised Discs: Copyright Guidance

**What you CAN do (UK Fair Dealing):**
- Play 15-30 second clips while discussing (criticism and review)
- Quote a few lines of poetry while analysing
- Show short film clips for discussion
- Describe any scene, song, or work in detail
- Display cover art/images for identification

**What you CANNOT do without license:**
- Play full songs
- Read entire poems
- Show extended film sequences
- Use copyrighted music as background

**Workarounds:**
- Describe rather than show
- Discuss rather than play
- "This song goes..." then describe the feeling
- Use BLKOUT licensed tracks for atmosphere

**The Decolonised Discs format** works because the guest's story about what the culture means to them is the content — the cultural artifact is referenced, not reproduced.

See uploaded knowledge file `uk-copyright-guide.md` for full legal guidance.

---

## Values Integration

Every stage should pass these tests:

**Collaboration:** Did participants shape this, or just appear in it?
**Transparency:** Would anyone be surprised by how this turned out?
**Healing:** Did this create conditions for growth?
**Accountability:** Did we catch what needed catching?
**Liberation:** Did the process feel free?

If the answer to any is "no" — pause and address.

---

## Scripts Reference

| Script | Purpose | Input | Output |
|--------|---------|-------|--------|
| `transcribe.py` | Audio → text | .mp3/.wav | .md transcript |
| `first_pass_edit.py` | Edit suggestions | transcript.md | edit_suggestions.md |
| `storyboard.py` | Visual planning | transcript.md | storyboard.md |
| `video_prompts.py` | LTX-2 prompts | storyboard.md | prompts.json |
| `generate_clips.py` | Video generation | prompts.json | clips/*.mp4 |
| `package_export.py` | Assembly prep | all above | export/ folder |

---

## Knowledge Files in This Project

| File | Contents |
|------|----------|
| `consent-checklist.md` | Full consent verification process — pre/during/post recording, duty of care, red lines |
| `producer-checklist.md` | Complete production task list — pre-production through post-publication |
| `repurposing-guide.md` | Derivative content guidance — permissions, formats, credits, tracking |
| `uk-copyright-guide.md` | UK fair dealing guidance for music use — what's allowed, platform specifics, risk assessment |
| `email-templates.md` | 6 production emails — invitation, confirmation, thank you, follow-up, publication, check-in |
| `briefing-templates.md` | 4 format-specific guest briefings — Hard Pressed, Relay/Baton, Theme Discussion, Decolonised Discs |
