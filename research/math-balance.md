# Research Digest — Mathematics, Probability & Balance

All dice/hypergeometric/sample-size figures were re-derived computationally; designer-attributed heuristics come from primary design blogs (daniel.games, League of Gamemakers) or interviews, with disagreements flagged.

## Core frameworks & models

- **2d6 triangular distribution (the "Catan model")** — 36 equiprobable outcomes; sums cluster: 7 = 6/36 = 16.67%; 6/8 = 13.89%; 5/9 = 11.11%; 4/10 = 8.33%; 3/11 = 5.56%; 2/12 = 2.78%. Exploited deliberately in *Catan* (1995): hex tokens print probability "dots," 6 and 8 are the contested spots (P(6 or 8) = 27.8%), and the modal roll (7) produces nothing — it fires the Robber, converting the most frequent outcome into interaction. Expect a 7 once per 6 rolls.
- **Flat die vs. bell curve (d20 vs. 3d6)** — d20 is uniform: 5% per face; crit-on-20 = 5%, crit-on-19–20 = 10%. 3d6 is near-normal: mean 10.5, SD ≈ 2.96, P(8–13) ≈ 67.6%, P(18) ≈ 0.46% (10× rarer than a natural 20). Matching crit rates on 3d6 needs ranges: ≥16 ≈ 4.63% (≈5%), ≥15 ≈ 9.26% (≈10%). On a bell curve each +1 modifier swings mid-target odds far more than d20's flat 5%/point — flat = swingy/luck-dominant, bell = reliable/skill-dominant.
- **Exploding dice EV** — reroll-and-add on max face: EV = n(n+1)/2(n−1) = base × n/(n−1). d4: 2.5→3.33 (+33%); d6: 3.5→4.20 (+20%); d8: +14%; d10: +11%; d12: +9%; d20: 10.5→11.05 (+5.3%). Small dice gain most, including *higher odds of reaching high targets* (the "target-number paradox": exploding d4 reaches ≥6 in ~19% of rolls vs ~17% for exploding d6). Exemplars: Savage Worlds, Deadlands, L5R.
- **Dice pools (success counting, binomial)** — roll N dice, count faces ≥ target. Mean = N·p, SD = √(N·p·(1−p)); e.g., 5d6 counting 5–6 (p=1/3) averages 1.67 successes. Three distinct tuning knobs: dice count, target number, successes required.
- **Hypergeometric model (cards, sampling without replacement)** — P(k of K desired cards in n draws from N-card deck). Anchors (60-card deck, 7-card opener): 4 copies → P(≥1) = 39.9%; 8 copies → 65.4%; 12 copies → 80.9%. Mana bases: 24 lands/60 → P(≥2 in opener) ≈ 85.7%; 17/40 (Limited) → 89.5%; 37/99 (Commander) → 81.4%. Hence "8–12 functionally identical cards" for effects you need every game. Using binomial (with-replacement) math for draws is a known error.
- **Deck thinning** — removing cards raises the density of what remains, but per-card effects are small (~1–2 pp per pair thinned from a mid-game deck). Real value: compounding and removing *bad* draws (Dominion's Chapel). Practical value of MTG fetch-land thinning specifically is [contested] — measurable but often outweighed by life/tempo cost.
- **Input vs. output randomness — Geoff Engelstein (Ludology/GameTek)** — input luck: random event, *then* decide (draw a hand; assign rolled dice — *Castles of Burgundy*): preserves agency. Output luck: decide, *then* roll to see if it worked (*Risk* combat, Monopoly Chance): swingy, anti-meritocratic when pass/fail. Piechnick's corollary: resolve contests with hidden information (opponent may play a shield) rather than dice.
- **"E is for Effort" value model — Christian Strain, League of Gamemakers (2017)** — balance mathematically *before* playtesting ("Tesla method," vs. Edison's 1,000-bulb brute iteration). Effort (e) = turns to acquire, starting from nothing: free red card = 1e; blue card costing two reds = 3e; if one turn gathers 2 gold, gold = 0.5e and the blue card should cost 4 gold. Adjust for supply & demand (scarce = above e-value). Playtesting then tests *perceived* balance — players misperceive (told to "roll close to average," players pick 2 dice over 10, though 10 dice is far more reliable).
- **Lowest-common-denominator conversion — Daniel Piechnick (daniel.games)** — convert everything to one resource to compare values; actions/turns are costs (a "free" card still costs a card; a 2×-cost action giving 2× reward is actually *better* — both consume one turn). Balance by **changing numbers, never adding rules**: put a tunable number on every component (Radlands camps carry a corner number; weaker camps grant a larger starting hand).
- **Power budget / cost curve (CCG-derived)** — budget = f(cost); multi-effect cards split the budget, so each effect is weaker than a focused card's. Hearthstone vanilla heuristic: fair minion stats ≈ 2×cost+1. Goals: no infinite combos (output ≤ input of same currency), no strictly-better cards at equal cost.
- **Point-salad path calibration** — community guidance: compute EV per path per unit effort; keep viable paths within ~10–15% of each other [contested — widely repeated, no single originator]. Piechnick's looser bar: an option chosen only 25% of the time is fine if worth considering. *Point Salad* (AEG 2019) exemplar: 108 scoring conditions, veggie counts scaled by player count, flip-point-card-to-veggie as pivot valve.
- **Intransitive balance (RPS triangles; nontransitive dice)** — cyclical A>B>C>A prevents dominant strategies; vs. random play each option wins/loses/draws equally. **Efron's dice (Bradley Efron, via Martin Gardner 1970)**: A = 4,4,4,4,0,0; B = 3,3,3,3,3,3; C, D arranged so each die beats the next with P = 2/3 (C beats A only 5/9). Use triangles for faction/strategy counters (infantry>cavalry>archers); transitive ladders only where escalation is the point (tech trees).
- **Feedback loops: positive vs. negative** — positive = success breeds success → snowball/runaway leader; negative = success breeds resistance → rubber-banding. *Characteristics of Games* (Elias, Garfield & Gutschera, MIT Press 2012) treats this as a core axis; Sirlin (*Playing to Win*) calls unchecked positive loops the "slippery slope." **Dynamic difficulty balancing / rubber-banding**: *Mario Kart* position-based item distribution (leaders get weak items, trailers get Blue Shells) plus AI speed adaptation — effective, and the canonical example players *resent* when overt.
- **Catch-up design patterns — Piechnick + exemplars** — hide catch-up inside arithmetic, never naked score-based handouts (negative example: Isle of Skye's income-per-player-behind). Patterns: **ramps** (Family Feud's double-points final round); **big moves** (Scrabble bingo +50 — a loser always has a theoretical path); **proportional penalties** ("all opponents lose half their health" hits the leader hardest); **politics** (Catan robber, Waterdeep attack cards — works only if the table targets the leader); **obscured leader** via hidden info (Waterdeep's hidden Lords = good; Small World's face-down VP = bad, becomes memory test); **structural** (Power Grid: last place acts first in buy phases — "stay behind then leap" is core strategy); or **end the game before the leader locks**. A trailing player needs only ~5% win probability to stay engaged.
- **Kingmaking** — a player who cannot win decides who does. Mitigations: hidden scores, simultaneous reveals, multiple end conditions, self-directed goals for trailing players.
- **Action economy** — fixed actions/turn is the master currency (*Pandemic* = 4, *Tikal* = 10 AP). Total decisions ≈ actions × turns × rounds — estimate, then verify each action's EV per action-point. Attacks on opponent action efficiency = "Net Action Advantage."
- **Player-count scaling & downtime arithmetic** — sequential-turn downtime per round = (n−1) × mean turn length (5 players × 60s = 4 min idle). Fixes: simultaneous play (7 Wonders: constant ~30 min at 3–7p), off-turn engagement (Catan/Machi Koro pay on others' turns), end-of-turn draw, fewer choices per turn, scaled components (two-sided boards, Sagrada dice = 2n+1, Point Salad veggie counts), fewer rounds at high counts.
- **Weight/length classes (community consensus)** — BGG weight 1–5. Length: filler ≤30 min (some 5–15), family ~30–60 (kids ~10–30), light euro 30–60, medium euro 60–90, euro 60–120, heavy 90–180+. Piechnick: length tracks weight; medium-light should aim **20–30 min**; "a good game ends one turn too soon"; if players can complete every path, the game is too long.
- **Co-op/solo difficulty calibration** — Matt Leacock (interviews): target ~**40% win rate for first-time groups**, ~**60% for experienced**; ship difficulty knobs (Pandemic: 4–6 Epidemic cards); tension in waves, not a monotonic ramp. Community bands for replayable co-ops run ~50–70% [contested — varies by source/audience].
- **Model-based balance + sample-size reality** — binomial 95% CI half-width on a win rate (worst case p=0.5): n=10 → ±31 pp; n=20 → ±22; n=30 → ±18; n=50 → ±14; n=100 → ±10; n=400 → ±5. Detecting a 55%-vs-50% faction edge at 80% power needs **~615 plays** (60% vs 50%: ~152). You cannot statistically balance on 10 plays: build the model first (Tesla method), use playtests for perceived balance and breakage. "30 playtests = statistical minimum" is [contested — arbitrary]. Games-user-research guidance: ~100 survey responses ≈ ±10%; diminishing returns past ~400. Piechnick: a game needs "maybe hundreds" of playtests; the public plays millions more times than you and *will* find imbalances you missed.
- **Push-your-luck EV (Pig as canonical model)** — *Pig* (first to 100; roll d6; 1 = lose turn total): EV-max simple rule is "hold at 20–21" ≈ 8.14 pts/turn (verified; hold-at-25 drops to 8.00). True optimal policy is opponent-aware (roll more when behind), computed by **Neller & Presser (2001; UMAP Journal 2004)** via value iteration. Lesson: compute the EV surface of your push-your-luck mechanic (AnyDice/spreadsheet) before tuning payouts; players misestimate bust odds (that's the fun), but each wager's house edge must be intentional.

## Catalog / techniques

- **Dice engineering** — pick the distribution shape deliberately: single die = flat swing; 2d6 = triangular and player-readable (Catan dots); 3d6+ = tight bell for skill reliability; pools = binomial success counts; exploding = long tail (price it: +20% EV on d6). Custom faces: two identical + rest unique; never blank faces; don't map roll directly to outcome (move/gain that much) — map to *choices* (assign, match, mitigate). Mitigation kit: rerolls (Yahtzee, King of Tokyo), ±pip modifiers (CoB workers), convert-bad-roll powers, luck currencies.
- **Card-odds procedure** — (1) model deck hypergeometrically; (2) compute P(≥1 copy) of each key card in opener and by turn T; (3) set copy counts from the 39.9/65.4/80.9 anchors; (4) for deckbuilders, price trashing high — removing a bad card improves every future draw; (5) track shuffle cycles: a bought card is seen ≈ (deck size ÷ hand size) draws per shuffle.
- **Costing & power budgets** — Strain's effort accounting → Piechnick's LCD conversion → explicit number per component. Rules: expensive actions must be *ridiculously* powerful (they cost saving turns); saturation kills value (20 axes ≉ 20× the value of 1); slow-to-achieve things are weaker than they look; things are usually weaker than you think — "don't baulk at making things three times stronger"; a hand of cards averages out individual imbalance; zero-cost cards are still balanced by the hand slot.
- **Feedback-loop toolbox** — pair every positive loop (engine, income, territory) with negative pressure (scarcity, proportional tax, end trigger, politics) or a cap (diminishing returns). Snowball games need short length or reset valves; come-from-behind games need ramps and big moves. Decide early which emotional arc the game sells.
- **Scaling techniques** — two-sided/sectioned boards (Power Grid regions), component-count scaling (Point Salad veggies, Sagrada 2n+1 dice), round-count scaling, simultaneous selection, nearest-neighbor interaction, co-op threat scaling.
- **Turn-time budgets** — short turns at low weight; new information (card draw) at *end* of turn so players plan during downtime; cap per-turn menu size to fight AP-paralysis.
- **Co-op threat engines** — card/dice-driven "cardboard antagonist" (Leacock): difficulty knob = threat density; win band 40–60%; solo modes inherit the same band.

## Numbers, heuristics & rules of thumb

- 2d6: 7 = 16.67%; 6/8 = 13.89%; 5/9 = 11.11%; 4/10 = 8.33%; 3/11 = 5.56%; 2/12 = 2.78%; P(6 or 8) = 27.8%.
- 3d6: mean 10.5, SD 2.96; P(8–13) ≈ 67.6%; P(≥16) ≈ 4.63%; P(18) ≈ 0.46%. d20: flat 5%/face.
- Exploding EV = base × n/(n−1): d4 +33%, d6 +20%, d12 +9%, d20 +5.3%.
- Card odds (60-card, 7 opener): 4-of = 39.9%, 8-of = 65.4%, 12-of = 80.9%. Thinning ≈ 1–2 pp per pair [contested practical value].
- Pig: hold at 20–21 ≈ 8.14 EV/turn; optimal policy is score-relative (Neller & Presser 2004).
- Win-rate CI (p=0.5): n=10 ±31 pp; n=50 ±14; n=100 ±10; n=400 ±5. ~615 plays to detect 55% vs 50% at 80% power.
- Co-op: Leacock ~40% first-play / ~60% experienced; community band 50–70% [contested].
- Length: filler <30; family 30–60; euro 60–120; heavy 2h+; medium-light 20–30 (Piechnick); "end one turn too soon."
- Downtime = (n−1) × turn length; simultaneous play collapses it (7 Wonders ~30 min at any count).
- Vanilla costing: stats ≈ 2×cost+1 (Hearthstone). Trailing player needs ≥ ~5% win chance (Piechnick). Option picked 25% of the time is balanced enough. Point-salad paths within ~10–15% EV [contested origin].
- The public will outplaytest you by orders of magnitude — expect post-release discoveries.

## Best-practice checklists

**Balance-by-model (before any playtest)**
1. Pick the LCD resource (usually turns/actions). 2. Compute effort cost e of every element. 3. Adjust for scarcity and saturation. 4. Give every component a tunable number. 5. No strictly-better options at equal cost; no infinite loops. 6. For random elements, compute the full distribution (AnyDice), not just the average. 7. Multi-path games: compute EV/path, check the 10–15% band.

**Feedback-loop audit**
1. List every positive loop. 2. Name each loop's negative pressure or cap. 3. Simulate mid-game: can a leader be uncatchable? If yes, add ramp, big move, proportional penalty, or earlier end trigger. 4. Hide catch-up inside general arithmetic; no naked leader-punishment. 5. Trailing players keep ≥ ~5% win chance. 6. Kingmaking check: can an out-of-contention player decide the winner?

**Scaling check**
1. Downtime = (n−1)×turn length at max count; if > ~2 min/round, add simultaneous play or off-turn engagement. 2. Scale congestible resources (board area, cards, dice pools) per count. 3. Verify 2-player works (most playtests happen there). 4. Measure real turn time in playtests.

**Co-op difficulty**
1. Define target win band (40–60%). 2. Ship ≥3 difficulty knobs. 3. Tune by logging win/loss + margin over dozens of plays, not by feel. 4. Tension oscillates in waves.

**Playtest statistics**
1. Log per play: winner seat, strategy, margin, length, dead elements, stalemates. 2. Change ONE variable per iteration. 3. Don't rebalance on <30 plays of a configuration — and remember 30 plays is still ±18 pp. 4. Model for balance; playtests for perceived balance and fun. 5. Track first-player win rate; if >55–60%, compensate later seats.

## Common pitfalls & failure modes

- **Balancing on 10 plays** — statistically empty (±31 pp); single-path playtesters devalue off-path elements (Strain's rubies/emeralds problem).
- **Balancing by adding rules, not numbers** — bloat, no tuning knob.
- **Spreadsheet false precision** — elaborate math invalidated by the next revision; keep the model coarse, then guess → play → adjust.
- **Overt catch-up mechanics** — score-based handouts/leader taxes read as anti-meritocratic (Isle of Skye income example).
- **Runaway leader / snowball** — engine and economic games; checked-out players by mid-game; pair loops with caps or end triggers.
- **Kingmaking & failed bashing-the-leader** — politics-as-catch-up fails if the table won't target the leader; kingmaking appears when trailers have no self-directed goals.
- **Strictly-worse outcomes** — a result dominated in every dimension (Sword 2/2 vs Spear 3/3) feels like theft; make weaker results *different*, with some upside.
- **Pass/fail output randomness** — decide-then-roll failure with no mitigation = agency loss; prefer input luck or fail-forward (+1 skill on failure).
- **Blank die faces; roll-equals-outcome dice** — wasted excitement budget.
- **Memory-based hidden scoring** (Small World) — obscuring via memory is a chore; use structurally hidden info (Waterdeep Lords).
- **Multiplayer solitaire** — simultaneous play with zero interaction; fix with shared races or denial.
- **Analysis paralysis** — big menus × AP systems; cap choices, sequence phases.
- **Length creep** — padding identical rounds; cut a round, then another.
- **Overkill & under-priced big actions** — saturation ignored; expensive actions not powerful enough to justify saving turns.
- **3-player area-control problem** — two players over-fight one region, third sweeps the rest.

## Canonical sources

**Books** — *Characteristics of Games* — Elias, Garfield & Gutschera (MIT Press, 2012); *GameTek: The Math and Science of Gaming* — Geoff Engelstein; *Achievement Relocked: Loss Aversion and Game Design* — Geoff Engelstein (2020); *Building Blocks of Tabletop Game Design* — Engelstein & Shalev (CRC Press, 2019); *Uncertainty in Games* — Greg Costikyan (MIT Press, 2013); *Playing to Win* — David Sirlin; *The Art of Game Design* — Jesse Schell; *Rules of Play* — Salen & Zimmerman.

**Papers** — Neller & Presser, "Optimal Play of the Dice Game Pig" (UMAP Journal 25(1), 2004); Hunicke, LeBlanc & Zubek, "MDA" (2004).

**Blogs & podcasts** — daniel.games (Daniel Piechnick design course: Balance, Catch-Up Mechanics, Randomness, Game Length, Playtesting — heavily quoted above); League of Gamemakers — leagueofgamemakers.com (Strain, "Finding Balance Before Playtesting," 2017); Stonemaier Games design blog — stonemaiergames.com; Board Game Design Lab — boardgamedesignlab.com; Games Precipice — gamesprecipice.com (player-scaling series); Ludology podcast; GameTek on The Dice Tower; BoardGameGeek wiki/forums (weight scale, glossary).

**Tools** — AnyDice (anydice.com + /docs; "Game Design with AnyDice" at thoughtfuldane.com); hypergeometric calculators (cardgamecalculator.com, Stat Trek); spreadsheets (EV/path, action accounting); Tabletop Simulator (~$20) + Discord playtest servers; r/tabletopgamedesign; emerging AI-simulation playtesting for balance metrics at scale.

**Math reference** — Wikipedia: "Nontransitive dice" (Efron's dice), "Dynamic game difficulty balancing" (rubber-banding, Mario Kart), "Hypergeometric distribution", "Pig (dice game)".
