# BLKOUT Logo Ident Implementation Guide

**Practical Technical Guide for Video, Web, and Social Media Deployment**

---

## Overview

This guide provides step-by-step technical instructions for implementing BLKOUT logo idents across all platforms. Whether you're a video editor, web developer, or social media manager, this document will help you deploy the idents correctly and efficiently.

**Prerequisites**: Familiarity with video editing software (Premiere, Final Cut, DaVinci Resolve), basic web development (HTML/CSS/JavaScript), or social media content management.

---

## Table of Contents

1. [Video Production Implementation](#video-production-implementation)
2. [Web Implementation](#web-implementation)
3. [Social Media Implementation](#social-media-implementation)
4. [Platform-Specific Workflows](#platform-specific-workflows)
5. [Troubleshooting](#troubleshooting)
6. [Asset Management](#asset-management)

---

## Video Production Implementation

### Adobe Premiere Pro

#### Adding Ident to Timeline

**Method 1: Import and Overlay (With Transparency)**

1. **Import WebM or ProRes 4444 ident file**
   ```
   File > Import > [select blkout-ident-standard-1080p-webm-alpha.webm]
   ```

2. **Create new sequence** (if starting fresh)
   - Right-click ident file > New Sequence from Clip
   - Or match existing sequence settings (1920x1080, 30fps)

3. **Place ident on Video Track 2** (above main content)
   - Drag ident file to timeline
   - Position at start (intro) or end (outro)
   - Ident transparency will allow background to show through

4. **Adjust duration if needed**
   - Standard ident: 4-5 seconds (use full duration)
   - Micro ident: 2-3 seconds (use full duration)
   - Full ident: 6-8 seconds (use full duration)

5. **Add audio** (if ident has separate audio file)
   - Import `blkout-ident-standard-audio-full.wav`
   - Drag to Audio Track 1, sync with video
   - Adjust levels: -12dB to -18dB average

**Method 2: Nested Sequence (For Reusability)**

1. Import ident, create sequence from clip
2. Rename sequence: "BLKOUT Ident - Standard"
3. In main project sequence, drag nested sequence to timeline
4. Benefit: Update ident once, changes apply everywhere

#### Exporting with Ident

**For YouTube/Web** (H.264):
```
File > Export > Media
Format: H.264
Preset: YouTube 1080p HD
Video Codec: H.264
Frame Rate: 30fps
Bitrate: VBR, 2 pass, Target 8-10 Mbps
Audio: AAC, 320 kbps, 48kHz
```

**For Archival** (ProRes):
```
Format: QuickTime
Video Codec: Apple ProRes 422 HQ
Frame Rate: Match source (30fps)
Audio: Linear PCM, 24-bit, 48kHz
```

---

### DaVinci Resolve

#### Adding Ident to Timeline

1. **Import ident into Media Pool**
   ```
   File > Import > File > [select ident file]
   ```

2. **Drag to timeline**
   - Place on Video Track 2 for transparency overlay
   - Or Video Track 1 if using on black background

3. **Enable alpha channel** (if not auto-detected)
   - Right-click clip in Media Pool > Clip Attributes
   - Check "Decode using: Clip" or "Decode using: Timeline"
   - Ensure Alpha mode is set to "Straight" or "Premultiplied"

4. **Color grading** (optional, use sparingly)
   - Switch to Color page
   - Adjust only if ident colors need slight correction
   - DO NOT change brand colors significantly

5. **Audio sync**
   - Import audio file separately if needed
   - Use waveform to manually sync, or
   - Use "Auto-Align Audio" if both tracks have sync reference

#### Rendering with Ident

**For YouTube** (H.264):
```
Deliver page > Format: QuickTime or MP4
Codec: H.264
Resolution: 1920x1080
Frame rate: 30fps
Quality: "Restrict to" 8000-10000 kb/s
Audio: AAC, 320 kbps
```

**For Social Media** (H.264, smaller file):
```
Format: MP4
Codec: H.264
Resolution: 1920x1080
Frame rate: 30fps
Quality: "Restrict to" 5000 kb/s
Audio: AAC, 192 kbps
```

---

### Final Cut Pro X

#### Adding Ident to Timeline

1. **Import ident**
   ```
   File > Import > Media > [select ident file]
   ```

2. **Add to timeline**
   - Drag ident to Connected Storyline above primary
   - Or place at start/end of Primary Storyline
   - Transparency automatically handled for MOV/ProRes 4444

3. **Adjust position**
   - Use Position tool (P) to reposition if needed
   - Scale to fit (usually 100% for 1080p ident in 1080p timeline)

4. **Add audio**
   - Import audio file
   - Connect to ident video clip (Q key)
   - Adjust levels in Audio Inspector

#### Exporting with Ident

**For YouTube**:
```
File > Share > Apple Devices 1080p
Or File > Share > Export File:
  Format: Video and Audio
  Video codec: H.264 Better Quality
  Resolution: 1920x1080
  Quality: High
```

**For Master File**:
```
File > Share > Master File (ProRes)
Video codec: Apple ProRes 422
Resolution: 1920x1080
Audio: Linear PCM
```

---

## Web Implementation

### HTML5 Video Element

#### Basic Implementation (Autoplay on Load)

```html
<!DOCTYPE html>
<html lang="en-GB">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>BLKOUT</title>
  <style>
    body {
      margin: 0;
      padding: 0;
      background-color: #264653; /* Deep Forest */
      display: flex;
      justify-content: center;
      align-items: center;
      min-height: 100vh;
    }

    .ident-container {
      position: relative;
      width: 100%;
      max-width: 1920px;
    }

    .blkout-ident {
      width: 100%;
      height: auto;
      display: block;
    }
  </style>
</head>
<body>
  <div class="ident-container">
    <video
      class="blkout-ident"
      autoplay
      muted
      playsinline
      id="blkoutIdent"
    >
      <source src="/assets/blkout-ident-standard-1080p-webm-alpha.webm" type="video/webm">
      <source src="/assets/blkout-ident-standard-1080p-h264-noalpha.mp4" type="video/mp4">
      Your browser does not support the video tag.
    </video>
  </div>

  <script>
    // Redirect to main content after ident plays
    const ident = document.getElementById('blkoutIdent');
    ident.addEventListener('ended', () => {
      window.location.href = '/main.html'; // Or reveal content
    });
  </script>
</body>
</html>
```

#### Hero Section with Looping Ident

```html
<section class="hero">
  <div class="hero-background">
    <video
      class="blkout-ident-loop"
      autoplay
      loop
      muted
      playsinline
    >
      <source src="/assets/blkout-ident-micro-1080p-webm-alpha.webm" type="video/webm">
      <source src="/assets/blkout-ident-micro-1080p-h264-noalpha.mp4" type="video/mp4">
    </video>
  </div>

  <div class="hero-content">
    <h1>BLKOUT</h1>
    <p>Community-Owned Liberation Platform</p>
    <a href="#join" class="cta-button">Join Us</a>
  </div>
</section>

<style>
  .hero {
    position: relative;
    height: 100vh;
    overflow: hidden;
  }

  .hero-background {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    z-index: 1;
  }

  .blkout-ident-loop {
    width: 100%;
    height: 100%;
    object-fit: cover;
    opacity: 0.3; /* Subtle background presence */
  }

  .hero-content {
    position: relative;
    z-index: 2;
    color: white;
    text-align: center;
    padding: 2rem;
  }

  .hero-content h1 {
    font-family: 'Poppins', sans-serif;
    font-weight: 700;
    font-size: 4rem;
    color: #D4261A; /* BLKOUT Red */
    margin: 0;
  }

  .hero-content p {
    font-family: 'Inter', sans-serif;
    font-size: 1.5rem;
    color: #F4A261; /* Warm Gold */
  }

  .cta-button {
    display: inline-block;
    padding: 1rem 2rem;
    background-color: #D4261A;
    color: white;
    text-decoration: none;
    border-radius: 4px;
    font-weight: 600;
    transition: background-color 0.3s ease;
  }

  .cta-button:hover {
    background-color: #E76F51; /* Warm Orange on hover */
  }
</style>
```

### React/Next.js Implementation

#### Component: `BlkoutIdent.tsx`

```tsx
import { useEffect, useRef, useState } from 'react';

interface BlkoutIdentProps {
  variation?: 'micro' | 'standard' | 'full';
  autoplay?: boolean;
  loop?: boolean;
  muted?: boolean;
  onEnded?: () => void;
  className?: string;
}

export default function BlkoutIdent({
  variation = 'standard',
  autoplay = true,
  loop = false,
  muted = true,
  onEnded,
  className = ''
}: BlkoutIdentProps) {
  const videoRef = useRef<HTMLVideoElement>(null);
  const [hasError, setHasError] = useState(false);

  useEffect(() => {
    const video = videoRef.current;
    if (video && onEnded) {
      video.addEventListener('ended', onEnded);
      return () => video.removeEventListener('ended', onEnded);
    }
  }, [onEnded]);

  const webmSrc = `/assets/blkout-ident-${variation}-1080p-webm-alpha.webm`;
  const mp4Src = `/assets/blkout-ident-${variation}-1080p-h264-noalpha.mp4`;

  if (hasError) {
    return (
      <div className="blkout-ident-fallback">
        <img
          src="/assets/blkout-logo-red.svg"
          alt="BLKOUT"
          className={className}
        />
      </div>
    );
  }

  return (
    <video
      ref={videoRef}
      className={`blkout-ident ${className}`}
      autoPlay={autoplay}
      loop={loop}
      muted={muted}
      playsInline
      onError={() => setHasError(true)}
    >
      <source src={webmSrc} type="video/webm" />
      <source src={mp4Src} type="video/mp4" />
      Your browser does not support video playback.
    </video>
  );
}
```

#### Usage Example:

```tsx
import BlkoutIdent from '@/components/BlkoutIdent';

export default function HomePage() {
  const handleIdentEnd = () => {
    console.log('Ident finished playing');
    // Proceed to main content
  };

  return (
    <div className="home-page">
      <section className="intro">
        <BlkoutIdent
          variation="standard"
          onEnded={handleIdentEnd}
          className="w-full max-w-4xl mx-auto"
        />
      </section>

      <section className="content">
        <h1>Welcome to BLKOUT</h1>
        {/* Rest of content */}
      </section>
    </div>
  );
}
```

### CSS Animation Fallback (Static Logo)

For browsers that don't support video or when ident files fail to load:

```css
.blkout-ident-fallback {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100%;
  height: 400px;
  background: linear-gradient(to bottom, #264653, #2A9D8F);
}

.blkout-ident-fallback img {
  max-width: 400px;
  width: 80%;
  animation: fadeInPulse 2s ease-in-out;
}

@keyframes fadeInPulse {
  0% {
    opacity: 0;
    transform: scale(0.9);
  }
  50% {
    opacity: 1;
    transform: scale(1.05);
  }
  100% {
    opacity: 1;
    transform: scale(1);
  }
}
```

---

## Social Media Implementation

### YouTube

#### Adding as Video Intro

**Method 1: Upload Intro Separately (YouTube Studio)**

1. Go to YouTube Studio > Content
2. Click on video > Editor (left sidebar)
3. Click "Add an intro" at beginning of timeline
4. Upload `blkout-ident-standard-1080p-h264-noalpha.mp4`
5. YouTube will append ident to start of video
6. Save changes

**Method 2: Bake Into Video (Recommended)**

1. Add ident to beginning of video in editing software (see above)
2. Export final video with ident included
3. Upload to YouTube as usual
4. Benefits: Better control, consistent quality, works offline

#### YouTube Video Settings

```
Title: [Your Content Title]
Description:
  [Video description]

  BLKOUT: Community-owned liberation platform for and by Black queer men in the UK
  https://platform-blkout.vercel.app

Tags: BLKOUT, Black queer men, liberation technology, [other relevant tags]

Thumbnail: Custom thumbnail featuring BLKOUT branding
```

---

### Instagram (Feed Posts, Reels, Stories)

#### Feed Posts (Square 1:1)

**Preparation**:
1. Export ident in 1080x1080 square format
2. Use micro ident (2-3s) to respect short attention spans
3. File format: MP4 (H.264), max 60 seconds total

**Encoding Settings**:
```
Resolution: 1080x1080
Frame rate: 30fps
Video codec: H.264
Bitrate: 5000 kb/s
Audio codec: AAC, 192 kbps
Max file size: 100MB (but aim for <10MB)
```

**Upload**:
1. Open Instagram app
2. Tap "+" to create post
3. Select your video (with ident baked in)
4. Add caption, location, tags
5. Share

**Caption Template**:
```
[Content description]

BLKOUT: For and by Black queer men in the UK 🏳️‍🌈
Community-owned • Liberation technology

#BLKOUT #BlackQueerMen #Liberation #CommunityOwned #UKQueer
```

#### Instagram Reels & Stories (Vertical 9:16)

**Preparation**:
1. Export ident in 1080x1920 vertical format
2. Use micro ident (2-3s)
3. Ensure audio is included (Reels favor audio)

**Encoding Settings**:
```
Resolution: 1080x1920
Frame rate: 30fps
Video codec: H.264
Bitrate: 5000 kb/s
Audio: AAC, 192 kbps (Reels work best with music/audio)
```

**Upload (Reels)**:
1. Instagram > Reels > Create
2. Upload video (with ident at start or end)
3. Add text, stickers, effects if desired
4. Add audio/music (or use ident's audio)
5. Write caption, add cover image
6. Share

**Upload (Stories)**:
1. Instagram > Your Story
2. Upload video
3. Add text, stickers (optional)
4. Share to Your Story or Close Friends

---

### TikTok

#### Preparation

**Ident for TikTok**:
- Use micro ident (2-3s)
- Vertical format: 1080x1920
- Keep total video under 60s (or 3min if allowed)
- Audio is CRITICAL for TikTok algorithm

**Encoding Settings**:
```
Resolution: 1080x1920 (vertical)
Frame rate: 30fps
Video codec: H.264
Bitrate: 5000 kb/s
Audio: AAC, 192 kbps (important!)
File format: MP4
Max size: 287.6 MB (but smaller is better for upload speed)
```

#### Upload Workflow

1. Open TikTok app
2. Tap "+" to create
3. Upload video (with ident baked in at start/end)
4. Edit:
   - Trim if needed
   - Add text overlay
   - Add effects/filters (sparingly to maintain brand)
   - **Audio**: Keep ident audio or add trending sound
5. Write caption with keywords:
   ```
   [Content hook/description]

   BLKOUT: For and by Black queer men in the UK 🏳️‍⚧️

   #BLKOUT #BlackQueerMen #QueerUK #Liberation #CommunityOwned #BlackLGBT
   ```
6. Add cover image (frame from video or custom)
7. Set privacy, comments, etc.
8. Post

**TikTok-Specific Tips**:
- First 3 seconds are critical (ident should be quick)
- Consider micro ident (2s) then jump into content
- TikTok algorithm favors native audio; ident sound can help
- Use trending sounds/music alongside ident for reach
- Test different placements (intro vs. outro)

---

### Twitter/X

#### Preparation

**Ident for Twitter/X**:
- Use micro or standard ident
- Square (1080x1080) or landscape (1920x1080)
- Max 2 minutes 20 seconds (140 seconds)
- Max 512MB file size (but aim for <10MB)

**Encoding Settings**:
```
Resolution: 1920x1080 or 1080x1080
Frame rate: 30fps
Video codec: H.264
Bitrate: 5000-8000 kb/s
Audio: AAC, 192 kbps
File format: MP4
```

#### Upload Workflow

1. Compose tweet
2. Click media icon, upload video (with ident)
3. Twitter will process and generate preview
4. Write tweet:
   ```
   [Content description or hook]

   BLKOUT: Community-owned liberation platform for and by Black queer men in the UK

   #BLKOUT #BlackQueerMen #Liberation
   ```
5. Add alt text to video (accessibility):
   ```
   BLKOUT logo animation with tagline "For and by Black queer men in the UK", followed by [content description]
   ```
6. Tweet

**Twitter/X Best Practices**:
- Keep videos short (under 60s for best engagement)
- First frame matters (thumbnail)
- Captions/subtitles recommended (many watch muted)
- Thread longer content rather than single long video

---

### Facebook

#### Preparation

**Ident for Facebook**:
- Standard or micro ident
- Square (1080x1080) or landscape (1920x1080)
- Max 240 minutes, but shorter is better
- Max 10GB, but aim for <100MB

**Encoding Settings**:
```
Resolution: 1920x1080 (landscape) or 1080x1080 (square)
Frame rate: 30fps
Video codec: H.264
Bitrate: 8000 kb/s
Audio: AAC, 192 kbps
File format: MP4 or MOV
```

#### Upload Workflow

1. Create post on Facebook Page
2. Click "Photo/Video"
3. Upload video (with ident baked in)
4. Facebook will process
5. Add title, description:
   ```
   [Content title]

   [Content description]

   BLKOUT is a community-owned liberation platform for and by Black queer men in the UK. Learn more: https://platform-blkout.vercel.app
   ```
6. Add captions (use Facebook's auto-caption tool, then edit for accuracy)
7. Choose thumbnail
8. Select audience, tags
9. Publish

---

## Platform-Specific Workflows

### LinkedIn (Professional Context)

**When to Use**:
- Organizational updates
- Partnership announcements
- Professional content about BLKOUT's mission

**Ident Choice**:
- Standard ident (4-5s)
- Professional tone but maintain brand boldness

**Encoding**:
```
Resolution: 1920x1080 (landscape)
Frame rate: 30fps
Max file size: 5GB (but aim for <50MB)
Format: MP4 (H.264)
Audio: AAC, 192 kbps
```

**Upload**:
1. Create post on LinkedIn
2. Click video icon
3. Upload video with ident
4. Add professional caption with mission statement
5. Tag relevant organizations/people
6. Publish

---

### Vimeo (High-Quality Archive)

**When to Use**:
- Long-form content
- Archival/portfolio pieces
- Embedded videos on website

**Ident Choice**:
- Standard or full ident (depending on content length)

**Encoding** (High Quality):
```
Resolution: 3840x2160 (4K) or 1920x1080
Frame rate: 24fps or 30fps
Video codec: H.264 or H.265 (HEVC)
Bitrate: 15-25 Mbps (4K), 8-12 Mbps (1080p)
Audio: AAC, 320 kbps
Format: MP4 or MOV
```

**Upload**:
1. Go to Vimeo, click "New video"
2. Upload video
3. While processing, add:
   - Title
   - Description (with BLKOUT mission)
   - Tags
   - Privacy settings
   - Allow downloads (if sharing source files)
4. Once processed, set thumbnail
5. Publish

**Embedding on Website**:
```html
<div style="padding:56.25% 0 0 0;position:relative;">
  <iframe
    src="https://player.vimeo.com/video/[VIDEO_ID]?h=[PRIVACY_HASH]&amp;badge=0&amp;autopause=0&amp;player_id=0&amp;app_id=58479"
    frameborder="0"
    allow="autoplay; fullscreen; picture-in-picture"
    style="position:absolute;top:0;left:0;width:100%;height:100%;"
    title="BLKOUT: [Video Title]"
  ></iframe>
</div>
<script src="https://player.vimeo.com/api/player.js"></script>
```

---

## Troubleshooting

### Video Issues

**Problem**: Ident transparency not showing (black background instead)

**Solution**:
- Ensure using WebM with alpha or ProRes 4444 format
- Check video track is above background in editing timeline
- Verify alpha channel is enabled in software settings
- If platform doesn't support alpha, use H.264 version on colored background

---

**Problem**: Ident audio too loud or too quiet

**Solution**:
- Adjust audio levels to -12dB to -18dB average
- Use audio meters in editing software
- Peak should not exceed -3dB
- Normalize audio if needed (Effect > Audio > Normalize in Premiere)

---

**Problem**: Video stutters or low quality on web

**Solution**:
- Re-encode at correct bitrate (8-10 Mbps for 1080p)
- Ensure frame rate matches source (30fps standard)
- Compress file size (target <10MB for web)
- Use WebM format for better compression with quality
- Test on multiple browsers and devices

---

**Problem**: Wrong aspect ratio on social media

**Solution**:
- Re-export ident in platform-specific dimensions:
  - Instagram Feed: 1080x1080 (square)
  - Instagram Stories/TikTok: 1080x1920 (vertical 9:16)
  - YouTube/Web: 1920x1080 (landscape 16:9)
- Use "Scale to fit" or "Crop to fit" in export settings
- Check preview before uploading

---

### Web Issues

**Problem**: Ident video not autoplaying on iOS/mobile

**Solution**:
- Add `muted` attribute (required for autoplay on iOS)
- Add `playsinline` attribute (prevents fullscreen on iOS)
- Use JavaScript to play on user interaction if needed:

```javascript
const video = document.getElementById('blkoutIdent');
document.addEventListener('click', () => {
  video.play();
}, { once: true });
```

---

**Problem**: Video won't load / shows error

**Solution**:
- Check file path is correct (case-sensitive on Linux servers)
- Verify MIME types are configured on server:
  ```
  .webm -> video/webm
  .mp4 -> video/mp4
  .mov -> video/quicktime
  ```
- Add CORS headers if loading from CDN
- Provide fallback `<source>` with different formats
- Add static image fallback if all else fails

---

**Problem**: Video file size too large (slow page load)

**Solution**:
- Compress video further (reduce bitrate to 5000 kb/s)
- Use WebM format (better compression than MP4)
- Lazy load video (only load when user scrolls to it):

```javascript
const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      const video = entry.target;
      video.src = video.dataset.src;
      video.load();
      observer.unobserve(video);
    }
  });
});

observer.observe(document.querySelector('.blkout-ident'));
```

```html
<video class="blkout-ident" data-src="/path/to/ident.webm" muted playsinline>
  Your browser does not support video.
</video>
```

---

### Social Media Issues

**Problem**: Instagram/TikTok compresses video too much (quality loss)

**Solution**:
- Export at highest quality (bitrate 10 Mbps)
- Use 1080p resolution (not lower)
- Avoid re-uploading same video (each upload compresses again)
- Keep file size under platform limits but not too small
- Use H.264 High Profile for better compression with quality

---

**Problem**: Social media crops or zooms ident incorrectly

**Solution**:
- Export in exact aspect ratio for platform (9:16 for Stories, 1:1 for Feed)
- Add safe zones (keep logo/text in center 80% of frame)
- Test upload before posting publicly (use drafts or private accounts)
- Some platforms allow repositioning - use "Adjust" or "Edit" before posting

---

**Problem**: Ident audio muted on autoplay (web/social)

**Solution**:
- Expected behavior (browsers/platforms mute autoplay)
- Use `muted` attribute for autoplay on web
- Provide unmute button for user control:

```html
<button id="unmuteBtn">🔇 Unmute</button>

<script>
  const video = document.getElementById('blkoutIdent');
  const btn = document.getElementById('unmuteBtn');

  btn.addEventListener('click', () => {
    video.muted = !video.muted;
    btn.textContent = video.muted ? '🔇 Unmute' : '🔊 Mute';
  });
</script>
```

---

## Asset Management

### Folder Structure (Recommended)

```
/BLKOUT-Idents/
├── /Source/
│   ├── blkout-ident-micro.aep (After Effects project)
│   ├── blkout-ident-standard.aep
│   ├── blkout-ident-full.aep
│   ├── /Illustrations/
│   │   ├── blkout-fist-solidarity.ai (Illustrator source)
│   │   └── blkout-fist-solidarity.svg
│   └── /Audio/
│       ├── ident-audio-full-master.wav
│       ├── ident-audio-minimal-master.wav
│       └── /Stems/ (individual audio layers)
│
├── /Exports/
│   ├── /Micro/
│   │   ├── blkout-ident-micro-1080p-webm-alpha.webm
│   │   ├── blkout-ident-micro-1080p-prores4444.mov
│   │   ├── blkout-ident-micro-1080p-h264-noalpha.mp4
│   │   ├── blkout-ident-micro-square-1080-h264.mp4 (Instagram)
│   │   ├── blkout-ident-micro-vertical-1080x1920-h264.mp4 (Stories/TikTok)
│   │   └── /Audio/
│   │       ├── blkout-ident-micro-audio-full.wav
│   │       └── blkout-ident-micro-audio-minimal.wav
│   │
│   ├── /Standard/
│   │   ├── blkout-ident-standard-1080p-webm-alpha.webm
│   │   ├── blkout-ident-standard-1080p-prores4444.mov
│   │   ├── blkout-ident-standard-4k-prores4444.mov
│   │   ├── blkout-ident-standard-1080p-h264-noalpha.mp4
│   │   └── /Audio/
│   │       ├── blkout-ident-standard-audio-full.wav
│   │       └── blkout-ident-standard-audio-minimal.wav
│   │
│   └── /Full/
│       ├── blkout-ident-full-1080p-webm-alpha.webm
│       ├── blkout-ident-full-1080p-prores4444.mov
│       ├── blkout-ident-full-4k-prores4444.mov
│       ├── blkout-ident-full-1080p-h264-noalpha.mp4
│       └── /Audio/
│           ├── blkout-ident-full-audio-full.wav
│           └── blkout-ident-full-audio-minimal.wav
│
├── /Documentation/
│   ├── LOGO-IDENT.md (main specification)
│   ├── IDENT-IMPLEMENTATION.md (this guide)
│   └── CHANGELOG.md
│
└── README.md (quick reference guide)
```

### Naming Convention

**Format**: `blkout-ident-[variation]-[resolution]-[format]-[alpha].ext`

**Examples**:
- `blkout-ident-standard-1080p-webm-alpha.webm`
- `blkout-ident-micro-4k-prores4444.mov`
- `blkout-ident-full-1080p-h264-noalpha.mp4`
- `blkout-ident-standard-square-1080-h264.mp4` (social)
- `blkout-ident-micro-vertical-1080x1920-h264.mp4` (social)

**Audio**:
- `blkout-ident-[variation]-audio-[type].wav`
- Example: `blkout-ident-standard-audio-full.wav`

### Cloud Storage & Sharing

**For Team Access**:
- Upload to Google Drive, Dropbox, or similar
- Share link with team members
- Organize by folder structure above
- Set permissions: View-only for most, Edit for editors

**For Archival**:
- Keep master/source files in separate archive
- Use Vimeo (private) or similar for video backups
- Version control for source files (Git LFS or similar)

**For Distribution**:
- CDN for web assets (Cloudflare, AWS S3 + CloudFront)
- Direct download links for editors/partners
- Include documentation with every distribution

### Version Control

**File Naming for Versions**:
- `blkout-ident-standard-v1.0-1080p-webm-alpha.webm`
- `blkout-ident-standard-v1.1-1080p-webm-alpha.webm`

**Track Changes**:
- Maintain CHANGELOG.md with updates
- Note what changed between versions
- Keep old versions in `/Archive/` folder

---

## Quick Reference Card

### Export Cheat Sheet

| Platform | Resolution | Frame Rate | Codec | Audio | File Size |
|----------|-----------|------------|--------|-------|-----------|
| **YouTube** | 1920x1080 | 30fps | H.264 | AAC 320kbps | <10MB |
| **Instagram Feed** | 1080x1080 | 30fps | H.264 | AAC 192kbps | <10MB |
| **Instagram Story** | 1080x1920 | 30fps | H.264 | AAC 192kbps | <10MB |
| **TikTok** | 1080x1920 | 30fps | H.264 | AAC 192kbps | <50MB |
| **Twitter/X** | 1920x1080 | 30fps | H.264 | AAC 192kbps | <10MB |
| **Website (WebM)** | 1920x1080 | 30fps | VP9 + alpha | Vorbis | <5MB |
| **Broadcast** | 3840x2160 | 24/30fps | ProRes 4444 | Linear PCM | <100MB |

### Ident Usage Cheat Sheet

| Content Type | Ident | Placement | Duration |
|--------------|-------|-----------|----------|
| Social post | Micro | Intro | 2-3s |
| YouTube video | Standard | Intro/Outro | 4-5s |
| Campaign video | Full | Intro | 6-8s |
| Website hero | Micro/Standard | Loop | 2-5s |
| Fundraising | Full | Intro | 6-8s |
| Webinar | Standard | Intro | 4-5s |

---

## Best Practices Summary

1. **Always use transparency** (WebM/ProRes 4444) when possible for versatility
2. **Optimize file sizes** - smaller is better for web/social without sacrificing quality
3. **Test before publishing** - preview on target platform to catch issues
4. **Maintain brand consistency** - don't alter colors, timing, or core design
5. **Provide fallbacks** - static logo image if video fails to load
6. **Respect platforms** - use correct aspect ratios and specs for each
7. **Audio matters** - include audio where appropriate, mute for autoplay
8. **Accessibility first** - add alt text, captions, and ensure contrast
9. **Archive source files** - keep editable originals for future updates
10. **Document everything** - track versions, changes, and deployment details

---

## Contact & Support

**Technical Questions**: Refer to main LOGO-IDENT.md documentation
**Implementation Help**: Bring to community governance or tech team
**Bug Reports**: Report issues with specific platform/browser details
**Feature Requests**: Propose through community governance process

---

**Remember**: The ident is a powerful branding tool, but content is king. Don't let a 5-second ident overshadow your message. Use idents to frame and elevate your content, not replace it.

---

*Last Updated: October 2025*
*Version: 1.0*
*Maintained By: BLKOUT Community*
