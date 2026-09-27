# Research Digest: Rulebook Writing & Game Communication

## Core frameworks & models

- **Stegmaier rulebook template** — Jamey Stegmaier, Stonemaier Games ("What Makes a Great Rulebook?", Nov 2025). Fixed order: *overview & goal → components → setup → gameplay overview → detailed gameplay → other info → end of game*; last page for icon guide, game flow, and/or index (a front TOC can replace the index). Rulebook length should signal game complexity — offload sub-rules to player aids. Habits: player aids (not a rulebook) during early playtesting; rulebook written only approaching blind playtesting; review the book backwards; written style guide; pre-production test = how *quickly* you can find answers.
- **Teach order / "start with the end"** — Christian Strain (League of Gamemakers, 2014): (1) control the table; name components while unboxing; (2) theme in 1–2 sentences (answers "why am I doing this"); (3) win condition + how the game ends, one sentence each; (4) what happens *on your turn*, from the player's perspective, revealing detail as it becomes relevant. Rulebook should mirror this verbal order (consensus: Pixy, Unpub, Backe).
- **Three audiences of a rulebook** — Chris Backe (2023): first-time player (learns), current players (look up), returning player (reminders). Drives the tutorial-vs-reference duality.
- **Dual-document model** — Leder Games' *Root*: *Learning to Play* (conversational, graphical) vs *The Law of Root* (formal reference: numbered decimal sections, Golden Rules first, Key Concepts, appendices, glossary, index; precedence: "If the Learning to Play guide conflicts with the Law, follow the Law"). Stegmaier praises *Dawn of the Zeds* for multiple rulebooks.
- **Diátaxis** — Daniele Procida (diataxis.fr; linked by Stegmaier). Documentation splits into tutorials / how-to guides / reference / explanation — a model for separating learn-to-play, quick-start, reference, and FAQ.
- **Golden-rules family (precedence & timing)** —
  - *MTG Comprehensive Rules*: 101.1 card text that contradicts the rules takes precedence (that situation only); 101.2 "can't" beats "can"; 101.3 impossible instruction parts ignored; 101.4 simultaneous choices resolve in **APNAP** order (active player, then non-actives in turn order).
  - *FFG / Android: Netrunner* "Golden Rule": "If the text of a card directly conflicts with the rules in this book, the card text takes precedence"; plus "Timing Priority" — turn player acts first in an order of their choosing, players alternate until one declines.
  - *Law of Root* §1: card > Law; Law > Learning guide; faction/hireling rule beats general rule; "cannot" is absolute; unclear order or decision-maker → the player taking their turn chooses.
- **Selinker's "Writing Precise Rules" maxims** — *Kobold Guide to Board Game Design* (2011): (1) no intermediary terminology (don't rename hexes "squares"); (2) real words, never varied once chosen (Jonathan Tweet: "Things are the same, or they are different"); (3) no more work than necessary (an RPG rule made you roll twice to compute a 50.5% coin flip — say "50%," roll once); (4) flavor, but sparingly; (5) text no smarter than the reader (Flesch-Kincaid: grade = 0.39×words/sentence + 11.8×syllables/word − 15.59; a *De Bellis Antiquitatis* paragraph scores 13.22); (6) discard rules that can't be written (MTG's *Dead Ringers*); (7) "take a breath" — short headed sections (a 1984 *Axis & Allies* mega-sentence rewritten to <147 words); (8) go easy on the eyes — minimize caps/bold; (9) hire professional editors; (10) final version playtested by strangers from the rules alone ("if they screw it up, you don't have a final version anymore").
- **Meeple Centred Design / TTAG** — Michael Heron et al. (*The Computer Games Journal*, 2018; TTAG books): heuristic toolkit spanning visual, cognitive, emotional, physical, communication, socioeconomic accessibility; TTAG book contains Daniel Solis's "Iconography" chapter.
- **Second-person direct address** — strong consensus (Stegmaier, Jaffee, Pixy, Unpub, Backe): "On your turn, choose…", never "the player…". Active voice, present tense, singular "they" when third person is unavoidable.

