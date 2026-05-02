#!/usr/bin/env node
/**
 * DEPRECATED — targets Kling Avatar via Kie.ai. The current AIvor pipeline
 * uses SadTalker via Replicate instead. See:
 *   apps/comms-blkout/remotion-videos/scripts/lipsync.mjs (canonical)
 *   ~/.claude/skills/aivor-animate/SKILL.md (current docs)
 *
 * Kept for reference in case Kling becomes preferable again. Unmaintained.
 *
 * AIvor Avatar Animation Script
 * Takes a portrait image and audio file, generates a lip-synced talking head
 * video via Kling Avatar API on Kie.ai.
 *
 * Usage:
 *   node animate-avatar.mjs --image <url> --audio <url> [options]
 *
 * Options:
 *   --image       Publicly accessible URL to AIvor portrait image (required)
 *   --audio       Publicly accessible URL to speech audio (required)
 *   --quality     standard | pro (default: standard)
 *   --prompt      Emotion/action description for the avatar
 *   --output      Output directory (default: /home/robbe/generated-images/aivor/videos)
 *   --name        Output filename without extension
 *   --poll-interval  Seconds between status checks (default: 10)
 *   --max-wait    Max seconds to wait (default: 300)
 */

import { writeFileSync, mkdirSync, existsSync } from 'fs';
import { join } from 'path';
import { parseArgs } from 'util';

const { values: args } = parseArgs({
  options: {
    image: { type: 'string' },
    audio: { type: 'string' },
    quality: { type: 'string', default: 'standard' },
    prompt: { type: 'string', default: 'A well-dressed Black British man in a tuxedo speaks warmly and confidently, with subtle head movements and natural expressions. Professional studio lighting with warm golden tones.' },
    output: { type: 'string', default: '/home/robbe/generated-images/aivor/videos' },
    name: { type: 'string' },
    'poll-interval': { type: 'string', default: '10' },
    'max-wait': { type: 'string', default: '300' },
  },
});

if (!args.image || !args.audio) {
  console.error('Error: --image and --audio are required (must be publicly accessible URLs)');
  console.error('');
  console.error('Tip: Upload local files to Supabase storage first:');
  console.error('  node scripts/supabase-query.mjs upload <file> avatars/');
  process.exit(1);
}

const KIE_API_KEY = process.env.KIE_AI_API_KEY;
if (!KIE_API_KEY) {
  console.error('Error: KIE_AI_API_KEY environment variable not set');
  console.error('Get your key at: https://kie.ai/api-key');
  process.exit(1);
}

const MODEL = args.quality === 'pro'
  ? 'kling/ai-avatar-pro'
  : 'kling/ai-avatar-standard';

const COSTS = {
  standard: { perSecond: 0.04, resolution: '720p' },
  pro: { perSecond: 0.08, resolution: '1080p' },
};

async function createAvatarTask() {
  console.log(`Creating Kling Avatar task (${args.quality}, ${COSTS[args.quality].resolution})...`);
  console.log(`  Image: ${args.image.substring(0, 60)}...`);
  console.log(`  Audio: ${args.audio.substring(0, 60)}...`);
  console.log(`  Prompt: ${args.prompt.substring(0, 60)}...`);
  console.log(`  Estimated cost: $${(15 * COSTS[args.quality].perSecond).toFixed(2)} (15s max)`);

  const response = await fetch('https://api.kie.ai/api/v1/jobs/createTask', {
    method: 'POST',
    headers: {
      'Authorization': `Bearer ${KIE_API_KEY}`,
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      model: MODEL,
      input: {
        image_url: args.image,
        audio_url: args.audio,
        prompt: args.prompt,
      },
    }),
  });

  const result = await response.json();

  if (result.code !== 200) {
    console.error(`Kie.ai error: ${result.msg} (code ${result.code})`);
    if (result.code === 401) console.error('Check your KIE_AI_API_KEY');
    if (result.code === 402) console.error('Insufficient credits — top up at kie.ai');
    if (result.code === 422) console.error('Validation error — check image/audio URLs are accessible');
    process.exit(1);
  }

  return result.data.taskId;
}

async function pollForResult(taskId) {
  const pollInterval = parseInt(args['poll-interval']) * 1000;
  const maxWait = parseInt(args['max-wait']) * 1000;
  const startTime = Date.now();

  console.log(`Task: ${taskId}`);
  console.log(`Polling every ${args['poll-interval']}s (max ${args['max-wait']}s)...`);

  while (Date.now() - startTime < maxWait) {
    await new Promise(r => setTimeout(r, pollInterval));

    const response = await fetch(
      `https://api.kie.ai/api/v1/jobs/getTaskDetails?taskId=${taskId}`,
      { headers: { 'Authorization': `Bearer ${KIE_API_KEY}` } }
    );

    const result = await response.json();

    if (result.code === 200 && result.data) {
      const task = result.data;

      if (task.status === 'completed' || task.status === 'success') {
        return task;
      }

      if (task.status === 'failed') {
        console.error(`Avatar generation failed: ${task.error || 'Unknown error'}`);
        process.exit(1);
      }

      const elapsed = Math.round((Date.now() - startTime) / 1000);
      console.log(`  [${elapsed}s] Status: ${task.status}`);
    }
  }

  console.error(`Timed out after ${args['max-wait']}s. Check task at kie.ai/logs`);
  process.exit(1);
}

// Main
const outputDir = args.output;
if (!existsSync(outputDir)) mkdirSync(outputDir, { recursive: true });

const date = new Date().toISOString().split('T')[0];
const filename = args.name || `aivor-talking-${args.quality}-${date}-${Date.now().toString(36)}`;

try {
  const taskId = await createAvatarTask();
  const task = await pollForResult(taskId);

  // Extract video URL
  const videoUrl = task.output?.video_url || task.output?.url || task.result?.url;

  if (videoUrl) {
    console.log('\nDownloading avatar video...');
    const videoResponse = await fetch(videoUrl);
    const videoBuffer = Buffer.from(await videoResponse.arrayBuffer());

    const outputPath = join(outputDir, `${filename}.mp4`);
    writeFileSync(outputPath, videoBuffer);

    console.log(`Saved: ${outputPath}`);
    console.log(`Size: ${(videoBuffer.length / (1024 * 1024)).toFixed(1)} MB`);
  } else {
    console.log('Task complete but no video URL found in response.');
    console.log('Full result:', JSON.stringify(task, null, 2));
    console.log('Check kie.ai/logs for the generated video.');
  }
} catch (error) {
  console.error(`Avatar animation failed: ${error.message}`);
  process.exit(1);
}
