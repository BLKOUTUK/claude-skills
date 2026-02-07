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
  <!-- Individual sign → organisation sign → amplify → donate -->
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
