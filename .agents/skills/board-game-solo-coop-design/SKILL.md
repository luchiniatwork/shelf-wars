---
name: board-game-solo-coop-design
description: >
  Solo and cooperative board game design. Use when the user wants to add a solo mode ("design a solo
  variant", "add an automa", "AI opponent", "virtual player", "bot deck", "beat your own score"),
  build or choose a cooperative structure ("full co-op vs semi-co-op vs traitor vs one-vs-many",
  "team game"), fix quarterbacking ("alpha player problem", "one player tells everyone what to do",
  "dominant leader", "table captain"), tune co-op difficulty ("win rate target", "difficulty dial",
  "too easy", "too hard", "escalation", "Pandemic-like tension"), design loss conditions and pacing
  ("doom track", "deck-out timer", "loss clocks"), or scale a co-op/solo game by player count. For
  probability, EV, and statistical analysis of win-rate logs use board-game-math-balance; for playtest
  protocols use board-game-playtesting; for mechanism selection use board-game-mechanisms; for solo-mode
  campaign positioning use board-game-crowdfunding; for writing the automa rulebook use
  board-game-rules-writing.
---

# Solo & Cooperative Design

## When to use / when not to use

Use when the task is: designing or auditing an automa/AI opponent, deciding whether a game should have a
solo mode, choosing or fixing a co-op structure (full, semi-co-op, traitor, one-vs-many, team),
diagnosing quarterbacking/alpha-player behavior, building the co-op difficulty curve and loss conditions,
calibrating difficulty dials against win-rate targets, or scaling a solo/co-op design across player counts.

Do NOT use for:
- Computing odds, EV, cost curves, or statistical confidence on win-rate logs → `board-game-math-balance`
- Playtest session protocols, feedback instruments, recruitment → `board-game-playtesting`
- Mechanism taxonomy and core-loop construction → `board-game-mechanisms`
- Fun theory, agency, session arc for multiplayer-competitive games → `board-game-design-theory`
- Solo mode as a crowdfunding selling point, pledge tiers → `board-game-crowdfunding`
- Rulebook text for the solo variant → `board-game-rules-writing`

## Core principles

1. **A solo opponent must impersonate a player, not generate weather.** The Automa Factory philosophy
   (Morten Monrad Pedersen, founded 2015 after Stegmaier commissioned a Viticulture solo mode in Feb 2014):
   the automa takes a human seat, the human keeps the multiplayer rules and win/lose criteria, key player
   interactions are simulated, and the human faces the same decisions as multiplayer. If your "AI" is just
   a random-event table, players feel no adversary — build a fake player instead.
2. **Abstract the opponent's internal state, keep its external pressure.** Strip everything that doesn't
   touch the human: the Scythe automa has no player mat. Simulate the *outputs* of an economy (blocking
   spots, competing for majorities, racing a score track), not the economy itself. (Automa Factory
   principle 6; Cornelius: "abstract away as much as is possible.")
3. **Budget the upkeep.** Solo players accept upkeep only if it is "not a huge amount more than the
   original game" (BGG solo-community survey via Cornelius, League of Gamemakers 2016). Working target:
   automa turn ≤ ~30 seconds and automa overhead ≤ ~20% of total session time [contested community
   heuristic]. Every extra deck, lookup, or sub-decision spends against this budget.
4. **Predictable enough to plan around, varied enough to surprise.** Deck-driven priority lists (a card
   says "do X; if impossible, do Y") beat dice-chaos tables: the player can read the revealed card and
   adapt, which creates counterplay. Pure randomness removes threat-readability; perfect determinism
   removes replay. One revealed-card lookahead is the standard compromise.
5. **The human never decides for the automa.** If the player makes the bot's choices, they will (even
   honestly) bias them. Resolve ties with arrows, priority lists, nearest/leftmost rules — never "your
   choice" (Automa Factory principle 5).
6. **Give a real win condition, not a high-score chase.** BGG solo players explicitly reject solo modes
   that are only "beat your previous score" (Cornelius, LoG 2016). Ship win/lose vs. the automa or vs. a
   scenario threshold; keep score-chasing as a secondary mastery layer at most.
7. **Solo is near table stakes for crowdfunding euros — design it in, don't bolt it on.** Stonemaier's
   publishing guideline is euros playable 1–5 (per their 2025 Tokaido acquisition post); they estimate
   ~10% of tabletop customers primarily play solo [contested, their estimate]. A dedicated solo-only
   niche even sustains monthly crowdfunding campaigns (Best With 1 Games, ~60k games shipped since Jan
   2024 [contested — publisher-reported figure, not independently verified]). Budget solo development
   from day one: retrofitting costs more and shows.
