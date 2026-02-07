#!/usr/bin/env python3
"""
BLKOUT Community Media - Storyboard Generator

Analyzes transcript and generates video storyboard with:
- Scene descriptions
- B-roll suggestions  
- Title card moments
- Visual prompts for video generation

Usage:
    python storyboard.py transcript.md --output storyboard.md
"""

import argparse
import re
import json
from pathlib import Path
from datetime import datetime

# Visual moment triggers
VISUAL_TRIGGERS = {
    'emotion': [
        r'\b(laugh|cry|smile|angry|happy|sad|excited|nervous|proud|ashamed)\b',
        r'\b(love|hate|fear|hope|joy|grief|rage|peace)\b',
    ],
    'action': [
        r'\b(walk|run|dance|fight|build|create|destroy|grow)\b',
        r'\b(journey|travel|move|arrive|leave|return)\b',
    ],
    'place': [
        r'\b(home|street|church|club|bar|school|work|hospital)\b',
        r'\b(London|Croydon|Brixton|Peckham|Tilbury)\b',
        r'\b(city|village|country|abroad|overseas)\b',
    ],
    'time': [
        r'\b(morning|night|dawn|dusk|midnight|noon)\b',
        r'\b(childhood|youth|older|younger|growing up)\b',
        r'\b(1960s|1970s|1980s|1990s|2000s|Windrush)\b',
    ],
    'relationship': [
        r'\b(mother|father|brother|sister|friend|lover|partner)\b',
        r'\b(community|family|ancestors|elders|youth)\b',
    ],
}

# Title card triggers
TITLE_TRIGGERS = [
    r'(?:the )?(?:first|second|third|final) (?:thing|point|question)',
    r'(?:topic|question) (?:one|two|three|four)',
    r'(?:let\'s|now|so) (?:talk about|discuss|move to)',
    r'(?:on|regarding|about) the (?:topic|subject|question) of',
]

def parse_transcript(content):
    """Parse transcript markdown into segments."""
    segments = []
    
    pattern = r'\*\*\[(\d{1,2}:\d{2}(?::\d{2})?)\]\*\*\s*(.+?)(?=\*\*\[|\n\n---|\Z)'
    matches = re.findall(pattern, content, re.DOTALL)
    
    for timestamp, text in matches:
        segments.append({
            'timestamp': timestamp,
            'text': text.strip()
        })
    
    return segments

def analyze_visual_moments(segments):
    """Identify moments that could benefit from visuals."""
    moments = []
    
    for seg in segments:
        text_lower = seg['text'].lower()
        
        for category, patterns in VISUAL_TRIGGERS.items():
            for pattern in patterns:
                matches = re.findall(pattern, text_lower)
                if matches:
                    moments.append({
                        'timestamp': seg['timestamp'],
                        'category': category,
                        'triggers': list(set(matches)),
                        'excerpt': seg['text'][:150],
                        'full_text': seg['text']
                    })
                    break  # One match per category per segment
    
    return moments

def identify_title_cards(segments):
    """Identify moments that need title cards."""
    cards = []
    
    for seg in segments:
        for pattern in TITLE_TRIGGERS:
            if re.search(pattern, seg['text'].lower()):
                cards.append({
                    'timestamp': seg['timestamp'],
                    'context': seg['text'][:100]
                })
                break
    
    return cards

def generate_scene_prompt(moment, style='xmen97'):
    """
    Generate a visual prompt for the moment.
    
    Uses X-Men 97 animation style by default.
    """
    base_style = """X-Men 97 animation style, bold black outlines, 
cel-shaded lighting, dramatic angles, deep purple (#4a1942) and warm gold (#d4af37) 
color palette, rich warm browns for skin tones, strong shadows, 
clearly stylized illustration"""

    category = moment['category']
    triggers = moment['triggers']
    
    # Build scene description based on category
    scene_elements = {
        'emotion': f"Close-up portrait showing {triggers[0]} emotion, expressive face",
        'action': f"Dynamic pose showing {triggers[0]}, motion lines, energy",
        'place': f"Establishing shot of {triggers[0]}, atmospheric lighting",
        'time': f"{triggers[0]} atmosphere, period-appropriate details",
        'relationship': f"Two figures representing {triggers[0]} connection, warm composition",
    }
    
    scene = scene_elements.get(category, "Abstract representation")
    
    prompt = f"{scene}. {base_style}. Black British context, Afrofuturist elements."
    
    return prompt

def suggest_camera(moment):
    """Suggest camera movement for the moment."""
    category = moment['category']
    
    cameras = {
        'emotion': 'Static',  # Let emotion carry it
        'action': 'Zoom In',  # Build energy
        'place': 'Slide Right',  # Reveal space
        'time': 'Zoom Out',  # Show passage
        'relationship': 'Static',  # Focus on connection
    }
    
    return cameras.get(category, 'Static')

