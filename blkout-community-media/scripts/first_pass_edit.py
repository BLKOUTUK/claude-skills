#!/usr/bin/env python3
"""
BLKOUT Community Media - First Pass Edit Script

Analyzes transcript and suggests edits.
Flags consent concerns, filler words, long pauses, and natural breaks.

Usage:
    python first_pass_edit.py transcript.md --output edit_suggestions.md
"""

import argparse
import re
import json
from pathlib import Path
from datetime import datetime

# Patterns to flag
FILLER_WORDS = [
    'um', 'uh', 'like', 'you know', 'kind of', 'sort of', 
    'basically', 'actually', 'literally', 'honestly'
]

CONSENT_FLAGS = [
    # Third party mentions
    r'\b(my (?:wife|husband|partner|ex|mother|father|boss|friend|colleague)[\'s]?)\b',
    r'\b(someone I know|a friend of mine|this person)\b',
    # Sensitive disclosures
    r'\b(HIV|diagnosis|medication|therapy|therapist|counselor)\b',
    r'\b(assault|abuse|violence|attacked)\b',
    r'\b(suicide|self.?harm|depression|anxiety|mental health)\b',
    r'\b(fired|sacked|unemployed|bankruptcy|debt)\b',
    r'\b(affair|cheating|divorce|breakup)\b',
    r'\b(arrested|police|court|criminal)\b',
    # Identity disclosures about others
    r'\b(came out|closeted|out as|gay|trans|queer)\b.*\b(they|their|he|she|friend|family)\b',
]

SEGMENT_MARKERS = [
    # Natural topic transitions
    r'(?:but )?(?:anyway|moving on|so|now|next)',
    r'(?:that )?(?:brings me to|reminds me of)',
    r'on (?:a )?(?:different|another|related) (?:note|topic|subject)',
]

def parse_transcript(content):
    """
    Parse transcript markdown into segments.
    
    Returns list of dicts with timestamp and text.
    """
    segments = []
    
    # Pattern: **[MM:SS]** or **[HH:MM:SS]** followed by text
    pattern = r'\*\*\[(\d{1,2}:\d{2}(?::\d{2})?)\]\*\*\s*(.+?)(?=\*\*\[|\n\n---|\Z)'
    
    matches = re.findall(pattern, content, re.DOTALL)
    
    for timestamp, text in matches:
        segments.append({
            'timestamp': timestamp,
            'text': text.strip()
        })
    
    return segments

def analyze_filler_words(segments):
    """Find filler word clusters."""
    findings = []
    
    for seg in segments:
        text_lower = seg['text'].lower()
        filler_count = 0
        found_fillers = []
        
        for filler in FILLER_WORDS:
            count = len(re.findall(r'\b' + filler + r'\b', text_lower))
            if count > 0:
                filler_count += count
                found_fillers.append(f"{filler} ({count})")
        
        if filler_count >= 3:
            findings.append({
                'timestamp': seg['timestamp'],
                'type': 'filler_cluster',
                'severity': 'low',
                'description': f"Filler word cluster: {', '.join(found_fillers)}",
                'suggestion': "Consider light cleanup if distracting"
            })
    
    return findings

def analyze_consent_concerns(segments):
    """Flag potential consent issues."""
    findings = []
    
    for seg in segments:
        for pattern in CONSENT_FLAGS:
            matches = re.findall(pattern, seg['text'], re.IGNORECASE)
            if matches:
                findings.append({
                    'timestamp': seg['timestamp'],
                    'type': 'consent_flag',
                    'severity': 'high',
                    'description': f"Potential consent concern: '{matches[0] if isinstance(matches[0], str) else matches[0][0]}'",
                    'suggestion': "Review for: third-party identification, sensitive disclosure, duty of care",
                    'excerpt': seg['text'][:200] + '...' if len(seg['text']) > 200 else seg['text']
                })
    
    return findings

def analyze_natural_breaks(segments):
    """Identify natural segment breaks."""
    findings = []
    
    for i, seg in enumerate(segments):
        for pattern in SEGMENT_MARKERS:
            if re.search(pattern, seg['text'].lower()):
                findings.append({
                    'timestamp': seg['timestamp'],
                    'type': 'segment_break',
                    'severity': 'info',
                    'description': "Potential natural segment break",
                    'suggestion': "Consider chapter marker or section break"
                })
                break
    
    return findings

