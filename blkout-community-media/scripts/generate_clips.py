#!/usr/bin/env python3
"""
BLKOUT Community Media - Video Clip Generator

Generates video clips from prompts using LTX-2 via Hugging Face.
Requires HF_TOKEN environment variable or interactive login.

Usage:
    python generate_clips.py prompts.json --output clips/
    python generate_clips.py prompts.json --output clips/ --dry-run
"""

import argparse
import json
import os
import time
from pathlib import Path
from datetime import datetime

# LTX-2 Space endpoint
LTX2_SPACE = "alexnasa/ltx-2-TURBO"

def check_gradio_installed():
    """Check if gradio_client is installed, install if not."""
    try:
        from gradio_client import Client
        return True
    except ImportError:
        import subprocess
        import sys
        print("Installing gradio_client...")
        subprocess.check_call([
            sys.executable, "-m", "pip", "install",
            "gradio_client", "--break-system-packages", "-q"
        ])
        return True

def generate_single_clip(prompt_data, output_dir, dry_run=False):
    """
    Generate a single video clip from prompt data.
    
    Args:
        prompt_data: Dict with prompt and parameters
        output_dir: Directory to save clip
        dry_run: If True, don't actually generate
    
    Returns:
        Path to generated clip or None
    """
    from gradio_client import Client
    
    scene_num = prompt_data['scene_number']
    timestamp = prompt_data['timestamp'].replace(':', '-')
    output_filename = f"scene_{scene_num:03d}_{timestamp}.mp4"
    output_path = output_dir / output_filename
    
    if dry_run:
        print(f"  [DRY RUN] Would generate: {output_filename}")
        print(f"    Prompt: {prompt_data['prompt'][:100]}...")
        print(f"    Camera: {prompt_data['parameters']['camera_lora']}")
        return None
    
    print(f"  Generating scene {scene_num}...")
    
    try:
        client = Client(LTX2_SPACE)
        
        result = client.predict(
            prompt=prompt_data['prompt'],
            generation_mode="Text-to-Video",
            duration=prompt_data['parameters']['duration'],
            width=prompt_data['parameters']['width'],
            height=prompt_data['parameters']['height'],
            camera_lora=prompt_data['parameters']['camera_lora'],
            enhance_prompt=prompt_data['parameters']['enhance_prompt'],
            randomize_seed=True,
            api_name="/ltx_2_TURBO_generate_video"
        )
        
        # Result is tuple of (video_path, seed)
        video_path = result[0] if isinstance(result, tuple) else result
        
        # Copy to output directory
        import shutil
        shutil.copy(video_path, output_path)
        
        print(f"    ✓ Saved: {output_filename}")
        return output_path
        
    except Exception as e:
        print(f"    ✗ Error: {e}")
        return None

def generate_all_clips(prompts_data, output_dir, dry_run=False, delay=5):
    """
    Generate all video clips from prompts.
    
    Args:
        prompts_data: Full prompts JSON data
        output_dir: Directory to save clips
        dry_run: If True, don't actually generate
        delay: Seconds between requests (rate limiting)
    
    Returns:
        List of generated clip paths
    """
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    
    scenes = prompts_data['scenes']
    total = len(scenes)
    generated = []
    
    print(f"Generating {total} clips...")
    print(f"Style: {prompts_data['style']}")
    print(f"Output: {output_dir}")
    print("")
    
    for i, scene in enumerate(scenes, 1):
        print(f"[{i}/{total}] Scene {scene['scene_number']}")
        
        result = generate_single_clip(scene, output_dir, dry_run)
        
        if result:
            generated.append(result)
        
        # Rate limiting between requests
        if not dry_run and i < total:
            print(f"    Waiting {delay}s...")
            time.sleep(delay)
    
    print("")
    print(f"Complete: {len(generated)}/{total} clips generated")
    
    return generated

def generate_manifest(prompts_data, generated_clips, output_dir):
    """Generate manifest file linking clips to timestamps."""
    manifest = {
        'generated': datetime.now().isoformat(),
        'source_prompts': prompts_data.get('generated'),
        'style': prompts_data['style'],
        'clips': []
    }
    
    for clip_path in generated_clips:
        # Extract scene number from filename
        filename = Path(clip_path).name
        scene_match = filename.split('_')[1]  # scene_001_...
        scene_num = int(scene_match)
        
        # Find corresponding prompt data
        scene_data = next(
            (s for s in prompts_data['scenes'] if s['scene_number'] == scene_num),
            None
        )
        
        if scene_data:
            manifest['clips'].append({
                'filename': filename,
                'scene_number': scene_num,
                'timestamp': scene_data['timestamp'],
                'category': scene_data['metadata']['category'],
                'duration': scene_data['parameters']['duration'],
            })
    
    manifest_path = output_dir / 'manifest.json'
    with open(manifest_path, 'w') as f:
        json.dump(manifest, f, indent=2)
    
    return manifest_path

def main():
    parser = argparse.ArgumentParser(
        description="Generate video clips from prompts using LTX-2"
    )
    parser.add_argument("input", help="Input prompts JSON file")
    parser.add_argument("--output", "-o", help="Output directory", default="clips")
    parser.add_argument(
        "--dry-run", "-n",
        action="store_true",
        help="Show what would be generated without doing it"
    )
    parser.add_argument(
        "--delay", "-d",
        type=int,
        default=5,
        help="Seconds between requests (default: 5)"
    )
    parser.add_argument(
        "--scenes", "-s",
        type=str,
        help="Specific scenes to generate (e.g., '1,3,5' or '1-5')"
    )
    
    args = parser.parse_args()
    
    input_path = Path(args.input)
    if not input_path.exists():
        print(f"Error: Input file not found: {input_path}")
        return 1
    
    # Check/install dependencies
    check_gradio_installed()
    
    # Read prompts
    with open(input_path) as f:
        prompts_data = json.load(f)
    
    # Filter scenes if specified
    if args.scenes:
        # Parse scene specification
        requested = set()
        for part in args.scenes.split(','):
            if '-' in part:
                start, end = map(int, part.split('-'))
                requested.update(range(start, end + 1))
            else:
                requested.add(int(part))
        
        prompts_data['scenes'] = [
            s for s in prompts_data['scenes']
            if s['scene_number'] in requested
        ]
        
        print(f"Filtered to {len(prompts_data['scenes'])} scenes")
    
    output_dir = Path(args.output)
    
    # Generate clips
    generated = generate_all_clips(
        prompts_data,
        output_dir,
        dry_run=args.dry_run,
        delay=args.delay
    )
    
    # Generate manifest
    if generated and not args.dry_run:
        manifest_path = generate_manifest(prompts_data, generated, output_dir)
        print(f"Manifest saved to: {manifest_path}")

if __name__ == "__main__":
    main()
