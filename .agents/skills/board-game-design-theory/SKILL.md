---
name: board-game-design-theory
description: >-
  Critique a board game idea or diagnose why a prototype "isn't fun", and design the player experience: interesting decisions, agency, tension, session arc, victory conditions. Use when the user says "critique my game idea", "is my game fun", "why isn't my game fun", "make decisions more interesting", "fix analysis paralysis", "add tension", "my game has no arc / flat ending", "design victory conditions", "depth vs complexity", "player agency", "MDA", "kinds of fun", "flow", "engagement curve", "runaway leader", or "what would players feel". Covers MDA, LeBlanc's 8 kinds of fun, Schell's lenses, Bartle and MTG psychographics, Sid Meier's interesting-decisions doctrine, flow, meaningful vs illusory choice, and experience-level feedback loops. For mechanisms use board-game-mechanisms; for probability/EV/balance math use board-game-math-balance; for playtest protocols use board-game-playtesting; for theme use board-game-theme-narrative; for automa/co-op use board-game-solo-coop-design.
---

# Board Game Design Theory & Player Experience

## When to use / when not to use

Use when the task is about the **experience**, not the parts:

- Critiquing a game idea or pitch before/after prototyping ("is this any good?").
- Diagnosing a flat prototype: no tension, no decisions, no arc, boring endgame, analysis paralysis.
- Choosing target emotions (aesthetics) and working backwards to mechanics (MDA).
- Designing or fixing victory conditions, scoring feel, and endgame drama.
- Balancing depth against complexity; agency against luck; session length against decision density.

Do NOT use for:

- Mechanism definitions, taxonomy, core-loop construction → `board-game-mechanisms`.
- Probability, expected value, cost curves, point-salad calibration, catch-up math, player-count scaling math → `board-game-math-balance`.
- Playtest protocols, feedback instruments, kill criteria → `board-game-playtesting`.
- Theme-mechanism resonance, naming, art direction → `board-game-theme-narrative`.
- Automa design, co-op difficulty calibration → `board-game-solo-coop-design`.
- Colorblind/cognitive/physical access → `board-game-accessibility`.

## Core principles

