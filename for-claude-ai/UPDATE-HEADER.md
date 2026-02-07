# Skill Sync Protocol

Each skill pasted into claude.ai Projects includes a sync header at the top. This header:

1. Records when the skill was last pasted in (version date)
2. Tells Claude where the canonical version lives (raw GitHub URL)
3. Instructs Claude to offer an update check at the start of each conversation

## How It Works

**When a user opens a Project with a BLKOUT skill:**

Claude sees the sync header and says something like:
> "This skill was last synced on [date]. Want me to check for updates from the repo?"

If yes, Claude fetches the raw GitHub URL and compares. If different, it tells the user:
> "There's an updated version. To update, replace this Project's instructions with the content at: [URL]"

**To manually update:**
1. Go to the raw GitHub URL shown in the skill header
2. Select all, copy
3. Open your claude.ai Project > Settings > Instructions
4. Replace all content, paste, save

## Raw GitHub URLs

- blkout-brand: https://raw.githubusercontent.com/BLKOUTUK/claude-skills/main/for-claude-ai/blkout-brand.md
- blkout-themes: https://raw.githubusercontent.com/BLKOUTUK/claude-skills/main/for-claude-ai/blkout-themes.md
- community-web-design: https://raw.githubusercontent.com/BLKOUTUK/claude-skills/main/for-claude-ai/community-web-design.md
- uk-community-funding: https://raw.githubusercontent.com/BLKOUTUK/claude-skills/main/for-claude-ai/uk-community-funding.md
- blkout-community-media: https://raw.githubusercontent.com/BLKOUTUK/claude-skills/main/for-claude-ai/blkout-community-media.md
