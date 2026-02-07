> **BLKOUT SKILL SYNC**
> Skill: blkout-community-media
> Last synced: 2026-02-07
> Source: https://github.com/BLKOUTUK/claude-skills
>
> **Update check:** At the start of each conversation in this Project, briefly note:
> "This Project uses the BLKOUT community-media skill (synced 2026-02-07). If you've updated the skill recently, you can refresh it by pasting the latest version from: https://raw.githubusercontent.com/BLKOUTUK/claude-skills/main/for-claude-ai/blkout-community-media.md"
>
> **To get the latest version**, visit:
> https://raw.githubusercontent.com/BLKOUTUK/claude-skills/main/for-claude-ai/blkout-community-media.md
> Select all -> Copy -> Replace this Project's instructions -> Paste -> Save

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

See `templates/invitation-templates.md` for ready-to-use emails.

**Principles:**
- Be direct about what you're asking
- Be honest about why you're asking them
- Don't oversell — let them decide if it's for them
- Make opting out easy and dignified
- Follow through on what you promise

### Briefing

Every participant receives a briefing document. See `templates/briefing-*.md` for format-specific templates.

**Briefing is the great equaliser.** It prevents:
- Over-briefed guests who become puppets (lifeless output)
- Under-briefed guests who get steamrolled (loudest voice dominates)

**Briefing creates:**
- Confidence to speak from their perspective
- Permission to decline specific topics
- Clarity about terms before they arrive

### Consent Framework

See `references/consent-checklist.md` for full verification process.

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

See `references/consent-checklist.md` for full process.

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

---

## Email Templates

See `templates/email-templates.md` for:
- Invitation (draft, personalise before sending)
- Confirmation (24 hours before, include address + phone)
- Thank you (post-recording, 24-hour window reminder, feedback request)

---

## Producer Checklist

See `references/producer-checklist.md` for complete task list covering:
- Pre-production (2 weeks → recording)
- Day of recording
- Post-production (24 hours → publication)
- Post-publication

---

## Repurposing

See `references/repurposing-guide.md` for:
- Derivative formats (clips, quotes, transcripts, articles)
- Additional permission requirements
- Chatham House in derivatives
- Credit templates
- What not to do
- When something goes wrong

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

## File Locations

- **Briefing templates:** `templates/briefing-*.md`
- **Email templates:** `templates/email-templates.md`
- **Invitation templates:** `templates/invitation-templates.md`
- **Consent checklist:** `references/consent-checklist.md`
- **Producer checklist:** `references/producer-checklist.md`
- **Repurposing guide:** `references/repurposing-guide.md`
- **Copyright guide:** `references/uk-copyright-guide.md`
- **Scripts:** `scripts/`

---

# Consent Checklist: Complete Reference

*For BLKOUT Community Media producers and editors*

---

## Core Principles

Consent in community media is not a checkbox — it's a practice. These aren't bureaucratic requirements; they're how we honor the people who trust us with their stories.

1. **Informed** — People know what they're agreeing to
2. **Ongoing** — Consent can be withdrawn; circumstances change
3. **Specific** — Different uses may require different permissions
4. **Documented** — We can show what was agreed
5. **Protective** — We hold more care than strictly required

---

## Pre-Recording Consent

### Before Invitation

- [ ] **Format clarity**: Can you clearly explain what they're being invited to?
- [ ] **Use clarity**: Can you clearly explain how the content will be used?
- [ ] **Risk assessment**: Have you considered any particular sensitivities for this person/topic?

### Invitation Stage

- [ ] **Written briefing sent**: Briefing document appropriate to format
- [ ] **Consent terms included**: Core terms explained in briefing
- [ ] **Questions invited**: Clear path to ask questions before agreeing
- [ ] **Opt-out easy**: No pressure language; declining is explicitly okay

### Confirmation Stage

- [ ] **Participation confirmed**: Explicit agreement received (email/message)
- [ ] **Terms acknowledged**: They've confirmed they've read and understood the terms
- [ ] **Questions answered**: Any questions they raised have been addressed
- [ ] **Special considerations noted**: Any specific requests or concerns documented

---

## Recording Consent

### At Start of Recording

- [ ] **Verbal confirmation**: "Before we start, I want to confirm you're happy to proceed on the terms we discussed. Any questions?"
- [ ] **Recording notice**: "I'm now starting the recording"
- [ ] **Brave space reminder**: "Remember, this is a brave space — you can pause or stop at any time"

### During Recording

- [ ] **Check-ins as needed**: If conversation goes to sensitive territory, pause to check in
- [ ] **Respect hesitation**: If they seem uncomfortable, acknowledge and offer to move on
- [ ] **No pressure for disclosure**: Never push for more than they want to share

### Before Ending Recording

- [ ] **Anything to add**: "Is there anything you'd like to add or clarify?"
- [ ] **Anything to flag**: "Is there anything you've said that you'd like us to be particularly careful with in the edit?"
- [ ] **24-hour reminder**: "Remember, you have 24 hours to request any cuts — just email me"

---

## Post-Recording Consent

### Immediate (Within 2 Hours)

- [ ] **Thank you email sent**: Confirms participation and restates 24-hour window
- [ ] **Contact clear**: They know who to contact for edit requests
- [ ] **Timeline shared**: When they can expect to see the edit

### 24-Hour Window

- [ ] **Window tracked**: Clear record of when 24 hours ends
- [ ] **Requests received**: Any edit requests documented
- [ ] **Requests honored**: All reasonable requests actioned
- [ ] **Confirmation sent**: If changes made, confirm what was removed

### Edit Review

- [ ] **Draft shared**: Participant sees edit before publication
- [ ] **Adequate time**: At least 48 hours to review (more if possible)
- [ ] **Feedback incorporated**: Any concerns addressed
- [ ] **Final approval**: Explicit sign-off received

---

## Special Consent Considerations

### Third Parties Mentioned

When a participant mentions someone else by name:

- [ ] **Identified in edit review**: Flag all named third parties
- [ ] **Necessity assessed**: Is naming them essential to the story?
- [ ] **Risk assessed**: Could identification harm them?
- [ ] **Options presented**: Can we anonymize? ("a friend", "someone I knew")
- [ ] **Participant consulted**: Their preference on how to handle
- [ ] **Editor decision**: Final call documents reasoning

**Default**: Remove or anonymize unless there's clear reason to keep and no evident risk.

### Sensitive Disclosures

When someone shares something that could affect them if public:

- [ ] **Identified in edit review**: Flag health, trauma, relationships, family, employment
- [ ] **In-moment check**: Did we check in during recording?
- [ ] **Highlight for participant**: Draw attention to this in draft review
- [ ] **Explicit confirmation**: "You shared X — are you comfortable with this being public?"

### Identity Disclosures About Others

When someone outs or identifies another person:

- [ ] **Automatic flag**: This should always be caught
- [ ] **Default removal**: This should not be published without exceptional reason
- [ ] **Participant informed**: Explain why this is being removed
- [ ] **Context preserved**: Find alternative framing that protects the third party

**This is non-negotiable**: We do not out people, ever, regardless of participant's wishes.

### Minors

If anyone under 18 is discussed or involved:

- [ ] **Heightened scrutiny**: Additional care in all decisions
- [ ] **Anonymization default**: Minors should not be identifiable
- [ ] **No imagery**: Do not generate images depicting specific minors
- [ ] **Story permission**: If telling a story significantly about a minor, consider whether it's theirs to tell

---

## Editor's Duty of Care

Even when participants don't flag concerns, editors must independently assess:

### Proactive Checks

- [ ] **Employment risk**: Could this harm their job or career?
- [ ] **Family risk**: Could this damage family relationships?
- [ ] **Safety risk**: Could this put them in physical danger?
- [ ] **Future self risk**: Might they regret this in 5, 10, 20 years?
- [ ] **Community risk**: Could this harm their standing in communities they value?

### When to Act Unilaterally

If you identify significant risk that the participant hasn't flagged:

1. **Raise it with them first**: "I noticed you said X — I want to flag that this could potentially [risk]. Are you comfortable with it staying in?"

2. **If they want to keep it**: Document the conversation. Respect their autonomy unless risk is severe.

3. **If risk is severe**: Reserve the right to remove even against their wishes. Explain clearly why. This should be rare.

### Documentation

For any duty of care intervention:
- What was the concern?
- Was it raised with participant?
- What was their response?
- What was the final decision?
- Who made it?

---

## Publication Consent

### Pre-Publication

- [ ] **Final edit approved**: Explicit participant sign-off
- [ ] **Publication date agreed**: Participant knows when it goes live
- [ ] **Platform confirmed**: They know where it will appear
- [ ] **Promotional use**: They know clips may be used on social media

### At Publication

- [ ] **Notification sent**: Participant told it's now live
- [ ] **Links provided**: They can find and share it
- [ ] **Thanks expressed**: Appreciation for their contribution

### Post-Publication

- [ ] **Monitoring**: Watch for any concerns that arise
- [ ] **Responsive**: Quick response if participant raises issues
- [ ] **Removal path clear**: They know they can request removal

---

## Archive & Removal

### Default Position

- Content is public and perpetual
- Participant can request removal at any time
- Valid reasons include: changed circumstances, personal safety, changed views, "I've changed my mind"

### Removal Request Process

1. **Receive request**: Document date and reason given
2. **Acknowledge**: Respond within 48 hours
3. **Assess**: Is this straightforward or complex?
4. **Action**: Remove from all platforms where feasible
5. **Confirm**: Tell participant what was removed and from where
6. **Archive**: Keep internal copy with removal documentation

### What We Can't Remove

- Content that has been legitimately copied by others
- Content in web archives (though we can request removal)
- Screenshots or recordings made by third parties

We should be honest about these limitations.

---

## Consent Record Template

For each production, maintain a consent record:

```
CONSENT RECORD: [Production Title]
Participant: [Name]
Recording Date: [Date]
Producer: [Name]

PRE-RECORDING
- Briefing sent: [Date]
- Confirmation received: [Date]
- Special considerations: [Notes]

RECORDING
- Verbal consent confirmed: [Yes/No]
- Issues during recording: [Notes]
- Flags raised by participant: [Notes]

POST-RECORDING
- Thank you sent: [Date]
- 24-hour window ended: [Date/Time]
- Edit requests received: [Notes]
- Draft sent for review: [Date]
- Final approval received: [Date]

EDITOR'S DUTY OF CARE
- Third parties flagged: [Notes]
- Sensitive disclosures flagged: [Notes]
- Proactive interventions: [Notes]

PUBLICATION
- Published: [Date]
- Platforms: [List]
- Notification sent: [Date]

ONGOING
- Removal requests: [None / Date and details]
- Other post-publication contact: [Notes]
```

---

## Quick Reference: Red Lines

Things we never do, regardless of consent given:

1. **Out someone** — Reveal someone's sexuality, gender identity, HIV status, etc. without their explicit, informed consent for that specific disclosure
2. **Identify minors** — Name or make identifiable children in contexts that could harm them
3. **Enable harm** — Publish content we believe will lead to physical harm
4. **Misrepresent** — Edit someone's words to change their meaning
5. **Ignore withdrawal** — Once consent is withdrawn, we stop using the content

---

*This document should be reviewed with legal counsel periodically and updated as practices evolve.*

---

# Producer Checklist

Complete task list for BLKOUT community media production. Work through sequentially.

---

## Pre-Production: 2 Weeks Before

### Week 2

- [ ] **Format confirmed** — Panel / Relay / Theme / Decolonised Discs
- [ ] **Date and venue secured**
- [ ] **Participants identified**
- [ ] **Invitations sent** (use `templates/email-templates.md`)
- [ ] **Briefing document drafted** (use appropriate `templates/briefing-*.md`)

### Week 1

- [ ] **All participants confirmed**
- [ ] **Briefing documents sent** (at least 5 days before)
- [ ] **Topics/questions finalised** (if applicable)
- [ ] **Video prompts prepared** (if using, for Hard Pressed)
- [ ] **Technical check:**
  - [ ] Recording equipment tested
  - [ ] Backup recording method available
  - [ ] Venue acoustics checked
- [ ] **Any travel/access needs confirmed with participants**

### 48 Hours Before

- [ ] **Final participant check-in** — everyone still confirmed?
- [ ] **All materials ready:**
  - [ ] Topic sheets/prompts printed
  - [ ] Playlist link ready (if applicable)
  - [ ] Any visual aids prepared
- [ ] **Run sheet drafted** — who does what when

### 24 Hours Before

- [ ] **Confirmation emails sent** (use template)
  - [ ] Address included
  - [ ] Phone numbers included
  - [ ] Arrival time clear
- [ ] **Equipment charged/packed:**
  - [ ] Primary recorder
  - [ ] Backup recorder
  - [ ] Batteries/power
  - [ ] Cables/adapters
  - [ ] Memory cards/storage

---

## Day of Recording

### Setup (1 hour before)

- [ ] **Venue check:**
  - [ ] Space configured
  - [ ] Seating arranged for format
  - [ ] Any distracting elements removed
- [ ] **Equipment setup:**
  - [ ] Primary recording tested
  - [ ] Backup recording tested
  - [ ] Sound levels checked
- [ ] **Materials laid out:**
  - [ ] Run sheet accessible
  - [ ] Topic prompts ready
  - [ ] Water/refreshments available

### Arrival (30 mins before)

- [ ] **Greet participants as they arrive**
- [ ] **Quick orientation:**
  - [ ] Where things are
  - [ ] What to expect
  - [ ] Remind them they can decline any topic
- [ ] **Confirm verbal consent** — "We're recording for [distribution]. You've got 24 hours post-recording to request edits. All good?"

### During Recording

- [ ] **Confirm recording started** (check both primary and backup)
- [ ] **Note any moments for review:**
  - [ ] Sensitive disclosures
  - [ ] Third-party mentions
  - [ ] Technical issues
  - [ ] Particularly powerful moments
- [ ] **Values checkpoints:**
  - [ ] Is everyone getting space?
  - [ ] Is pace right?
  - [ ] Any signs of discomfort?
- [ ] **Close cleanly** — thank participants, remind them of 24-hour window

### Wrap (immediately after)