8. **Co-op difficulty is architecture, not a vibe.** Build a ratchet: pressure must escalate on a
   schedule players can feel. Pandemic's epidemic card is the exemplar — one card that (a) raises the
   infection rate, (b) spikes a new city to 3 cubes, (c) reshuffles the infection discard onto the deck
   so known hot zones re-flare. Provide dials or feedback loops so challenge tracks player skill
   (Leacock).
9. **Set an explicit win-rate target before tuning.** Designer-stated first-play targets span 0%–75%
   (see table). There is no universal number; there IS a universal failure: no target at all. Pick the
   target from audience and structure, publish difficulty settings, and calibrate against logged results.
10. **Quarterbacking is structural, not social.** It flourishes when three legs coincide: perfect shared
    information, symmetric player capability, unlimited communication (plus a fourth: low per-player
    cognitive load). Break at least one leg deliberately. "A good co-op design knows [one player running
    the game] is a possibility and figures out something that gets in the way of that" (Mike Selinker).
    Leacock: worst with mismatched skill levels or strangers; it can't be eliminated, only designed around.
11. **Semi-co-ops fail by kingmaking and spite.** If one player can lose individually but drag everyone
    down, losing becomes a tie and a loser becomes the tie's author (Tom Jolly, LoG 2015). Either remove
    the everyone-loses state, give an escape/stash mechanism, or accept that "competitive elements will
    always rule cooperative elements" and design for that.
12. **Scale the system, not just the numbers.** More players changes more than monster count: hand-economy
    totals, role coverage, coordination cost, downtime. Pandemic's action:infection ratio is constant
    (4 actions vs. current rate, per player, at any count) — which is why the community still argues about
    which count is hardest [contested]. Test every advertised count; never extrapolate.

## How to apply it

### A. Design an automa for a euro (procedure)
1. List every interaction a human opponent creates (blocking, racing, competing for scarce cards/tiles,
   shared markets, end-trigger pressure).
