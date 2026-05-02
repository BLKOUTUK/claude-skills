#!/usr/bin/env node
/**
 * AIvor Speech Generation Script
 * Generates AIvor's voice reading a script using Chatterbox TTS or Kie.ai ElevenLabs.
 * For Qwen3-TTS, use the Python script (generate-speech-qwen.py) instead.
 *
 * Usage:
 *   node generate-speech.mjs --text "Script text" --backend chatterbox|elevenlabs [options]
 *
 * Options:
 *   --text        The script for AIvor to read (required)
 *   --backend     chatterbox | elevenlabs (default: chatterbox)
 *   --output      Output directory (default: /home/robbe/generated-images/aivor/videos)
 *   --name        Output filename without extension
 */

import { writeFileSync, mkdirSync, existsSync } from 'fs';
import { join } from 'path';
import { parseArgs } from 'util';

const { values: args } = parseArgs({
  options: {
    text: { type: 'string' },
    backend: { type: 'string', default: 'chatterbox' },
    output: { type: 'string', default: '/home/robbe/generated-images/aivor/videos' },
    name: { type: 'string' },
  },
});

if (!args.text) {
  console.error('Error: --text is required');
  process.exit(1);
}

const CHATTERBOX_URL = process.env.CHATTERBOX_URL || 'https://chatterbox.blkoutuk.cloud';
const KIE_API_KEY = process.env.KIE_AI_API_KEY;
const GIELGUD_PATH = '/home/robbe/blkout-platform/apps/ivor-core/public/gielgud30.mp3';

async function generateViaChatterbox(text) {
  console.log('Generating AIvor speech via Chatterbox TTS...');
  console.log(`Text (${text.length} chars): ${text.substring(0, 80)}...`);

  // Use the upload endpoint for voice cloning
  const formData = new FormData();
  formData.append('input', text);

  // Read the voice file
  const { readFileSync } = await import('fs');
  const voiceBuffer = readFileSync(GIELGUD_PATH);
  const voiceBlob = new Blob([voiceBuffer], { type: 'audio/mpeg' });
  formData.append('voice_file', voiceBlob, 'gielgud30.mp3');

  const response = await fetch(`${CHATTERBOX_URL}/v1/audio/speech/upload`, {
    method: 'POST',
    body: formData,
  });

  if (!response.ok) {
    const errorText = await response.text();
    throw new Error(`Chatterbox error (${response.status}): ${errorText}`);
  }

  return Buffer.from(await response.arrayBuffer());
}

async function generateViaElevenLabs(text) {
  if (!KIE_API_KEY) {
    console.error('Error: KIE_AI_API_KEY required for ElevenLabs backend');
    process.exit(1);
  }

  console.log('Generating AIvor speech via ElevenLabs (Kie.ai)...');

  const response = await fetch('https://api.kie.ai/api/v1/jobs/createTask', {
    method: 'POST',
    headers: {
      'Authorization': `Bearer ${KIE_API_KEY}`,
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      model: 'elevenlabs-tts',
      input: {
        text,
        voice: 'british_male_warm',
      },
    }),
  });

  const result = await response.json();
  if (result.code !== 200) {
    throw new Error(`ElevenLabs/Kie error: ${result.msg}`);
  }

  console.log(`Task created: ${result.data.taskId}`);
  console.log('Polling for result...');

  // Poll for completion
  const startTime = Date.now();
  while (Date.now() - startTime < 120000) {
    await new Promise(r => setTimeout(r, 5000));

    const statusRes = await fetch(
      `https://api.kie.ai/api/v1/jobs/getTaskDetails?taskId=${result.data.taskId}`,
      { headers: { 'Authorization': `Bearer ${KIE_API_KEY}` } }
    );
    const status = await statusRes.json();

    if (status.data?.status === 'completed' || status.data?.status === 'success') {
      const audioUrl = status.data.output?.audio_url || status.data.output?.url;
      if (audioUrl) {
        const audioRes = await fetch(audioUrl);
        return Buffer.from(await audioRes.arrayBuffer());
      }
    }

    if (status.data?.status === 'failed') {
      throw new Error(`Generation failed: ${status.data.error}`);
    }

    console.log(`Status: ${status.data?.status}...`);
  }

  throw new Error('Timed out waiting for TTS generation');
}

// Main
const outputDir = args.output;
if (!existsSync(outputDir)) mkdirSync(outputDir, { recursive: true });

const date = new Date().toISOString().split('T')[0];
const filename = args.name || `aivor-speech-${date}-${Date.now().toString(36)}`;
const outputPath = join(outputDir, `${filename}.wav`);

try {
  let audioBuffer;

  if (args.backend === 'chatterbox') {
    audioBuffer = await generateViaChatterbox(args.text);
  } else if (args.backend === 'elevenlabs') {
    audioBuffer = await generateViaElevenLabs(args.text);
  } else {
    console.error(`Unknown backend: ${args.backend}`);
    process.exit(1);
  }

  writeFileSync(outputPath, audioBuffer);
  console.log(`\nSaved: ${outputPath}`);
  console.log(`Size: ${(audioBuffer.length / 1024).toFixed(1)} KB`);

  // Estimate duration (~150 words/min for AIvor's measured pace)
  const wordCount = args.text.split(/\s+/).length;
  const estimatedSeconds = Math.ceil(wordCount / 2.5); // ~2.5 words/sec
  console.log(`Words: ${wordCount}`);
  console.log(`Estimated duration: ~${estimatedSeconds}s`);

  if (estimatedSeconds > 15) {
    const segments = Math.ceil(estimatedSeconds / 15);
    console.log(`\nNote: ${estimatedSeconds}s exceeds Kling's 15s limit.`);
    console.log(`Split into ${segments} segments for avatar generation.`);
  }
} catch (error) {
  console.error(`\nSpeech generation failed: ${error.message}`);
  process.exit(1);
}