## Catalog / techniques

**Structure & anatomy**
- Pixy Games' 15-part layout (2016) and Meeple Mountain's 14-element list (Gary, 2021) converge on the anatomy in the checklist below; Meeple Mountain adds: a "how to read components" section; typical-turn section as the most-read (make it detailed); special/out-of-turn actions; FAQ seeded from playtest questions; **version/date on the document**.
- Neutronium (2026) three-part anti-front-loading model: Part 1 goal & win condition (≤1 page); Part 2 minimum rules to complete Turn 1 (2–3 pages); Part 3 full reference formatted for random access (searchable headers, labeled edge cases).
- Explicit "how to start" (Law of Game Design, 2014): a group read every page of *Shadows Over Camelot* aloud and still asked "how do we start?" — state the kick-off. Teach-the-teacher page: *Asking for Trobils* reprint added a full page that is a quick-start guide *for explaining the game*, not for playing it.

**Terminology & style discipline**
- Stonemaier Style Guide (public, 2019): serial comma; hyphenate modifiers; numerals whenever possible (not at sentence start); numbered lists only for sequential steps; cross-references as "(see Gameplay)"; bold = terms, italics = examples/notes, never underline; remove all "should"; flag every "except"/"remember" as a design cue (exceptions should be designed out; "remember" means the interface failed); "gain" not "take" from supply; "mat" = unique to a player, "board" = shared; acronyms spelled out once; bracketed notes to the graphic designer.
- Capitalization is contested: Selinker lowercases most terms; Jaffee avoids capitalizing game terms; Sen-Foong Lim's compromise — **bold a key term at first instance only**. All agree: pick a convention, write it down, apply uniformly.
- Glossary/keyword discipline: draft the glossary even if unprinted — it forces one-term-per-concept ("pawn" vs "token": pick one, search-replace; "better repetitive than confusing" — Meeple Mountain). Unpub "Rulebook Building 101": keep a keyword list, define once, apply with 100% consistency ("action" vs "activation" slips get noticed).
- ekted's *Gamer's Mind* series (2010): (1) **induction** — replace tables with base+modifier rules; (2) **under/over-specification** — exceptions imply things; a redundant-looking exception makes readers hunt for nonexistent meaning; (3) **sequence hierarchy** — turn/round/phase defined precisely, with explicit sub-phases ("before combat"); (4) **word precision** — "either"/"or" are ambiguous; rules need code-level explicitness.