2. For each, define the *minimum simulation*: what does the human need to feel? (e.g., "2 of 8 action
   spots blocked each round" — not a fake worker with fake resources.)
3. Choose the driver: priority-list action cards (default), deck-as-timer, race track, or app (see
   `references/automa-design.md` for the pattern catalog and when each fits).
4. Build the deck: small (typically 10–25 cards), each card = one primary action + tiebreak arrows/icons;
   include a reshuffle/escalation beat if the multiplayer game has rising pressure.
5. Add 3–5 named difficulty tiers that vary *bonuses/quantities*, not rules (e.g., automa scores +N per
   tier, or starts with extra assets). Rules forks per tier are a teachability bug.
6. Upkeep audit: time 10 automa turns; total automa admin must stay ≤ ~20% of session. Cut state first.
7. Verify against the Automa Factory 6-principle checklist (reference file).
8. Blind-test solo specifically — solo testers find upkeep and ambiguity bugs multiplayer testers can't.

### B. Calibrate difficulty dials and win rate
1. Choose the target from the audience table below (first-play vs. repeat-play targets differ).
2. Pick 1–3 dial types: quantity knobs (more/fewer threat cards), stat knobs (bonuses), resource knobs
   (starting assets), timer knobs (round/clock length), rules knobs (extra enemy powers — use sparingly).
3. Define 3–5 named settings (Introductory / Standard / Heroic is the Pandemic template: 4/5/6 epidemic
   cards in the deck).
4. Log every test play: setting, win/lose, margin, turns played, when the outcome felt decided.
5. Change ONE dial per test batch. ~10 logged plays per setting is enough for dial-*direction* triage
   (obviously too easy/hard — at p=0.5, n=10 carries ±31 pp); a trustworthy win-rate estimate with a
   usable confidence interval needs ~100+ logged plays of that config (n=100 → ±10 pp) — CI table and
   formula in `board-game-math-balance`. [contested]
6. Ship the rulebook with the settings named and with advice for first-time players ("start at Standard").

### C. Diagnose and mitigate quarterbacking
Run the checklist; full mitigation catalog with exemplars in `references/coop-antipatterns.md`:
- [ ] Can one player legally/computationally see all relevant state? → add hidden or asymmetric info
      (Hanabi, Mysterium) or raise per-player cognitive load (Spirit Island).
- [ ] Can players talk without limit? → constrain channel (The Crew's radio tokens), ban it (Magic Maze),
      compress it with real time (Space Alert), or make communication cost resources (Hanabi clue tokens).
- [ ] Are all players interchangeable? → asymmetric roles/powers with private domains (Pandemic roles),
      split controls (Magic Maze movement directions), personal stakes (Dead of Winter secret objectives).
- [ ] Is one player's turn solvable by another? → individual ownership devices (Pandemic: The Cure's
      personal dice — Leacock: "I've never seen a player reach across the table and roll another player's
      dice!").
- [ ] Accept it when appropriate: teaching games, family games, intentional mentor dynamics. House-rule
      fallback (Strain): advice allowed only from adjacent players.

### D. Choose a co-op structure
- **Full co-op** (Pandemic, Forbidden Island): everyone wins/loses together. Default; needs quarterbacking
  countermeasures and a difficulty ratchet.
- **Co-op with individual winner** (Legendary's scoring variant, Castle Panic Master Slayer): beware
  leader-tanking and spite endings (Jolly). Use only with no everyone-loses state or with escape valves.
- **Traitor / hidden roles** (Shadows over Camelot 2005, Battlestar Galactica 2008, Dead of Winter 2014):
  suspicion blocks open solving, but demands balance for the betrayer and rules for reveal timing.
- **One-vs-many** (Fury of Dracula, Descent 2e, Specter Ops): a human overlord replaces AI upkeep;
  consider the app-driven variant (Mansions of Madness 2e 2016, Journeys in Middle-earth 2019) when the
  overlord seat is a barrier.
- **Solo-only designs** (Friday 2011, Under Falling Skies 2020, Final Girl 2021): design the loop
  around one brain from the start — see principle 7 and reference file.
- **Team vs team** (Codenames teams 2015, Decrypto 2018, Captain Sonar 2016): two co-op teams compete;
  each team is a mini full co-op with the same quarterbacking and difficulty-ratchet needs. Design
  handles: shared clue-giver/overlord roles that rotate or gate information (Codenames spymaster),
  simultaneous team turns so neither side waits (Captain Sonar's real-time sub stations), and skill
  asymmetry between seats so every teammate owns a subsystem. Balance target: near-50% match win rate
  between equally skilled teams — validate per `board-game-math-balance`.

### E. Build the tension ratchet and loss clocks
1. Design 2–3 *visible, independent* loss clocks. Pandemic's three: 8 outbreaks, disease-cube shortage,
   player-deck exhaustion (deck-as-timer). Independent clocks force triage.
2. Engineer escalation into the threat deck, not just more threat: rate increase + new-hot-spot spike +
   discard-recycling (Pandemic's Increase/Infect/Intensify) is the canonical 3-part escalation step.
3. Alternate hope and fear (Leacock: Pandemic works through "alternating waves of hope and fear") — give
   players a stabilizing tool right after each escalation beat.
4. Let losing be fast: mechanisms that end doomed sessions early protect retry morale (Hawthorne, Mice
   and Mystics).
5. Never let players lose 30+ minutes before the loss registers: if a position is unwinnable, the game
   should end or telegraph the cliff.

### F. Scale by player count
1. Write the per-round budget for each count: team actions vs. system pressure per round (not per player).
2. Scale what the extra players *trivialize* (board coverage, role coverage, total held cards) and what
   they *complicate* (coordination, information passing, travel).
3. Prefer per-player quotas in threat effects ("spawn 1 enemy per hero") over flat counts; flat counts
   make low counts impossible or high counts trivial.
4. Solo-first check: if your game is co-op, decide whether solo = one player controlling multiple roles
   (official Pandemic solo variant: 3 roles, one shared hand, 7-card limit) or a dedicated automa — and
   say which in the rules.

## Key numbers & heuristics

| Heuristic / datum | Value | Source |
|---|---|---|
| Pandemic difficulty dial | 4 / 5 / 6 Epidemic cards = Introductory / Standard / Heroic | Pandemic rulebook (Z-Man) |
| Pandemic loss clocks | 8 outbreaks; cube shortage when needed; player-deck exhaustion | Pandemic rulebook |
| Epidemic escalation step | Increase rate → Infect bottom card to 3 cubes → Intensify (reshuffle infection discards onto deck) | Pandemic rulebook |
| Pandemic setup infection | 9 cities: 3 cities ×3 cubes, 3 ×2, 3 ×1 (18 cubes) | Pandemic rulebook |
| First-play co-op win-rate targets | Bauza 0% (Ghost Stories); De Witt 40% (Castle Panic); Leacock ~40% (Pandemic); Hawthorne 70% (Mice & Mystics); Selinker 75% (Pathfinder ACG) | League of Gamemakers, "Win Ratios in First Time Cooperative Play" (2016) |
| Legacy/campaign session target | ~2:1 win:loss (~67%) to protect morale across irreversible sessions | Matt Leacock, LoG interview (2017) |
| Solo win-rate players *say* they want | 25–30% win rate | BGG solo-community survey via Cornelius, LoG 2016 [contested] |
| Solo share of market | ~10% of tabletop customers primarily play solo | Stonemaier estimate, 2025 [contested] |
| Automa upkeep budget | automa turn ≤ ~30 s; admin ≤ ~20% of session | community heuristic [contested] |
| Automa deck size | typically ~10–25 cards (Tokaido automa pack: 23 cards + rulebook + reference guides) | Stonemaier Tokaido post 2025; community practice |
| Difficulty tiers | 3–5 named settings; vary quantities/bonuses, not rules | Automa Factory practice; Pandemic template |
| Gloomhaven scenario level | average party level ÷ 2, rounded up, ±1 for taste; stats/gold/traps key off level 0–7 | Gloomhaven rulebook (2017) |
| Spirit Island difficulty | published difficulty ratings 1–10 per adversary/level | Spirit Island rulebook (2017) |
| Calibration sample | one dial per batch; ~10 logged plays = dial-direction triage only (±31 pp at n=10); ~100+ plays per config for a rate estimate (±10 pp) | practitioner practice [contested]; CI math in `board-game-math-balance` |

## Common pitfalls

- **Bookkeeping bot**: automa upkeep eats the game (multi-deck lookups, fake resource tracking). Manifests
  as testers saying "fun, but I spent half my time running the AI." Fix: cut internal state (principle 2).
- **Weather machine**: opponent is a random-event deck with no persistent threat to read. Players report
  "it doesn't feel like an opponent." Fix: priority lists + visible momentum.
- **High-score cop-out**: solo mode is only "beat your best score." BGG solo players explicitly reject
  this (Cornelius). Fix: win/lose condition vs. automa or scenario threshold.
- **Quarterbacked co-op**: one experienced player plays four pawns while others execute. Detect by
  watching who speaks in tests (Leacock: watch, don't just ask). Fix per checklist C.
- **Flat difficulty**: threat is constant from turn 1 to end; no ratchet, no climax. Fix: escalation step
  + loss clocks (procedure E).
- **Unwinnable-but-still-playing**: early bad luck dooms the run but the loss registers 45 minutes later.
  Fix: fast-loss mechanisms and visible doom (Hawthorne).
- **Reverse kingmaker (semi-co-op)**: a player who can't win tanks the group so "everyone loses" feels
  like a tie (Jolly). Fix: remove everyone-loses states or add escape/stash valves.
- **Free-stuff difficulty**: tiers that add *rules* (new enemy powers, exceptions) instead of quantities —
  teachability collapses and testing surface explodes. Fix: quantity/stat/resource dials first.
- **Count-extrapolation**: tested at 2p and 4p, shipped 1–5. Fix: per-round budget per count (procedure F).
- **Automa as stretch-goal afterthought**: solo mode promised late, designed late, reads as bookkeeping.
  Fix: principle 7 — design from day one.

## Reference files

- `references/automa-design.md` — LOAD WHEN designing or auditing an actual automa/AI deck: Automa
  Factory 6 principles in depth, pattern catalog (priority lists, deck-as-timer, race track, flowchart
  bots, app-driven), worked example, upkeep audit checklist, difficulty-tier design.
- `references/coop-antipatterns.md` — LOAD WHEN diagnosing quarterbacking, semi-co-op/traitor failures,
  or difficulty-feel complaints: mitigation catalog mapped to exemplar games, semi-coop failure taxonomy,
  failure-mode table with detection signals.
- `references/coop-difficulty-architecture.md` — LOAD WHEN building the escalation curve, loss clocks,
  or a calibration plan: Pandemic dissection with exact numbers, dial catalog, win-rate calibration
  worksheet, player-count scaling methods.

## Related skills

- `board-game-design-theory` — agency, interesting decisions, session arc (why co-ops need ratchets)
- `board-game-mechanisms` — mechanism taxonomy; pick the threat/AI driver mechanisms here
- `board-game-math-balance` — probability/EV, cost curves, statistics for your win-rate logs
- `board-game-theme-narrative` — thematic fit of AI opponents, traitor fiction, nemesis design
- `board-game-prototyping` — building the automa deck/bot physically or in TTS
- `board-game-playtesting` — solo/co-op test protocols, logging, kill criteria
- `board-game-rules-writing` — writing the solo variant rulebook and automa reference cards
- `board-game-manufacturing` — extra decks/cards for solo modes in component specs
- `board-game-publishing` — solo mode in sell sheets; publisher expectations (1–5 player counts)
- `board-game-crowdfunding` — solo mode as campaign feature, stretch-goal positioning
- `board-game-market-analysis` — solo/co-op segment sizing and comparable titles
- `board-game-accessibility` — cognitive load of automa upkeep; solo mode as access to the hobby
