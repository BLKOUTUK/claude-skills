#!/usr/bin/env python3
"""
BLKOUT Community Media: Export Package Generator

Generates a production package for final assembly in Remotion or Flexclip.
Collects all generated clips, audio, transcripts, and metadata into a structured
export folder ready for editing.

Usage:
    python package_export.py PROJECT_DIR --output EXPORT_DIR [options]

Arguments:
    PROJECT_DIR     Directory containing project files (clips, transcript, etc.)
    --output DIR    Output directory for the export package
    --format        Target editor: 'remotion' or 'flexclip' (default: remotion)
    --include-raw   Include raw/unedited clips alongside finals
    --music DIR     Path to music library directory to include
"""

import argparse
import json
import os
import shutil
from datetime import datetime
from pathlib import Path


def create_export_structure(export_dir: Path, format_type: str) -> dict:
    """Create the export folder structure."""
    
    # Common structure
    folders = {
        'audio': export_dir / 'audio',
        'video': export_dir / 'video',
        'stills': export_dir / 'stills',
        'transcripts': export_dir / 'transcripts',
        'metadata': export_dir / 'metadata',
        'music': export_dir / 'music',
    }
    
    # Add editor-specific folders
    if format_type == 'remotion':
        folders['remotion'] = export_dir / 'remotion'
        folders['compositions'] = export_dir / 'remotion' / 'compositions'
    elif format_type == 'flexclip':
        folders['flexclip'] = export_dir / 'flexclip'
    
    for folder in folders.values():
        folder.mkdir(parents=True, exist_ok=True)
    
    return folders


def collect_clips(project_dir: Path, folders: dict, include_raw: bool) -> list:
    """Collect video clips from project directory."""
    
    clips_collected = []
    clips_dir = project_dir / 'clips'
    
    if not clips_dir.exists():
        print(f"  No clips directory found at {clips_dir}")
        return clips_collected
    
    for clip_file in clips_dir.glob('*.mp4'):
        # Skip raw clips unless requested
        if '_raw' in clip_file.name and not include_raw:
            continue
        
        dest = folders['video'] / clip_file.name
        shutil.copy2(clip_file, dest)
        clips_collected.append({
            'filename': clip_file.name,
            'path': str(dest.relative_to(folders['video'].parent.parent)),
            'size_bytes': clip_file.stat().st_size
        })
        print(f"  Copied clip: {clip_file.name}")
    
    return clips_collected


def collect_audio(project_dir: Path, folders: dict) -> list:
    """Collect audio files from project directory."""
    
    audio_collected = []
    
    # Look for common audio extensions
    audio_extensions = ['.mp3', '.wav', '.m4a', '.aac', '.ogg']
    
    for ext in audio_extensions:
        for audio_file in project_dir.glob(f'*{ext}'):
            dest = folders['audio'] / audio_file.name
            shutil.copy2(audio_file, dest)
            audio_collected.append({
                'filename': audio_file.name,
                'path': str(dest.relative_to(folders['audio'].parent.parent)),
                'size_bytes': audio_file.stat().st_size
            })
            print(f"  Copied audio: {audio_file.name}")
    
    return audio_collected


def collect_transcripts(project_dir: Path, folders: dict) -> list:
    """Collect transcripts and edit documents."""
    
    transcripts_collected = []
    
    # Look for markdown files that might be transcripts
    for md_file in project_dir.glob('*.md'):
        dest = folders['transcripts'] / md_file.name
        shutil.copy2(md_file, dest)
        transcripts_collected.append({
            'filename': md_file.name,
            'path': str(dest.relative_to(folders['transcripts'].parent.parent))
        })
        print(f"  Copied transcript: {md_file.name}")
    
    return transcripts_collected


def collect_storyboard(project_dir: Path, folders: dict) -> dict:
    """Collect storyboard and prompts files."""
    
    storyboard_data = {}
    
    # Storyboard markdown
    storyboard_file = project_dir / 'storyboard.md'
    if storyboard_file.exists():
        dest = folders['metadata'] / 'storyboard.md'
        shutil.copy2(storyboard_file, dest)
        storyboard_data['storyboard'] = str(dest.relative_to(folders['metadata'].parent.parent))
        print(f"  Copied storyboard")
    
    # Prompts JSON
    prompts_file = project_dir / 'prompts.json'
    if prompts_file.exists():
        dest = folders['metadata'] / 'prompts.json'
        shutil.copy2(prompts_file, dest)
        storyboard_data['prompts'] = str(dest.relative_to(folders['metadata'].parent.parent))
        print(f"  Copied prompts")
    
    # Manifest JSON (links clips to timestamps)
    manifest_file = project_dir / 'clips' / 'manifest.json'
    if manifest_file.exists():
        dest = folders['metadata'] / 'clip_manifest.json'
        shutil.copy2(manifest_file, dest)
        storyboard_data['manifest'] = str(dest.relative_to(folders['metadata'].parent.parent))
        print(f"  Copied clip manifest")
    
    return storyboard_data


