> **BLKOUT SKILL SYNC**
> Skill: community-web-design
> Last synced: 2026-02-07
> Source: https://github.com/BLKOUTUK/claude-skills
>
> **Update check:** At the start of each conversation in this Project, briefly note:
> "This Project uses the BLKOUT community-web-design skill (synced 2026-02-07). If you've updated the skill recently, you can refresh it by pasting the latest version from: https://raw.githubusercontent.com/BLKOUTUK/claude-skills/main/for-claude-ai/community-web-design.md"
>
> **To get the latest version**, visit:
> https://raw.githubusercontent.com/BLKOUTUK/claude-skills/main/for-claude-ai/community-web-design.md
> Select all -> Copy -> Replace this Project's instructions -> Paste -> Save

# Community Web Design

Build web pages that earn trust, honour community, and move people to action.

## Core Principles

These aren't style preferences--they're how the design earns trust:

- **Trust the people** -> No manipulation, no dark patterns. Clear information, honest CTAs
- **Move at the speed of trust** -> Progressive disclosure over overwhelming. Let relationships deepen
- **Small is good, small is all** -> Quality over scale. 10 committed people > 1000 passive clicks
- **Critical connections > critical mass** -> Design for depth of engagement, not vanity metrics
- **Less prep, more presence** -> Pages should feel human, not corporate. Warmth over polish

## Stack Decision

**Default to HTML/Tailwind** for:
- Landing pages, campaign pages, content showcases
- Subject briefings, documentation, guides
- Sign-up forms (simple), directories (static)

**Use React artifacts** for:
- Dashboards with state management
- Surveys, quizzes, competitions (multi-step, scoring)
- Interactive tools with calculations or filtering

## Page Types

### Landing Pages & Campaign Funnels

Journey: Awareness -> Understanding -> Connection -> Action

1. **Hook** - One clear statement of who this is for and why it matters
2. **Context** - The situation that makes this necessary
3. **Invitation** - What you're asking people to join/support/do
4. **Social proof** - Community voices. "Who else is here?"
5. **Action** - Single clear next step per viewport

Avoid: Countdown timers, fake scarcity, manipulation tactics.

### Coalition Building Pages

Pattern: Multiple organisations, shared purpose, distributed ownership

1. **Shared frame** - What brings us together
2. **Partner presence** - Equal visual weight, alphabetical or rotating
3. **Collective asks** - "We" language, shared positions
4. **Multiple entry points** - Different actions for different capacities
5. **Resource commons** - Shared assets, briefings, toolkits

### Membership Portals & Dashboards

Pattern: Belonging, not access. Relationship, not transaction.

1. **Welcome** - Personal, name-based, acknowledges contribution
2. **Community pulse** - What's happening, who's active
3. **Your journey** - Engagement history, suggested actions
4. **Resources** - Tools relevant to their role
5. **Connection** - Ways to reach others

### Interactive Tools

**Surveys:**
1. Purpose statement - Why asking, what happens with answers
2. Progress indicator - Always show position
3. Conditional logic - Skip irrelevant questions
4. Immediate value - Show something useful mid-survey
5. Gratitude close - Acknowledge contribution

**Directories:**
1. Search/filter first
2. Consent-based profiles
3. Connection facilitation
4. Reciprocity prompt - Invite viewers to add themselves

### Subject Briefings

1. **TL;DR** - One paragraph summary up front
2. **Why this matters** - Stakes and context
3. **Key points** - Scannable, clearly headed
4. **Deeper reading** - Expandable or linked
5. **Action bridge** - "Now you know this, here's what you can do"

### Content Showcases

1. **The work first** - Video/image/content as hero
2. **Context layer** - Who made this, why it matters
3. **Engagement invitation**
4. **Related threads**
5. **Creator presence**

## Visual Identity Modes

### BLKOUT UK / Black queer contexts

**Core aesthetic principle:** Boldness and masculinity, disrupted by beauty and vulnerability.

This is not "either/or" but "both/and" -- strength AND softness, bold AND vulnerable, masculine AND beautiful. The tension between these creates the BLKOUT aesthetic.

**Three-layer structure:**

1. **Foundation (the people at heart)**
   - Black bodies, faces looking directly at camera
   - Not decorative -- the ground everything stands on
   - Presence, witnessing, being witnessed
   - Hero imagery should show joy, power, vulnerability in equal measure
   - 20-30% opacity when used as background layer

