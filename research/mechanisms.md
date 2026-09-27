# Research Digest — Board Game Mechanisms: Taxonomy & Selection

## Core frameworks & models

- **BGG mechanism taxonomy (BoardGameGeek, community-maintained)** — the de-facto controlled vocabulary: each BGG game entry carries 1–N "mechanisms" tags (Worker Placement, Set Collection, etc.). Community-cited count was **51 mechanisms circa 2014** (Reddit/BGG advanced search); the list has grown since and is now well past 150 [contested — no official stable count; treat any exact number as a snapshot].
- **Building Blocks of Tabletop Game Design — Geoff Engelstein & Isaac Shalev (CRC Press, 2019)** — encyclopedia of **~196 mechanisms grouped into 13 categories** (e.g., Game Structures, Turn Order, Actions, Resolution, Game End & Victory, Uncertainty, Economics…). The standard printed taxonomy.
- **Characteristics of Games — George Skaff Elias, Richard Garfield, Karl Robert Gutschera (MIT Press, 2012)** — analytic framework of game "heuristics" (length, number of players, elimination, catch-up mechanics) used to diagnose design tradeoffs rather than catalog mechanisms.
- **MDA: Mechanics–Dynamics–Aesthetics — Hunicke, LeBlanc & Zubek (2004)** — mechanics create run-time dynamics, which create player-felt aesthetics; the canonical justification for choosing mechanisms by intended *experience*, not by feature checklist.
- **Uncertainty in Games — Greg Costikyan (MIT Press, 2013)** — **11 sources of uncertainty** (performative, solver's, player unpredictability, hidden information, randomness, analytic complexity…). Explains why even luck-free games stay tense: other players' minds are the randomizer.
- **League of Gamemakers, "Breaking Down Games" — Teale Fristoe (2015)** — dissects games into **8 systemic "parts"**: Goal, Actions, Resources, Acquisition, Scoring, Elimination, Uncertainty, Interaction. Notes elimination "leads to a pretty bad action arc, as players feel much weaker towards the end."
- **Input vs. output randomness — Geoff Engelstein (Ludology/GameTek)** — input luck (roll, then decide how to use it: *Castles of Burgundy*) preserves agency; output luck (decide, then roll to see if it worked: *Risk*) creates swinginess. Core lens for dice design.
- **Stonemaier 10-step design process — Jamey Stegmaier** — Motivation → Ideation → Research → Prototype (MVP, no rulebook) → solo "plunge" playtest → functionality playtests → fun playtests → rulebook → blind balance/clarity playtests → pitch/publish. His design tenets push "elegant, streamlined core games that have incredible depth and complexity," quick setup, and smooth flow.
- **Depth-to-complexity ratio (community consensus, echoed by Knizia)** — elegance = maximal decision depth per rule. Knizia: "Simple games, but then the people bring themselves into it… out of the simplicity, a second level of depth." Saint-Exupéry's "perfection… when there is nothing left to take away" is the most-quoted bloat antidote in design blogs.

## Catalog / techniques

Mechanism entries: experience — tension source — scaling — exemplars — common partners.

- **Worker placement** — competition over scarce actions; blocking. Tension: you can never do everything; turn order is a resource. Scales 1–5; low counts reduce contention, high counts increase hate-drafting of spaces (Lords of Waterdeep gets *more* tense at 4–5p). Exemplars: Keydom (1998, R. Breese — first), Caylus (2005 — popularizer), Agricola (2007 — feeding pressure: 2 food/family member, accumulating spaces), Lords of Waterdeep (2012 — contracts + WP), Viticulture (2013 — Grande worker breaks blocking; split-season boards mitigate scaling). Partners: engine building, contracts, resource conversion.
- **Deck/bag/pool building** — growth fantasy; you literally build your tool. Tension: curation vs. draw luck; dilution. Scales cleanly (solitaire-friendly) but low interaction → "multiplayer solitaire" risk. Exemplars: Dominion (2008 — genre origin), Quarriors (2011 — dice pool), Orléans (2014 — bag building), Clank! (2016 — recombined with point-to-point board), Quacks of Quedlinburg (2018 — bag building + push-your-luck). Partners: engine building, set collection, push-your-luck, route building.
- **Drafting (card/tile/dice)** — simultaneous hidden choice; reading opponents. Tension: keep-vs-deny; you see a fraction of the pool. Card drafting (7 Wonders 2010, Sushi Go! 2013) loses texture at 2p (needs dummy/2p variants; best 4–6). Tile drafting: Azul (2017 — factory-offer denial, scales 2–4 smoothly), Kingdomino (2016 — draft order tied to tile quality). Dice drafting: Sagrada (2017 — pool = 2×players+1 dice, an explicit scaling rule). Partners: tableau/engine building, set collection, polyomino placement.
- **Set collection** — completion dopamine; visible progress. Tension: shared scarcity, timing. Exemplars: Ticket to Ride (2004), Sushi Go!, Splendor (2014). Partners: drafting, hand management, contracts.
- **Area control / area majority** — visible map drama, territorial identity. Two types: exclusive ownership (war games: Risk 1959, Dune 1979) vs. majority scoring (Euros: El Grande 1995 — first big area-majority success; Web of Power/China 2000/2005 — "purest" distillation; Small World 2009 — deterministic conquest math: defenders+1). Tension: overextension vs. concentration; scoring-round timing. Known 3-player problem: two players over-contest one region while the third sweeps the rest. Tigris & Euphrates (1997) — grid tile-based influence. Rattus (2010) inverts it: sometimes you *don't* want the majority. Partners: action points, card-driven actions, route building, negotiation.
- **Tile-laying** — shared map emerges; spatial puzzle. Tension: drawing what you need; exploiting others' placements. Exemplars: Carcassonne (2000), Kingdomino, Isle of Skye (2015 — adds pricing). Partners: area majority, set collection, network building.
- **Push-your-luck** — stop/continue decisions; audible table drama. Tension: probability vs. greed; players systematically misestimate odds. Exemplars: Can't Stop (1980, Sackson), Incan Gold (2005 — simultaneous reveal adds group psychology), Quacks (2018), Martian Dice (2011). Partners: bag building, roll-and-write.
- **Roll-and-write / flip-and-write** — simultaneous play, near-zero downtime, minimal components. Tension: committing random results to permanent grid space; combo chaining. Exemplars: Yahtzee (1956 — ancestor: reroll mitigation), Qwixx (2012), Ganz schön clever (2018 — dice-selection cascade), Welcome To (2018 — flip-and-write, no dice; supports 1–100 players), Cartographers (2020 — shared goals + ambush cards). Failure mode: multiplayer solitaire; fix via shared races or denial. Post-2018 boom driven by low cost and mass player-count.
- **Engine / tableau building** — compounding power fantasy; slow start → explosive end. Tension: invest vs. score now; watch opponents' engines. Exemplars: Race for the Galaxy (2007), Splendor, Terraforming Mars (2016), Wingspan (2019 — action-cube activation). Failure mode: runaway leader → needs catch-up or scoring caps. Partners: deck building, dice-as-resources (Roll for the Galaxy 2015).
- **Trick-taking & climbing** — micro-round structure, 20+ decisions/hand. Tension: hand depletion timing; reading voids. Renaissance exemplars: The Crew (2019 — cooperative trick-taking, Kennerspiel 2020), Cat in the Box (2022), Scout (2019 — climbing; can't rearrange hand). Tichu (1991) — climbing ancestor. Partners: ladder/role bidding, cooperative constraints.
- **Auctions** — player-driven pricing solves balance-by-valuation. Types: **open/English** (Modern Art 1992, Power Grid 2004 — once-passed = out of that plant auction; tension + "waiting out" strategy risk), **sealed bid** (valuation prediction, removes bluff-calling), **Dutch/descending** (urgency; favors fast deciders), **once-around** (Ra 1999 — sun discs are spent bids; Cyclades 2009 — one bid per god; Cyclades Legendary Edition uses an exponential bidding scale to shorten bidding). Knizia's "auction trilogy": Modern Art, Medici (1995), Ra. Scaling: weak below 3 players (too little competition). Failure mode: new players can't value lots (Power Grid's market correction mitigates). Partners: hand management, set collection, area control (Revolution! 2009 — blind bid with 3 currencies).
- **Route / network building** — map optimization, connectivity goals. Tension: contested corridors, capacity. Exemplars: Ticket to Ride, Power Grid (connection phase), Brass (2007 — network = economy), Through the Desert (1998). Partners: pick-up-and-deliver, stock/market, area control.
- **Pick-up-and-deliver** — logistical puzzle; route efficiency. Tension: capacity limits, delivery timing races. Exemplars: Himalaya (2002), Railways of the World (2005), Istanbul (2014 — mancala-ish merchant movement). Partners: contracts, network building, engine upgrades.
- **Hand management** — few plays from many options; timing is everything. Tension: when to spend good cards. Exemplars: Twilight Struggle (2005 — opponent-event cards), Hanamikoji (2013). Partner to nearly everything.
- **Action points (AP)** — fixed budget/turn (Pandemic 2008: 4 actions; Tikal 1999: 10 AP) — enables combos but causes AP-paralysis. Mitigations: sub-action menus, forced sequencing.
- **Action queue / programming** — commit before resolution; comedy and bluffing from misprediction. Exemplars: RoboRally (1994), Colt Express (2014), Mechs vs. Minions (2016 — damage = program locks). Partners: simultaneous selection, modular board.
- **Simultaneous selection** — kills downtime; double-think tension. Exemplars: Diplomacy (1959), Race for the Galaxy role selection, 7 Wonders, Food Chain Magnate turn structure. Scales upward beautifully — the go-to fix for 5+ player downtime.
- **Hidden roles / social deduction / traitor** — conversation-as-gameplay. Needs 5+ players (Resistance 5–10; Avalon adds asymmetric information). Traitor in cooperative frame: Shadows over Camelot (2005 — first modern traitor), Battlestar Galactica (2008 — mid-game loyalty deal fixes early accusations), Dead of Winter (2014 — secret objectives soften pure traitor). Werewolf/Mafia (1986, Davidoff). Pitfalls: eliminated players sit out; experienced-player meta dominates.
- **Semi-cooperative** — shared loss, individual win. Tension: how much do I help? Exemplars: Dead of Winter, CO₂ (2012), New Angeles (2016). Failure: kingmaking at endgame; needs shared-loss enforcement.
- **Legacy / destruction / unlockables** — permanent consequence converts decisions into narrative. Risk Legacy (2011, Rob Daviau — genre origin; deface/destroy components; inspired by episodic RPG structure; cites Risk 2210 A.D., Betrayal, HeroScape). Pandemic Legacy (2015, Daviau/Leacock — 12-month campaign, 12–24 sessions; #1 on BGG for years). Charterstone (2017, Stegmaier — playable post-campaign state). Gloomhaven (2017 — envelope/character unlocks, no destruction). Design needs: paced reveals (sealed envelopes), meaningful permanence, decision-tree cost.
- **Dice mitigation techniques (Engelstein et al.)** — rerolls (Yahtzee, King of Tokyo); +/-pip modifiers (Castles of Burgundy workers); dice-as-resources instead of pass/fail checks (Alien Frontiers 2010, CoB); roll-many-choose-subset; bell-curve aggregation (2d6 Catan: 7 = 6/36 ≈ 16.7% vs. flat d20); mitigation currencies (fate/luck tokens); degrees of success; push-your-luck framing; drafting dice from a shared pool (Sagrada); tech/powers that convert bad rolls (Euphoria, Grand Austria Hotel). Rule: prefer input luck; if output luck, price it with reroll/modify options.
- **Rondel** — action wheel: cost = distance travelled; future-denial tension (you can't revisit cheaply). Exemplars: Antike (2005, Mac Gerdts — popularizer), Imperial (2006), Navegador (2010), FCM-style loops. **Mancala action selection**: sow-and-resolve; planning = counting. Exemplars: Trajan (2011, Feld — mancala + rondel hybrid), Five Tribes (2014, Cathala), Istanbul (stack movement variant).
- **Tech trees** — long-horizon investment asymmetry. Exemplars: Civilization (1980), Through the Ages (2015), Gaia Project (2017). Partners: engine building, action points.
- **Modular board** — replayability via setup variance (Catan hexes, Eclipse). Doubles as scaling tool (board size ∝ player count).
- **Memory** — pure (Memory) or embedded (Hanabi inverted-information; sleuthing in deduction games). Accessibility caveat.
- **Dexterity** — physical skill as resolution (Crokinole, Flick 'em Up 2015, Catacombs 2010, Ascending Empires 2011 dexterity+area control). Accessibility caveat; polarizing.
- **Negotiation / trading** — unscripted player economy. Chinatown (1999), Catan trading, Diplomacy, Bohnanza (1997 — forced hand-order trading). Downtime and "alpha negotiator" risks.
- **Voting** — group judgment as resolution (Werewolf eliminations, New Angeles, Democracity). Needs odd counts / tiebreakers.
- **Storytelling** — constrained narrative generation (Once Upon a Time 1993, Tales of the Arabian Nights 1985). Low strategy tolerance groups.
- **Deduction grids / logic** — information triangulation. Clue (1949), Cryptid (2018 — honest-information rules), Alchemists (2014 — app-checked logic grid).
- **Polyomino placement / pattern building** — spatial Tetris-fit puzzle. Patchwork (2014 — time-track economy), Barenpark (2016), Isle of Cats (2019 — draft + polyomino + payment), Cascadia (2021 — pattern scoring, SdJ 2022). Solitaire-leaning; add drafting for interaction.
- **Contracts** — quests as score funnels (Lords of Waterdeep, Century: Spice Road 2017, Wingspan bonus cards). Turns engine output into goals.
- **Market / speculation** — value manipulation + timing of exits. Acquire (1964, Sackson), Stockpile (2015 — insider info), Container (2007 — closed player economy), Power Grid resource market (price scales with demand).
- **Tug-of-war tracks** — zero-sum bipolar meters concentrate conflict. Twilight Struggle influence, Watergate (2022 — momentum track), 13 Days (2016). Best at exactly 2 players (or 2 teams).

## Numbers, heuristics & rules of thumb

- **How many mechanisms:** no authoritative count exists. Community rule of thumb: **1 core mechanism + 2–3 supporting mechanisms** [contested as a universal rule — source is consensus across designer blogs, not a named originator]. The binding constraint is teachability and depth-to-complexity ratio, not a count. Engelstein's *The Expanse* postmortem: cut faction goals, an economy system, and a tension track because they "pushed the game past the complexity we wanted for the target audience" without adding interest.
- **BGG mechanism list:** ~51 (2014 citation) → significantly longer today [contested; list is crowd-edited].
- **Building Blocks of Tabletop Game Design:** 196 mechanisms, 13 categories.
- **Costikyan uncertainty sources:** 11.
- **League of Gamemakers system parts:** 8.
- **Sagrada dice pool:** 2n+1 dice for n players (5/7/9 at 2/3/4p) — template for scaling shared pools linearly.
- **Catan dice math:** 7 = 6/36 ≈ 16.7% of 2d6 outcomes (6/8 at 5/36) — the canonical bell-curve-vs-flat argument.
- **Pandemic Legacy campaign:** 12 in-game months, ≤2 attempts/month → 12–24 sessions.
- **Player-count behavior (consensus):** auctions and social deduction fail <3 and <5 players respectively; open drafting thins at 2p (add dummy hands); simultaneous mechanisms are the default fix at 5+p; 3-player area control invites kingmaking-by-proxy.
- **Stegmaier tenets:** quick setup, easy to learn, smooth flow, meaningful choices — use as mechanism-selection filter.
- **Playtest pipeline (Stegmaier):** solo plunge → family functionality → friends for fun → written rulebook → blind tests with surveys; "probe for examples and reasons, not solutions."

## Best-practice checklists

**Selecting a mechanism:**
1. Name the target aesthetic first (MDA): tension, growth, drama, puzzle, social?
2. Pick the tension source explicitly (scarcity, blocking, hidden info, probability, time).
3. Check player-count math at min and max: contention at low count, downtime at high count.
4. Check teachability: one sentence for the core action?
5. Check the luck profile: prefer input luck; if output luck, attach reroll/modify/convert mitigations.
6. Verify it produces interaction appropriate to audience (blocking/denial = medium; direct conflict = high; shared races = low).
7. Kill it if it can't justify its rules weight (Saint-Exupéry test).

**Combining mechanisms into a core loop:**
1. One mechanism owns the turn structure (the core); others must feed its inputs or consume its outputs.
2. Close the resource loop: generate → convert → score. Every currency should be earnable, spendable, and scarce.
3. Use at most one primary randomizer; additional luck needs mitigation tech.
4. Funnel all subsystems into one scoring system (or two, one being a loss condition).
5. Test the loop solitaire before adding interaction layers (Fristoe: experiment with a single bare mechanic first).
6. Add downtime control (simultaneity, short turns) once the loop works.

**Scaling a design:**
- Linear shared pools (2n+1), modular board size, per-count setup cards (Agricola/7 Wonders "3+" cards), split seasonal boards (Viticulture).

## Common pitfalls & failure modes

- **Mechanical bloat** — subsystems that don't earn their complexity (Engelstein's Expanse cuts). Manifests as long teach, forgotten rules ("remember/except" moments in playtests — Stegmaier's red flag words).
- **Analysis paralysis** — too many equal options per turn (AP systems, big hand sizes); symptom: turn length variance exploding.
- **Multiplayer solitaire** — engine builders, roll-and-writes, deck builders with no contestable space; fix with shared races, drafting, or shared markets.
- **Runaway leader** — compounding engines without catch-up or caps; symptom: winner decided at 60% mark.
- **Kingmaking / 3-player area control** — two players' over-contest lets the third win uncontested (documented in area-majority literature).
- **Auction misvaluation** — novices can't price lots; open auctions develop "waiting out" stalls (Power Grid) — price floors, once-around formats, or market correction help.
- **Quarterbacking** — co-op + traitor designs where one alpha player directs others.
- **Player elimination downtime** — elimination "leads to a pretty bad action arc" (Fristoe); avoid in >45-min games.
- **Meta-dependent social deduction** — experienced groups steamroll; needs asymmetric information (Avalon) or mid-game reveals (BSG).
- **Legacy cost/replayability ceiling** — one group per copy; post-campaign state must still function (Charterstone's solution).
- **Dexterity & memory exclusions** — accessibility failures; never gate core scoring purely behind them for family/casual targets.
- **Push-your-luck math blindness** — players misjudge bust odds; good designs surface odds through repeated small rounds (Incan Gold) not single big ones.

## Canonical sources

- *Building Blocks of Tabletop Game Design: An Encyclopedia of Mechanisms* — Geoff Engelstein & Isaac Shalev (2019)
- *Characteristics of Games* — Elias, Garfield & Gutschera (2012)
- *Uncertainty in Games* — Greg Costikyan (2013)
- *The Kobold Guide to Board Game Design* — Mike Selinker (ed., 2012)
- *Eurogames: The Design, Culture and Play of Modern European Board Games* — Stewart Woods (2012, academic)
- *The Art of Game Design: A Book of Lenses* — Jesse Schell (2008)
- BoardGameGeek wiki "Game Mechanisms" — boardgamegeek.com/wiki/page/Game_Mechanisms (Cloudflare-blocked to scrapers; browse manually)
- Stonemaier Games blog — stonemaiergames.com/kickstarter/how-to-design-a-tabletop-game/ (design hub; 10-step process; 12 Tenets)
- League of Gamemakers — leagueofgamemakers.com (Mechanics archives; "Breaking Down Games")
- Board Game Design Lab — boardgamedesignlab.com (podcast + articles)
- Nerdlab — nerdlab-games.com (Mechanical Deep Dives series, e.g., 3-part card drafting)
- Ludology podcast & GameTek (Dice Tower) — Engelstein's randomness/luck material
- iSlaytheDragon "All Under Control: A Guide to Area Control/Majority" (2013) — islaythedragon.com
- Communities: Board Game Designers Forum, r/tabletopgamedesign, BGG design forums
