---
name: board-game-rules-writing
description: >-
  Write, structure, test, and maintain board game rulebooks and game text. Covers rulebook anatomy
  (Stegmaier order: overview & goal, components, setup, gameplay, endgame, index), teach-order
  principle, second-person active voice, terminology discipline (one term per concept, keyword lists,
  style guides), learning-vs-reference documents (Root dual-document model), examples of play,
  first-turn scripts, quick-start guides, player aids, iconography standards, card/board information
  hierarchy, readability specs, edge-case and timing rules (golden rules, APNAP), rulebook
  blind-testing, localization-ready writing, living FAQ/errata. Triggers: "write a rulebook", "how do
  I explain my game", "rulebook template", "player aid", "icon guide", "quick start", "glossary",
  "FAQ/errata", "localize my rulebook", or "blind rules test". For playtest protocols/recruitment use
  board-game-playtesting; for colorblind palettes/access audits use board-game-accessibility; for
  booklet print specs use board-game-manufacturing.
---

# Board Game Rules Writing

The rulebook is the only component guaranteed to reach every table — players will not research your game online (Jaffee), and "you're not going to come in the box" (Selinker). Write it as a product, test it like the game, maintain it after launch.

## When to use / when not to use

Use for:
- Drafting, restructuring, or reviewing a rulebook, quick-start guide, player aid, or glossary
- Choosing document architecture (single book vs. learn-to-play + reference split)
- Terminology/style audits: ambiguous phrasing, inconsistent terms, undefined words
- Card/board text and icon hierarchy; icon legend design
- Edge-case and timing rules (precedence, "can't beats can", simultaneous effects)
- Preparing text for localization; setting up FAQ/errata after release
- Blind-testing a rulebook as a document

Not for (route there instead):
- Running playtest sessions, recruitment, feedback instruments, kill criteria → `board-game-playtesting`
- Colorblind-safe palettes, double-coding audits, cognitive/physical access → `board-game-accessibility`
- Booklet print file prep, paper/binding quotes, page-count imposition → `board-game-manufacturing`
- Whether a rule should exist at all (depth vs. complexity) → `board-game-design-theory`
- Naming, flavor text voice, worldbuilding → `board-game-theme-narrative`

## Core principles

1. **Serve three audiences** (Chris Backe, 2023): the first-time learner (tutorial), the current player mid-game (reference lookup), and the returning player (reminders). One document can serve all three only if its anatomy separates learning order from lookup order.
2. **Mirror the verbal teach.** Christian Strain's teach order (League of Gamemakers, 2014): name components while unboxing → theme in 1–2 sentences ("why am I doing this") → win condition + how the game ends, one sentence each → what happens *on your turn*, from the player's perspective, detail revealed as it becomes relevant. Rulebook section order = this order.
3. **Fixed anatomy** (Stegmaier, verified 2025): *overview & goal → components → setup → gameplay overview → detailed gameplay → other info → end of game*. Reserve the last page for icon guide, game-flow summary, and/or index (a front table of contents can replace the index).
4. **Talk to one player**: second person ("you"), active voice, present tense — "Pay $1 to gain 2 resources," never "The player pays…" (Stegmaier). Singular "they" if third person is unavoidable.
5. **One term per concept, defined before first use.** Jonathan Tweet: "Things are the same, or they are different." Keep a keyword list; never rename (no "hexes" becoming "squares"). Better repetitive than confusing.
6. **Length signals complexity.** Offload sub-rules to player aids and card text (Stegmaier extracted Tokaido Duo's character rules into player aids). A minor concept needing a full page → the concept is too complex for its contribution. The word "exception" → 99% of the time a rule to remove from the game, not the book.
7. **Repeat binding constraints where players look them up.** A livestreamed *Lanterns* player read only the detailed action text and missed the "once per turn" limit stated only in the overview (Randy Hoyt). Restate limits inside each detailed entry.
8. **An image of every component; an example per non-obvious rule.** Illustrate gameplay *situations*, not isolated rules (Unpub). Highlight flow-breaking rules the way *Ticket to Ride* highlights its wild-draw exception.
9. **Timing is rules text, not vibes.** State precedence explicitly: card text > rulebook; "can't" beats "can"; active player decides unresolved order (MTG Comprehensive Rules 101; Law of Root §1). "At start of phase" precedes everything in the phase; "at end of" follows everything.
10. **Ship-gate = blind test from the document alone** (Selinker: final version playtested by strangers from the rules; "if they screw it up, you don't have a final version anymore"). Stegmaier: ~25% of blind playtesting's value is rulebook improvement. A missed rule is a rulebook bug even if it's "clear as day."
11. **Write once, publish in many languages.** Short sentences, no idioms, no jokes that only work in English, editable master text, per-language terminology glossary (Geeky Pen).
12. **The rulebook is a living document.** Version/date every file. Post-release: per-game Rules & FAQ page, dated errata, migrate FAQ answers into the next printing's proper sections (Tom Jolly; Leder Games' dated *Law of Root* revisions).