- [ ] **Confirm recordings saved**
- [ ] **Back up recordings immediately** (don't leave on single device)
- [ ] **Quick participant check-in** — how are they feeling?
- [ ] **Note any immediate edit requests**
- [ ] **Collect any items** (playlist contributions, object images, etc.)

---

## Post-Production

### Within 2 Hours

- [ ] **Recordings backed up to cloud/second device**
- [ ] **Thank you emails sent** (use template)
  - [ ] Include specific appreciation
  - [ ] 24-hour window clearly stated
  - [ ] Editor contact included

### 24 Hours After Recording

- [ ] **Edit window closed** — note any requests received
- [ ] **Begin transcription:**
  ```bash
  python scripts/transcribe.py input.mp3 --output transcript.md
  ```
- [ ] **Review transcript for obvious errors**

### 48-72 Hours After Recording

- [ ] **First pass edit analysis:**
  ```bash
  python scripts/first_pass_edit.py transcript.md --output edit_suggestions.md
  ```
- [ ] **Consent review:**
  - [ ] Process any participant edit requests
  - [ ] Editor duty of care review — anything participants might have missed?
  - [ ] Third-party mentions assessed
  - [ ] Sensitive disclosures flagged

### If Creating Video

- [ ] **Storyboard generation:**
  ```bash
  python scripts/storyboard.py transcript.md --output storyboard.md
  ```
- [ ] **Storyboard review** — does this serve the content?
- [ ] **Video prompt generation:**
  ```bash
  python scripts/video_prompts.py storyboard.md --output prompts.json --style xmen97
  ```
- [ ] **Prompt review** — check style consistency, no inappropriate imagery
- [ ] **Video generation:**
  ```bash
  python scripts/generate_clips.py prompts.json --output clips/
  ```
- [ ] **Clip review:**
  - [ ] Style consistent?
  - [ ] No unintended content?
  - [ ] Matches transcript moments?

### Final Edit

- [ ] **Audio edit:**
  - [ ] Requested cuts made
  - [ ] Duty of care cuts made
  - [ ] Technical cleanup (levels, noise)
  - [ ] Transitions smooth
- [ ] **If video:**
  - [ ] Assembly in Remotion/Flexclip
  - [ ] Clips match audio
  - [ ] Title cards/credits added
  - [ ] Music from licensed library only

### Pre-Publication Review

- [ ] **Listen/watch complete piece**
- [ ] **Final consent check:**
  - [ ] All edit requests honoured?
  - [ ] Anything new that needs flagging?
  - [ ] Would any participant be surprised by this?
- [ ] **Technical check:**
  - [ ] Audio quality acceptable?
  - [ ] Video quality acceptable?
  - [ ] No glitches/artifacts?
- [ ] **Metadata prepared:**
  - [ ] Title
  - [ ] Description
  - [ ] Participant credits (as agreed)
  - [ ] Content notes/warnings if needed

---

## Publication

- [ ] **Upload to distribution platform(s)**
- [ ] **Publication notification emails sent** (use template)
  - [ ] Include direct link(s)
  - [ ] Remind of Chatham House terms
  - [ ] Ask about social tagging preference
- [ ] **Social media posts** (if applicable)
- [ ] **Archive copy secured:**
  - [ ] Raw recording
  - [ ] Final edit
  - [ ] Transcript
  - [ ] Participant consent records

---

## Post-Publication

### First Week

- [ ] **Monitor for issues:**
  - [ ] Any participant concerns?
  - [ ] Any third-party concerns?
  - [ ] Technical problems with playback?
- [ ] **Engagement response** (comments, shares, etc.)

### One Month After

- [ ] **Performance review:**
  - [ ] Views/listens
  - [ ] Engagement
  - [ ] Feedback received
- [ ] **Process notes:**
  - [ ] What worked well?
  - [ ] What would you change?
  - [ ] Anything for skill improvement?

### Ongoing

- [ ] **Chatham House monitoring** — if you see content being misattributed, address it
- [ ] **Participant check-ins** — annual or at significant moments (use template)
- [ ] **Archive maintenance** — ensure backups remain accessible

---

## Quick Reference: Key Contacts

| Role | Contact |
|------|---------|
| Producer | [Name / contact] |
| Editor | [Name / contact] |
| Technical | [Name / contact] |
| Participant liaison | [Name / contact] |

---

## Quick Reference: Scripts

```bash
# Transcription
python scripts/transcribe.py input.mp3 --output transcript.md

# First pass edit
python scripts/first_pass_edit.py transcript.md --output edit_suggestions.md

# Storyboard (video)
python scripts/storyboard.py transcript.md --output storyboard.md

# Video prompts
python scripts/video_prompts.py storyboard.md --output prompts.json --style xmen97

# Video generation
python scripts/generate_clips.py prompts.json --output clips/

# Export package
python scripts/package_export.py --transcript transcript.md --storyboard storyboard.md --clips clips/ --output export/
```

---

# Repurposing Guide: Derivative Content

*Extending the life of community media while respecting its origins.*

---

## Principles

Content created with BLKOUT has multiple potential lives. Each derivative use should:

1. **Honor the original** — Maintain the spirit and meaning
2. **Credit properly** — Attribution is non-negotiable
3. **Assess permissions** — Some uses require additional consent
4. **Add value** — Derivatives should serve community, not just extract

---

## Standard Permissions (Included in Consent)

These uses are covered by standard consent terms and don't require additional permission:

### Full Episode Distribution
- Podcast platforms (Spotify, Apple, etc.)
- Video platforms (YouTube, Vimeo)
- BLKOUT website embedding
- Archive storage

### Promotional Clips
- Social media clips (up to 60 seconds)
- Trailer/teaser content
- Newsletter embedding
- Partner promotion (with BLKOUT credited)

### Community Archive
- Internal storage
- Research access (with appropriate protocols)
- Historical documentation

---

## Extended Permissions (May Require Additional Consent)

These uses may need additional permission depending on the specific content:

### Compilation Episodes
**What**: Combining content from multiple episodes into themed compilations
**When additional consent needed**:
- If context changes significantly
- If combining with people the participant wouldn't expect
- If the compilation creates new meaning

**Process**:
1. Draft the compilation
2. Identify all participants affected
3. Share relevant section with each
4. Obtain explicit approval
5. Document permissions

### Educational Use
**What**: Using content in workshops, training, presentations
**When additional consent needed**:
- Commercial educational settings
- When audience context differs significantly from original
- When clips will be discussed/analyzed

**Process**:
1. Describe the educational context
2. Share how content will be used
3. Offer anonymization option
4. Document permissions

### Academic/Research Use
**What**: Inclusion in research projects, academic papers, theses
**When additional consent needed**: Always

**Process**:
1. Research ethics review (if applicable)
2. Contact participant with specific request
3. Provide full details of use
4. Offer anonymization option
5. Share drafts where their content appears
6. Document permissions

### Commercial Licensing
**What**: Use by third parties for commercial purposes
**When additional consent needed**: Always

**Process**:
1. Define commercial terms
2. Contact participant with specific request
3. Negotiate revenue sharing if applicable
4. Formal written agreement
5. Legal review recommended

### Broadcast/Mainstream Media
**What**: Inclusion in TV, radio, film, major publications
**When additional consent needed**: Always

**Process**:
1. Full details of outlet, context, reach
2. Explicit written consent
3. Editorial control provisions if possible
4. Credit requirements specified
5. Formal agreement

---

## Never Without Explicit Consent

These uses always require fresh, specific, informed consent:

- **Any use that changes the original meaning**
- **Political advertising or campaign materials**
- **Endorsement of products/services**
- **AI training data** (requires explicit opt-in)
- **Content monetization by third parties**
- **Any use participant previously expressed concern about**

---

## Derivative Format Guide

### Social Clips

**Purpose**: Promotion, engagement, reach
**Length**: 15-60 seconds
**Requirements**:
- Must not misrepresent full context
- Credit overlay or caption
- Accessible (captions)
- Link to full episode

**Caption template**:
```
[Quote or description]

From [Episode Title] with [Participant Name]
Full episode: [link]

#BLKOUT #[FormatHashtag]
```

### Audiograms

**Purpose**: Audio promotion with visual element
**Length**: 30-60 seconds
**Requirements**:
- Waveform or caption animation
- Participant name visible
- Episode title visible
- BLKOUT branding
- Accessibility: captions or transcript

### Quote Cards

**Purpose**: Shareable single quotes
**Requirements**:
- Quote must be verbatim (no paraphrasing)
- Attribution: Name and episode
- BLKOUT branding
- "From [Episode Title]" context

**Template elements**:
```
"[Quote]"
— [Name], [Episode Title]
BLKOUT Community Media
```

### Highlight Reels

**Purpose**: Showcasing multiple moments/people
**Length**: 2-5 minutes
**Requirements**:
- All participants credited
- Context preserved for each clip
- Clear transitions between contributions
- Accessible (captions)

### Transcripts

**Purpose**: Accessibility, SEO, searchability
**Format**: Full text with timestamps
**Requirements**:
- Accurate transcription
- Speaker identification
- [inaudible] markers where needed
- Edit for readability without changing meaning
- Published alongside or linked from audio/video

### Blog Posts/Articles

**Purpose**: Written coverage of episode themes
**Requirements**:
- Clear attribution for all quotes
- Context for any excerpts
- Links to original
- No invention of quotes/statements

---

## Credit Templates

### Standard Credit (Short)
```
From BLKOUT Community Media's [Format Name]
```

### Standard Credit (Full)
```
From "[Episode Title]" — [Format Name]
BLKOUT Community Media
[Link]
```

### Social Media Credit
```
[Quote/Description]
From @BLKOUTUK's [Format Name]
Listen/Watch: [link]
```

### Embedded Credit (In Video)
```
[BLKOUT Logo]
[Episode Title]
[Format Name]
blkoutuk.com
```

### Academic Citation
```
[Participant Last Name], [First Name]. "[Episode Title]." [Format Name],
BLKOUT Community Media, [Day Month Year]. [URL].
```

### Press/Media Credit
```
[Name], speaking on BLKOUT Community Media's [Format Name],
episode "[Episode Title]" ([Date]). Used with permission.
```

---

## Repurposing Checklist

Before any derivative use:

- [ ] **Covered by standard consent?** Check original terms
- [ ] **Context preserved?** Does the meaning remain true?
- [ ] **Credit included?** Is attribution clear and complete?
- [ ] **Quality maintained?** Does it represent BLKOUT well?
- [ ] **Accessible?** Captions, alt text, transcripts as needed
- [ ] **Additional consent required?** If so, obtained and documented?
- [ ] **Sensitive content?** Extra care for anything flagged in original
- [ ] **Third parties?** Any additional people affected?

---

## When Participants Request Repurposing

Participants may want to use content featuring themselves:

### Personal Use
- Sharing on personal social media: Generally encouraged
- Personal portfolio/website: Generally fine
- Professional materials (CV, website): Generally fine

**Ask them to**:
- Credit BLKOUT
- Link to original where possible
- Contact us for high-quality files

### Commercial Use
If a participant wants to use their appearance commercially:
- Discuss with BLKOUT first
- Consider whether it affects other participants
- Agree terms in writing

### Speaking/Presentations
If a participant wants to use clips in their own talks:
- Generally encouraged
- Ask for BLKOUT credit
- Offer support with files/formats

---

## Tracking Derivative Use

Maintain a record of derivative content:

```
DERIVATIVE USE LOG

Original: [Episode Title]
Date: [Original Publication Date]

DERIVATIVES:
1. [Date] - [Type] - [Platform] - [Description]
2. [Date] - [Type] - [Platform] - [Description]

ADDITIONAL PERMISSIONS OBTAINED:
- [Date] - [Participant] - [Use] - [Documentation location]

THIRD PARTY USE:
- [Date] - [Requestor] - [Use] - [Terms] - [Documentation]
```

---

## Sunset Considerations

Some content may have natural expiry:
- Time-sensitive topics
- Participant role changes
- Organizational changes
- Participant requests

**Annual review questions**:
- Is this content still accurate?
- Would participant still want this public?
- Does it still represent BLKOUT's values?
- Should it be archived rather than actively promoted?

---

*This guide should be reviewed annually and updated as practices evolve.*

---

# UK Copyright & Fair Dealing Guide

*For Decolonised Discs and other music-featuring content*

---

## Overview

BLKOUT Community Media uses music under UK fair dealing provisions. This guide explains what we can do, what we can't, and how to stay on the right side of copyright law.

**Disclaimer**: This is practical guidance, not legal advice. For complex situations or when significant risk is involved, consult a qualified intellectual property lawyer.

---

## UK Fair Dealing Basics

Unlike US "fair use" (which is flexible and case-by-case), UK "fair dealing" allows specific uses:

### Permitted Purposes

1. **Research and private study**
2. **Criticism and review**
3. **Quotation**
4. **News reporting**
5. **Caricature, parody, pastiche**

For Decolonised Discs, we primarily rely on **criticism and review** and **quotation**.

### Requirements for Fair Dealing

1. **The dealing must be fair** — Not excessive, not a substitute for the original
2. **The work must have been made available to the public** — Published commercially
3. **Sufficient acknowledgment must be given** — Credit the work and creator

---

## What We Can Do

### Short Clips for Commentary

**Legal basis**: Criticism and review / Quotation

We can play short extracts of commercially released music when:
- The extract is used to discuss, analyze, or reflect on the music
- The commentary (guest's story/memories) is the primary content
- The music extract supports rather than replaces the commentary
- Full credit is given

**Practical guidelines**:
- Keep clips to 15-30 seconds typically
- Never use a clip as "background music" without commentary
- Ensure the guest's discussion is the star, not the music itself

### Identifying Music

We can name:
- Song titles
- Artist names
- Album titles
- Years of release
- Record labels

This is factual information, not copyrighted material.

### Discussing Music

We can discuss:
- The music's sound, style, production
- Its cultural significance
- Personal memories and associations
- Its impact and influence
- Lyrics (limited quotation, with commentary)

### Guest Singing/Humming

If a guest spontaneously sings or hums a snippet:
- Keep it brief (a line or two)
- In context of discussion
- Not a performance

This falls under quotation and likely fair dealing, though more legally grey than recorded clips.

---

## What We Cannot Do

### Full Track Playback
- Never play a song in full
- Never use music as background/intro without commentary
- Never create a "mixtape" style episode that's primarily music

### Creating Substitutes
- Don't use so much of a song that listeners wouldn't need to hear the original
- Don't compile "best bits" that replicate an artist's value

### Unreleased Material
- Demos, bootlegs, leaked tracks = no fair dealing protection
- Private recordings = permission required

### Cover Versions in Episode
- If you perform/record a cover, mechanical licensing applies
- This is different from playing the original commercially released version

### Sync Licensing Situations
- If you want to use music under video (not commentary), you need sync license
- This includes: intro music, background music, montage sequences

---

## Platform-Specific Considerations

### YouTube

YouTube's Content ID system may flag audio even when use is legal.

**If flagged**:
1. You can dispute under fair dealing
2. Provide reasoning: "This is commentary/criticism under UK fair dealing"
3. May need to appeal to human reviewer

**Mitigation**:
- Keep clips short
- Ensure commentary is audible around clips
- Consider timestamps in description showing context

### Spotify/Podcast Platforms

Audio-only platforms generally less aggressive on copyright.
Same principles apply:
- Keep clips short
- Ensure commentary context
- Full credit in show notes

### Social Media Clips

When repurposing for social:
- Even shorter clips (10-15 seconds max)
- Commentary must be visible/audible (captions help)
- Credit in caption/on screen

---

## Required Attribution

Every music use must include:

### Verbal (During Episode)
Host or guest names the song and artist before or after clip plays.

Example: "So this is 'Nuthin' but a 'G' Thang' by Dr. Dre..."

### Written (Show Notes)
```
Music featured in this episode:
- "[Song Title]" by [Artist] ([Album], [Year])
- "[Song Title]" by [Artist] ([Album], [Year])
All music used under UK fair dealing for criticism and review.
```

### Full Episode Credit
```
MUSIC CREDITS
[List all tracks with full details]
All music extracts are used under UK Copyright, Designs and Patents Act 1988
fair dealing provisions for criticism and review. No copyright infringement intended.
```

---

## Specific Scenarios

### Scenario 1: Guest Wants to Feature Obscure Track
**Question**: Does it matter how famous the song is?
**Answer**: No — fair dealing applies equally to obscure and famous works.

### Scenario 2: Playing Instrumental Section
**Question**: Can we use instrumental sections more freely?
**Answer**: No — the recording copyright belongs to the performer/label regardless of lyrics.

### Scenario 3: Two Guests Choose Same Song
**Question**: Can we use a song more than once across episodes?
**Answer**: Yes — each use is assessed independently. Ensure each use has its own commentary context.

### Scenario 4: Song Has Been Removed from Streaming
**Question**: Can we still use it?
**Answer**: If it was commercially released at any point, likely yes. If it was only ever on unofficial channels, be cautious.

### Scenario 5: Guest Wants to Play Their Own Music
**Question**: If guest is a musician playing their own work?
**Answer**: They hold the copyright (usually) so they can grant permission. Get it in writing. Note: label may hold recording rights.

### Scenario 6: Sampling and Interpolations
**Question**: Song we want to use samples another song?
**Answer**: Your fair dealing use of the later song doesn't require clearing the sample — that's the original artist's responsibility. You're fine.

### Scenario 7: Live Recording from Concert
**Question**: Guest wants to discuss a live performance they attended?
**Answer**: Use the commercial release version, not bootleg live recordings.

---

## Risk Assessment

### Lower Risk
- Short clips (under 20 seconds)
- Established commercial releases
- Clear commentary context
- Full attribution
- Discussion-focused content

### Higher Risk
- Longer clips (over 30 seconds)
- Recently released music
- Minimal commentary around music
- Viral potential clips
- No clear critical purpose

### Highest Risk (Avoid)
- Full songs or near-full songs
- Music as background without commentary
- No attribution
- Claiming ownership
- Monetizing primarily on the music value

---

## If We Receive a Takedown

### YouTube/Platform Takedown

1. **Don't panic** — Fair dealing is a legal defense
2. **Review the use** — Is our use genuinely fair?
3. **Dispute if appropriate** — Platforms have processes
4. **Document everything** — Correspondence, our reasoning
5. **Consider consultation** — If significant, get legal advice

### Direct Cease and Desist

If we receive a letter from a rights holder:

1. **Take seriously** — Respond promptly and professionally
2. **Don't remove immediately** — Unless clearly in the wrong
3. **Explain our position** — Fair dealing for criticism/review
4. **Seek advice** — This is where a lawyer helps
5. **Negotiate if needed** — Sometimes compromise is sensible

---

## Licensing Alternatives

If fair dealing doesn't cover a use, options include:

### Mechanical License
- For audio-only cover versions
- UK: Via MCPS (Mechanical Copyright Protection Society)

### Sync License
- For music accompanying video
- Negotiate directly with publisher/label
- Can be expensive

### Creative Commons / Royalty-Free
- Some artists release under permissive licenses
- Check terms carefully
- Still credit appropriately

### BLKOUT Licensed Tracks
- Our 12 licensed tracks can be used freely in productions
- See music library section of SKILL.md

---

## Template: Copyright Notice for Episodes

```
COPYRIGHT NOTICE

This episode contains extracts of copyrighted music used under UK Copyright,
Designs and Patents Act 1988 fair dealing provisions for criticism and review.

All music remains the intellectual property of the respective rights holders.

Music featured:
[List tracks with artist and album]

BLKOUT Community Media does not claim ownership of any third-party content.
For licensing inquiries regarding original music, contact the rights holders directly.
```

---

## Checklist: Before Using Music

- [ ] Is the song commercially released?
- [ ] Is our use short (15-30 seconds typical)?
- [ ] Is there genuine commentary/discussion around the music?
- [ ] Is the music supporting the conversation, not the main attraction?
- [ ] Have we credited the song, artist, and album?
- [ ] Is this clearly criticism/review or quotation, not just entertainment?
- [ ] Have we documented our fair dealing reasoning?

If all boxes are checked, proceed with reasonable confidence.

---

## Resources

**UK Government Guidance**:
https://www.gov.uk/guidance/exceptions-to-copyright

**IPO Copyright Notice**:
https://www.gov.uk/government/publications/copyright-notice-digital-images-photographs-and-the-internet

**Useful Reference**:
Copinger and Skone James on Copyright (legal textbook, for deep research)

---

*This guide reflects UK law as understood at time of writing. Copyright law evolves. Review annually.*

---

# Email Templates

Ready-to-use emails for the production pipeline. Personalise before sending.

---

## 1. Invitation Email (Draft)

**Subject:** Would you join us for [Format Name]?

---

Hi [Name],

I'm reaching out because [specific reason you're asking them — be honest and direct].

**What it is:**
[Format Name] is [one sentence description]. [One sentence about what makes it distinctive].

**What we're asking:**
- [Time commitment]
- [Date/timing if known]
- [Any prep required]

**What you'd get:**
- [What's in it for them — be honest, not overselling]

**The terms:**
We record and share via [distribution]. You'd have 24 hours post-recording to request any edits. Full briefing comes if you say yes.

If this isn't for you, no worries at all. If you're interested but have questions, I'm happy to talk through it.

[Your name]

---

**Personalisation notes:**
- Name exactly why you're asking *them* — generic invitations feel generic
- Be honest about time/effort required
- Don't oversell — let them decide if it's for them
- Make declining easy and dignified

---

## 2. Confirmation Email (24 Hours Before)

**Subject:** Tomorrow: [Format Name] — logistics

---

Hi [Name],

Looking forward to seeing you tomorrow. Here are the details:

**When:** [Date and time]
**Where:** [Full address with any access notes]
**Please arrive by:** [Time — usually 30 mins before start]

**Contact on the day:**
[Name]: [Phone number]
[Backup name]: [Phone number]

**What to bring:**
- [Any items mentioned in briefing]
- Yourself — preparation is about confidence, not scripts

**Quick reminders:**
- [Any format-specific reminders]
- If you need to reach us before then: [contact details]

See you tomorrow.

[Your name]

---

**Personalisation notes:**
- Check address is complete and correct
- Include both a primary and backup contact
- Keep it practical, not promotional

---

## 3. Thank You Email (Post-Recording)

**Subject:** Thank you — and next steps

---

Hi [Name],

Thank you for being part of [Format Name] [yesterday/on Date]. [One specific thing you appreciated about their contribution — be genuine].

**Your 24-hour edit window is now open.**

If there's anything you'd like us to cut or adjust — moments that felt too raw, stories that on reflection you'd rather not share publicly, anything at all — let me know by [specific time/date].

After that window closes, we'll proceed with editing. You'll hear from us again when it's ready to publish.

**A few questions if you have a moment:**

1. How did the process feel? (Anything we could do better for future participants?)
2. Would you be open to being part of future productions?
3. Anyone you'd recommend we reach out to?

No pressure on any of these — just want to keep learning.

Thanks again for your time and trust.

[Your name]

**Contact for edit requests:** [editor email/phone]

---

**Personalisation notes:**
- Be specific about what you appreciated — generic thanks feel hollow
- Make the 24-hour window clear and easy to use
- Frame feedback as learning, not obligation
- Include editor contact prominently

---

## 4. Follow-Up (If No Response to Edit Window)

**Subject:** Quick check-in before we proceed

---

Hi [Name],

Just checking in — your 24-hour edit window closes [today at time / has now closed].

If there's nothing you need adjusted, we'll proceed with editing. But if you've been meaning to flag something and haven't had a chance, let me know and we can extend.

Either way, thanks again for being part of this.

[Your name]

---

**Personalisation notes:**
- Only send if you have specific reason to check (e.g., they seemed uncertain during recording)
- Don't send as routine — it can feel pressuring

---

## 5. Publication Notification

**Subject:** [Format Name] is live

---

Hi [Name],

[Format Name] is now live:
[Link to full episode]

[If clips exist:]
We've also created some clips:
- [Clip 1 link]
- [Clip 2 link]

**Sharing:**
Feel free to share wherever feels right for you. If you'd like us to tag you on social, let us know your handles.

**Chatham House reminder:**
Others can share that you were present, but can't attribute specific comments to you without your permission.

Thank you again for being part of this. It matters.

[Your name]

---

**Personalisation notes:**
- Include direct links — don't make them search
- Remind them of Chatham House terms
- Offer but don't assume they want to be tagged

---

## 6. Anniversary/Check-In (Optional)

**Subject:** Checking in — [X months/year] since [Format Name]

---

Hi [Name],

It's been [time] since you were part of [Format Name]. I wanted to check in.

**Is everything still okay with the content?**
If your circumstances have changed and you'd like us to revisit anything, we're open to that conversation.

**Anything new you'd want to share?**
If the conversation sparked something you've been thinking about since, we'd love to hear.

No action needed if all is well. Just wanted you to know we're still here.

[Your name]

---

**Personalisation notes:**
- Use sparingly — once a year max, or at significant moments
- Frame as care, not content extraction
- Make "no response needed" clear

---

# Relay / Baton: Guest Briefing

*One conversation leads to the next.*

---

## What is Relay?

Relay is BLKOUT's conversational interview series. Each episode features one person in conversation with a BLKOUT host. At the end of each episode, you pass the baton — nominating someone from your own network to be featured next.

The result is a chain of connection: each guest is chosen by the person before them, creating a map of Black queer community as it actually exists, through relationship rather than algorithm.

## The Vibe

- **Conversation, not interview** — You're talking with someone, not performing for an audience
- **Your story, your terms** — You decide what to share and how deep to go
- **Curiosity over interrogation** — We're interested in you, not trying to catch you out
- **The baton matters** — Your nomination shapes where this goes next

## What to Expect

### Before Recording

1. **Pre-conversation call** — 15-minute chat with your host to meet each other and discuss themes
2. **No questions in advance** — We want genuine conversation, not rehearsed answers
3. **Think about your baton** — Who from your life would you want to hear from?

### During Recording

- **Duration**: ~60-75 minutes recording (edited to ~40-50 minutes)
- **Format**: One-on-one conversation (video call or in-person)
- **Style**: Flowing dialogue — expect tangents, laughter, real talk
- **Closing**: You'll pass the baton on camera

### After Recording

- **24-hour edit window** — Request any cuts within 24 hours
- **Draft review** — You'll hear/see the edit before publication
- **Baton follow-up** — We'll ask you to introduce us to your nominee

---

## Themes We Might Explore

Every conversation is different, shaped by who you are. But here are the kinds of things that often come up:

- **Your path** — How did you get where you are? What shaped you?
- **Community** — Where do you find your people? What does belonging feel like?
- **Work/craft** — What do you do and why does it matter to you?
- **Joy** — What brings you alive? What do you love?
- **Challenges** — What have you navigated? What did it teach you?
- **Vision** — What do you hope for? What are you building toward?

**You're never obligated to discuss anything you don't want to.** The conversation follows your comfort, not a script.

---

## The Baton

At the end of your episode, you'll pass the baton to someone else.

### How to Choose

Your nominee should be:
- Someone you know personally (not a celebrity you admire from afar)
- Someone whose story you'd genuinely want to hear
- Someone who identifies as Black and queer (however they define those terms)

They don't need to be famous, accomplished, or "impressive." The point is relationship — who matters to you?

### What Happens Next

1. You'll name them on camera: "I'm passing the baton to [name] because..."
2. After recording, we'll ask you to make an introduction (email or message)
3. They're free to accept or decline — no pressure either way
4. If they decline or don't respond, we'll ask you for an alternative

**Note**: You can discuss your choice with us before recording if you want to check anything.

---

## Consent Terms

By participating, you're agreeing to:

### What We Record

- Video and/or audio of your conversation
- Your baton nomination and explanation

### How We Use It

- **Primary use**: Published episode (video, audio podcast, or both)
- **Derivative use**: Clips for social media, promotional material
- **Archive**: Stored as part of BLKOUT's community archive

### Your Protections

1. **Chatham House Adaptation**
   - We can say you were featured
   - Direct quotes used outside the episode will be cleared with you first

2. **Identity Disclaimer**
   - Appearing on Relay does not constitute commentary on your sexual identity beyond what you explicitly share
   - You're a Black queer person in community; nothing more is assumed

3. **24-Hour Edit Window**
   - Within 24 hours of recording, you can request any cut
   - No explanation required
   - We will honour all reasonable requests

4. **Editor's Duty of Care**
   - Even if you don't flag something, our editor may remove content they believe could harm you
   - We'll discuss any such edits with you before publication

5. **Archive Stewardship**
   - Default: public and perpetual
   - You can request removal at any time with valid reason

---

## Practical Details

### Pre-Conversation Call
*[Date/time to be confirmed]*

### Recording Date & Time
*[To be completed]*

### Location/Platform
*[To be completed]*

### Duration
Plan for 90 minutes total (includes setup, recording, and wrap)

### Technical Requirements (if remote)
- Stable internet connection
- Quiet space
- Camera at eye level if possible
- Good lighting on your face
- Headphones recommended

---

## Questions?

Contact: *[Producer name and email]*

Come ready to have a conversation. That's all we need.

---

*Relay is a BLKOUT Community Media production.*

---

# Hard Pressed: Guest Briefing

*Welcome to Hard Pressed — where we get into it.*

---

## What is Hard Pressed?

Hard Pressed is BLKOUT's panel discussion format. Think less Question Time, more Loose Women — a group of Black queer people talking honestly about life, culture, politics, and everything in between.

Each episode explores 2-3 topics, mixing the serious with the light, the personal with the political. We're not here for gotcha moments or performance debates. We're here for real conversation.

## The Vibe

- **Brave space, not safe space** — We can't guarantee safety, but we can guarantee care
- **No wrong answers** — Your perspective is yours; you don't represent anyone else
- **Less prep, more presence** — Come as you are, not as you think you should be
- **Disagreement is welcome** — But we disagree with ideas, not people

## What to Expect

### Before Recording

1. **Topics shared in advance** — You'll receive 2-3 topic areas at least 48 hours before recording
2. **No script required** — These are conversation starters, not exam questions
3. **Your object** — Bring something meaningful to you (we'll explain more below)

### During Recording

- **Duration**: ~90 minutes total recording (edited to ~45-60 minutes)
- **Format**: Video call or in-person (you'll be told which)
- **Topics**: ~10-15 minutes per topic, flowing naturally
- **Style**: Discussion, not interview — everyone participates

### After Recording

- **24-hour edit window** — You can request cuts within 24 hours of recording
- **Draft review** — You'll see the edit before publication
- **Publication notice** — We'll let you know when it goes live

---

## "The Subject as Object"

At the start of each episode, we ask each guest to introduce themselves through **an object that means something to them**.

This isn't about showing off or finding the "right" answer. It's about starting from something real. Your object might be:

- Something you carry every day
- Something from your childhood
- Something you made
- Something someone gave you
- Something you're wearing right now

When we record, you'll have ~2 minutes to share your object and why it matters. This becomes your introduction — not your job title, not your bio, just you.

**Note**: If your object involves other people's stories (e.g., a gift from someone), you can share your relationship to it without naming them.

---

## Topics for This Episode

*[To be completed by producer before sending]*

### Topic 1: [Title]
[Brief description — 2-3 sentences framing the conversation]

### Topic 2: [Title]
[Brief description]

### Topic 3: [Title]
[Brief description]

**Note**: These are starting points. Conversations go where they go — that's the point.

---

## Consent Terms

By participating, you're agreeing to:

### What We Record

- Video and audio of the session
- Your contributions to the discussion
- Your object introduction

### How We Use It

- **Primary use**: Published episode (video, audio podcast, or both)
- **Derivative use**: Clips for social media, promotional material
- **Archive**: Stored as part of BLKOUT's community archive

### Your Protections

1. **Chatham House Adaptation**
   - We can say you were there
   - We cannot attribute specific quotes without your explicit permission
   - Published quotes will be cleared with you first

2. **Identity Disclaimer**
   - Appearing on Hard Pressed does not constitute commentary on your sexual identity
   - You're a Black queer person in community; nothing more is assumed

3. **24-Hour Edit Window**
   - Within 24 hours of recording, you can request any cut
   - No explanation required
   - We will honour all reasonable requests

4. **Editor's Duty of Care**
   - Even if you don't flag something, our editor may remove content they believe could harm you
   - We'll discuss any such edits with you before publication

5. **Archive Stewardship**
   - Default: public and perpetual
   - You can request removal at any time with valid reason
   - "I've changed my mind" is a valid reason

---

## Practical Details

### Date & Time
*[To be completed]*

### Location/Platform
*[To be completed — include any technical requirements for video calls]*

### What to Wear
Whatever makes you feel like yourself. Avoid very small patterns (they strobe on camera) and pure white (can blow out). Beyond that — be you.

### Technical Requirements (if remote)
- Stable internet connection
- Quiet space
- Camera at eye level if possible
- Good lighting on your face (natural light or lamp in front of you)
- Headphones recommended

---

## Questions?

Contact: *[Producer name and email]*

We want you to feel ready, not rehearsed. If anything's unclear, just ask.

---

*Hard Pressed is a BLKOUT Community Media production.*

---

# Theme Discussion: Contributor Briefing

*Going deep on what matters.*

---

## What is Theme Discussion?

Theme Discussion is BLKOUT's format for exploring a single topic in depth. Each episode gathers multiple voices around one theme — not to reach consensus, but to map the territory of how Black queer people think about, experience, and navigate a particular subject.

This isn't a debate. It's more like a collective meditation — different perspectives illuminating different facets of the same question.

## The Vibe

- **Depth over breadth** — One topic, fully explored
- **Many truths** — Your perspective adds to the picture; it doesn't need to be the whole picture
- **Thinking aloud welcome** — You don't need to have it all figured out
- **Disagreement as data** — If you see it differently, that's valuable information

## What to Expect

### Before Recording

1. **Theme shared in advance** — You'll know the topic and key questions at least one week before recording
2. **Reflection prompts** — Optional prompts to help you think through your perspective
3. **No research required** — We want your experience and thinking, not a position paper

### Recording Format

Theme Discussions can be recorded in different ways:

- **Group session**: Multiple contributors together (like Hard Pressed but single-topic)
- **Individual interviews**: Separate conversations edited together
- **Hybrid**: Some combination of both

You'll be told which format applies to your episode.

### After Recording

- **24-hour edit window** — Request any cuts within 24 hours
- **Context check** — If your words are edited alongside others, we'll ensure context is preserved
- **Draft review** — You'll see how you appear in the edit before publication

---

## This Episode's Theme

### Theme: [Title]

*[To be completed by producer]*

[2-3 paragraphs framing the theme — what it is, why it matters, what we're curious about]

### Key Questions

We'll explore questions like:

1. [Question 1]
2. [Question 2]
3. [Question 3]

**These are starting points, not a checklist.** The conversation will find its own path.

### Reflection Prompts (Optional)

If it's helpful, you might spend some time thinking about:

- [Prompt 1]
- [Prompt 2]
- [Prompt 3]

You don't need to write anything down or prepare formal answers. These are just invitations to reflect.

---

## What We're Looking For

We're not looking for:
- Expert opinions
- Definitive answers
- Polished takes
- Agreement with each other

We are looking for:
- Your honest perspective
- Stories from your experience
- Your questions and uncertainties
- What you've noticed, wondered, struggled with

**Your contribution matters because you're you**, not because of any credentials.

---

## Consent Terms

By participating, you're agreeing to:

### What We Record

- Video and/or audio of your contribution
- Your responses to questions about the theme

### How We Use It

- **Primary use**: Published episode (video, audio podcast, or both)
- **Derivative use**: Clips for social media, promotional material
- **Thematic collections**: Your contribution may appear in future compilations on this theme
- **Archive**: Stored as part of BLKOUT's community archive

### Your Protections

1. **Context Preservation**
   - If your words are edited alongside others, we'll ensure your meaning is preserved
   - We won't cut your contribution to make it seem like you said something you didn't

2. **Identity Disclaimer**
   - Appearing on this episode does not constitute commentary on your sexual identity beyond what you explicitly share
   - You're a Black queer person in community; nothing more is assumed

3. **24-Hour Edit Window**
   - Within 24 hours of recording, you can request any cut
   - No explanation required
   - We will honour all reasonable requests

4. **Editor's Duty of Care**
   - Even if you don't flag something, our editor may remove content they believe could harm you
   - We'll discuss any such edits with you before publication

5. **Archive Stewardship**
   - Default: public and perpetual
   - You can request removal at any time with valid reason

---

## Practical Details

### Recording Date & Time
*[To be completed]*

### Recording Format
*[Group session / Individual interview / Other — to be completed]*

### Location/Platform
*[To be completed]*

### Duration
*[To be completed — varies by format]*

### Technical Requirements (if remote)
- Stable internet connection
- Quiet space
- Camera at eye level if possible
- Good lighting on your face
- Headphones recommended

---

## Questions?

Contact: *[Producer name and email]*

There's no wrong way to contribute. Just bring yourself.

---

*Theme Discussion is a BLKOUT Community Media production.*

---

# Decolonised Discs: Guest Briefing

*The music that made us.*

---

## What is Decolonised Discs?

Decolonised Discs is BLKOUT's music-led conversation format. You choose the tracks; we follow the stories. Each episode features one guest sharing songs that have shaped them — not a "best of" list or a display of taste, but a musical autobiography.

The format is inspired by Desert Island Discs, but centred on Black queer experience and freed from the colonial nostalgia of that format. We're interested in music as memory, identity, survival, joy, and liberation.

## The Vibe

- **Your music, your reasons** — No justification needed for your choices
- **Stories over analysis** — We're not reviewing the songs; we're following where they take you
- **The personal is political** — But it doesn't have to be heavy; joy counts too
- **No guilty pleasures** — If you love it, it belongs here

## What to Expect

### Before Recording

1. **Choose your tracks** — Select 6-8 songs that matter to you (see guidance below)
2. **Share your list** — Send us your tracks at least one week before recording
3. **Optional notes** — You can share a few words about each track, or save it all for the conversation

### During Recording

- **Duration**: ~90 minutes recording (edited to ~60 minutes)
- **Format**: One-on-one conversation with host
- **Structure**: We'll work through your tracks, letting each one open a conversation
- **Music**: We'll play clips during recording (see copyright note below)

### After Recording

- **24-hour edit window** — Request any cuts within 24 hours
- **Draft review** — You'll hear the edit before publication
- **Music clearance** — We'll handle the copyright considerations (see below)

---

## Choosing Your Tracks

### How Many?
Choose **6-8 songs**. This gives us enough for a full episode with room for the conversation to breathe.

### What Kind?
Any genre, any era, any language. The only criterion is: **this song matters to you**.

Consider songs that:
- Remind you of a specific time or place
- Helped you understand something about yourself
- Got you through something difficult
- Connect you to family, community, or culture
- Simply bring you joy
- Changed how you heard music
- You're almost embarrassed to admit you love

### Selection Tips

- **Mix it up** — Different moods, different eras, different stories
- **Be honest** — The "impressive" choice is less interesting than the true one
- **Include joy** — Not everything needs to be profound or painful
- **Trust yourself** — If you keep thinking about a song, it probably belongs on your list

### What We Need From You

For each track, please provide:
- Song title
- Artist
- Album (if you know it)
- Year (approximately, if you know it)

You can also include a sentence about why you chose it, but this is optional — you might prefer to save the story for the conversation.

---

## Copyright & Music Use

### What Happens in the Episode

We want to use your chosen music in the published episode. Here's how we navigate copyright:

**During Recording**
- We'll play clips of your tracks as conversation prompts
- This helps anchor the discussion and jog memory

**In the Published Episode**
- We'll include short clips (typically 15-30 seconds) under UK fair dealing provisions
- Clips are used for "criticism, review, or quotation" — your commentary is the primary content
- We clearly identify all tracks (title, artist)

**What Fair Dealing Allows**
Under UK copyright law, we can use limited extracts for criticism and review provided:
- The use is "fair" (short clips, not replacements for the original)
- The work has been made available to the public
- Sufficient acknowledgment is given

**What This Means for You**
- You can choose any commercially released song
- We handle the copyright considerations — you don't need to clear anything
- If a specific track proves problematic, we'll discuss alternatives with you

### Limitations

We may not be able to use:
- Very long clips (we keep it short)
- Unreleased or private recordings without permission
- Tracks where the entire value would be the music itself rather than your commentary

If any of your choices raise issues, we'll talk to you about it before publication.

---

## Consent Terms

By participating, you're agreeing to:

### What We Record

- Video and/or audio of your conversation
- Your stories and reflections about your chosen music

### How We Use It

- **Primary use**: Published episode (video, audio podcast, or both)
- **Derivative use**: Clips for social media, promotional material
- **Archive**: Stored as part of BLKOUT's community archive

### Your Protections

1. **Chatham House Adaptation**
   - We can say you were featured
   - Direct quotes used outside the episode will be cleared with you first

2. **Identity Disclaimer**
   - Appearing on Decolonised Discs does not constitute commentary on your sexual identity beyond what you explicitly share
   - You're a Black queer person in community; nothing more is assumed

3. **24-Hour Edit Window**
   - Within 24 hours of recording, you can request any cut
   - No explanation required
   - We will honour all reasonable requests

4. **Editor's Duty of Care**
   - Even if you don't flag something, our editor may remove content they believe could harm you
   - We'll discuss any such edits with you before publication

5. **Archive Stewardship**
   - Default: public and perpetual
   - You can request removal at any time with valid reason

---

## Practical Details

### Track List Deadline
Please send your tracks by: *[Date — at least 1 week before recording]*

### Recording Date & Time
*[To be completed]*

### Location/Platform
*[To be completed]*

### Duration
Plan for 2 hours total (includes setup, recording, and wrap)

### Technical Requirements (if remote)
- Stable internet connection
- Quiet space
- Camera at eye level if possible
- Good lighting on your face
- Headphones recommended
- Access to your tracks (streaming or files) to listen during recording

---

## Preparing Your List

When you're ready, send your track list to: *[Producer email]*

Use this format:
```
DECOLONISED DISCS — [Your Name]

1. [Song Title] — [Artist] ([Album], [Year])
   Optional note: [Why this track?]

2. [Song Title] — [Artist] ([Album], [Year])
   Optional note:

[etc.]
```

---

## Questions?

Contact: *[Producer name and email]*

The only wrong list is someone else's. Choose yours.

---

*Decolonised Discs is a BLKOUT Community Media production.*