1. **Fun ≈ meaningful decisions ÷ time.** Soren Johnson (Game Developer May 2013 issue; designer-notes.com, July 2013): for two games with equal choice, the shorter one is more fun. Raise decision quality or cut playtime; every added choice costs time, complexity, or repetition.
2. **You ship mechanics; players receive aesthetics** (MDA — Hunicke, LeBlanc & Zubek 2004). The designer controls only rules; feelings emerge at runtime. Name the target feelings *first*, then derive mechanics backwards.
3. **A choice is interesting only when it is impactful AND informed** (Sid Meier via Soren Johnson, Game Developer Jan 2009 issue; designer-notes.com, May 2009). Too little information → a guess, not a choice; complete information → a solvable puzzle, not a choice (Luke Laurie, "Good Games – Hard Choices", League of Gamemakers 2016).
4. **Depth-to-complexity ratio is the quality metric.** Elegance = maximal decision depth per rule. Every system costs cognitive budget; Blizzard capped RTS races at ~12 units each for decades (Johnson). Spend complexity on the core loop; cut the rest (Saint-Exupéry: "perfection is attained not when there is nothing more to add, but when there is nothing left to take away").
5. **Players must believe outcomes came from their decisions** — even under luck (Laurie). Prefer input luck (roll, then decide) over output luck (decide, then roll); always offer mitigation (Engelstein — see `board-game-math-balance`).
6. **Keep players in the flow channel**: challenge ≈ skill. Above → anxiety; below → boredom (Csikszentmihályi, *Beyond Boredom and Anxiety*, 1975). Difficulty, teach load, and session length must match the declared audience.
7. **Engineer the session arc** (Schell's Lens of the Interest Curve): hook → rising peaks with rests → climax → fast resolution. Opening, midgame, and endgame must each have a job. "A good game ends one turn too soon" (Piechnick).
8. **Serve more than one psychographic.** Bartle's Achiever/Explorer/Socializer/Killer (1996); MTG's Timmy/Johnny/Spike (Rosewater 2002); League's Sue/BUTCH/Aimeyj/Raphael (Domeny 2015). A game serving one aesthetic is a niche product.
9. **The victory condition is the behavior spec.** Players do exactly what scores. Score what you want them to do; align the explicit goal with players' *real* goals — "if you're making a humorous party game, don't make the optimal strategy to sit there quietly" (Teale Fristoe, League of Gamemakers 2015).
10. **No player should be dead while the game lives on.** A trailing player needs only ~5% win probability to stay engaged (Piechnick); keep last place ≥60–70% of the leader's score (Fristoe); avoid elimination and runaway leaders.

## How to apply it

### A. 60-second idea screen

Ask the designer five questions. Fail any two → redesign before prototyping; then run the full checklist (`references/idea-critique-checklist.md`).

1. **Fantasy**: In one sentence, who does the player get to be and what do they get to feel? (Map to LeBlanc's 8 kinds of fun below.)
2. **Decision test**: Describe the hardest choice a player faces on a typical turn. If none exists, the idea has no game yet (Candy Land problem).
3. **Tension source**: What makes the decision hard — scarcity, timing race, spatial contest, hidden information, social pressure, risk/reward? Name at least one.
4. **Arc**: What changes between turn 1 and the last turn? (Escalation, engine growth, board contraction?) If nothing changes, the interest curve is flat.
5. **Ending**: What triggers the end, and can the leader still be caught on the final turn?

### B. MDA mapping (experience → mechanics)

1. Write 2–3 target aesthetics from LeBlanc's list: **Sensation, Fantasy, Narrative, Challenge, Fellowship, Discovery, Expression, Submission** (+ Competition, noted in the MDA paper).
2. For each aesthetic, name the *dynamic* that must exist (e.g., Challenge → "visible skill growth and near-losses"; Fellowship → "talking is a game action").
3. Derive candidate mechanics → hand off to `board-game-mechanisms`.
4. After playtests, check: do players report the intended feelings unprompted? If not, the M→D→A chain broke — fix dynamics, not decoration.

### C. Decision audit

List every decision on a typical turn. Classify each:

| Class | Symptom | Fix |
|---|---|---|
| Meaningful | Impactful + informed; players disagree about best move | Keep; protect it |
| Rote | Obvious best option every time | Automate it away or delete |
| Illusory | Options exist but outcomes are equivalent | Ensure *variation in value* (Laurie principle 3); make differences visible |
| Guess | Player lacks information | Add partial information or forecasting |
| Overload | Too many options (11 → 3, Laurie) | Cut options, chunk into phases, use simultaneous selection |

### D. Analysis-paralysis triage (Luke Laurie, League of Gamemakers 2014)

Five design principles: (1) optimize number/complexity of decisions; (2) optimize information — enough to act deliberately, not enough to compute a perfect move; (3) ensure variation in value between options; (4) apply mechanics consistently; (5) provide clear goals and progress feedback. Ten mechanical fixes: phase-chunk turns, impose limits, shorten turns, add hidden info/randomness, reduce opportunity cost, escalate gradually, prevent cataclysmic change, eliminate calculation, minimize visual noise, use simultaneous actions. Carcassonne thought experiment: draw 1 tile/turn works; draw 5 and the game halts — more options is not more fun.

### E. Victory-condition selection

| Structure | Exemplars | Experience effect | Watch-outs |
|---|---|---|---|
| Score race (first to N) | Catan (10 VP), Root (30 VP) | Visible progress, leader-hunting | Runaway leader; needs catch-up or hidden info |
| Fixed length, highest score | Terra Mystica (6 rounds), Agricola | Predictable pacing; endgame math | "Math-problem finale" (Fristoe); anticlimax |
| Triggered end + final scoring | Ticket to Ride (≤2 trains left), Puerto Rico | Sudden acceleration; timing decisions | Players can't read remaining time → frustration |
| Objective checklist | Pandemic (4 cures), mission-driven co-ops | Clear subgoals; engine rewards (Fristoe) | All-or-nothing; binary loss feel |
| Elimination | Chess, King of Tokyo | Peak drama | Eliminated players sit out — worst arc violation |
| Sudden-death / instant win | Twilight Struggle (DEFCON, Europe control, 20 VP), Root Dominance cards | Permanent tension; alternate paths | Feels arbitrary if unreadable; needs signaling |
| Hybrid point-salad | Wingspan, 7 Wonders | Multiple paths (Stonemaier tenet 9) | Path imbalance — calibrate EV per path (`board-game-math-balance`) |

Scoring-feel rules (Fristoe): keep totals ≤10 when possible (above that players need score aids); scale values up over time (triangular/square curves) so the late game outweighs the early game; beware multipliers (swingy); hide part of the score to keep losers invested — but reveal enough for leader-hunting to work.

### F. Session-arc check

- **Opening (first ~25%)**: decisions must be legible immediately; if turn 1 requires understanding the whole game, expect bounce-off. Subgoals and engine rewards orient new players (Fristoe).
- **Midgame**: tension peak — scarcity bites, interaction highest, engines race. If nothing escalates here, add a clock or depletion pressure.
- **Endgame**: converge — board shrinks, resources convert to points, last turn should contain a real decision for every player still able to win. End on the climax, not on bookkeeping.

## Key numbers & heuristics

| Heuristic | Value | Source |
|---|---|---|
| Evergreen bestseller profile | ~5 max players, ~45 min, BGG weight 2.10, $47 MSRP, avg pub. year 2012 | Stegmaier, Dec 2019 snapshot, n=14 (ICv2 2017–2019); cf. 2022 n=21 update (2–4 players, ~$50) in `board-game-market-analysis` |
| Choices per turn | ~3 good; 11 → paralysis | Laurie 2014 [contested — audience-dependent] |
| Working memory | 7±2 chunks (Miller 1956); modern 4±1 (Cowan 2001) | Cognitive psychology |
| Trailing-player engagement floor | ~5% win chance suffices | daniel.games [contested] |
| Last-place score floor | ≥60–70% of leader's total | Fristoe 2015 |
| Complexity budget exemplar | ~12 units per faction, capped for 3 games | Blizzard RTS, via Johnson 2013 |
| Loss aversion | losses hurt ≈2× equivalent gains (λ≈2.25) | Tversky & Kahneman 1992 (cumulative prospect theory) [approx.] |
| Co-op win-rate targets | ~40% first-time, ~60% experienced | Matt Leacock — see `board-game-solo-coop-design` |
| Score granularity | >10 total → players need scoring aids | Fristoe 2015 |
| Length classes | filler ≤30m; family 30–60m; euro 60–120m; heavy 90–180m+ | Community consensus — see `board-game-math-balance` |
| Bartle Test reach | 800,000+ completions by Oct 2011 | Andreasen & Downey test (via Wikipedia) |
| Evergreen competitive/co-op split | 9 competitive / 5 co-op of 14 | Stegmaier, Dec 2019 snapshot, n=14; cf. 2022 n=21 update in `board-game-market-analysis` |

## Common pitfalls

- **Candy Land problem**: zero meaningful decisions; the game plays the players.
- **Multiplayer solitaire**: no shared scarcity or interaction; tension source missing.
- **Dominant strategy**: one solved path makes all choices illusory (Alpha Centauri Unit Workshop — Johnson).
- **Analysis paralysis**: too many options/info — apply Laurie's 5 principles and 10 methods.
- **Runaway leader / dead-man-walking**: positive feedback, no catch-up; a loser knows by midgame.
- **Kingmaking**: an eliminated-from-contention player decides the winner (mitigations → `board-game-math-balance`).
- **Math-problem finale** (Fristoe): the climax is replaced by 10 minutes of arithmetic; keep scores trackable or staged.
- **Two-games-fighting** (Covert Action Rule, Meier via Johnson): two good sub-games that destroy each other's focus — one good game beats two great ones.
- **Luck swamping agency**: output luck decides outcomes with no mitigation; players stop believing decisions matter (Laurie).
- **Design for the designer, not the player**: lore dumps, opaque simulations, cleverness the player can't perceive — "the player should have the fun" (Meier via Johnson).
- **Choice overload as content**: mistaking option count for depth; variety often *emerges because designers limited choice* (Johnson on Atom Zombie Smasher/FTL).

## Reference files

- `references/frameworks.md` — load when you need the full framework catalog: MDA/8-kinds-of-fun detail with tabletop exemplars, Bartle + MTG + League + Quantic Foundry psychographic mappings, Schell's lenses most useful for tabletop, flow theory, agency (Johnson, Church's formal abstract design tools), depth/complexity/emergence, interest curves, the extended victory-condition taxonomy, experience-level feedback loops, meaningful-vs-illusory choice taxonomy, and sources.
- `references/idea-critique-checklist.md` — load when the user asks you to critique, score, or diagnose a game idea or prototype. Run the 10-section scored diagnostic top to bottom and report verdicts per section with fixes.

## Related skills

- `board-game-mechanisms` — mechanism taxonomy, tension sources, core loops.
- `board-game-math-balance` — probability, EV, cost curves, catch-up math, scaling.
- `board-game-playtesting` — test protocols, feedback instruments, kill criteria.
- `board-game-theme-narrative` — theme-mechanism resonance, worldbuilding.
- `board-game-solo-coop-design` — automa, difficulty dials, quarterbacking.
- `board-game-accessibility` — sensory/cognitive/socioeconomic access.
- `board-game-prototyping` — prototype stages and materials for testing these ideas.
- `board-game-market-analysis` — positioning the experience for a segment.