def copy_music_library(music_dir: Path, folders: dict) -> list:
    """Copy music library tracks."""
    
    music_collected = []
    
    if not music_dir or not music_dir.exists():
        return music_collected
    
    audio_extensions = ['.mp3', '.wav', '.m4a', '.aac', '.ogg', '.flac']
    
    for ext in audio_extensions:
        for music_file in music_dir.glob(f'*{ext}'):
            dest = folders['music'] / music_file.name
            shutil.copy2(music_file, dest)
            music_collected.append({
                'filename': music_file.name,
                'path': str(dest.relative_to(folders['music'].parent.parent))
            })
            print(f"  Copied music: {music_file.name}")
    
    return music_collected


def generate_remotion_config(export_dir: Path, manifest: dict):
    """Generate Remotion-specific configuration files."""
    
    remotion_dir = export_dir / 'remotion'
    
    # Generate a basic composition config
    composition_config = {
        "fps": 30,
        "width": 1920,
        "height": 1080,
        "durationInFrames": 0,  # To be calculated
        "clips": [],
        "audio": manifest.get('audio', [])
    }
    
    # Calculate duration from clips if manifest available
    if manifest.get('storyboard', {}).get('manifest'):
        manifest_path = export_dir / manifest['storyboard']['manifest']
        if manifest_path.exists():
            with open(manifest_path, 'r') as f:
                clip_manifest = json.load(f)
                composition_config['clips'] = clip_manifest.get('clips', [])
    
    config_path = remotion_dir / 'composition.json'
    with open(config_path, 'w') as f:
        json.dump(composition_config, f, indent=2)
    
    print(f"  Generated Remotion config: composition.json")
    
    # Generate README for Remotion
    readme = """# Remotion Export Package

## Contents

- `/audio` - Main audio track(s) for the episode
- `/video` - Generated video clips from LTX-2
- `/music` - Licensed BLKOUT music tracks
- `/transcripts` - Transcripts and edit notes
- `/metadata` - Storyboard, prompts, and clip manifest

## Import Order

1. Create new Remotion project
2. Import main audio from `/audio`
3. Import clips from `/video`
4. Reference `composition.json` for clip placement
5. Add music from `/music` library
6. Add title cards and credits

## Clip Naming Convention

Clips are named: `scene_XX_[description].mp4`

The `clip_manifest.json` in `/metadata` maps clips to timecodes.

## Music Usage

All tracks in `/music` are licensed for BLKOUT productions.
See music library documentation for mood/tempo guidance.
"""
    
    readme_path = remotion_dir / 'README.md'
    with open(readme_path, 'w') as f:
        f.write(readme)


def generate_flexclip_config(export_dir: Path, manifest: dict):
    """Generate Flexclip-specific guidance."""
    
    flexclip_dir = export_dir / 'flexclip'
    
    # Flexclip doesn't have a config format, so we generate guidance
    readme = """# Flexclip Import Guide

## Contents

- `/audio` - Main audio track(s) for the episode
- `/video` - Generated video clips from LTX-2
- `/music` - Licensed BLKOUT music tracks
- `/transcripts` - Transcripts and edit notes
- `/metadata` - Storyboard and clip timing information

## Import Steps

1. Create new Flexclip project
2. Set dimensions: 1920x1080 (or 1080x1920 for vertical)
3. Import main audio from `/audio` to timeline
4. Import video clips from `/video`
5. Reference `storyboard.md` for clip placement guidance
6. Add music from `/music` library
7. Use Flexclip's text tools for title cards

## Clip Placement

Clips are named: `scene_XX_[description].mp4`

Check `/metadata/clip_manifest.json` for timecode suggestions.
These align with the original transcript timestamps.

## Export Settings

Recommended export:
- 1080p (1920x1080)
- 30fps
- MP4/H.264
- High quality

For social clips, consider:
- 1080x1080 (Instagram feed)
- 1080x1920 (Stories/Reels/TikTok)
"""
    
    readme_path = flexclip_dir / 'README.md'
    with open(readme_path, 'w') as f:
        f.write(readme)
    
    print(f"  Generated Flexclip guide: README.md")


def generate_master_manifest(export_dir: Path, manifest: dict):
    """Generate the master manifest for the export package."""
    
    manifest['exported_at'] = datetime.now().isoformat()
    manifest['export_version'] = '1.0'
    
    manifest_path = export_dir / 'manifest.json'
    with open(manifest_path, 'w') as f:
        json.dump(manifest, f, indent=2)
    
    print(f"  Generated master manifest")


