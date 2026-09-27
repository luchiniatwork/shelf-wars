# Research Digest: Prototyping & Playtesting Methodology

Factual backbone for the `prototyping-playtesting` skill. Sources: 12 grounded web searches (designer blogs, publisher resources, community consensus) + 11 fetched canonical pages (Stonemaier Games ×2, League of Gamemakers ×3, Gamasutra/Game Developer, MVP Board Games, Games Precipice, Kathleen Mercury, Cardboard Edison, Board Game Design Lab hub).

## Core frameworks & models

- **Stegmaier's prototype→playtest→development pipeline** (Jamey Stegmaier, Stonemaier Games, 2023): Early prototyping (minimum viable content) → local guided playtesting (designer at table) → blind/unguided waves (rules-only, paid testers) → development (formal data analysis, "playtesters raise questions; developers propose answers"). Minimum 3 blind waves before calling a game ready.
- **Ugly-prototype philosophy** (Stegmaier; echoed by Geoff Engelstein): early prototypes should be functional, not beautiful — polish breeds attachment, wastes iteration cost, and pulls tester feedback toward aesthetics instead of mechanics.
- **Caputo's three "how many playtests" approaches** (Scott Caputo, League of Gamemakers, 2015): (1) *Test Plan* — cover every card/faction/power, every significantly different setup combo, and both extreme player counts; (2) *People* — self → friends/family ("friendly playtests") → strangers ("unfriendly playtests") → target market → repeat players → mechanics & theme experts; (3) *Goal* — test until someone would buy it, strategies are statistically balanced, and length hits target.
- **Cumulative playtest stages** (Peter, MVP Board Games, DToW #10, 2014): solo (controlling 2–3 seats) → co-designer/close friend → family & game group → conventions (Unpub) → blind tests → publisher. Stages stack; none are ever retired. 100+ tests per design.
- **Rockholz's 10 Insightful Playtest Questions** (Wesley Rockholz, Gamasutra, 2014): question set engineered to replace useless "did you have fun?" items with probes of engagement, strategy, and control (full list under Catalog).
- **WINQ feedback form** (Kathleen Mercury, kathleenmercury.com, built on Stanford d.school methods): four written categories — what **W**orks, what needs **I**mprovement, what **N**ew ideas can you offer, what **Q**uestions do you have. Designer prepares ≥3 questions for testers beforehand; both designer and testers fill forms; designer writes a self-reflection summarizing how feedback will be incorporated.
- **Stress test** (D&D Next playtest team, via Games Precipice, 2014): strip the game of all thematic trappings and run the bare math repeatedly to fix numerical balance and rules contradictions, one mechanic at a time, deliberately trying to break it. Distinct from thematic/full playtests.
- **Engelstein's playtester paradox** (Geoff Engelstein, Ludology): paired slides — "always listen to your playtesters" and "never listen to your playtesters." Testers are reliable at reporting *that* something is wrong and how it felt; unreliable at prescribing fixes. Trust your design instinct for solutions.
- **Protospiel reciprocity norm** (Protospiel events; documented by Luke Laurie, League of Gamemakers, 2014): "participants are expected to give as much time as they take" — run your game, play others' games.
- **Perceived-time fun proxy** (Rockholz): ask "how long did you feel like you were playing?" and compare to the clock; engagement compresses perceived time. Replaces "did you have fun?"

## Catalog / techniques

### Prototype lifecycle stages & what to invest

1. **Proof-of-concept / solo sim.** Hand-written index cards, spare tokens, sketch boards. Stegmaier: for a game that will eventually have 100 cards, design only 10–20 up front — "just enough for the game to function." Goal: prove the core loop is fun and functional; catch broken interactions before spending other people's time. Cost target ~$0 (Joe Slack: start with materials that cost "even $0").
2. **Ugly functional prototype.** Printed paper inserts slipped into opaque sleeves over backing cards (old MTG cards or poster board) for shuffleable stiffness; full-sheet label paper stuck to 0.022"–0.030" chipboard for boards/tiles; bulk cubes/meeples/dice. Iterate by reprinting inserts only.
3. **Polished prototype.** Data-merge pipelines: nanDECK (free; CSV-driven card generation with scripting), Component.Studio ($9.99/mo, 3-day trial; Google Sheets → components; exports PnP PDFs and pushes to The Game Crafter/Tabletop Simulator), Inkscape (free; Inkcards/playing-card extensions), Affinity Designer (one-time purchase; pair with Affinity Publisher for data merge). Short-run physicals via The Game Crafter. Design with ~2 mm bleed, trim, and safe zones; 300 gsm cardstock where the printer allows.
4. **Pitch/PnP-grade.** Functional accuracy beats production art: publishers expect to redo art/graphic design but need legible UI, finalized component counts, and card text matching the rulebook. Stegmaier: don't invest in professional art for publisher pitches; do invest in "thoughtful graphic design" for usability. PnP files must state what testers print vs. supply (dice, pawns, scissors).

Reference material costs (community guides): index cards ≈$3/100 or $10/1000; full-sheet labels ≈$10–15/100; ~100 meeples in 10 colors ≈$10; ~100 d6 ≈$10–15; ~7 polyhedral sets ≈$10. Sleeve brands recommended: Dragon Shield Matte, UltraPro, KMC; avoid "penny sleeves" (rip in play).

### Digital playtesting platforms

- **Tabletop Simulator (TTS):** paid Steam app; strongest physics/3D and Lua scripting (automation, scripted setup); Steam Workshop distribution; every tester normally needs a copy, though Steam Remote Play lets a host bring non-owners in. Learning curve for building; best for complex games and later-stage balance loops.
- **Tabletopia:** browser-based 3D; free tier usually sufficient for one prototype; testers join free via link; no-code setup; reported clunky for mid-game edits. Stegmaier uses Tabletopia but treats digital strictly as a *secondary* option — physical-component issues get obscured digitally.
- **Screentop.gg:** free, browser, no accounts; testers join by link (best accessibility incl. mobile); 2D, fast to iterate; no scripting; components can't be changed mid-game.
- **Playingcards.io:** free, browser, card-focused; minimal setup; no-code automation for piles/shuffling; weak for non-card components and small card text; needs external voice/chat.
- Also seen in group calendars: Tabletop Playground. [contested] One search claimed Protospiel Online bars TTS use — verify before repeating.

### Playtest formats and what each can measure

- **Solo self-play / simulation:** measures core-loop functionality, rule-flow logic, early bug/scoring-collapse detection, iteration speed. Cannot measure social dynamics, true balance (designer can't forget hidden info), rules clarity for newcomers, or fun. Use from first playable build through the whole lifecycle.
- **Guided (designer present):** measures engagement, pacing/downtime, emotional spikes (watch for joy/frustration/confusion — Stegmaier), emerging strategies, component usability, targeted hypotheses. Cannot measure unaided rulebook comprehension; designer presence biases politeness. Stegmaier plays *in* the game (learns most at the table); MVP found note-taking is better when *not* playing — split per preference.
- **Blind (rules-only, no designer help):** the only format that measures rulebook clarity, iconography, setup intuitiveness, unbiased experience. Every question testers ask is a rulebook bug (Stegmaier), even if the answer is in the book — highlight it better. Cannot surface early-stage mechanical breakage usefully or deep strategy. Start blind waves when the game is fun and functional and the rulebook is near-final.
- **Remote blind:** PnP kit or digital build + written reports/surveys. Video recording of sessions: Stegmaier tried it for Charterstone and found it not useful without excellent A/V setups [contested — other designers rely on it].

### Session protocol & logging

- Set one goal per session (balance? flow? a specific mechanic?); frame it for testers up front (Stegmaier; also "ask the designer what they're trying to get out of the playtest").
- Change one variable per iteration once the core holds together; early stage tolerates multi-change thrash. "Stack the deck" deliberately to force edge content (Caputo: it's OK to force factions/cards).
- Log fields (synthesis of League of Gamemakers practitioners + Stegmaier survey): game + rules version number, date, player count, tester names, teach time, game length, turn/round length, final scores/outcome, setup/factions used, every rules question + interim ruling, observed behavior (hesitation, phone-checking), broken elements, pros/cons, "would play again?", planned changes.
- Named examples: Brad Brooks logged Letter Tycoon play length, scores, and which letter tiles each player bought to detect over/under-powered powers (and dropped a discard-frequency metric when it proved uninformative). Peter (What the Food?!) logged name/length/date/final scores and ran a core group of 6 super-fans playing weekly to finish balancing.
- Stegmaier's wave protocol: quiz-screened lead playtesters; 3 sessions within 3 weeks; quantitative survey after each session + final report; paid (store credit or PayPal); he reads *no* reports until the wave closes to avoid partial-picture processing; notes set aside ~1 day before implementing changes.
- Post-wave: correlate scores with strategies to detect dominant lines (Caputo).

### Feedback instruments & question design

- Never ask leading/loaded questions ("Is my game not awesome?!", "Wasn't combat exciting?") — you learn nothing and invite confirmation bias (Luke Laurie). Avoid bare yes/no items.
- Observe first, ask after: body language, engagement dips, phone-checking, puzzled faces are the signal (Engelstein: the biggest late-cycle insights are behavioral, requiring in-person or self-recorded play). Save deep discussion for the debrief; don't interrupt flow.
- Stegmaier's standing questions to testers: what happened, why did it happen, how did it make you feel — and *don't* propose solutions ("that's the job of the designer and developer").
- MVP's icebreaker trio (early and late stage alike): favorite part? least favorite part? if you could make one change, what?
- Rockholz's 10 Insightful Playtest Questions: (1) How long did you *feel* you were playing? (2) Did you feel you were making friends or enemies? (3) Could you play again without looking at the rules? (4) What was your strategy? (5) How far ahead could you predict opponents' moves? (6) To what extent did you react to opponents' moves? (7) Can you explain why the winner won? (8) How much did you feel in control of the outcome? (9) Did anything block you from executing your plans? (10) Name the most similar game you've played (market-fit proxy).
- Caputo's purchase test: "Would you buy this game if it were available?" — target ≥1 yes per table before pitching.
- NPS-for-games (borrowed instrument): 0–10 "likelihood to recommend"; promoters 9–10, passives 7–8, detractors 0–6; NPS = %promoters − %detractors (−100…+100); value is in the trend and the follow-up "why?". Stegmaier's simpler version: 1–10 rating per session; ready when scores are consistently 8–10 and feedback is fine-tuning only.
- "Rate fun per round" / emotional-arc tracking: no single canonical named technique found [contested as a named method]; practice is mid-game pulse-checks or post-game recall of peak/trough moments to map the fun curve.
- WINQ written grids let testers note issues mid-game without stopping play.

### Rules-comprehension (usability) testing

- Blind rules-only test is the core instrument. Variants: teach-back ("teach me how to play" from the book); summarization (read book, explain the game back); look-up timing (MVP: make testers find answers in the book themselves and watch how long it takes; note forgotten/missed rules and emphasize them in revision).
- If a rule needs many exceptions, simplify or cut it. Consistent terminology, examples, diagrams, logical structure (components → setup → how to play → details → endgame → reference).
- MVP blind-test etiquette: observe silently; intervene only when the answer isn't in the book; when you intervene, take a note and fix the book.

### Blind-test kit contents

Complete playable prototype; near-final rulebook; all components (or PnP PDFs + explicit list of household items testers must supply); structured feedback form (Google Forms typical) covering player count, play time, rules-clarity pain points, likes/dislikes, balance/fun, open notes, follow-up consent; written instructions (purpose = test the book; no external help; if stuck, guess, note, continue); confidentiality expectations; your own tracking spreadsheet (who, when sent, feedback due).

### Recruitment

Ladder: self → family/friends → local meetups/game stores → conventions (Unpub events; Protospiel — scheduled slots + open tables + reciprocity) → online pools. Online: Break My Game (501(c)(3); daily Discord events), Blind Playtesters.org, PlaytestNW, Virtual Playtesting, Remote Playtesting groups, Protospiel Online (Discord + virtual tables); Cardboard Edison maintains the canonical calendar/list (cardboardedison.com/playtest-groups). PnP communities: Playtest-coop.com; BGG forums. Stonemaier model: quiz-selected paid lead playtesters (~130 credited) who run their own groups. Incentives: finished/KS-edition copies, credit, payment.

## Numbers, heuristics & rules of thumb

- **10–20 cards** of a planned 100 for the first prototype (Stegmaier).
- **≥30 playtests** before pitching (Caputo). His rationale — "30 is a minimum population size in statistics" — is a misapplication of the CLT rule of thumb [contested as statistics; fine as a floor].
- **100+ playtests** per published design (MVP); "test until you stop making changes, then test 20 more times" (community maxim, unattributed).
- **≥3 blind waves** minimum; **5 lead testers/wave**, each running 1–4 additional players, **3 sessions within 3 weeks**; game is ready when ratings are **8–9–10/10** and remaining feedback is fine-tuning (all Stegmaier).
- **10+ repeat plays** by one group for strategy games to expose solvability and long-term balance (Caputo).
- **≥1 "would buy" per table** before pitching (Caputo).
- Test **both extreme player counts**: auctions/market/bidding/deduction notoriously break at 2p; downtime and chaos spike at max count (Caputo).
- **Idea → first prototype in <1 week** (rapid-prototyping maxim, unattributed).
- Prototype supply prices: see Catalog (index cards $3/100; labels $10–15/100; meeples $10/100; Component.Studio $9.99/mo).
- D&D Next stress-test program used thousands of testers (WotC scale; not achievable for indies — principles transfer).
- Small samples can't prove balance: treat single-session outliers as hypotheses, not noise — they often flag edge cases that resurface.
- Campaign/legacy games: recruit testers committed to many sessions and raise compensation accordingly (Stegmaier).

## Best-practice checklists

**Per session:** state the session goal → confirm stage-appropriate testers → teach just enough, layer rules as relevant (don't front-load everything) → observe silently, note every question → allow broken-element demonstration once, then steer away (remove the element if they keep exploiting it) → end on time; abort hopeless sessions early → debrief: favorite/least-favorite/one-change, then targeted probes → written forms collected → log session → set notes aside ~a day → implement one-variable change → version-number the new build.

**Before blind waves:** core loop proven fun in guided tests → rulebook drafted to near-final → components legible without explanation → kit assembled (prototype, book, form, instructions, tracking sheet) → testers screened (quiz or prior reliability) → schedule (3 sessions/3 weeks) → hold all reports until wave closes → process, iterate, re-wave.

**Question hygiene:** no leading questions; no yes/no-only items; problems over solutions; specifics over adjectives ("Cards 2, 8, 19, 54 felt too expensive," not "some cards felt expensive" — Stegmaier); report misplayed rules explicitly — patterns of identical misplay indicate a rules/UX problem, not player error.

**Change discipline:** one major system per version; preserve old versions; document what was tried and why it failed; don't tweak a build a publisher is currently evaluating (MVP); follow the fun — pivot toward what testers actually enjoy.

## Common pitfalls & failure modes

- **Friends-and-family-only testing:** supportive bias, sugar-coated feedback, false confidence. Counter: strangers and target-market players ("unfriendly playtests").
- **Defending the design:** justifying mechanics mid-feedback kills honesty. Never tell a tester they're wrong; file it and look for the root feeling (Laurie).
- **Changing 5 things at once:** destroys attribution; you can't tell which change caused which effect.
- **Testing too late:** waiting for polish makes core changes expensive; test ugly and early (Engelstein: games are "amazingly good in my head" until real players arrive).
- **Premature polish:** polished prototypes attract art feedback (wrong signal for early tests — MVP) and make the designer change-averse.
- **Statistical overreach:** balancing on tiny samples; or dismissing outliers that reveal edge cases.
- **Unstructured "game night" testing:** rules changed mid-session on a whim, no version notes, vague feedback ("it was fun") — unrepeatable and wasted.
- **Soliciting solutions instead of symptoms:** testers prescribe fixes; designers should extract what/why/how-it-felt (Stegmaier doctrine; Engelstein paradox).
- **Repeatedly exploiting a found exploit:** after a broken element is demonstrated, continuing to use it invalidates the rest of the session (Stegmaier).
- **Asking "did you have fun?"** — unactionable; use perceived-time, favorite/least-favorite, strategy-walkthrough probes instead (Rockholz).
- **Rulebook by accretion:** fixing blind-test findings by adding exceptions instead of restructuring; measure look-up time and misplays instead.
- **Tic-tac-toe effect** (Rockholz): fully predictable optimal lines → solved game → ties/staleness; detected via questions 4–7.

## Canonical sources

- *The White Box: A Game Design Kit in a Box* — Jeremy Holcomb (essay collection; Geoff Engelstein foreword)
- *Game Production: Prototyping and Producing Your Board Game* — Geoff Engelstein (2025)
- *The Kobold Guide to Board Game Design* — Mike Selinker et al.
- *The Art of Game Design: A Book of Lenses* — Jesse Schell (playtesting lenses)
- *The Game Inventor's Guidebook* — Brian Tinsman
- Stonemaier Games blog — https://stonemaiergames.com (esp. "Tabletop Game Prototyping, Playtesting, and Development"; "How to Be a Better Playtester")
- League of Gamemakers — https://www.leagueofgamemakers.com (Scott Caputo "How Many Times…"; Luke Laurie "How to Playtest"; "Ask the League: Play Test Sessions")
- Board Game Design Lab — https://www.boardgamedesignlab.com (playtesting hub + podcast)
- Games Precipice — https://www.gamesprecipice.com ("The Role of Playtesting")
- Rockholz, "10 Insightful Playtest Questions" — Gamasutra/Game Developer blogs (2014)
- Kathleen Mercury (WINQ forms) — http://www.kathleenmercury.com
- Cardboard Edison — https://cardboardedison.com (playtest-group directory/calendar)
- Raph Koster — https://www.raphkoster.com ("Feedback Does Not Equal Game Design" et al.)
- Ludology podcast (Engelstein) — playtesting episodes
- Tools: nanDECK (free), Component.Studio, Inkscape, Affinity Designer/Publisher, The Game Crafter, Cutterpillar cutters; TTS, Tabletopia, Screentop.gg, Playingcards.io
- Communities/events: Unpub, Protospiel (+Online), Break My Game (501c3), Blind Playtesters.org, PlaytestNW, Metatopia; BGG forums; Playtest-coop.com (PnP)
- James Mathe, "How to Make a Board Game" — jamesmathe.com [domain unresolvable at fetch time; content survives via mirrors/quotes — verify current location]
