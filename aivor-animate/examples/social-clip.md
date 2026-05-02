# Example: AIvor Social Media Clip

## Request
"Create a short AIvor clip announcing the board recruitment for Instagram Reels"

## Script
"Brothers, we're building something extraordinary. BLKOUT is recruiting board members — community leaders who'll shape the next decade of liberation technology. If you believe Black queer men deserve better, this is your invitation. Apply now at blkoutuk.com."

## Parameters
- Scenario: abstract (gold particles on black)
- Duration: ~15s (42 words)
- Quality: pro (1080p for social)
- Aspect: 9:16 (Reels/TikTok)
- Emotion: confident

## Pipeline Steps

1. **TTS**: Qwen3-TTS with `--emotion confident`
2. **Upload**: Audio to Supabase storage
3. **Avatar**: Kling Avatar Pro via Kie.ai
   - Image: `a_without_holding_a_ja.png` (formal look)
   - Prompt: "A confident Black British man in a tuxedo delivers an inspiring call to action, strong eye contact, purposeful gestures, dramatic golden lighting"
4. **Background**: Generate animated gold particles via Remotion (no API cost)
5. **Compose**: Avatar overlaid on particle background, BLKOUT branding, CTA card at end
6. **Render**: 1080x1920 @ 30fps

## Cost Estimate
- TTS: Free
- Kling Avatar Pro (15s): $1.20
- Background: Free (Remotion)
- Total: ~$1.20

## Output
```
/home/robbe/generated-images/aivor/videos/aivor-abstract-board-recruitment-2026-03-02.mp4
```
