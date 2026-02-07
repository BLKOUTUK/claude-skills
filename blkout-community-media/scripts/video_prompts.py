#!/usr/bin/env python3
"""
BLKOUT Community Media - Video Prompts Generator

Converts storyboard into LTX-2 video generation prompts.
Maintains X-Men 97 illustration style throughout.

Usage:
    python video_prompts.py storyboard.md --output prompts.json --style xmen97
"""

import argparse
import re
import json
from pathlib import Path
from datetime import datetime

# X-Men 97 style elements
XMEN97_STYLE = {
    'base': """X-Men 97 animation style, 2D hand-drawn aesthetic, bold black outlines, 
cel-shaded lighting with strong dramatic shadows, flat-plane composition, 
vibrant saturated colors, dynamic poses, dramatic camera angles""",
    
    'colors': """deep purple (#4a1942), warm gold (#d4af37), rich browns for skin tones, 
near-black (#1a1a2e) for shadows, off-white (#f5f2eb) for highlights""",
    
    'context': """Black British context, Afrofuturist visual elements, 
community celebration, dignity and power, never stereotyped or diminished""",
    
    'negative': """photorealistic, 3D render, CGI, anime style, chibi, 
cartoon network style, realistic photography, stock image aesthetic"""
}

# Camera movement options for LTX-2
CAMERA_OPTIONS = {
    'Static': 'No LoRA',
    'Zoom In': 'Zoom In',
    'Zoom Out': 'Zoom Out',
    'Slide Left': 'Slide Left',
    'Slide Right': 'Slide Right',
    'Slide Up': 'Slide Up',
    'Slide Down': 'Slide Down',
}

def parse_storyboard(content):
    """Parse storyboard markdown into scenes."""
    scenes = []
    
    # Find scene blocks
    scene_pattern = r'### Scene (\d+) — \[([^\]]+)\](.*?)(?=### Scene|\n## |\Z)'
    matches = re.findall(scene_pattern, content, re.DOTALL)
    
    for num, timestamp, block in matches:
        scene = {
            'number': int(num),
            'timestamp': timestamp,
        }
        
        # Extract category
        cat_match = re.search(r'\*\*Category:\*\* (\w+)', block)
        scene['category'] = cat_match.group(1) if cat_match else 'general'
        
        # Extract triggers
        trig_match = re.search(r'\*\*Triggers:\*\* ([^\n]+)', block)
        scene['triggers'] = trig_match.group(1).split(', ') if trig_match else []
        
        # Extract visual prompt
        prompt_match = re.search(r'```\n(.+?)\n```', block, re.DOTALL)
        scene['base_prompt'] = prompt_match.group(1) if prompt_match else ''
        
        # Extract camera
        cam_match = re.search(r'\*\*Camera:\*\* (\w+)', block)
        scene['camera'] = cam_match.group(1) if cam_match else 'Static'
        
        # Extract audio excerpt for context
        excerpt_match = re.search(r'> (.+?)\.\.\.', block)
        scene['audio_context'] = excerpt_match.group(1) if excerpt_match else ''
        
        scenes.append(scene)
    
    return scenes

def build_ltx2_prompt(scene, style='xmen97'):
    """
    Build complete LTX-2 prompt for a scene.
    
    Combines scene-specific elements with consistent style.
    """
    if style == 'xmen97':
        style_elements = XMEN97_STYLE
    else:
        raise ValueError(f"Unknown style: {style}")
    
    # Start with base prompt from storyboard
    prompt_parts = [scene['base_prompt']]
    
    # Ensure style is present (might be in base, but reinforce)
    if 'X-Men 97' not in scene['base_prompt']:
        prompt_parts.append(style_elements['base'])
    
    # Add color guidance if not present
    if '#4a1942' not in scene['base_prompt']:
        prompt_parts.append(style_elements['colors'])
    
    # Add context
    prompt_parts.append(style_elements['context'])
    
    # Build final prompt
    prompt = '. '.join(filter(None, prompt_parts))
    
    # Clean up
    prompt = re.sub(r'\s+', ' ', prompt).strip()
    prompt = re.sub(r'\.+', '.', prompt)
    
    return prompt

def generate_prompts_json(scenes, style='xmen97'):
    """Generate JSON structure for video generation."""
    prompts = []
    
    for scene in scenes:
        prompt_data = {
            'scene_number': scene['number'],
            'timestamp': scene['timestamp'],
            'prompt': build_ltx2_prompt(scene, style),
            'parameters': {
                'duration': 5,
                'width': 768,
                'height': 512,
                'camera_lora': CAMERA_OPTIONS.get(scene['camera'], 'No LoRA'),
                'enhance_prompt': True,
                'scrapingTool': 'raw-http',  # Faster for generation
            },
            'metadata': {
                'category': scene['category'],
                'triggers': scene['triggers'],
                'audio_context': scene['audio_context'],
                'style': style,
            }
        }
        
        prompts.append(prompt_data)
    
    return {
        'generated': datetime.now().isoformat(),
        'style': style,
        'style_guide': XMEN97_STYLE if style == 'xmen97' else {},
        'negative_prompt': XMEN97_STYLE['negative'],
        'scenes': prompts,
        'count': len(prompts),
    }

def generate_markdown_summary(data, output_path):
    """Generate human-readable summary of prompts."""
    lines = []
    
    lines.append("# Video Generation Prompts")
    lines.append("")
    lines.append(f"**Generated:** {data['generated']}")
    lines.append(f"**Style:** {data['style']}")
    lines.append(f"**Scene count:** {data['count']}")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## Prompts")
    lines.append("")
    
    for scene in data['scenes']:
        lines.append(f"### Scene {scene['scene_number']} — [{scene['timestamp']}]")
        lines.append("")
        lines.append(f"**Camera:** {scene['parameters']['camera_lora']}")
        lines.append("")
        lines.append("**Prompt:**")
        lines.append(f"> {scene['prompt'][:200]}...")
        lines.append("")
        lines.append("---")
        lines.append("")
    
    lines.append("## Negative Prompt (Global)")
    lines.append("")
    lines.append(f"> {data['negative_prompt']}")
    lines.append("")
    
    return '\n'.join(lines)

def main():
    parser = argparse.ArgumentParser(
        description="Generate LTX-2 video prompts from storyboard"
    )
    parser.add_argument("input", help="Input storyboard markdown file")
    parser.add_argument("--output", "-o", help="Output JSON file", default=None)
    parser.add_argument(
        "--style", "-s",
        help="Visual style (default: xmen97)",
        default="xmen97",
        choices=["xmen97"]
    )
    
    args = parser.parse_args()
    
    input_path = Path(args.input)
    if not input_path.exists():
        print(f"Error: Input file not found: {input_path}")
        return 1
    
    output_path = Path(args.output) if args.output else input_path.with_suffix('.json')
    
    # Read storyboard
    content = input_path.read_text()
    
    # Parse scenes
    scenes = parse_storyboard(content)
    
    if not scenes:
        print("Warning: No scenes found in storyboard")
        print("Expected format: ### Scene N — [timestamp]")
        return 1
    
    print(f"Found {len(scenes)} scenes")
    
    # Generate prompts
    data = generate_prompts_json(scenes, args.style)
    
    # Write JSON
    with open(output_path, 'w') as f:
        json.dump(data, f, indent=2)
    print(f"Prompts JSON saved to: {output_path}")
    
    # Write summary markdown
    summary_path = output_path.with_name(output_path.stem + '_summary.md')
    summary = generate_markdown_summary(data, summary_path)
    summary_path.write_text(summary)
    print(f"Summary saved to: {summary_path}")

if __name__ == "__main__":
    main()
