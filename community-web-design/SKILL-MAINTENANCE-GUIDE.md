# Community Web Design Skill - Maintenance Guide

## Current Status (Feb 7, 2026)

The `community-web-design` skill has been updated with critical insights about BLKOUT's aesthetic structure. This guide explains how to keep the skill accessible across conversations.

## What Changed

### Added: BLKOUT Three-Layer Aesthetic Structure

**Core principle:** Boldness and masculinity, disrupted by beauty and vulnerability.

The skill now documents:
1. **Foundation layer** - Black bodies/faces as ground (people at heart)
2. **Protective shell** - Bold typography, dark backgrounds (the structure)
3. **Disruption** - Beauty/vulnerability breaking through (the tenderness)

Plus specific implementation details:
- Typography weights and usage patterns
- Opacity levels for imagery layers
- Color applications (when bold, when soft)
- The insight that aesthetic develops through iteration

## How to Update the Skill in Claude.ai

### Method 1: Via Skills Interface (Recommended)

1. Download the updated `SKILL.md` from this conversation's outputs
2. Go to claude.ai → Settings → Skills
3. Find "community-web-design" skill
4. Click Edit
5. Replace the content with the updated SKILL.md
6. Save

### Method 2: Via File Upload

If the skill doesn't exist yet:
1. Download `SKILL.md` from outputs
2. Go to claude.ai → Settings → Skills
3. Click "Create Skill" or "Import"
4. Upload the SKILL.md file
5. Ensure the skill name is: `community-web-design`

## Verification

To verify the skill is properly loaded in a new conversation:

1. Start a new chat
2. Ask: "Can you check if you have access to the community-web-design skill?"
3. Claude should be able to reference the three-layer aesthetic structure
4. If Claude can't see it, the skill needs to be re-uploaded

## Backup Strategy

### Google Drive Backup

1. Upload `SKILL.md` to your BLKOUT Google Drive
2. Store in: `/BLKOUT/Design System/Skills/`
3. Keep versioned backups: `SKILL-2026-02-07.md`

This ensures:
- The skill is searchable via Google Drive MCP
- Version history is preserved
- Can be recovered if accidentally deleted from Skills interface

## Why Both Methods Matter

**Skills Interface:**
- Automatically available to Claude in all conversations
- Integrated into Claude's system prompt
- Best for active, frequently-used skills

**Google Drive:**
- Permanent backup outside Claude's system
- Version control and history
- Can be shared with collaborators
- Searchable via drive_search tool if Skills interface fails

## File Structure

```
BLKOUT Google Drive/
├── Design System/
│   ├── Skills/
│   │   ├── community-web-design/
│   │   │   ├── SKILL.md (current version)
│   │   │   ├── SKILL-2026-02-07.md (dated backup)
│   │   │   ├── patterns-landing.md
│   │   │   ├── patterns-interactive.md
│   │   │   └── visual-systems.md
```

## When to Update the Skill

Update when:
- New aesthetic insights emerge through iteration
- Pattern examples need refinement
- BLKOUT's visual identity evolves
- Core principles shift or expand
- Implementation details change

Don't update for:
- One-off project variations
- Client-specific customizations
- Experimental ideas not yet validated

## Migration Notes

**Before (original skill):**
- Generic guidance: "Bold colour, Typography that commands"
- No structural framework
- Surface-level aesthetic description

**After (updated skill):**
- Three-layer structural framework
- Specific implementation details (weights, opacities, patterns)
- Core principle: disruption as aesthetic strategy
- Recognition that iteration develops the aesthetic

## Next Steps

1. Download `SKILL.md` from conversation outputs
2. Upload to Claude.ai Skills interface
3. Backup to Google Drive at `/BLKOUT/Design System/Skills/`
4. Test in a new conversation to verify access
5. Update this guide if the process changes

## Troubleshooting

**Problem:** Claude can't see the updated skill in new conversations
**Solution:** Check Skills interface, ensure skill is "enabled"

**Problem:** Skill content reverts to old version
**Solution:** Re-upload from Google Drive backup

**Problem:** Skill not triggering automatically
**Solution:** Explicitly reference it: "Use the community-web-design skill for this"

## Contact

For questions about skill maintenance:
- Check `/mnt/skills/user/community-web-design/` in Claude's filesystem
- Search Google Drive for latest version
- Reference this conversation: chat ID in transcript header

---

Last updated: February 7, 2026
Updated by: Claude (in conversation with Rob)
Version: 2.0 - Added BLKOUT three-layer aesthetic structure
