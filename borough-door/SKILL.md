---
name: borough-door
description: Open a new BLKOUT borough door — the full pipeline from recon to a built, verified, gated static page. Use when Rob asks to build/open/add a borough (or city) door, refresh an existing door's data, or run a borough deep-dive. The next borough is a data file, not code.
---

# Borough Door — open a door in a new borough

Built 27 Aug 2026 from the Croydon/Lambeth/Enfield proof build (the strategy: `~/blkout/projects/32-boroughs/local-everywhere-strategy-v1.md`; the build spec + gates: `~/blkout/projects/32-boroughs/croydon-door-spec-v1.md`; design receipts: `~/blkout/projects/32-boroughs/design-loop/receipts.md`).

**The machinery** (all in `~/blkout/platform/apps/events-calendar/`):
- Generator: `scripts/borough-doors/build-borough-doors.mjs` — reads `scripts/borough-doors/data/<slug>.json`, emits `public/<slug>/index.html`. Run it with **explicit slugs** (`… build-borough-doors.mjs haringey`); a bare run refuses — see §7. Template identity: typographic-poster grammar, photographic grounds, gradient colour plates, sticky headings on plain dark sections, flexbox-only (no CSS grid — old engines). It FAILS LOUD: prints miscentred-skipped and not-currency-checked entries every build — read them.
- Landmark pipeline: `scripts/borough-doors/make-landmark.py SKETCH.png OUT.png [--window top|mid] [--threshold N]`.
- Shared census table: `scripts/borough-doors/data/_census.json` (from the Critical Frequency dossier Table 5).
- Borough map geometry: `scripts/borough-doors/data/_boroughs-map.json` — 33 ONS borough outlines pre-projected to SVG. See §7.
- Superseded renderer: `scripts/borough-doors/build-borough-doors-v1.mjs` — reference only, nothing builds from it.


**Known-broken, as at 31 Aug 2026** (check before assuming these are fixed):
- **Lambeth's four archive links are dead** — they use `blkoutuk.com/stories/<slug>`, which returns the SPA shell for every slug. See §1.3. Either republish the pieces or empty the box.
- **Currency outstanding**: Croydon 6 entries, Lambeth 11, Enfield 2. Haringey is the only door at zero. The generator prints the list every build.
- **Haringey's acceptance test (§6.5) has not been run** — it needs the page indexed first.

## 1 · Recon — the estate knows more than the web. In this order:
1. **Own project corpora** (`~/blkout/projects/*`) — grep for the borough. The Croydon kinship story sat unread in Ivor's Compass docs while I searched databases.
2. **Events DB** (Supabase `events`, status='approved', location/title/description ilike) → the "recently in the borough" strip. **Past events are rot-proof data** — proof of life that never goes stale.
3. **Story archive** (`legacy_articles` + `published_articles`, title/content ilike) → the "From the BLKOUT archive" box.
   ⚠ **A row in the table does NOT mean a page exists.** `blkoutuk.com/stories/<slug>` is a stale pattern — it returns a ~4.9 KB SPA shell for *every* slug, including ones that work elsewhere. `voices.blkoutuk.com/articles/<slug>` renders only what is actually published there; legacy rows render on neither. **Verify each deep link by content, not status:** fetch it, and check the `<title>` names the article and the byte count differs from an invented slug on the same route. Four identical byte counts = four dead links returning 200. Haringey's archive box is empty for exactly this reason; **Lambeth ships four dead links today** and is still to be fixed.
4. **Archive DB** (`~/archive_2026/search-archive.py`) — for INTERNAL knowledge only. **The archive's water is private water**: correspondence informs, it is never quoted on a public page.
5. **Images**: `findimg` first, BUT it answers content-type queries, not identity queries — also run `find /mnt/e -iname "*<borough>*" -o -iname "*<event>*"` (McAlmont was found by filename, not by caption). Provenance check EVERY image before use — a credited photo (@handle) is someone else's; Rob's portrait is not a crowd shot.
6. **The local curators' sites** — every borough has someone already curating (LGBT forum links page, council LGBT page, community org programme). Mine their directories BEFORE drafting; their post-dates reveal THEIR currency too. Bitten twice in one day skipping this.
7. **Web search** last, for what remains.

