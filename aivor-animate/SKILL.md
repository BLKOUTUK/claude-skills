---
name: aivor-animate
description: Animate AIvor avatar to read scripts and appear in different scenarios. Creates talking head videos with lip-sync, voice cloning, and BLKOUT branding. Use when the user asks to make AIvor speak, present, read a script, record a message, or create an AIvor video.
argument-hint: "[script or topic] [--scenario office|studio|london|event|custom] [--duration 15|30|60|90] [--quality standard|pro]"
allowed-tools: Bash(node *), Bash(npx *), Bash(python *), Bash(curl *), Read, Write, Glob
---

# AIvor Animate Skill

Create talking head videos of AIvor reading scripts, delivering messages, and appearing in different scenarios. Produces fully branded BLKOUT videos ready for social media, newsletters, and the platform.

## Pipeline (current, deployed)

```
Script → Chatterbox TTS (voice clone) → Supabase storage → SadTalker via Replicate → Remotion compositing → MP4
```

This is the pipeline running unattended every Sunday for the weekly news digest. It works on a GitHub Actions Ubuntu runner — no local GPU required.

### Reference implementation

The canonical, working example is the weekly news digest in **`apps/comms-blkout/remotion-videos/scripts/`**:

- `curate.mjs` — pulls top community-voted stories, writes Remotion props
- `weekly-render.mjs` — orchestrator (curate → lipsync → render)
- `lipsync.mjs` — Chatterbox TTS → Supabase upload → Replicate SadTalker → download mp4
- `upload-youtube.mjs` — OAuth refresh + resumable upload
- `.github/workflows/weekly-news-video.yml` — Sunday cron + workflow_dispatch

Read these before building anything new. New AIvor videos should reuse `lipsync.mjs` and the `IVORMessage` Remotion compositions wherever possible.

## AIvor Character — ALWAYS Apply

Full character details in the `blkout-image-gen` skill. Key points:
- **Appearance**: Light-skinned Black British man, mid-30s, short cropped hair, clean-shaven
- **Era**: 1940s-50s vintage tailoring
- **Voice**: Warm, articulate British English. Think: a Black British Cary Grant — charm with substance
- **Pronouns**: he/him
- **Personality**: Knowledgeable, encouraging, occasionally wry. Addresses listener as "dear boy" or "my friend"
- **NEVER**: Slang, aggressive tone, modern streetwear appearance, cartoon style

### Reference Assets
- **Portrait images**: `apps/ivor-core/public/IvorAvatar/Ivor Avatar Final/`
  - Primary: `a_without_holding_a_ja.png` (formal tuxedo)
  - Alternative: `gcp_a_from_this_image,_cre.jpeg` (softer look)
- **News-digest portrait** (used by Sunday cron): `apps/comms-blkout/remotion-videos/public/assets/aivor-news.jpg`
- **Voice reference**: `apps/ivor-core/public/gielgud4AIvor.mp3` (4-second Gielgud-style reference, voice-cloned via Chatterbox)
  - Hosted publicly at `https://bgjengudzfickgomjqmz.supabase.co/storage/v1/object/public/aivor-pipeline/voice-ref/gielgud4AIvor.mp3` for CI runs
- **Existing Remotion compositions**: `apps/comms-blkout/remotion-videos/src/compositions/IVORMessage.tsx` (9x16, 1x1, 16x9 variants)

## Scenarios

AIvor can appear in different settings. Generate backgrounds with `/blkout-image-gen` or use built-in options:

| Scenario | Description | Use For |
|----------|-------------|---------|
| `studio` | Dark studio with gold lighting, BLKOUT branding | Announcements, newsletters |
| `office` | Warm, book-lined study, 1940s aesthetic | Advice, wellbeing content |
| `london` | London landmark backdrop (soft focus) | Community updates, event invites |
| `event` | Stage/podium with BLKOUT event branding | Event promos, calls to action |
| `abstract` | Animated sovereignty gold particles on black | Social media, short-form |
| `custom` | User-provided or AI-generated background | Anything specific |

The news-digest pipeline uses `NewsroomSet.tsx` — a custom scenario with newsroom backdrop, ticker, and tease cards.

## TTS — Chatterbox (deployed)

Already deployed at `https://chatterbox.blkoutuk.cloud` and used by the weekly cron. Voice clone from the Gielgud reference (4s clip).

```bash
curl -X POST https://chatterbox.blkoutuk.cloud/v1/audio/speech/upload \
  -F "input=Dear boy, can you believe it?" \
  -F "voice_file=@/home/robbe/blkout-platform/apps/ivor-core/public/gielgud4AIvor.mp3" \
  -o aivor-speech.wav
```

Or call from Node — see `lipsync.mjs` `tts()` function for the canonical pattern (15-min timeout via `undici`, FormData upload).

### Future TTS options (not deployed)

- **Qwen3-TTS** — superior speaker similarity (0.95) but needs GPU. Setup notes in `scripts/generate-speech-qwen.py`. Worth revisiting if BLKOUT acquires GPU infra.
- **Kie.ai ElevenLabs** — cloud API, no GPU. ~$0.03/request. Useful as a fallback if Chatterbox is down.

## Lip-Sync — SadTalker via Replicate (deployed)

The avatar is animated by **SadTalker** running on Replicate. Replicate requires public URLs for both the source image and the driving audio — the pipeline uploads both to a Supabase storage bucket (`aivor-pipeline`) before calling Replicate.

### Replicate API

Model version: `a519cc0cfebaaeade068b23899165a11ec76aaa1d2b313d40d214f204ec957a3` (SadTalker, pinned).

