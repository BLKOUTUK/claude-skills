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
    Learn more →
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
