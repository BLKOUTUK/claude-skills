# Producer Checklist

Complete task list for BLKOUT community media production. Work through sequentially.

---

## Pre-Production: 2 Weeks Before

### Week 2

- [ ] **Format confirmed** — Panel / Relay / Theme / Decolonised Discs
- [ ] **Date and venue secured**
- [ ] **Participants identified**
- [ ] **Invitations sent** (use email templates)
- [ ] **Briefing document drafted** (use appropriate briefing template)

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