## 2 · NotebookLM deep dive (per borough)
`notebooklm create "Borough Deep Dive: <B> — Black Queer History & Community"` → `source add-research "<crafted borough query>" --mode deep --no-wait` → background agent: `research wait --import-all` → save `source list --json` to `~/blkout/projects/32-boroughs/research/<slug>-sources.json` → `generate report --format briefing-doc --append "<the borough-door instruction — see croydon example in research/>"` → download `<slug>-briefing.md`. The source JSONs hold the bibliography URLs. For sparse boroughs, instruct: *absence clearly stated is a finding*. Mine the briefing into history/bibliography/facts — it is secondary synthesis: **every claim that reaches the page verifies against primary sources at the currency check**.
⚠ **Attributes bleed between similar entities — verify claim by claim, not entity by entity.** Haringey's briefing said the Black Lesbian and Gay Centre published a *quarterly* magazine called *Blackout*; the quarterly was Joseph Beam's US *Black/Out*, a different publication of the same year. The entity was real, one adjacent attribute was imported from its near-twin. **And the local curator's own site can be wrong**: Haringey Vanguard's site calls the Bernie Grant Arts Centre "formerly Black Gay and Lesbian Centre" — the BLGC's permanent home was a Peckham railway arch and its plaque is in Southwark.