def generate_storyboard(segments, moments, title_cards, input_path):
    """Generate markdown storyboard document."""
    lines = []
    
    # Header
    lines.append("# Video Storyboard")
    lines.append("")
    lines.append(f"**Source:** {input_path}")
    lines.append(f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    lines.append(f"**Style:** X-Men 97 Animation")
    lines.append("")
    lines.append("---")
    lines.append("")
    
    # Summary
    lines.append("## Overview")
    lines.append("")
    lines.append(f"- **Total segments:** {len(segments)}")
    lines.append(f"- **Visual moments:** {len(moments)}")
    lines.append(f"- **Title cards:** {len(title_cards)}")
    lines.append("")
    
    # Style guide
    lines.append("## Style Guide")
    lines.append("")
    lines.append("All generated visuals use **X-Men 97 animation style**:")
    lines.append("")
    lines.append("- Bold black outlines")
    lines.append("- Cel-shaded lighting with strong shadows")
    lines.append("- Deep purple (#4a1942) and warm gold (#d4af37) palette")
    lines.append("- Rich warm browns for skin tones")
    lines.append("- Dynamic poses, dramatic angles")
    lines.append("- Clearly stylized — never photorealistic")
    lines.append("")
    lines.append("**Why illustration:** Transparency about AI-generated content.")
    lines.append("Real community photography (with consent) for real people.")
    lines.append("")
    lines.append("---")
    lines.append("")
    
    # Title cards section
    if title_cards:
        lines.append("## Title Cards")
        lines.append("")
        for i, card in enumerate(title_cards, 1):
            lines.append(f"### Card {i} — [{card['timestamp']}]")
            lines.append("")
            lines.append(f"**Context:** {card['context']}...")
            lines.append("")
            lines.append("**Suggested text:** [TO BE FILLED]")
            lines.append("")
            lines.append("**Design notes:**")
            lines.append("- Deep purple background (#4a1942)")
            lines.append("- Gold text (#d4af37)")
            lines.append("- Fraunces or similar display font")
            lines.append("")
        lines.append("---")
        lines.append("")
    
    # Scene-by-scene
    lines.append("## Scenes")
    lines.append("")
    
    for i, moment in enumerate(moments, 1):
        lines.append(f"### Scene {i} — [{moment['timestamp']}]")
        lines.append("")
        lines.append(f"**Category:** {moment['category'].title()}")
        lines.append(f"**Triggers:** {', '.join(moment['triggers'])}")
        lines.append("")
        lines.append("**Audio excerpt:**")
        lines.append(f"> {moment['excerpt']}...")
        lines.append("")
        lines.append("**Visual prompt:**")
        lines.append(f"```")
        lines.append(generate_scene_prompt(moment))
        lines.append(f"```")
        lines.append("")
        lines.append(f"**Camera:** {suggest_camera(moment)}")
        lines.append("**Duration:** 5 seconds")
        lines.append("")
        lines.append("**Notes:** [Add production notes here]")
        lines.append("")
        lines.append("---")
        lines.append("")
    
    # B-roll suggestions
    lines.append("## B-Roll Suggestions")
    lines.append("")
    lines.append("Generic shots that can cover transitions or extend scenes:")
    lines.append("")
    lines.append("- **London skyline** — establishing, golden hour")
    lines.append("- **Community gathering** — stylized crowd, warm tones")
    lines.append("- **Abstract patterns** — Afrofuturist geometric, purple/gold")
    lines.append("- **Hands in connection** — reaching, holding, building")
    lines.append("- **Text overlay background** — subtle animation for quotes")
    lines.append("")
    
    # Assembly notes
    lines.append("---")
    lines.append("")
    lines.append("## Assembly Notes")
    lines.append("")
    lines.append("**For Remotion/Flexclip:**")
    lines.append("")
    lines.append("1. Import audio track")
    lines.append("2. Place title cards at marked timestamps")
    lines.append("3. Layer generated clips over audio")
    lines.append("4. Add transitions (prefer cuts or simple fades)")
    lines.append("5. Add lower thirds for speaker identification (if consented)")
    lines.append("6. Add end card with BLKOUT branding")
    lines.append("")
    lines.append("**Music from BLKOUT licensed library only.**")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("*Storyboard is a starting point. Human creative judgment shapes the final edit.*")
    
    return '\n'.join(lines)

def main():
    parser = argparse.ArgumentParser(
        description="Generate video storyboard from transcript"
    )
    parser.add_argument("input", help="Input transcript markdown file")
    parser.add_argument("--output", "-o", help="Output storyboard file", default=None)
    
    args = parser.parse_args()
    
    input_path = Path(args.input)
    if not input_path.exists():
        print(f"Error: Input file not found: {input_path}")
        return 1
    
    output_path = Path(args.output) if args.output else input_path.with_name(
        input_path.stem + '_storyboard.md'
    )
    
    # Read transcript
    content = input_path.read_text()
    
    # Parse
    segments = parse_transcript(content)
    
    if not segments:
        print("Warning: No timestamped segments found")
        return 1
    
    print(f"Analyzing {len(segments)} segments...")
    
    # Analyze
    moments = analyze_visual_moments(segments)
    title_cards = identify_title_cards(segments)
    
    print(f"Found {len(moments)} visual moments")
    print(f"Found {len(title_cards)} title card opportunities")
    
    # Generate storyboard
    storyboard = generate_storyboard(segments, moments, title_cards, input_path)
    
    # Write
    output_path.write_text(storyboard)
    print(f"Storyboard saved to: {output_path}")

if __name__ == "__main__":
    main()