def generate_assembly_guide(export_dir: Path, manifest: dict):
    """Generate a human-readable assembly guide."""
    
    guide = f"""# Assembly Guide

**Exported**: {datetime.now().strftime('%Y-%m-%d %H:%M')}
**Target Editor**: {manifest.get('format', 'remotion')}

## Package Contents

### Audio ({len(manifest.get('audio', []))} files)
"""
    
    for audio in manifest.get('audio', []):
        guide += f"- {audio['filename']}\n"
    
    guide += f"""
### Video Clips ({len(manifest.get('clips', []))} clips)
"""
    
    for clip in manifest.get('clips', []):
        guide += f"- {clip['filename']}\n"
    
    guide += f"""
### Music Library ({len(manifest.get('music', []))} tracks)
"""
    
    for track in manifest.get('music', []):
        guide += f"- {track['filename']}\n"
    
    guide += """
## Assembly Checklist

### Pre-Assembly
- [ ] Review transcript in `/transcripts`
- [ ] Review storyboard in `/metadata`
- [ ] Check clip manifest for timing reference

### Audio Assembly
- [ ] Import main audio track
- [ ] Set project duration to match audio
- [ ] Add any music beds from `/music`

### Video Assembly
- [ ] Import clips from `/video`
- [ ] Place clips according to storyboard timing
- [ ] Adjust clip durations as needed
- [ ] Add transitions between clips

### Graphics
- [ ] Add opening title card
- [ ] Add participant name lower thirds
- [ ] Add closing credits
- [ ] Add BLKOUT branding

### Final Checks
- [ ] Audio levels consistent
- [ ] All clips properly synced
- [ ] Credits complete and accurate
- [ ] Export test at 30s mark

### Export
- [ ] Export full resolution master
- [ ] Export social media cuts if needed
- [ ] Archive project file

## Notes

[Add any episode-specific notes here]
"""
    
    guide_path = export_dir / 'ASSEMBLY_GUIDE.md'
    with open(guide_path, 'w') as f:
        f.write(guide)
    
    print(f"  Generated assembly guide")


def main():
    parser = argparse.ArgumentParser(
        description='Generate export package for Remotion or Flexclip'
    )
    parser.add_argument('project_dir', help='Project directory with clips, audio, transcript')
    parser.add_argument('--output', '-o', required=True, help='Export output directory')
    parser.add_argument('--format', '-f', choices=['remotion', 'flexclip'], 
                        default='remotion', help='Target editor format')
    parser.add_argument('--include-raw', action='store_true', 
                        help='Include raw/unedited clips')
    parser.add_argument('--music', help='Path to music library directory')
    
    args = parser.parse_args()
    
    project_dir = Path(args.project_dir)
    export_dir = Path(args.output)
    music_dir = Path(args.music) if args.music else None
    
    if not project_dir.exists():
        print(f"Error: Project directory not found: {project_dir}")
        return 1
    
    print(f"\n=== BLKOUT Export Package Generator ===\n")
    print(f"Project: {project_dir}")
    print(f"Export to: {export_dir}")
    print(f"Format: {args.format}")
    print()
    
    # Create export structure
    print("Creating export structure...")
    folders = create_export_structure(export_dir, args.format)
    
    # Initialize manifest
    manifest = {
        'project': str(project_dir),
        'format': args.format,
        'clips': [],
        'audio': [],
        'transcripts': [],
        'music': [],
        'storyboard': {}
    }
    
    # Collect files
    print("\nCollecting video clips...")
    manifest['clips'] = collect_clips(project_dir, folders, args.include_raw)
    
    print("\nCollecting audio...")
    manifest['audio'] = collect_audio(project_dir, folders)
    
    print("\nCollecting transcripts...")
    manifest['transcripts'] = collect_transcripts(project_dir, folders)
    
    print("\nCollecting storyboard data...")
    manifest['storyboard'] = collect_storyboard(project_dir, folders)
    
    if music_dir:
        print("\nCopying music library...")
        manifest['music'] = copy_music_library(music_dir, folders)
    
    # Generate editor-specific configs
    print("\nGenerating editor configuration...")
    if args.format == 'remotion':
        generate_remotion_config(export_dir, manifest)
    else:
        generate_flexclip_config(export_dir, manifest)
    
    # Generate manifest and guide
    print("\nGenerating documentation...")
    generate_master_manifest(export_dir, manifest)
    generate_assembly_guide(export_dir, manifest)
    
    # Summary
    print(f"\n=== Export Complete ===\n")
    print(f"Clips: {len(manifest['clips'])}")
    print(f"Audio: {len(manifest['audio'])}")
    print(f"Transcripts: {len(manifest['transcripts'])}")
    print(f"Music tracks: {len(manifest['music'])}")
    print(f"\nPackage location: {export_dir}")
    print(f"See ASSEMBLY_GUIDE.md for next steps\n")
    
    return 0


if __name__ == '__main__':
    exit(main())