def analyze_long_segments(segments):
    """Flag potentially long uninterrupted sections."""
    findings = []
    
    for seg in segments:
        word_count = len(seg['text'].split())
        if word_count > 300:  # Roughly 2 minutes of speech
            findings.append({
                'timestamp': seg['timestamp'],
                'type': 'long_segment',
                'severity': 'info',
                'description': f"Long segment ({word_count} words, ~{word_count // 150} mins)",
                'suggestion': "Consider if visual breaks or b-roll needed"
            })
    
    return findings

def generate_report(findings, input_path):
    """Generate markdown edit suggestions report."""
    lines = []
    
    # Header
    lines.append("# First Pass Edit Suggestions")
    lines.append("")
    lines.append(f"**Source:** {input_path}")
    lines.append(f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## Summary")
    lines.append("")
    
    # Count by type
    type_counts = {}
    for f in findings:
        type_counts[f['type']] = type_counts.get(f['type'], 0) + 1
    
    lines.append(f"- **Consent flags:** {type_counts.get('consent_flag', 0)} ⚠️")
    lines.append(f"- **Filler clusters:** {type_counts.get('filler_cluster', 0)}")
    lines.append(f"- **Segment breaks:** {type_counts.get('segment_break', 0)}")
    lines.append(f"- **Long segments:** {type_counts.get('long_segment', 0)}")
    lines.append("")
    
    # Priority section: Consent
    consent_findings = [f for f in findings if f['type'] == 'consent_flag']
    if consent_findings:
        lines.append("---")
        lines.append("")
        lines.append("## ⚠️ Consent Review Required")
        lines.append("")
        lines.append("**These items require human review before proceeding.**")
        lines.append("")
        
        for finding in consent_findings:
            lines.append(f"### [{finding['timestamp']}] {finding['description']}")
            lines.append("")
            lines.append(f"**Suggestion:** {finding['suggestion']}")
            lines.append("")
            if 'excerpt' in finding:
                lines.append("**Excerpt:**")
                lines.append(f"> {finding['excerpt']}")
                lines.append("")
            lines.append("- [ ] Reviewed")
            lines.append("- [ ] Action: _______________")
            lines.append("")
    
    # Other findings by timestamp
    other_findings = [f for f in findings if f['type'] != 'consent_flag']
    if other_findings:
        lines.append("---")
        lines.append("")
        lines.append("## Other Suggestions")
        lines.append("")
        
        # Sort by timestamp
        other_findings.sort(key=lambda x: x['timestamp'])
        
        for finding in other_findings:
            icon = {
                'filler_cluster': '🔊',
                'segment_break': '📍',
                'long_segment': '⏱️'
            }.get(finding['type'], '•')
            
            lines.append(f"- **[{finding['timestamp']}]** {icon} {finding['description']}")
            lines.append(f"  - *{finding['suggestion']}*")
            lines.append("")
    
    # Footer
    lines.append("---")
    lines.append("")
    lines.append("## Editor Notes")
    lines.append("")
    lines.append("*Add your notes here:*")
    lines.append("")
    lines.append("### Decisions Made")
    lines.append("")
    lines.append("- ")
    lines.append("")
    lines.append("### Outstanding Questions")
    lines.append("")
    lines.append("- ")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("*This is automated analysis. Human judgment required for all edit decisions.*")
    
    return '\n'.join(lines)

def main():
    parser = argparse.ArgumentParser(
        description="Analyze transcript and suggest edits"
    )
    parser.add_argument("input", help="Input transcript markdown file")
    parser.add_argument("--output", "-o", help="Output suggestions file", default=None)
    
    args = parser.parse_args()
    
    input_path = Path(args.input)
    if not input_path.exists():
        print(f"Error: Input file not found: {input_path}")
        return 1
    
    output_path = Path(args.output) if args.output else input_path.with_name(
        input_path.stem + '_edit_suggestions.md'
    )
    
    # Read transcript
    content = input_path.read_text()
    
    # Parse into segments
    segments = parse_transcript(content)
    
    if not segments:
        print("Warning: No timestamped segments found in transcript")
        print("Expected format: **[MM:SS]** text")
        return 1
    
    print(f"Analyzing {len(segments)} segments...")
    
    # Run analysis
    findings = []
    findings.extend(analyze_consent_concerns(segments))
    findings.extend(analyze_filler_words(segments))
    findings.extend(analyze_natural_breaks(segments))
    findings.extend(analyze_long_segments(segments))
    
    # Generate report
    report = generate_report(findings, input_path)
    
    # Write output
    output_path.write_text(report)
    print(f"Edit suggestions saved to: {output_path}")
    
    # Summary
    consent_count = len([f for f in findings if f['type'] == 'consent_flag'])
    if consent_count > 0:
        print(f"\n⚠️  {consent_count} consent flag(s) require human review")

if __name__ == "__main__":
    main()