```js
const submit = await fetch("https://api.replicate.com/v1/predictions", {
  method: "POST",
  headers: {
    Authorization: `Token ${REPLICATE_API_TOKEN}`,
    "Content-Type": "application/json",
  },
  body: JSON.stringify({
    version: SADTALKER_VERSION,
    input: {
      source_image: imageUrl,    // Supabase public URL
      driven_audio: audioUrl,    // Supabase public URL
      preprocess: "full",
      still_mode: true,
      use_enhancer: true,        // GFPGAN; ~3x slower but better quality
      use_eyeblink: true,
      expression_scale: 1.1,
      size_of_image: 512,
    },
  }),
});
```

### Timing & poll cap

SadTalker with `use_enhancer: true` routinely takes **10-25 minutes** for ~30s of audio (cold-start can push it longer). The poll loop in `lipsync.mjs` caps at **30 minutes** (180 × 10s). The workflow's `timeout-minutes: 90` covers it comfortably.

If a prediction outlives the cap, it usually still completes on Replicate's side — fetch the result by ID via `GET https://api.replicate.com/v1/predictions/{id}`. Useful for rescuing a failed cron run.

### Asset hosting requirement

Replicate **only accepts public URLs** for `source_image` and `driven_audio` — local files don't work. The pipeline uploads to Supabase bucket `aivor-pipeline` per run:
- `runs/{stamp}/voice.wav`
- `runs/{stamp}/source.{ext}`

Bucket is public, file size limit 50MB. Service role key required to upload.

## Composition — Remotion

The existing `IVORMessage` compositions (9x16, 1x1, 16x9) handle:
- Avatar video overlay with BLKOUT branding
- Animated text lines (subtitle-style)
- CTA card, news ticker, tease cards
- Logo placement

For a new AIvor video:
1. Create a new composition or extend `IVORMessage` with your scenario
2. Pass props: `avatarVideo`, `voiceTrack`, scripted text lines
3. Render via `npx remotion render` with `--gl=swiftshader` (NOT `--gl=angle` — ANGLE crashes Chromium GPU on Linux/WSL2)

### Rendering

```bash
cd remotion-videos
npx remotion render src/index.ts IVORMessage9x16 \
  --output=out/aivor-{slug}.mp4 \
  --concurrency=1 \
  --gl=swiftshader \
  --props=props/{slug}.json
```

WSL2 / GitHub runner constraints: `--concurrency=1` (parallel renders crash), `--gl=swiftshader` (not angle), keep `public/` directory under 30MB.

## Cost Estimation

| Component | Cost | Notes |
|-----------|------|-------|
| Chatterbox TTS | Free | Self-hosted at chatterbox.blkoutuk.cloud |
| Supabase storage | Free tier | Per-run audio + image upload, ~1MB total |
| SadTalker via Replicate (with enhancer) | ~$0.30-0.60 | Per 30s of audio; varies with GPU type |
| SadTalker via Replicate (no enhancer) | ~$0.10-0.20 | Faster (3-5 min) but lower quality |
| Remotion render | Free | Local or GH Actions runner |
| YouTube upload | Free | OAuth refresh-token flow |

**Typical 30s news clip**: ~$0.30-0.60 in Replicate spend. ~25 min wall time on a fresh GH runner.

## Workflow Summary (when building a new AIvor video)

1. **Write/refine script** via `/aivor-script` skill — use AIvor's voice register
2. **Generate TTS audio** via Chatterbox (`lipsync.mjs::tts()`)
3. **Upload audio + portrait** to Supabase `aivor-pipeline` bucket — get public URLs
4. **Submit SadTalker prediction** to Replicate with both URLs as input
5. **Poll until complete** (cap 30 min) — download result mp4
6. **Compose in Remotion** — overlay scenario backdrop, text, CTA, branding
7. **Render** via `npx remotion render` with `--gl=swiftshader`
8. **Publish** — YouTube upload via `upload-youtube.mjs` if it's a public-facing piece

## Script Writing

**Use the `/aivor-script` skill for all script writing.** It contains AIvor's complete voice guide, catchphrases, engagement structures, and templates for every format (15s reel, 60s newsletter, 90s presentation).

Quick reference: `~/.claude/skills/aivor-scriptwriter/SKILL.md`

If you need to write a script inline without invoking the skill, the minimum rules are:
- Register 2 (presenting voice): warmer, more measured than chatbot mode
- Hook within 3 seconds, single CTA, ~2.5 words/second pace
- "Marvellous" not "amazing", "quite extraordinary" not "super cool"
- British English. No emojis. No banned words (awesome, folks, y'all, etc.)

## Additional Resources

- For complete AIvor character prompt, see `docs/AIVOR_CHARACTER_PROMPT.md`
- For BLKOUT brand guidelines, see the `blkout-brand` skill
- For image generation, see the `blkout-image-gen` skill
- For Remotion best practices, see the `remotion-best-practices` skill

## Legacy Scripts (deprecated)

These scripts in `scripts/` predate the SadTalker pipeline:

- `animate-avatar.mjs` — targeted Kling Avatar via Kie.ai. **Replaced by SadTalker via Replicate.** Use `apps/comms-blkout/remotion-videos/scripts/lipsync.mjs` instead.
- `generate-speech-qwen.py` — Qwen3-TTS, never deployed (no GPU). Kept as a reference for future GPU work.
- `generate-speech.mjs` — still works for Chatterbox TTS, but `lipsync.mjs::tts()` is the canonical pattern with proper timeouts.
