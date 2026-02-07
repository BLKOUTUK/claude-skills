#!/usr/bin/env python3
"""
BLKOUT Community Media - Transcription Script

Transcribes audio files using OpenAI Whisper.
Outputs markdown with timestamps and speaker identification.

Usage:
    python transcribe.py input.mp3 --output transcript.md
    python transcribe.py input.wav --output transcript.md --model medium
"""

import argparse
import subprocess
import sys
import json
from pathlib import Path
from datetime import timedelta

def check_whisper_installed():
    """Check if whisper is installed, install if not."""
    try:
        import whisper
        return True
    except ImportError:
        print("Installing openai-whisper...")
        subprocess.check_call([
            sys.executable, "-m", "pip", "install", 
            "openai-whisper", "--break-system-packages", "-q"
        ])
        return True

def format_timestamp(seconds):
    """Convert seconds to HH:MM:SS format."""
    td = timedelta(seconds=seconds)
    total_seconds = int(td.total_seconds())
    hours, remainder = divmod(total_seconds, 3600)
    minutes, secs = divmod(remainder, 60)
    if hours > 0:
        return f"{hours:02d}:{minutes:02d}:{secs:02d}"
    return f"{minutes:02d}:{secs:02d}"

def transcribe_audio(input_path, model_name="base", language="en"):
    """
    Transcribe audio file using Whisper.
    
    Args:
        input_path: Path to audio file
        model_name: Whisper model (tiny, base, small, medium, large)
        language: Language code
    
    Returns:
        dict with segments and full text
    """
    import whisper
    
    print(f"Loading Whisper model: {model_name}")
    model = whisper.load_model(model_name)
    
    print(f"Transcribing: {input_path}")
    result = model.transcribe(
        str(input_path),
        language=language,
        verbose=False
    )
    
    return result

def generate_markdown(result, input_path):
    """
    Generate markdown transcript from Whisper result.
    
    Args:
        result: Whisper transcription result
        input_path: Original audio file path
    
    Returns:
        Markdown string
    """
    lines = []
    
    # Header
    lines.append(f"# Transcript: {Path(input_path).stem}")
    lines.append("")
    lines.append(f"**Source:** {Path(input_path).name}")
    lines.append(f"**Duration:** {format_timestamp(result['segments'][-1]['end'] if result['segments'] else 0)}")
    lines.append(f"**Generated:** {__import__('datetime').datetime.now().strftime('%Y-%m-%d %H:%M')}")
    lines.append("")
    lines.append("---")
    lines.append("")
    
    # Segments with timestamps
    lines.append("## Transcript")
    lines.append("")
    
    current_paragraph = []
    paragraph_start = None
    
    for segment in result['segments']:
        start = segment['start']
        text = segment['text'].strip()
        
        if not text:
            continue
        
        # Start new paragraph every ~30 seconds or at natural breaks
        if paragraph_start is None:
            paragraph_start = start
        
        current_paragraph.append(text)
        
        # Check for paragraph break
        is_sentence_end = text.endswith(('.', '!', '?'))
        time_since_start = start - paragraph_start
        
        if is_sentence_end and (time_since_start > 30 or len(current_paragraph) > 5):
            # Output paragraph with timestamp
            timestamp = format_timestamp(paragraph_start)
            paragraph_text = ' '.join(current_paragraph)
            lines.append(f"**[{timestamp}]** {paragraph_text}")
            lines.append("")
            current_paragraph = []
            paragraph_start = None
    
    # Remaining text
    if current_paragraph:
        timestamp = format_timestamp(paragraph_start or 0)
        paragraph_text = ' '.join(current_paragraph)
        lines.append(f"**[{timestamp}]** {paragraph_text}")
        lines.append("")
    
    # Footer
    lines.append("---")
    lines.append("")
    lines.append("*Transcription by Whisper. Review for accuracy before use.*")
    lines.append("")
    lines.append("## Edit Notes")
    lines.append("")
    lines.append("*Use this section to flag moments for review:*")
    lines.append("")
    lines.append("- [ ] Consent review: [timestamp] - [description]")
    lines.append("- [ ] Technical issue: [timestamp] - [description]")
    lines.append("- [ ] Highlight: [timestamp] - [description]")
    
    return '\n'.join(lines)

def main():
    parser = argparse.ArgumentParser(
        description="Transcribe audio for BLKOUT community media"
    )
    parser.add_argument("input", help="Input audio file (MP3, WAV, etc.)")
    parser.add_argument("--output", "-o", help="Output markdown file", default=None)
    parser.add_argument(
        "--model", "-m", 
        help="Whisper model (tiny, base, small, medium, large)", 
        default="base"
    )
    parser.add_argument(
        "--language", "-l",
        help="Language code",
        default="en"
    )
    
    args = parser.parse_args()
    
    input_path = Path(args.input)
    if not input_path.exists():
        print(f"Error: Input file not found: {input_path}")
        sys.exit(1)
    
    output_path = Path(args.output) if args.output else input_path.with_suffix('.md')
    
    # Check/install whisper
    check_whisper_installed()
    
    # Transcribe
    result = transcribe_audio(input_path, args.model, args.language)
    
    # Generate markdown
    markdown = generate_markdown(result, input_path)
    
    # Write output
    output_path.write_text(markdown)
    print(f"Transcript saved to: {output_path}")
    
    # Also save raw JSON for further processing
    json_path = output_path.with_suffix('.json')
    with open(json_path, 'w') as f:
        json.dump({
            'text': result['text'],
            'segments': [
                {
                    'start': s['start'],
                    'end': s['end'],
                    'text': s['text']
                }
                for s in result['segments']
            ]
        }, f, indent=2)
    print(f"Raw transcript JSON saved to: {json_path}")

if __name__ == "__main__":
    main()
