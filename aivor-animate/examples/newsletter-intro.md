# Example: AIvor Newsletter Video Introduction

## Request
"Make AIvor record a 15-second intro for the March 2026 newsletter"

## Script (written in AIvor's voice)
"My dear friends, welcome to March. This month, we celebrate not just our tenth anniversary, but the extraordinary community you've helped build. From our first gathering to today's digital liberation platform — every step has been a revolution. Let me show you what's ahead."

## Parameters
- Scenario: studio
- Duration: ~15s (38 words at AIvor's measured pace)
- Quality: standard (720p, good enough for newsletter embed)
- Emotion: warm

## Pipeline Steps

1. **TTS**: Generate speech via Qwen3-TTS with `--emotion warm`
2. **Upload audio**: To Supabase storage for public URL
3. **Avatar**: Kling Avatar Standard via Kie.ai
   - Image: `a_without_holding_a_ja.png` (formal tuxedo)
   - Prompt: "A well-dressed Black British man in a tuxedo speaks warmly, welcoming expression, subtle nods, professional golden studio lighting"
4. **Compose**: Remotion with BLKOUT branding overlay
5. **Render**: 1080x1920 (9:16 for social) or 1080x608 (16:9 for newsletter)

## Cost Estimate
- TTS: Free (Qwen3-TTS local or Chatterbox)
- Kling Avatar Standard (15s): $0.60
- Total: ~$0.60

## Output
```
/home/robbe/generated-images/aivor/videos/aivor-studio-newsletter-march-2026-03-02.mp4
```