**Examples, scripts, aids**
- Images everywhere (Jaffee, Pixy): picture every component; an example per non-obvious section; highlight flow-breaking rules (*Ticket to Ride*'s wild draw); *Glory to Rome* praised for card-interaction examples; *Dominion*'s ABC mnemonic.
- Randy Hoyt (Foxtrot, on LoG): rulebooks serve as tutorial *and* reference — a livestreamed *Lanterns* player read only the detailed action text and missed the "once per turn" limit in the overview; fix = repeat constraints inside each detailed entry ("First, **once** per turn, …").
- Player-aid design (Board Game Business top-5): #5 no walls of text; #4 one double-sided card; #3 white space; #2 visually distinct; #1 use symbols (with legend). Stegmaier: prefer text on cards over icon combos; overflow goes to an appendix (Apiary) or component backs (Tokaido).
- Unpub: illustrate *gameplay situations*, not single rules in isolation; stage photos with the prototype; middle-grade reading level; read-aloud test for nested clauses.

**Iconography & visual hierarchy**
- Card anatomy (Joseph Z. Chen, "Anatomy of a Card", 2017): name top & largest; art center; **cost top-left for hand cards** (most visible when fanned); **cost bottom edge for market/display cards** (*Dominion* — cost is irrelevant once in hand, thumbs cover the bottom); effect text readable *from across the table* in tableau games; card type signaled by color **and** icon/label (colorblind). MTG's top-right mana cost is the notable outlier (Future Sight tested a left-edge cost).
- **Double-coding** (Brian Chandler, Colorblind Games): pair color with shape/pattern/text on all components. Exemplars: *Tussie Mussie* (background patterns), *The Isle of Cats* (ear/tail feature shapes), *Fantastic Factories* (symbol+color). ColorADD (UNO, Sea Salt & Paper) criticized: not intuitive (rote memorization), **not rotationally symmetrical** (blue/red differ only by rotation — fails for upside-down cards), proprietary. ArtiSlime quadruple-codes: color + component-color icons + written name + Venn-diagram dot. Stegmaier: last-page icon guide; icons should need no appendix.

**Readability & manufacturing**
- PrintNinja standards: saddle-stitched page counts **must be multiples of 4**; sizes track the box (tuck 2.5″×3.5″; standard box → 6″×9″/8″×8″; large → 8.5″×11″); 70–80 lb gloss text standard; 80–100 lb matte for 20+ page books; format ladder: folded sheet, accordion (4–8 panels), saddle-stitched, perfect-bound (48+ pp), box lid/extra cards for trivial rules.
- Stegmaier's preferred trim: **180×240 mm** — big enough for rules/visuals/examples, small enough to stay on the table during play.
- Avoid thematic fonts for body text (Meeple Mountain, Unpub); legible faces (Calibri/Arial cited).

**Process**
- Stegmaier oversight pipeline: blind playtesters (rulebook alone surfaces clarity failures) → data analyst → Automa team → cultural consulting → copyeditors (style guide) → typeset → proofreaders; ~10 reviewers with full access to all file versions at all stages.
- Blind playtest definition (Meeple Mountain): complete prototype + rules to testers who have *never* played; success = learning from the rules unaided. Law of Game Design: run a designer-present read-the-rulebook playtest *mid-development* (catches rules problems while rescuing the mechanical test); full blind tests come later. Stegmaier: a missed rule is a rulebook bug even if "clear as day." Review by reading the book backwards; multiple external proofreaders; paid editor recommended (Meeple Mountain, Selinker).

**Localization-ready writing**
- Geeky Pen (localization agency): (1) finish development *before* translating (re-translation compounds; anecdotal 30% overrun); (2) edit the source rulebook first — translators aren't rules editors; errors multiply across languages; (3) terminology glossary as a spreadsheet, one column per language; (4) master text editable (Google Docs) — PDF/InDesign-only sources can cost a week of manual table creation; (5) CAT tools (translation memory) keep expansions consistent. Kobold Guide: language-independent components enable multi-language rulebooks; Selinker's *Gloria Mundi* symbol-translation failure ("one symbol cannot do the work of ten") — favor text + localization over icon-only design.

**Living FAQ / errata**
- Tom Jolly (LoG): FAQs belong *after* publication, for genuinely frequent questions and actual errors — never ship a new game with one; on 2nd printing, migrate answers into the sections where players look; distribute living FAQs via BoardGameGeek.
- Leder Games: dated *Law of Root* revisions (2022 → 2024 → 2025) plus an interactive rules site (rules.ledergames.com) — the living-reference model inherited from wargame "living rules" (GMT). Stegmaier: per-game "Rules & FAQ" pages; blind-playtest questions feed FAQ content.

## Numbers, heuristics & rules of thumb

- **180×240 mm** rulebook trim (Stegmaier).
- Blind playtesting ≈ **25%** about improving the rulebook (Stegmaier).
- "**Exception**" in rules → **99%** of the time a sign the rule should be removed from gameplay (Stegmaier).
- A minor concept needing a **full page** → too complex for its contribution (Stegmaier).
- Fonts: one practitioner uses 16 pt bold heads / 12 pt sub-heads / **10 pt body** (Meeple Mountain). The oft-repeated "~9–10 pt minimum body text" claim is **weakly sourced [contested]** — no manufacturer or accessibility source states it; go larger.
- **WCAG contrast ratios** (web standard commonly applied to print): 4.5:1 body text; 3:1 large text (≥18 pt / 14 pt bold); 3:1 for UI components/meaningful graphics.
- Color vision deficiency: **1 in 12 men (8%), 1 in 200 women (0.5%)**, ~4.5% of population, ~300 M people worldwide (Colour Blind Awareness) → never encode by color alone; icons rotationally readable.
- **10+ icons** → full icon legend/appendix (Meeple Mountain).
- Rulebook editors: roughly **$25–50/hour**; veterans >$100/hour (Meeple Mountain informal poll).
- Law of Root timing clarity: "at start of phase" precedes everything in the phase; "at end of" follows everything; simultaneous win triggers → current-turn player wins; no interrupts unless a rule explicitly allows.
- "Players dread reading rulebooks / most groups appoint a designated rules reader" (Neutronium) — widely echoed but **uncited [contested]**; Jaffee's verifiable version: few players will research rules online, so the rulebook is the only guaranteed interface.

## Best-practice checklists

**Skeleton (Stegmaier + Pixy + Meeple Mountain)**
1. Front matter: player count, time, age, one-line pitch, 1–2 sentence theme, **win condition up front**.
2. Component inventory with photos of every component (doubles as missing-parts check).
3. Setup: order-of-operations steps; labeled diagram; explicit face-up/face-down, public/secret info, first-player rule (even "choose randomly").
4. Gameplay overview (turn/round structure, mnemonics), then detailed gameplay; terms defined before first use; binding constraints repeated inside each detailed entry (Lanterns lesson).
5. Explicit "how to start"; annotated example turn for non-obvious interactions.
6. End of game, scoring, tiebreakers.
7. Back matter: icon legend, game-flow summary, glossary, index/TOC, version date, credits.
8. Heavy games: split learn-to-play vs reference documents (Root model); consider a teach-the-teacher page.

**Style pass**
- Second person, active voice, present tense; one term per concept (keyword list + written style guide); bold key terms at first instance only.
- Short sentences; numbered lists for sequences; no "should"; flag "except"/"remember" as design smells; an example per non-obvious rule; image of every component; read-aloud test; backwards proofread; ≥2 external proofreaders, ideally a paid editor ($25–50/hr).

**Accessibility & usability pass**
- Double-code all color-dependent information; icons readable at any rotation; low icon count with a legend; body ≥10 pt on high-contrast backgrounds (target 4.5:1); no critical text on busy art; legible body font; hand-visibility test for card-cost placement.
- Player aids: ideally one per player, max one double-sided card, white space, no walls of text, turn summary + icon glossary.

**Testing & maintenance**
- Mid-development: designer-present rulebook playtest; pre-print: blind playtest from the printed rules alone; log every question → FAQ/errata candidates; PPC lookup-speed test.
- Post-release: per-game Rules & FAQ page; dated living-rulebook/errata PDFs; BGG FAQ distribution; migrate FAQ answers into the next printing's proper sections.
- Localization: freeze development first; edit English source; per-language glossary spreadsheet; editable master text; CAT tool with translation memory.

## Common pitfalls & failure modes

- **Reference-manual-only syndrome**: precise but unreadable, no teach order (Jaffee's VCR-manual analogy). **Front-loading**: everything explained before the player can act; produces the "designated rules reader" workaround (Neutronium).
- **Terms used before defined** (Jolly); **two terms/one concept** or **one term/two concepts** (Afrika Korps "squares"; Tweet's maxim).
- **Buried constraints**: stated once in an overview, absent where players look them up (Lanterns). **Ambiguous phrasing**: "in order to" read as "in sequence" (*Lords of Vegas* post-release confusion); "either"/"or" inclusivity (ekted); "should" implying optionality.
- **Unwriteable rules kept in the game** (Dead Ringers): if you can't explain it, redesign it (Selinker; Pixy: hard to explain = hard to understand).
- **Fiddly rules** covering one card or rare corners — cut the rule or fix the component (Jolly; Stegmaier's exception heuristic). **Premature FAQ** in a first printing = unfixed rules (Jolly).
- **Icon soup**: icons needing deciphering; *Bang!*'s "book icon = see rulebook" anti-pattern; *Race for the Galaxy*'s symbol system criticized by Selinker. **Over-emphasis**: all-caps/bold-everything destroys hierarchy (*Magic Realm*); capitalization creep (Jaffee).
- **Walls of text** (Selinker's "take a breath"); **missing kick-off** (Shadows Over Camelot anecdote); **assuming hobby literacy** (undefined "hand," "deck," "worker placement" — Unpub).
- **Color-only coding**; non-rotational icon codes (ColorADD); text on busy art; thematic body fonts; small text read at distance (*Hanabi* teardown).
- **Translating before development is finished**; PDF-only source text; no glossary (Geeky Pen).

## Canonical sources

**Books**
- *The Kobold Guide to Board Game Design* — ed. Mike Selinker (2011): "Writing Precise Rules" chapter; "Design Intuitively" (need the rulebook as little as possible).
- *Tabletop Game Accessibility: Meeple Centred Design* — Heron et al. (CRC Press); includes Solis's "Iconography" chapter.
- *Building Blocks of Tabletop Game Design* — Engelstein & Shalev (2019): shared mechanism vocabulary.

**Blogs & articles**
- Stonemaier Games: "What Makes a Great Rulebook?"; "The Stonemaier Games Style Guide"; "Proofreading and Product Oversight Process (2021)" — stonemaiergames.com.
- League of Gamemakers (leagueofgamemakers.com/tag/writing-rulebooks/): Jaffee "Following Rules Is Hard, Writing Rules Is Harder"; Hoyt "Watching People Use Your Rulebook"; Jolly "FAQs, Fiddliness, Redundancy, and Hierarchy"; Strain "Teaching a Game"; Vaughan "Take the Trobil to Teach Your Game Right".
- Board Game Design Lab: boardgamedesignlab.com/rules/ (hub); podcast episodes with Stegmaier, Dustin Schwartz, Mike Lee, Jason Perez, Morten Pederson.
- Pixy Games: "How to Write a Board Game Rule Book" (pixygamesuk.blogspot.com, 2016).
- Law of Game Design (lawofgamedesign.com): "Why You Should Write Your Rules Early" (origin of the Selinker quote "you're not going to come in the box"); "Playtest from the Rulebook"; "Include 'How to Start' in Your Rules".
- Also: Gamer's Mind (ekted.blogspot.com) Rules 1–4; Unpub "Rulebook Building 101" (Dustin Schwartz, Google Doc); Joseph Z. Chen "Anatomy of a Card" (Medium, 2017); Colorblind Games (colorblindgames.com); Meeple Like Us teardowns + TTAG portal (meeplelikeus.co.uk); Meeple Mountain "Top Six Rules for Rulebook Writing" (2021); Neutronium (2026) [some claims unsourced]; Entro Games (Backe, 2023); Diátaxis (diataxis.fr).

**Manufacturer / publisher resources**
- PrintNinja "Instructions and Rule Booklets" standards; Panda GM Design Guidebook; Leder Games resources + rules.ledergames.com; Magic Comprehensive Rules §101; Android: Netrunner core rules (FFG) & Null Signal comprehensive rules; GMT "living rules" PDFs; Geeky Pen (geekypen.com); Colour Blind Awareness (CVD stats); WCAG 2.1 (contrast).

**Communities & exemplars**
- BoardGameGeek: per-game rules forums, FAQ uploads, threads "Best/worst written rulebooks" (#2981281) and "In praise of excellent rulebooks" (#3328162).
- Praised rulebooks to study: *Root*/*Arcs* (dual documents; Arcs' welcoming tone), *Jaws of the Lion* (tutorial), *Dungeon Lords* (humor), *Barcelona* (history), *Galactic Cruise* (organization), *Dawn of the Zeds* (multiple rulebooks), *Origin Story* (audience awareness) — Stegmaier's list; plus *Splendor* (4-page rulebook), *Belfort* (diagrams), *Glory to Rome* (interaction examples), *Ticket to Ride* (highlighted exceptions), *SmallWorld* (character overview cards), *Dominion* (ABC turn structure), *Commands & Colors: Ancients* (layout), *Lanterns* 2nd printing (reference redundancy), *Asking for Trobils* (teach-the-teacher page).
- Watch It Played (Rodney Smith) — video-teaching standard; complement, never substitute (Jaffee).