## 3 · Author the data file — copy an existing one; every rule lives in the data
- **Three rings**: `here` (in-borough, centring-gated) · `besideUs` (allies — exempt from centring, framed as neighbours) · `worthTheJourney` (centring-gated; choose STRATEGICALLY per borough — nearest Black-queer-centred first; never repeat one list everywhere). ⚠ **UK Black Pride was de-listed from every door on 31 Aug 2026 (Rob) — do not reinstate it as a ring entry.** Enfield still names Lady Phyll and UK Black Pride in its history note, quiz and bibliography: that is her biography and the borough's ancestral anchor, not a listing.
- **Every entry**: `centres` grade (`black-queer-men`/`black-lgbtq` render in destination rings; else skipped loudly) + `currencyChecked` (true only if verified TODAY — the floor has TWO axes: currency AND centring).
- **History note**: needs a TRUE ancestral anchor — a named person who grew up/worked there (Ivor: Croydon; Pearl + the Windrush labour exchange: Lambeth; Lady Phyll: Enfield). First sentence renders italic; split paragraphs with `\n\n`. Public record only; no unannounced dates; no false borough claims.
- **Quiz** only where facts are verified (its absence is honest data); 2–3 questions; reveals carry the stories; score lines in register and grounded in real things.
- **Services**: check SHL coverage — **Croydon, Sutton, Hillingdon, Hounslow, Greenwich opted out** (Croydon runs its own postal kits). SHL + 56 Dean Street + NHS finder for participating boroughs; add Black-led services (Black Psychotherapy, NAZ, BAATN) where near.
- **`neighbours`**: adjacency list. Drives both the pills and the borough map's neighbour outlines; both auto-link when a door's data file exists.
- **A concluded project belongs in `bibliography`, never a ring.** Haringey Vanguard ended Feb 2021; its archive lives on at Bruce Castle and the LMA. Listing a finished project as live fails the currency axis even though the work still matters.
- **`centres` vocabulary is fixed**: `black-queer-men` and `black-lgbtq` pass the destination gate (`here`, `worthTheJourney`). `black-men`, `lgbtq-general`, `black-general` render in `besideUs` only, which is exempt. Grade honestly — Black Thrive Haringey has no Black queer strand (unlike Lambeth's, which runs Queer Minds), so it is a neighbour, not a destination.
- **`retired` list**: dead orgs with end-year + source, so stale official pages can't resurrect them. Even the council's directory fails currency (2 of Croydon's 3 local listings were dead). **The curator is the technology** — Rob's ambient knowledge outperforms every scrape; show him early.
- **`archive` box** (standing, every door) + `gallery` (real BLKOUT events on that ground; consent recorded in `consentNote`; captions carry event + date; filing dates ≠ event dates).
- **Quiet states everywhere**: "checked <date>, nothing listed" in full typography. Never pad. Retired/resting/quiet are states, not failures.

## 4 · Landmark (the signature device)
Generate via **blkout-image-gen** (never raw tool calls): pencil-sketch prompt — cream/silver graphite linework on deep near-black, the borough's landmark (Rob picks it), and **"a completely PLAIN BLANK empty pale disc"** — in the building where it offers a circle (clock face → `--window mid`) else a full moon above (`--window top`) — "thin warm gold rim. No text, no words, no logos." Then `make-landmark.py` embeds the real white BLK OUT roundel (pencil-grain treated; NEVER an AI-generated logo) and keys the background transparent. `--threshold 70–90` for textured-ground sketches; `--disc cx,cy,d` when auto-detection merges the moon with other bright regions (clock faces, lit windows). **Measure the disc, do not eyeball it** — on Alexandra Palace auto-detection was 137 px off in x and 50% too large in diameter, because it merged the disc with the building's bright linework. Threshold the sketch at `lum>200`, take the rows/cols where that mask exceeds ~35% of its max, and read centre and diameter off those bounds. **Then check the result against the existing landmarks** rather than your eye: they sit at 66–83% fully transparent, 10–20% visible, mean-luminance-of-visible ≈ 85–110. Haringey landed at 76 / 13 / 110 with `--threshold 60`; `--moon-scale/--moon-rise` exist as repair tools but regenerating with "a SMALL distant moon, no larger than one-eighth of the image width, high in a top corner" is correct-by-construction. Wire as `d.landmark`.

## 5 · Build and verify — behaviour, not presence
- `node scripts/borough-doors/build-borough-doors.mjs <slug>`; read its warnings.
- **Capture end-to-end, once per new slug**: curl the page's exact anon REST insert to `event_interest` (slug `<slug>-door`) → confirm the `first_gestures` trigger row → DELETE both test rows (use a `@blkoutuk.invalid` address). The slug in the gesture string IS the borough tag.
- Render check: `python3 ~/.claude/skills/design-loop/render.py public/<slug>/index.html --width 1200`. Layout is flexbox-only because that engine has no CSS grid or `:has`.
  ⚠ **The render cannot see a large part of this template.** wkhtmltoimage has no `position:sticky`, unreliable `background-attachment:fixed`, and captures one static frame — so sticky headings, the locked photographic grounds, every scroll reveal, the dot fill, the count-up and the map animation all render as if absent. Use it to check layout, contrast and content; **say plainly which pixels were never rendered**, and get Rob to scroll a real browser for anything motion-dependent. Cheapest way to serve one: `python3 -m http.server 8788` in `public/`, then `http://localhost:8788/<slug>/`.

## 6 · Gates before deploy (all of them, every borough)
1. **Rob's copy nod** — history note, named people, quiz, captions.
2. **Currency check** the build-warning list (~12 months' activity; a live website is not a live organisation; ask-the-source annually once live).
3. **Consent** recorded in the data file for identifiable-person images.
4. Deploy drill per CLAUDE.md: clean `git status`, then content-length match on the real file, 6–10 consecutive requests (SPA shell lies).
   ⚠ **Measured on this app, before the Haringey deploy: two borough URLs both already returned `HTTP 200`, `text/html`, and a byte-identical 7,086 b — one of them for a page that did not exist yet.** Status code and content-type cannot distinguish a real door from the catch-all. Poll on the exact local byte count and nothing else.
   ⚠ `git status` clean also means **no render artefacts**: `design-loop/render.py` drops a multi-MB `index-render/` beside the page. Now gitignored in this repo; check it stayed out.
   ⚠ When editing an existing data file, **do not round-trip it through `json.dump`** — it reformats every compact object and buries a two-line change in a 400-line diff. Edit the text surgically and re-parse to confirm it is still valid JSON.
5. Acceptance test (intervention 4): the real query — "groups for Black gay men in <borough>" — against ChatGPT/Claude/Gemini, before and after.
6. **Open the door on the Discover gateway.** The map on `comms.blkoutuk.com/discover` is how people find the doors from the platform, and its borough list is **hardcoded** — a new door is invisible there until you add it.
   - File: `apps/comms-blkout/src/components/discover/BoroughDoorsWidget.tsx` → add `<slug>: '<Borough>'` to `OPEN_DOORS`.
   - Deliberately not a runtime fetch: a cross-origin call to events.blkoutuk.com just to render a menu fails worse than a stale list. The trade is one line per door.
   - Add the borough's name to the `boroughs` keyword list in `apps/comms-blkout/src/pages/discover/DiscoverPage.tsx` so search finds it.
   - The map geometry is **duplicated** at `apps/comms-blkout/src/data/boroughs-map.json`. If the geometry is ever regenerated, copy it to both.
   - ⚠ **Discover lives in comms-blkout, NOT community-platform** — that app's `discover` route is a hard redirect to comms. Editing it there builds a page nobody reaches.
   - ⚠ **A local `npm run build` in comms-blkout can fail on code that never reaches the deploy.** `src/socialsync-content-generation/` is **gitignored** (`.gitignore:36`, 0 tracked files), so it is absent from the repo, absent from the Docker build context, and `tsc -b` never sees it in CI — the app deploys fine regardless. It carried 12 TypeScript errors locally until 1 Sep 2026. **Before treating a local build failure as a blocker, check whether the failing paths are tracked** (`git ls-files <dir>`); an untracked directory cannot break a deploy.

## 7 · The template — adopted 31 Aug 2026

`build-borough-doors.mjs` is the renderer. Built as a parallel design, compared against the original, and **adopted on Rob's call** — it is now the door, not an experiment.

```
node scripts/borough-doors/build-borough-doors.mjs <slug> [<slug>…]   # named doors
node scripts/borough-doors/build-borough-doors.mjs --all              # every door
```

**All four doors were retrofitted onto it on 31 Aug 2026.** The superseded renderer is kept as `build-borough-doors-v1.mjs` for reference only.

⚠ **A bare run refuses and exits 1, by design** — name slugs or pass `--all` deliberately, so nobody reskins every live door by reflex.

### Swapping templates: prove parity before you ship, twice over

Retrofitting nearly dropped **five** things, none of which raised an error, because the new template had been written against one borough that happened not to use them. Both checks are needed — the first missed what the second caught:

1. **Diff the fields each renderer reads.** `set(re.findall(r'\bd\.(\w+)', src))` on old vs new. This caught `gallery` (4 consented photographs on Croydon, 6 on Lambeth) and the census comparison table.
2. **Diff the visible text of every built page against its committed output.** Strip tags, keep lines >25 chars, set-subtract. This caught what field-diffing could not: the `recently` strip, the whole **Places directory block** (which reads `scripts/places/places.json` — the same source as `/places`, and where the never-list gate lives), the "Run a room" bullet, the closing note, the events-calendar card, and copy I had silently reworded.

Then **probe the survivors positively** — a set-difference reports formatting as loss. v1 splits a history note's first sentence into `<em>` and prefixes list items with an em-dash, which changes text nodes without changing content. Substring-test the distinctive phrases and require 100%; assuming "that's just formatting" is how a real loss ships.

Grammar is scrollcraft's **typographic poster** (§2.5) — chosen because the reference site is type-as-architecture and because `findimg` found no BLKOUT photography of the borough, which is the case that grammar exists for. Registry rows already taken on this machine: split stage (`/movement`) and chaptered editorial (`enterprise-story`); check `FINGERPRINTS.md` before reusing either.

**What it carries beyond v1:** photographic grounds, gradient colour plates, sticky headings on the plain dark sections, an index menu (Derek Aidoo's note — vital sections should not be lost on one long page), a guess-the-census-figure interaction, and the section numerals stamped in document order.

**Rules this template earned the hard way — all of them cost a round trip:**
- **Do not hide content and rely on JS to show it.** `NodeList.forEach` does not exist in the render engine, so a throw left every section body permanently invisible with no error. Reveals are now armed *by* JS per element: if the script dies, nothing was ever hidden.
- **Stamp section numerals after assembly, not at construction.** Numbers assigned as each block is built follow evaluation order, not document order; they ran 01, 03…02 twice.
- **A pinned heading needs a background, and no background matches a gradient or a photograph.** Sticky headings therefore apply only to plain dark sections — never over `.gold`, `.invert` or `.has-bg`, where they paint a visible rectangle.
- **`overflow-x: hidden` on `body` silently disables `position: sticky` everywhere inside it.** Use `overflow-x: hidden; overflow-x: clip;` — clip does the same clipping without creating a scroll container.
- **Build texture from gradients with solid colour stops.** Low-alpha washes, SVG data URIs and inline `<svg>` all failed invisibly here: a double-escaped `%23` fill painted nothing, `.plate.gold > *` (two classes) outranked `svg.splash` and forced it into flow, and the old render engine will not position inline SVG at all. Gradients were the one mechanism that rendered everywhere.
- **The borough map is the Next door section's moment.** All 33 London boroughs from `data/_boroughs-map.json` — ONS Local Authority Districts (Dec 2023, generalised), projected to SVG once so builds never refetch. This borough gold, open doors clickable, the rest dark. **The OGL attribution line under it is not optional**: "Contains OS data © Crown copyright and database right 2025." To regenerate, re-query the ONS Open Geography Portal for `LAD23CD LIKE 'E09%'`, project equirectangular with a `cos(lat)` correction, and keep outer rings only.
- **Each door wears different photographs.** `GROUNDS` maps slug → a power frame for the history and a joy frame for the door; a borough with no entry gets a distinct pair from a hash of its slug. Four doors repeating the same two images looked like a template, which is what the design was meant to stop being.
- **One animated moment per section, and never a second one in the section that already carries the signature move.** The count section holds the masked figure, the guess and the dot fill; a staggered census table on top of it made that section busy while every other section sat still. Animation belongs where the motion means something — Next door holds it, in the map: the boroughs settle in, then this one takes the gold and its neighbours draw their edges, because that section is about opening doors one borough at a time. Ask what the motion *says* before adding it.
- **The census figure is a guess-first interaction** (Rob's idea): the number is masked until the visitor commits a guess, then resolves against it. Public census data only — nothing about the visitor is read, stored or sent. **Never display a per-borough count of members or contacts**; an earlier version lit a dot per signup and was cut for exactly that reason.
- **Photographic grounds come from `src/components/foundation/FoundationLayer.tsx`** — 33 curated images with an audited per-image anchor map (eyes first, hands if no eye line). Port the anchors; do not re-crop by guess. **Two sections per page, no more** (Rob, 31 Aug).
- Backticks inside the CSS block terminate the JS template literal. Twice.

## 8 · Tooling gotchas
- **Kie.ai image generation**: the skill's `generate.mjs` creates the task, then its polling step dies with `fetch failed` and exits **0**. The image is usually fine — take the `Task created: <id>` line from the output and fetch `https://api.kie.ai/api/v1/jobs/recordInfo?taskId=<id>` directly for the result URL. Gemini direct returned `RESOURCE_EXHAUSTED` (free tier, `limit: 0`).
- **`notebooklm source list` returning empty is a false negative** — the API shape changed and the wrapper swallows it. Read `research status --json` and count `sources` instead. It reported 0 while 70 were attached.
- **`grep` is line-based**, so it cannot see multi-line CSS rules or JSON objects. Twice it reported a rule missing that was present. Parse with Python when checking whether a rule exists.

## Register (the door's voice)
Men first, professionals second (`#working-with-us` is the anchor registry emails point at). Warm door, not civic directory: "Come as you are. We answer." Creation not deficit. The one-story-outward discipline: no internal metaphor stack in page copy. Fun (quiz) · useful (rings, services, census) · reciprocal ("Make it truer" — corrections credited; the page's own history proves it works).