## How to apply it

### A. Draft the skeleton (learning layer)

1. Front matter, page 1: player count, time, age, one-line pitch, theme in 1–2 sentences, **win condition stated up front**.
2. Components: photo/diagram of *every* component, labeled — doubles as a missing-parts check.
3. Setup: numbered order-of-operations steps + labeled diagram. State explicitly: face-up/face-down, public/secret information, first-player rule (even "choose randomly").
4. **"How to start"**: state the kick-off in one sentence. (A group read every page of *Shadows Over Camelot* aloud and still asked "how do we start?" — Law of Game Design.)
5. Gameplay overview: turn/round structure on one page, with a mnemonic if the structure allows it (*Dominion*'s ABC: Action, Buy, Clean-up).
6. Detailed gameplay: one headed section per action/phase, terms defined before first use, binding constraints repeated inside each entry.
7. End of game: trigger, scoring, tiebreakers — in that order.
8. Back matter: icon legend, game-flow summary, glossary, index/TOC, version + date, credits.

Full annotated skeleton with per-section instructions: load `references/rulebook-template.md`.

### B. Build the reference layer

1. Choose architecture: weight ≤ ~8–12 pages → single book. Heavy/asymmetric games → dual documents: conversational *Learning to Play* + formal *Law of Root*-style reference (numbered decimal sections, Golden Rules first, appendices, index). State precedence: "If the Learning to Play guide conflicts with the Law, follow the Law."
2. Reference sections get numbered headings (1.0, 1.1, 1.1.1) so players can cite and search; learning sections get narrative flow.
3. Put Golden Rules on page 1 of the reference: (a) component text that contradicts rules wins, for that case only; (b) "cannot" is absolute; (c) ignore impossible instruction parts; (d) simultaneous choices resolve active-player-first, then in turn order (APNAP).
4. Add a **first-turn script**: a literal walkthrough of Turn 1 ("You have 5 cards and 2 coins. Do this."). For heavy games, add a quick-start page or a teach-the-teacher page (*Asking for Trobils* reprint added a full page teaching *the explainer*).
5. Seed the FAQ from playtest questions; label every edge case with a searchable header.

### C. Terminology & style pass (run on every draft)

- [ ] Every game term appears on the keyword list; one term per concept, one concept per term; defined at first use, **bolded at first instance only** (Sen-Foong Lim compromise — capitalization of terms is [contested]: Selinker/Jaffee lowercase, others capitalize; pick one convention and write it in the style guide).
- [ ] Second person, active voice, present tense throughout; no "the player" in instructional text.
- [ ] Zero instances of "should"; every "except" and "remember" flagged as a design smell (Stonemaier Style Guide: exceptions should be designed out; "remember" means the interface failed).
- [ ] Numbered lists only for sequential steps; bullets only when order doesn't matter.
- [ ] Numerals for numbers (except at sentence start); serial comma; acronyms spelled out once; "gain" not "take" from the supply; "mat" = one player's, "board" = shared.
- [ ] Read-aloud test: any sentence you can't speak in one breath gets split (Selinker's "take a breath" — a 1984 *Axis & Allies* mega-sentence was rewritten to <147 words).
- [ ] Ambiguity grep: "either…or" (inclusive?), "in order to" (sequence vs. purpose — *Lords of Vegas* post-release confusion), "another/the other" with >2 players, undefined "hand/deck/discard" for non-hobby readers.

