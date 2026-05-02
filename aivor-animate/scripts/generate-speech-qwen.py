#!/usr/bin/env python3
"""
AIvor Speech Generation via Qwen3-TTS (Voice Cloning)

Generates AIvor's voice reading a script using Qwen3-TTS with the Gielgud
reference audio for voice cloning. Requires GPU with CUDA.

Usage:
    python generate-speech-qwen.py --text "Script text" [options]

Options:
    --text        The script for AIvor to read (required)
    --output      Output directory (default: /home/robbe/generated-images/aivor/videos)
    --name        Output filename without extension
    --emotion     Emotion tag: happy, serious, warm, confident (default: warm)
    --ref-audio   Path to reference audio (default: gielgud30.mp3)
    --model       Model variant: base, custom (default: base)
"""

import argparse
import os
import sys

def main():
    parser = argparse.ArgumentParser(description='AIvor Speech Generation via Qwen3-TTS')
    parser.add_argument('--text', required=True, help='Script text for AIvor to read')
    parser.add_argument('--output', default='/home/robbe/generated-images/aivor/videos',
                        help='Output directory')
    parser.add_argument('--name', default=None, help='Output filename without extension')
    parser.add_argument('--emotion', default='warm',
                        choices=['happy', 'serious', 'warm', 'confident'],
                        help='Emotion for speech delivery')
    parser.add_argument('--ref-audio',
                        default='/home/robbe/blkout-platform/apps/ivor-core/public/gielgud30.mp3',
                        help='Path to voice reference audio')
    parser.add_argument('--model', default='base', choices=['base', 'custom'],
                        help='Qwen3-TTS model variant')
    args = parser.parse_args()

    # Check GPU availability
    try:
        import torch
        if not torch.cuda.is_available():
            print("Warning: No CUDA GPU detected. Qwen3-TTS requires GPU.")
            print("Falling back to CPU (will be slow) or use --backend chatterbox with the Node.js script.")
            device = "cpu"
        else:
            device = "cuda:0"
            print(f"Using GPU: {torch.cuda.get_device_name(0)}")
    except ImportError:
        print("Error: PyTorch not installed. Install with: pip install torch")
        sys.exit(1)

    # Check qwen_tts
    try:
        from qwen_tts import Qwen3TTSModel
    except ImportError:
        print("Error: qwen-tts not installed.")
        print("Install with: pip install -U qwen-tts")
        print("Or: conda create -n qwen3-tts python=3.12 -y && conda activate qwen3-tts && pip install -U qwen-tts")
        sys.exit(1)

    import soundfile as sf
    from datetime import date

    # Check reference audio exists
    if not os.path.exists(args.ref_audio):
        print(f"Error: Reference audio not found at {args.ref_audio}")
        print("The Gielgud reference audio must be present for voice cloning.")
        sys.exit(1)

    # Prepare text with emotion tags if supported
    text = args.text
    emotion_map = {
        'happy': 'joyful and celebratory',
        'serious': 'grave and measured',
        'warm': 'warm and encouraging',
        'confident': 'bold and assured',
    }

    # Reference text describes the voice style
    ref_text = (
        "A warm, measured British voice speaking with quiet authority "
        "and occasional warmth. The tone is articulate, confident, and "
        f"{emotion_map.get(args.emotion, 'warm and encouraging')}."
    )

    print(f"Loading Qwen3-TTS model ({args.model})...")
    model_name = {
        'base': 'Qwen/Qwen3-TTS-12Hz-1.7B-Base',
        'custom': 'Qwen/Qwen3-TTS-12Hz-1.7B-CustomVoice',
    }[args.model]

    model = Qwen3TTSModel.from_pretrained(
        model_name,
        device_map=device,
        dtype=torch.bfloat16 if device != "cpu" else torch.float32,
    )

    print(f"Generating speech ({len(text)} chars, emotion: {args.emotion})...")
    print(f"Text: {text[:100]}{'...' if len(text) > 100 else ''}")

    wavs, sr = model.generate_voice_clone(
        text=text,
        language="English",
        ref_audio=args.ref_audio,
        ref_text=ref_text,
    )

    # Save output
    os.makedirs(args.output, exist_ok=True)
    today = date.today().isoformat()
    filename = args.name or f"aivor-speech-qwen-{today}"
    output_path = os.path.join(args.output, f"{filename}.wav")

    sf.write(output_path, wavs[0], sr)

    # Calculate duration
    duration = len(wavs[0]) / sr
    word_count = len(text.split())

    print(f"\nSaved: {output_path}")
    print(f"Duration: {duration:.1f}s")
    print(f"Sample rate: {sr}Hz")
    print(f"Words: {word_count}")
    print(f"Words/sec: {word_count / duration:.1f}")

    if duration > 15:
        segments = int(duration // 15) + 1
        print(f"\nNote: {duration:.0f}s exceeds Kling's 15s limit.")
        print(f"Split into {segments} segments for avatar generation.")
        print("Segment boundaries (seconds):")
        for i in range(segments):
            start = i * 15
            end = min((i + 1) * 15, duration)
            print(f"  Segment {i+1}: {start:.0f}s - {end:.1f}s")


if __name__ == '__main__':
    main()