2. **Protective shell (the structure)**
   - Bold typography: Work Sans 900 weight, uppercase, tight tracking
   - Dark backgrounds: deep blacks (#1a1a2e), purples (#4a1942)
   - Heavy borders: 4-8px gold (#d4af37) borders as power statements
   - No rounded corners -- sharp edges
   - Chunky titles: 5xl-7xl sizes
   - This shell "holds the sound of the sea" -- contains the movement

3. **Disruption (beauty/vulnerability breaking through)**
   - Tender language: "You, Beloved", "We receive you either way"
   - Italic moments of softness breaking the uppercase
   - Colorful elements at higher opacity (30%+) -- not hidden
   - Gradients (purple/gold fades) softening hard edges
   - Mix of uppercase commands and lowercase intimacy
   - Phrases acknowledging vulnerability: "We know this work is vulnerable"

**Typography:**
- Headlines: Work Sans Black (900), uppercase, tracking-tight
- Commands without shouting -- weight carries authority, not aggression
- Body: Work Sans Regular/Medium (400-500)
- Disruption moments: italic, lowercase, softer weight

**Colour:**
- Deep purples, golds, black as power (the shell)
- RGB shifts, gradients as beauty (the disruption)
- Generous space -- room to exist and breathe

**Imagery:**
- Centre joy AND struggle
- Black queer men claiming space
- Faces looking at lens -- direct witness
- Bodies in motion and stillness

**In practice:**
- No emojis (use typography weight and color for emphasis)
- Gold em-dashes (--) for lists, not bullets
- Moments of breath between bold sections
- The aesthetic develops through iteration, not prescription

### Coalition / collaborative contexts
- Neutral base allowing partner brands to coexist
- Flexible colour system for multiple identities
- Accessible typography, no single imposed voice

### Investor / enterprise contexts
- Sophistication without stuffiness
- Nature-forward imagery (for eco contexts)
- Confidence and groundedness
- Clear value proposition without hype

## Typography

**Headlines:** DM Serif Display, Fraunces, Playfair Display (warmth)
**Body:** Work Sans, Source Sans Pro, Atkinson Hyperlegible (accessibility)
**Avoid:** Inter, Roboto for body--feels corporate

## Implementation

**HTML/Tailwind:**
- Mobile-first always
- Custom colours in config for brand consistency
- WCAG AA contrast minimum
- Semantic HTML, focus states

**React:**
- Functional components with hooks
- localStorage for draft saves where appropriate
- Tailwind for styling consistency

## Context-Specific References

The following reference sections provide detailed pattern databases for landing pages, interactive tools, and visual systems.

---

# Landing Page Patterns

## Campaign Landing Page

For advocacy, petitions, sign-ons, calls to action.

```html
<!-- Structure -->
<section class="hero">
  <!-- Emotional hook: 1 sentence, who this is for -->
  <!-- Supporting image: people, not logos -->
</section>

<section class="context">
  <!-- 2-3 paragraphs: situation, stakes, opportunity -->
  <!-- Pull quote from community voice -->
</section>

<section class="ask">
  <!-- Clear single action -->
  <!-- Form or button -->
  <!-- What happens next (transparency) -->
</section>

<section class="community">
  <!-- Who else has joined -->
  <!-- Partner logos if coalition -->
  <!-- Counter or social proof -->
</section>

<section class="resources">
  <!-- For those who want more -->
  <!-- Briefings, FAQs, contact -->
</section>
```

### Tailwind Example - Campaign Page

```html
<body class="bg-stone-50 text-stone-900 font-sans">

  <!-- Hero -->
  <header class="min-h-[70vh] flex items-center px-6 py-16 md:px-12 lg:px-24">
    <div class="max-w-3xl">
      <h1 class="font-serif text-4xl md:text-6xl leading-tight mb-6">
        [Headline that names the reader and the stakes]
      </h1>
      <p class="text-xl md:text-2xl text-stone-600 mb-8">
        [One sentence expanding on what this is about]
      </p>
      <a href="#act" class="inline-block bg-stone-900 text-white px-8 py-4 text-lg hover:bg-stone-800 transition-colors">
        [Primary CTA]
      </a>
    </div>
  </header>

  <!-- Context -->
  <section class="bg-white px-6 py-16 md:px-12 lg:px-24">
    <div class="max-w-2xl mx-auto prose prose-lg">
      <!-- Narrative content here -->
    </div>
  </section>

  <!-- Action -->
  <section id="act" class="bg-stone-900 text-white px-6 py-16 md:px-12 lg:px-24">
    <div class="max-w-xl mx-auto text-center">
      <h2 class="font-serif text-3xl mb-6">[Invitation to act]</h2>
      <!-- Form here -->
    </div>
  </section>

</body>
```

## Coalition Landing Page

For multi-organisation initiatives, shared campaigns.

```html
<section class="shared-frame">
  <!-- What unites us (not who leads) -->
  <!-- The collective position/demand -->
</section>

<section class="partners">
  <!-- Equal visual weight -->
  <!-- Grid of logos, same size -->
  <!-- Alphabetical or randomised order -->
</section>

<section class="collective-asks">
  <!-- Numbered demands/positions -->
  <!-- "We" language throughout -->
</section>

<section class="multiple-entries">
  <!-- Different ways to engage -->
  <!-- Acknowledge different capacities -->
  <!-- Individual sign -> organisation sign -> amplify -> donate -->
</section>

<section class="resource-commons">
  <!-- Shared toolkit -->
  <!-- Briefings, graphics, templates -->
  <!-- All partners can use -->
</section>
```

## Investor/Enterprise Landing

For social enterprise, investment attraction, market validation.

```html
<section class="proposition">
  <!-- Clear value statement -->
  <!-- What you offer, who benefits -->
</section>

<section class="opportunity">
  <!-- Market context -->
  <!-- Why now, why this -->
  <!-- Numbers if relevant (but not hype) -->
</section>

<section class="credibility">
  <!-- Team/founder presence -->
  <!-- Track record -->
  <!-- Partnerships/endorsements -->
</section>

<section class="engagement">
  <!-- What you're looking for -->
  <!-- Clear next step for interested parties -->
  <!-- Expression of interest form -->
</section>
```

### Tailwind Example - Investor Page

```html
<body class="bg-white text-stone-800">

  <!-- Nav -->
  <nav class="flex justify-between items-center px-6 py-4 md:px-12">
    <span class="font-medium">[Brand]</span>
    <a href="#connect" class="text-sm border border-stone-800 px-4 py-2 hover:bg-stone-800 hover:text-white transition-colors">
      Get in Touch
    </a>
  </nav>

  <!-- Hero - restrained, confident -->
  <header class="px-6 py-24 md:px-12 lg:px-24 border-b">
    <h1 class="font-serif text-3xl md:text-5xl max-w-2xl leading-snug mb-6">
      [Value proposition - what you're building]
    </h1>
    <p class="text-lg text-stone-600 max-w-xl">
      [One sentence on the opportunity]
    </p>
  </header>

  <!-- Opportunity -->
  <section class="grid md:grid-cols-2 gap-12 px-6 py-16 md:px-12 lg:px-24">
    <div>
      <h2 class="font-serif text-2xl mb-4">The Opportunity</h2>
      <p class="text-stone-600 leading-relaxed">
        [Market context, why now]
      </p>
    </div>
    <div>
      <h2 class="font-serif text-2xl mb-4">Our Approach</h2>
      <p class="text-stone-600 leading-relaxed">
        [What makes this different]
      </p>
    </div>
  </section>

  <!-- CTA -->
  <section id="connect" class="bg-stone-100 px-6 py-16 md:px-12 lg:px-24 text-center">
    <h2 class="font-serif text-2xl mb-4">Interested?</h2>
    <p class="text-stone-600 mb-8 max-w-md mx-auto">
      [What happens when they reach out]
    </p>
    <!-- Form or email link -->
  </section>

</body>
```

## Manifesto/Declaration Page

For shared statements, collective positions.

```html
<section class="preamble">
  <!-- Context for why this exists -->
  <!-- Who is speaking (collectively) -->
</section>

<section class="declaration">
  <!-- The statement itself -->
  <!-- Numbered points or flowing prose -->
  <!-- Visually distinct treatment -->
</section>

<section class="signatories">
  <!-- Who has signed -->
  <!-- Growing list, recent additions highlighted -->
</section>

<section class="join">
  <!-- Add your name/organisation -->
  <!-- Different signature types (individual, org, ally) -->
</section>

<section class="spread">
  <!-- Share tools -->
  <!-- Graphics to download -->
  <!-- Suggested messages -->
</section>
```

## Content Showcase / Episode Page

For video, podcast, creative work.

```html
<section class="feature">
  <!-- The work itself - video/audio player -->
  <!-- Full-width or generous sizing -->
</section>

<section class="context">
  <!-- Episode/piece title -->
  <!-- Who made it, when -->
  <!-- Brief description -->
</section>

<section class="engage">
  <!-- Transcript/show notes (expandable) -->
  <!-- Discussion prompts -->
  <!-- Share options -->
</section>

<section class="related">
  <!-- Other episodes/work -->
  <!-- Thematic connections -->
</section>

<section class="creator">
  <!-- About the maker(s) -->
  <!-- How to follow/support -->
</section>
```

---

# Interactive Tools Patterns

## Multi-Step Survey

React pattern for surveys with conditional logic and progress tracking.

```jsx
import { useState } from 'react';

const Survey = () => {
  const [step, setStep] = useState(0);
  const [answers, setAnswers] = useState({});

  const questions = [
    {
      id: 'purpose',
      type: 'intro',
      content: {
        title: 'Before we begin',
        description: 'This survey takes about 5 minutes. Your responses help us [specific purpose]. All answers are [confidentiality statement].',
      }
    },
    {
      id: 'q1',
      type: 'single',
      question: '[Question text]',
      options: ['Option A', 'Option B', 'Option C'],
      // Optional: conditional next
      nextIf: { 'Option A': 'q2a', 'Option B': 'q2b', default: 'q2' }
    },
    // More questions...
    {
      id: 'complete',
      type: 'outro',
      content: {
        title: 'Thank you',
        description: 'Your input matters. Here\'s what happens next: [concrete next step]',
        // Optional: show something useful
        insight: (answers) => `Based on your responses, you might find [X] helpful.`
      }
    }
  ];

  const progress = ((step + 1) / questions.length) * 100;

  return (
    <div className="min-h-screen bg-stone-50 p-6">
      {/* Progress bar */}
      <div className="max-w-xl mx-auto mb-8">
        <div className="h-1 bg-stone-200 rounded-full">
          <div
            className="h-1 bg-stone-800 rounded-full transition-all duration-300"
            style={{ width: `${progress}%` }}
          />
        </div>
        <p className="text-sm text-stone-500 mt-2">
          {step + 1} of {questions.length}
        </p>
      </div>

      {/* Question content */}
      <div className="max-w-xl mx-auto">
        {/* Render based on question type */}
      </div>
    </div>
  );
};
```

### Question Types

**Single choice:**
```jsx
<div className="space-y-3">
  {options.map((option, i) => (
    <button
      key={i}
      onClick={() => handleAnswer(question.id, option)}
      className={`w-full text-left p-4 border rounded-lg transition-colors
        ${selected === option ? 'border-stone-800 bg-stone-100' : 'border-stone-200 hover:border-stone-400'}`}
    >
      {option}
    </button>
  ))}
</div>
```

**Multiple choice:**
```jsx
<div className="space-y-3">
  {options.map((option, i) => (
    <label key={i} className="flex items-center gap-3 p-4 border rounded-lg cursor-pointer hover:border-stone-400">
      <input
        type="checkbox"
        checked={selected.includes(option)}
        onChange={() => toggleOption(option)}
        className="w-5 h-5"
      />
      <span>{option}</span>
    </label>
  ))}
</div>
```

**Free text:**
```jsx
<textarea
  value={answers[question.id] || ''}
  onChange={(e) => handleAnswer(question.id, e.target.value)}
  placeholder="Share your thoughts..."
  className="w-full p-4 border border-stone-200 rounded-lg min-h-[150px] focus:outline-none focus:border-stone-400"
/>
```

**Scale/Rating:**
```jsx
<div className="flex justify-between gap-2">
  {[1, 2, 3, 4, 5].map((n) => (
    <button
      key={n}
      onClick={() => handleAnswer(question.id, n)}
      className={`w-12 h-12 rounded-full border-2 transition-colors
        ${selected === n ? 'border-stone-800 bg-stone-800 text-white' : 'border-stone-300 hover:border-stone-500'}`}
    >
      {n}
    </button>
  ))}
</div>
<div className="flex justify-between text-sm text-stone-500 mt-2">
  <span>Strongly disagree</span>
  <span>Strongly agree</span>
</div>
```

## Quiz with Scoring

For assessments, self-discovery tools, engagement.

```jsx
const Quiz = () => {
  const [currentQ, setCurrentQ] = useState(0);
  const [scores, setScores] = useState({});
  const [showResult, setShowResult] = useState(false);

  const questions = [
    {
      question: '[Question]',
      options: [
        { text: 'Option A', scores: { typeA: 2, typeB: 0 } },
        { text: 'Option B', scores: { typeA: 0, typeB: 2 } },
        { text: 'Option C', scores: { typeA: 1, typeB: 1 } },
      ]
    },
    // More questions...
  ];

  const results = {
    typeA: {
      title: 'You are a [Type A]',
      description: '[What this means]',
      resources: ['Resource 1', 'Resource 2']
    },
    typeB: {
      title: 'You are a [Type B]',
      description: '[What this means]',
      resources: ['Resource 1', 'Resource 2']
    }
  };

  const handleAnswer = (option) => {
    const newScores = { ...scores };
    Object.entries(option.scores).forEach(([type, points]) => {
      newScores[type] = (newScores[type] || 0) + points;
    });
    setScores(newScores);

    if (currentQ < questions.length - 1) {
      setCurrentQ(currentQ + 1);
    } else {
      setShowResult(true);
    }
  };

  const getResult = () => {
    const topType = Object.entries(scores).sort((a, b) => b[1] - a[1])[0][0];
    return results[topType];
  };

  // Render quiz or result...
};
```

## Directory with Search/Filter

For member directories, resource libraries, partner lists.

```jsx
const Directory = () => {
  const [search, setSearch] = useState('');
  const [filters, setFilters] = useState({});

  const entries = [
    {
      id: 1,
      name: '[Name]',
      type: '[Category]',
      location: '[Location]',
      tags: ['tag1', 'tag2'],
      description: '[Brief description]',
      contact: '[How to reach]'
    },
    // More entries...
  ];

  const filterOptions = {
    type: ['Category A', 'Category B', 'Category C'],
    location: ['London', 'Manchester', 'Birmingham', 'Online']
  };

  const filtered = entries.filter(entry => {
    // Search match
    const searchMatch = !search ||
      entry.name.toLowerCase().includes(search.toLowerCase()) ||
      entry.description.toLowerCase().includes(search.toLowerCase());

    // Filter matches
    const filterMatch = Object.entries(filters).every(([key, value]) =>
      !value || entry[key] === value
    );

    return searchMatch && filterMatch;
  });

  return (
    <div className="max-w-4xl mx-auto p-6">
      {/* Search */}
      <div className="mb-6">
        <input
          type="text"
          value={search}
          onChange={(e) => setSearch(e.target.value)}
          placeholder="Search..."
          className="w-full p-4 border border-stone-200 rounded-lg"
        />
      </div>

      {/* Filters */}
      <div className="flex gap-4 mb-8">
        {Object.entries(filterOptions).map(([key, options]) => (
          <select
            key={key}
            value={filters[key] || ''}
            onChange={(e) => setFilters({...filters, [key]: e.target.value})}
            className="p-2 border border-stone-200 rounded"
          >
            <option value="">All {key}s</option>
            {options.map(opt => (
              <option key={opt} value={opt}>{opt}</option>
            ))}
          </select>
        ))}
      </div>

      {/* Results */}
      <div className="space-y-4">
        {filtered.map(entry => (
          <div key={entry.id} className="p-6 border border-stone-200 rounded-lg">
            <h3 className="font-medium text-lg">{entry.name}</h3>
            <p className="text-stone-600 text-sm mb-2">{entry.type} - {entry.location}</p>
            <p className="text-stone-700">{entry.description}</p>
            <div className="flex gap-2 mt-3">
              {entry.tags.map(tag => (
                <span key={tag} className="text-xs bg-stone-100 px-2 py-1 rounded">
                  {tag}
                </span>
              ))}
            </div>
          </div>
        ))}
      </div>

      {/* Add yourself prompt */}
      <div className="mt-12 p-6 bg-stone-100 rounded-lg text-center">
        <p className="text-stone-600 mb-4">Should you be listed here?</p>
        <button className="bg-stone-800 text-white px-6 py-2 rounded">
          Add your entry
        </button>
      </div>
    </div>
  );
};
```

## Sign-up Form (HTML/Tailwind)

For simple email capture, interest registration.

```html
<form class="max-w-md mx-auto" action="[endpoint]" method="POST">
  <div class="mb-4">
    <label for="email" class="block text-sm font-medium mb-1">Email</label>
    <input
      type="email"
      id="email"
      name="email"
      required
      class="w-full p-3 border border-stone-300 rounded focus:outline-none focus:border-stone-500"
      placeholder="you@example.com"
    />
  </div>

  <div class="mb-4">
    <label for="name" class="block text-sm font-medium mb-1">Name (optional)</label>
    <input
      type="text"
      id="name"
      name="name"
      class="w-full p-3 border border-stone-300 rounded focus:outline-none focus:border-stone-500"
    />
  </div>

  <!-- Optional: What brings you here -->
  <div class="mb-6">
    <label class="block text-sm font-medium mb-2">What brings you here?</label>
    <div class="space-y-2">
      <label class="flex items-center gap-2">
        <input type="checkbox" name="interest[]" value="stay-informed" class="w-4 h-4" />
        <span>Stay informed</span>
      </label>
      <label class="flex items-center gap-2">
        <input type="checkbox" name="interest[]" value="get-involved" class="w-4 h-4" />
        <span>Get involved</span>
      </label>
      <label class="flex items-center gap-2">
        <input type="checkbox" name="interest[]" value="support" class="w-4 h-4" />
        <span>Offer support</span>
      </label>
    </div>
  </div>

  <button
    type="submit"
    class="w-full bg-stone-800 text-white py-3 rounded hover:bg-stone-700 transition-colors"
  >
    Join us
  </button>

  <p class="text-xs text-stone-500 mt-4 text-center">
    [What happens with their data - be specific and honest]
  </p>
</form>
```

## Competition/Giveaway Entry

```jsx
const Competition = () => {
  const [step, setStep] = useState('entry'); // entry | confirm | success
  const [entry, setEntry] = useState({ email: '', name: '', answer: '' });

  return (
    <div className="max-w-lg mx-auto p-6">
      {step === 'entry' && (
        <form onSubmit={(e) => { e.preventDefault(); setStep('confirm'); }}>
          <h2 className="font-serif text-2xl mb-4">[Competition title]</h2>
          <p className="text-stone-600 mb-6">[What you could win]</p>

          {/* Entry fields */}
          <input
            type="email"
            required
            value={entry.email}
            onChange={(e) => setEntry({...entry, email: e.target.value})}
            placeholder="Your email"
            className="w-full p-3 border border-stone-300 rounded mb-4"
          />

          <input
            type="text"
            required
            value={entry.name}
            onChange={(e) => setEntry({...entry, name: e.target.value})}
            placeholder="Your name"
            className="w-full p-3 border border-stone-300 rounded mb-4"
          />

          {/* Optional: skill-based entry */}
          <textarea
            value={entry.answer}
            onChange={(e) => setEntry({...entry, answer: e.target.value})}
            placeholder="[Optional creative prompt]"
            className="w-full p-3 border border-stone-300 rounded mb-6 min-h-[100px]"
          />

          <button type="submit" className="w-full bg-stone-800 text-white py-3 rounded">
            Enter
          </button>

          <p className="text-xs text-stone-500 mt-4">
            [Clear terms: draw date, how winner contacted, what happens with data]
          </p>
        </form>
      )}

      {step === 'confirm' && (
        <div className="text-center">
          <h2 className="font-serif text-2xl mb-4">Confirm your entry</h2>
          <p className="text-stone-600 mb-6">
            We'll email {entry.email} if you win. Make sure that's right!
          </p>
          <div className="flex gap-4 justify-center">
            <button onClick={() => setStep('entry')} className="px-6 py-2 border border-stone-300 rounded">
              Go back
            </button>
            <button onClick={() => setStep('success')} className="px-6 py-2 bg-stone-800 text-white rounded">
              Confirm
            </button>
          </div>
        </div>
      )}

      {step === 'success' && (
        <div className="text-center">
          <h2 className="font-serif text-2xl mb-4">You're in!</h2>
          <p className="text-stone-600 mb-6">
            [What happens next - when draw happens, how they'll know]
          </p>
          {/* Optional: share for extra entries */}
          <p className="text-sm text-stone-500">
            [Invite to share, follow, etc. - but don't make it manipulative]
          </p>
        </div>
      )}
    </div>
  );
};
```

---

# Visual Systems

## Colour Palettes by Context

### BLKOUT UK / Black Queer Contexts

**Primary palette:**
```css
:root {
  --blk-deep: #1a1a2e;      /* Near-black with warmth */
  --blk-purple: #4a1942;    /* Deep purple - power */
  --blk-gold: #d4af37;      /* Gold - celebration, value */
  --blk-warm: #2d2a32;      /* Warm dark grey */
  --blk-light: #f5f2eb;     /* Off-white - breathing room */
}
```

**Usage:**
- Deep purple/black for backgrounds, headers
- Gold for accents, CTAs, highlights
- Warm grey for body text on light backgrounds
- Off-white for main content areas

**Mood:** Bold, unapologetic, joyful, claiming space

### Coalition / Collaborative Contexts

**Neutral base:**
```css
:root {
  --coal-base: #fafaf9;     /* Stone 50 - clean slate */
  --coal-text: #44403c;     /* Stone 700 - readable */
  --coal-accent: #78716c;   /* Stone 500 - subtle */
  --coal-border: #e7e5e4;   /* Stone 200 - definition */
  --coal-dark: #1c1917;     /* Stone 900 - headers */
}
```

**Usage:**
- Base for backgrounds
- Allow partner brand colours to pop
- Use accent sparingly
- Dark only for important headers

**Mood:** Neutral, professional, inclusive, not imposing

### Investor / Enterprise Contexts

**Sophisticated palette:**
```css
:root {
  --inv-cream: #fefdfb;     /* Warm white */
  --inv-text: #374151;      /* Cool grey - trustworthy */
  --inv-accent: #059669;    /* Emerald - growth (eco) */
  --inv-muted: #9ca3af;     /* Grey 400 - secondary */
  --inv-dark: #111827;      /* Grey 900 - authority */
}
```

**For Caribbean/eco contexts (Yukayeke):**
```css
:root {
  --yuk-sand: #fef9f3;      /* Warm sand */
  --yuk-ocean: #0d9488;     /* Teal - water */
  --yuk-earth: #78350f;     /* Amber 900 - earth */
  --yuk-leaf: #166534;      /* Green 800 - nature */
  --yuk-sunset: #ea580c;    /* Orange - warmth */
}
```

**Mood:** Grounded, confident, natural, trustworthy

### Mental Health / Advocacy Contexts

**Gentle strength palette:**
```css
:root {
  --mh-soft: #f8fafc;       /* Slate 50 - calming */
  --mh-text: #334155;       /* Slate 700 - clear */
  --mh-hope: #7c3aed;       /* Violet - transformation */
  --mh-ground: #64748b;     /* Slate 500 - steady */
  --mh-warm: #fef3c7;       /* Amber 100 - light */
}
```

**Mood:** Calming, hopeful, accessible, not clinical

## Typography Systems

### Warm & Distinctive (BLKOUT, creative contexts)

```html
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,400;9..144,600&family=Work+Sans:wght@400;500&display=swap" rel="stylesheet">
```

```css
:root {
  --font-display: 'Fraunces', serif;
  --font-body: 'Work Sans', sans-serif;
}

h1, h2, h3 { font-family: var(--font-display); }
body { font-family: var(--font-body); }
```

**Alternative pairings:**
- DM Serif Display + DM Sans
- Playfair Display + Source Sans Pro
- Libre Baskerville + Open Sans

### Professional & Accessible (Coalitions, advocacy)

```html
<link href="https://fonts.googleapis.com/css2?family=Source+Serif+4:wght@400;600&family=Atkinson+Hyperlegible:wght@400;700&display=swap" rel="stylesheet">
```

```css
:root {
  --font-display: 'Source Serif 4', serif;
  --font-body: 'Atkinson Hyperlegible', sans-serif;
}
```

**Why Atkinson Hyperlegible:** Designed for low-vision readers, excellent for accessibility-focused projects.

**Alternative pairings:**
- Merriweather + Open Sans
- Lora + Source Sans Pro

### Confident & Modern (Investor, enterprise)

```html
<link href="https://fonts.googleapis.com/css2?family=DM+Serif+Display&family=DM+Sans:wght@400;500;700&display=swap" rel="stylesheet">
```

```css
:root {
  --font-display: 'DM Serif Display', serif;
  --font-body: 'DM Sans', sans-serif;
}
```

**Alternative pairings:**
- Cormorant Garamond + Montserrat
- Libre Baskerville + Karla

## Type Scale

Use a consistent scale. Recommended base: 16px/1rem.

```css
:root {
  --text-xs: 0.75rem;    /* 12px - captions */
  --text-sm: 0.875rem;   /* 14px - small text */
  --text-base: 1rem;     /* 16px - body */
  --text-lg: 1.125rem;   /* 18px - lead */
  --text-xl: 1.25rem;    /* 20px - subhead */
  --text-2xl: 1.5rem;    /* 24px - section head */
  --text-3xl: 1.875rem;  /* 30px - major head */
  --text-4xl: 2.25rem;   /* 36px - page title */
  --text-5xl: 3rem;      /* 48px - hero */
  --text-6xl: 3.75rem;   /* 60px - display */
}
```

**Line heights:**
- Body text: 1.6-1.75
- Headers: 1.1-1.3
- Tight (large display): 1.0-1.1

## Spacing System

Use Tailwind's 4px base (or similar):

```
4   = 1rem/4  = 0.25rem = 4px
8   = 1rem/2  = 0.5rem  = 8px
12  = 1rem*.75= 0.75rem = 12px
16  = 1rem    = 1rem    = 16px
24  = 1.5rem  = 1.5rem  = 24px
32  = 2rem    = 2rem    = 32px
48  = 3rem    = 3rem    = 48px
64  = 4rem    = 4rem    = 64px
96  = 6rem    = 6rem    = 96px
```

**General principles:**
- Generous margins (don't crowd)
- Consistent rhythm (stick to the scale)
- More space > less space (let things breathe)

## Responsive Breakpoints

```css
/* Mobile first */
/* sm: 640px */
/* md: 768px */
/* lg: 1024px */
/* xl: 1280px */
/* 2xl: 1536px */
```

**Common patterns:**
- Single column below md
- Two columns md-lg
- Max-width container on large screens
- Font size increases at larger breakpoints

## Accessibility Checklist

**Colour:**
- [ ] 4.5:1 contrast for body text (WCAG AA)
- [ ] 3:1 contrast for large text (18px+ bold or 24px+)
- [ ] Don't rely on colour alone for meaning
- [ ] Test with colour blindness simulator

**Typography:**
- [ ] Base font size 16px minimum
- [ ] Line height 1.5+ for body text
- [ ] Max line length ~65-75 characters

**Interaction:**
- [ ] Focus states visible
- [ ] Touch targets 44px minimum
- [ ] Skip links for keyboard navigation
- [ ] Form labels associated with inputs

**Content:**
- [ ] Alt text for images
- [ ] Semantic HTML (proper heading hierarchy)
- [ ] Sufficient colour contrast on hover/focus states

## Component Patterns

### Buttons

```html
<!-- Primary -->
<button class="bg-stone-900 text-white px-6 py-3 rounded hover:bg-stone-800 transition-colors focus:outline-none focus:ring-2 focus:ring-stone-900 focus:ring-offset-2">
  Primary Action
</button>

<!-- Secondary -->
<button class="border border-stone-300 text-stone-700 px-6 py-3 rounded hover:border-stone-500 transition-colors focus:outline-none focus:ring-2 focus:ring-stone-500 focus:ring-offset-2">
  Secondary Action
</button>

<!-- Ghost -->
<button class="text-stone-600 underline underline-offset-4 hover:text-stone-900 focus:outline-none focus:ring-2 focus:ring-stone-500">
  Tertiary Action
</button>
```

### Cards

```html
<article class="p-6 border border-stone-200 rounded-lg hover:border-stone-300 transition-colors">
  <h3 class="font-medium text-lg mb-2">[Title]</h3>
  <p class="text-stone-600 text-sm mb-4">[Description]</p>
  <a href="#" class="text-sm font-medium text-stone-900 hover:underline">
    Learn more ->
  </a>
</article>
```

### Form inputs

```html
<div class="mb-4">
  <label for="field" class="block text-sm font-medium text-stone-700 mb-1">
    Label
  </label>
  <input
    type="text"
    id="field"
    name="field"
    class="w-full p-3 border border-stone-300 rounded focus:outline-none focus:border-stone-500 focus:ring-1 focus:ring-stone-500"
    placeholder="Placeholder text"
  />
  <p class="text-xs text-stone-500 mt-1">Helper text if needed</p>
</div>
```

### Navigation

```html
<nav class="flex items-center justify-between px-6 py-4">
  <a href="/" class="font-medium text-lg">[Brand]</a>

  <div class="hidden md:flex items-center gap-8">
    <a href="#" class="text-stone-600 hover:text-stone-900">Link</a>
    <a href="#" class="text-stone-600 hover:text-stone-900">Link</a>
    <a href="#" class="bg-stone-900 text-white px-4 py-2 rounded hover:bg-stone-800">
      CTA
    </a>
  </div>

  <!-- Mobile menu button -->
  <button class="md:hidden">
    <svg><!-- Menu icon --></svg>
  </button>
</nav>
```