### D. Readability & information hierarchy pass

- [ ] Body text ≥10 pt on high-contrast background (practitioner template: 16 pt bold heads / 12 pt sub-heads / 10 pt body; the "~9–10 pt minimum" folklore is [contested] — go larger, never smaller).
- [ ] Contrast ≥ 4.5:1 for body text, ≥ 3:1 for large text and meaningful icons (WCAG 2.1, applied to print); no critical text on busy art.
- [ ] Legible body font (Calibri/Arial class); thematic fonts only for headings, never body.
- [ ] Card anatomy (Joseph Z. Chen, 2017): name top and largest; **cost top-left for hand cards** (visible when fanned); **cost bottom edge for market/display cards** (*Dominion* — cost is irrelevant once in hand); tableau-game effect text readable from across the table; card type by color **and** icon/label.
- [ ] Icons: double-code color + shape/text; rotationally readable; if the game needs 10+ icons, add a full icon legend on the rulebook's last page and on player aids.

Deep standards: load `references/iconography.md`.

### E. Test the document

1. **Mid-development**: designer-present rulebook playtest — testers read the book aloud, you stay silent and log every stumble (catches rules problems while the mechanical test still runs — Law of Game Design).
2. **Pre-print**: blind playtest — complete prototype + printed rules to people who have never played; success = learning unaided. Log every question; each is a rulebook bug report or an FAQ candidate.
3. **Lookup-speed test** (Stegmaier's pre-production test): hand testers a list of mid-game questions; measure how *fast* they find answers. Slow = fix headings, index, or redundancy, not the rule text.
4. **Backwards proofread**: read the book last page to first (breaks narrative blindness). ≥2 external proofreaders; paid editor recommended ($25–50/hr, veterans >$100 [contested — informal poll]).

### F. Ship & maintain

- Version + date on every rulebook file and PDF.
- No FAQ in a first printing — a FAQ at launch means unfixed rules (Jolly). FAQs are for genuinely frequent questions discovered *after* publication.
- Post-release: per-game Rules & FAQ page + BoardGameGeek FAQ upload; dated living-rulebook revisions (GMT/Leder model); migrate every FAQ answer into the section where players look, at next printing.
- Localization handoff: freeze development first, edit the English source before translating, deliver an editable master (Google Docs, not PDF/InDesign-only) + a glossary spreadsheet with one column per language + CAT-tool translation memory for expansions.

Localization checklist and living-FAQ operations: load `references/style-localization-faq.md`.

## Key numbers & heuristics

| Claim | Value | Source |
|---|---|---|
| Rulebook section order | overview & goal → components → setup → gameplay overview → detailed gameplay → other info → end of game; last page = icon guide/flow/index | Stegmaier, "What Makes a Great Rulebook?" (2025, verified) |
| Preferred trim size | 180×240 mm — fits rules + examples, stays on the table | Stegmaier (2025) |
| Blind playtesting's purpose | ~25% is rulebook improvement | Stegmaier (2025) |
| "Exception" heuristic | 99% of exceptions should be removed from gameplay | Stegmaier (2025) |
| Minor-concept page test | Full page for a minor concept → too complex for its contribution | Stegmaier (2025) |
| Booklet page count | Saddle stitch: multiple of 4, 8–64 pages; perfect bound: even page count, 28+ pages; typical rulebook 4–16 pages; default 70 lb gloss text; sizes 5.5×8.5″, 6×9″, 8.5×11″, A5, A4, or custom | PrintNinja (verified) |
| Body text size | ≥10 pt; heads 16 pt / sub-heads 12 pt | Meeple Mountain practitioner template; "9–10 pt minimum" [contested] |
| Contrast | 4.5:1 body, 3:1 large text & meaningful graphics | WCAG 2.1 (applied to print) |
| Color-vision deficiency | 8% of men, 0.5% of women (~4.5% of players) → never encode by color alone | Colour Blind Awareness |
| Icon legend threshold | 10+ icons → full legend + appendix | Meeple Mountain |
| Theme intro length | 1–2 sentences | Strain, League of Gamemakers (2014) |
| Precedence defaults | card text > rulebook; "can't" > "can"; impossible parts ignored; simultaneous = active player first (APNAP) | MTG Comprehensive Rules 101.1–101.4; Law of Root §1 |
| Readability target | Flesch-Kincaid grade = 0.39×(words/sentence) + 11.8×(syllables/word) − 15.59; aim middle-grade | Selinker, *Kobold Guide to Board Game Design* (2011) |
| Editor rates | ~$25–50/hr; veterans >$100/hr | Meeple Mountain informal poll [contested] |
| Re-translation overrun | ~30% anecdotal if translated before development freeze | Geeky Pen [contested] |

## Common pitfalls

- **Reference-manual-only syndrome** — precise, exhaustive, unteachable; no learn-order (Jaffee's VCR-manual analogy). Fix: dual documents or the 3-part anti-front-loading split (goal ≤1 page → minimum rules for Turn 1, 2–3 pages → full random-access reference).
- **Front-loading** — everything explained before the player may act; produces the "designated rules reader" workaround and abandoned rulebooks.
- **Terms used before defined** (Jolly) and **two terms/one concept** ("pawn" vs. "token" — pick one, search-replace the loser).
- **Buried setup exceptions** — setup exceptions scattered in later chapters; keep all setup facts in Setup, cross-reference elsewhere.
- **Buried constraints** — stated once in an overview, absent where looked up (*Lanterns*). Repeat inside each detailed entry.
- **Ambiguous "you"** — in 2+ player effects, "you" vs. "each player" vs. "target player" must be mechanically distinct every time.
- **Unwriteable rules kept** — if you can't write it clearly, redesign it (Selinker's *Dead Ringers*: MTG rewrote the card's text repeatedly to make it printable rather than cut it — and still shipped one of the most famously convoluted card texts ever printed).
- **Fiddly corner rules** — a rule covering one card or a rare corner: cut the rule or fix the component (Jolly).
- **Icon soup** — icons needing deciphering; *Bang!*'s "book icon = go read the rulebook" anti-pattern; Selinker's *Gloria Mundi* lesson: one symbol cannot do the work of ten — prefer text + localization over icon-only design.
- **Over-emphasis** — all-caps/bold everywhere destroys hierarchy (*Magic Realm*); bold first instances only.
- **Missing kick-off** — no explicit "how to start" (*Shadows Over Camelot* anecdote).
- **Assuming hobby literacy** — undefined "hand," "deck," "worker placement" (Unpub).
- **Color-only coding** and **non-rotational icon codes** (ColorADD: blue/red differ only by rotation — fails for upside-down cards).
- **Premature FAQ** in a first printing = shipping known-unfixed rules (Jolly).
- **Translating before development freeze**; PDF-only source text; no glossary (Geeky Pen).

## Reference files

- `references/rulebook-template.md` — Load when drafting or restructuring a rulebook, quick-start, or first-turn script. Annotated section-by-section skeleton with instructions, setup checklist, timing/golden-rules block, and exemplar citations.
- `references/iconography.md` — Load when designing icons, card layouts, player aids, or visual hierarchy. Icon standards, double-coding rules, card anatomy by card type, readability specs, exemplars and anti-exemplars.
- `references/style-localization-faq.md` — Load for the full style-guide table, precision-writing maxims (Selinker, ekted), localization-ready writing and handoff checklist, and living FAQ/errata operations.

## Related skills

- `board-game-design-theory` — whether a rule earns its complexity; depth vs. rules weight; idea critique
- `board-game-playtesting` — session protocols, blind-test recruitment, feedback instruments, kill criteria
- `board-game-accessibility` — colorblind palettes, double-coding audits, cognitive/physical/vision access, language independence
- `board-game-manufacturing` — booklet print specs, imposition, binding, quotes
- `board-game-prototyping` — building the test copies the rulebook ships with
- `board-game-theme-narrative` — flavor text voice, naming, worldbuilding on cards
- `board-game-crowdfunding` — campaign-page rules downloads and preview PDFs
- `board-game-solo-coop-design` — automa rulebooks and AI-opponent instructions
