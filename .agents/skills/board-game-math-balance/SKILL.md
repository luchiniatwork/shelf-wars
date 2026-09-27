---
name: board-game-math-balance
description: >
  Mathematics, probability, and balance for board game design. Use when the user wants to compute dice or
  card odds ("2d6 distribution", "d20 vs 3d6", "dice pools", "exploding dice", "chance of drawing a card",
  "hypergeometric"), value push-your-luck wagers ("expected value", "should I roll again"), price components
  ("is this card overcosted", "cost curve", "power budget"), calibrate point salads ("are all paths
  viable"), balance factions ("asymmetric balance", "RPS triangle", "intransitive counters"), engineer
  feedback loops ("runaway leader", "rubber-banding", "catch-up mechanic", "kingmaking", "snowball"), set
  pacing ("how long should my game be", "turn length", "downtime", "player count scaling"), tune solo/co-op
  difficulty ("win rate", "difficulty dial", "too hard"), or judge balance from few playtests ("balanced
  after 5 plays"). For playtest protocols use board-game-playtesting; for automa/co-op structure use
  board-game-solo-coop-design; for mechanism selection use board-game-mechanisms.
---

# Board Game Mathematics, Probability & Balance

## When to use / when not to use

Use when the task involves numbers: dice/card probabilities, expected value, costing and power budgets,
point-salad calibration, faction/strategy balance, feedback-loop diagnosis, game-length and turn budgets,
player-count scaling math, difficulty win-rate statistics, or statistical interpretation of playtest results.

Do NOT use for:
- Which mechanism to pick, mechanism taxonomy → `board-game-mechanisms`
- Fairness *perception*, agency, fun theory → `board-game-design-theory`
- Playtest session protocols, feedback instruments, recruitment → `board-game-playtesting`
- Automa construction, co-op structure, quarterbacking, win-rate *target-setting* →
  `board-game-solo-coop-design` (that skill owns the target bands and the opponent's design; this skill owns
  the statistical validation of win-rate logs — CI and sample-size math below)
- Expressing odds/rules text → `board-game-rules-writing`

## Core principles

1. **Balance = every option viable, not every option equal.** An option chosen only ~25% of the time can
   still be balanced enough if it's worth considering (Daniel Piechnick, daniel.games). Imbalance inside a
   viability band is texture; Chess endures with a first-move advantage. Choose fun over balance, elegance
   over balance — but never ship a strictly-worse outcome at equal cost.
2. **Compute the whole distribution, never just the average.** d20 and 3d6 share mean 10.5, but P(≥16) is
   25% vs 4.6%. Distribution shape is the product: flat = swingy/readable, bell = reliable/skill-rewarding,
   pools = success-counting, exploding = rare spikes.
3. **Model first, playtest second (the "Tesla method").** Math finds structural imbalance before the table
   does (Christian Strain, League of Gamemakers 2017); playtests then measure *perceived* balance and find
   breakage. Players misperceive odds — told to "roll close to average," they pick 2 dice over 10, though 10
   is far more reliable (Strain).
4. **Convert everything to one currency.** Strain's effort (e): turns-to-acquire from nothing — free red
   card = 1e, card costing two reds = 3e; if one turn gathers 2 gold, gold = 0.5e. Piechnick: convert all
   costs/values to the game's lowest-common-denominator resource before comparing.
5. **Actions and turns are costs.** A "free" card still costs the draw/hand slot. An action costing 2× with
   2× reward is *better*, because both consume the same turn (Piechnick). Expensive, slow-to-reach effects
   must be ridiculously powerful to repay the saving turns.
6. **Price compression and area effects superlinearly.** Two effects in one action cost more than the two
   halves separately (premium ~25–50% [contested folk range]); effects hitting n targets scale at least
   linearly in cost, typically more for global effects.
7. **Every positive loop needs a named counterweight.** Success-breeds-success (engine, income, territory)
   is the runaway leader in waiting (*Characteristics of Games*, Elias/Garfield/Gutschera 2012; Sirlin's
   "slippery slope" in *Playing to Win*). Pair it with scarcity, a cap, proportional pressure, or an end
   trigger.
8. **Hide catch-up inside general arithmetic.** Never naked score-based handouts — they read as
   anti-meritocratic (Piechnick; counterexample: Isle of Skye's income-per-player-behind). Prefer structural
   levers (Power Grid's last-place-acts-first) over visible leader taxes.
9. **Downtime is multiplication.** Idle time per round = (n−1) × mean turn length: 5 players × 60 s turns =
   4 min idle per round. Fix turn length, shrink per-turn menus, or go simultaneous (7 Wonders holds ~30 min
   at 3–7 players via simultaneous drafting).
10. **No balance claim without a confidence interval.** A win rate from 20 plays carries ±22 pp; detecting a
    10-pp gap between two strategies needs ~390 plays *per arm* (binomial statistics). Use bots and EV
    models for fine distinctions; humans for feel and fun.
11. **A trailing player needs only ~5% win probability to stay engaged** (Piechnick) — guarantee that path,
    not equality.

## How to apply

### A. Audit the randomness
1. List every randomizer (dice, deck, bag, tile stack) and the decision it gates.
2. Classify each: **input randomness** (randomize, then decide — draw a hand, assign rolled dice, *Castles
   of Burgundy*) preserves agency; **output randomness** (decide, then roll to resolve — *Risk* combat,
   pass/fail checks) is swingy and anti-meritocratic when unmitigated (Geoff Engelstein, GameTek/Ludology;
   Piechnick: resolve contests with hidden information, e.g. defender may play a shield, instead of dice).
3. Compute each distribution in AnyDice → load `references/probability-tables.md`.
4. Check tail frequency per session: P(event) × rolls/session. A 5% crit happens ~3 times in a 60-roll
   game — players will treat it as normal, not rare. Design crit/fumble effects accordingly.
5. Add mitigation where output luck gates big outcomes: rerolls (King of Tokyo), ±pip modifiers (CoB
   workers), convert-bad-roll powers, luck currencies.

### B. Build cost curves & power budgets
1. Pick the LCD currency (usually turns/actions; Strain's e).
2. Tabulate every component's cost and effect; convert effects to the currency.
3. Fit power ≈ f(cost) by eyeball or regression in a spreadsheet; flag outliers >~1 residual SD for
   repricing or justification (build-around, fun spike, rarity).
4. Apply premiums/discounts: action compression +25–50% [contested folk]; multi-target/area ≥ linear;
   restriction or telegraphing = discount.
5. Invariants: no strictly-better option at equal cost; no infinite loops (output ≤ input of same currency);
   expensive actions must be *ridiculously* powerful (Piechnick).
6. Give every component a tunable number so fixes change numbers, never add rules (Piechnick: Radlands camps
   carry a corner number; weaker camps grant a larger starting hand).
→ Worked example: `references/balance-playbook.md`

### C. Calibrate a point salad
1. Enumerate scoring paths (typically 4–8 in Feld-style designs).
2. Estimate each path's realistic total VP and actions consumed for a competent player.
3. Compute VP/action per path; tune knobs (reward size, cost, scarcity, synergy slots) until paths sit
   within ~10–15% of the median [contested — widely repeated community heuristic, no single originator].
4. Ensure no fixed path ordering across board states — else it's a script, not a salad.
5. Validate with greedy-bot Monte Carlo before human tests.

### D. Engineer feedback loops
1. Diagnose: record player rank at 25/50/75% of game vs final rank across 10–20 plays or sims. Early rank
   locks in → snowball; leader changes every round → chaos/no agency.
2. Choose a policy per the game's promise: euro/engine games usually want mild snowball + bounded catch-up;
   family/conflict games want rubber-banding.
3. Pick levers from the catalog (ramps, big moves, proportional penalties, structural turn-order
   compensation, obscured leader, end-trigger timing) → `references/balance-playbook.md`.
4. Guard against overcorrection: catch-up so strong that leading early is *wrong* teaches sandbagging.
5. Kingmaking audit: any player who cannot win should lack the power to decide who does — use hidden
   scores, simultaneous reveals, multiple end conditions, self-directed goals for trailers.
6. Verify trailing players keep ≥ ~5% win chance at all times.

### E. Scale across player counts
1. Compute downtime at max count: (n−1) × turn length. If idle > ~2 min/round, add simultaneous phases,
   off-turn engagement (Catan/Machi Koro pay on others' turns), or end-of-turn card draw.
2. Scale congestible resources per count: board area (Small World ships 4 maps; Power Grid uses n regions),
   route rules (Ticket to Ride bans double routes at 2–3p), component counts (Sagrada dice = 2n+1), resource
   refresh tables (Power Grid).
3. Auctions and trading weaken below 4 players [contested folk] — provide alternate rules; conflict games at
   3p breed kingmaking (two fight over one region, third sweeps).
4. Test min AND max count, not just the sweet spot. Most playtests happen at 2p — verify it works there.

### F. Set difficulty (solo/co-op) & validate statistically
1. Pick a target win-rate band (target-setting is owned by `board-game-solo-coop-design`). Reference data:
   Matt Leacock — ≈40% win rate for first-time groups, and 60% for legacy-style sessions (LoG "Win Ratios in
   First Time Cooperative Play", 2016); 2:1 win:loss for legacy (2017 interview). Community bands for
   replayable co-ops run ~50–70% [contested — varies by source/audience].
2. Ship ≥3 difficulty knobs (Pandemic: 4/5/6 Epidemic cards).
3. Estimate win rate with models/bots first; tune threat density, not feel.
4. Log every play (win/loss, margin, config). Compute CI: half-width ≈ 1.96·√(p(1−p)/n). Do not declare
   balance below ~100 logged plays of a config.
→ Full statistics: `references/pacing-scaling-difficulty.md`

### G. Budget pacing & turn time
1. Pick a class target: filler ≤30 min (some 5–15), family 30–60, medium-light euro 20–30 (Piechnick),
   euro 60–120, heavy 90–180+ (BGG/industry usage).
2. Budget backwards: minutes = players × turns/player × seconds/turn ÷ 60. A 60-min 4p euro at 25
   turns/player allows 36 s/turn.
3. Cap the per-turn menu (~3–5 meaningful options) to fight analysis paralysis; deliver new information
   (card draw) at end of turn so players plan during downtime.
4. "A good game ends one turn too soon" (Piechnick); if players can complete every path, the game is too
   long. Cut a round, then cut another.

## Key numbers & heuristics

| Figure | Value | Use / source |
|---|---|---|
| 2d6 sums | 7 = 16.67%; 6/8 = 13.89%; 5/9 = 11.11%; 4/10 = 8.33%; 3/11 = 5.56%; 2/12 = 2.78% | Catan hex pips; P(6 or 8) = 27.8%; 7 (robber) ≈ once per 6 rolls (arithmetic) |
| d20 vs 3d6 | Both mean 10.5; d20 flat 5%/face; 3d6 SD ≈ 2.96, P(8–13) ≈ 67.6%, P(≥16) ≈ 4.63%, P(18) ≈ 0.46% | Choose flat (swingy) vs bell (reliable) resolution curve (arithmetic) |
| Exploding die EV | base × n/(n−1): d4 +33%, d6 +20%, d10 +11%, d20 +5.3% | Savage Worlds/Deadlands-style dice (algebra, verified) |
| Exploding reach paradox | Exploding d4 reaches ≥6 at 18.8% vs exploding d6 at 16.7% | Small dice spike more (computed) |
| Card odds (60-card, 7-card opener) | 4 copies: P(≥1) = 39.9%; 8: 65.4%; 12: 80.9%; 4-of by draw 10: 52.8%; 24 lands: P(≥2) = 85.7% | Set copy counts from these anchors (hypergeometric, computed) |
| Pig (push-your-luck) | Hold at 20–21 ≈ 8.14 EV/turn; hold-at-25 ≈ 8.0 | Canonical model; optimal score-relative policy: Neller & Presser, UMAP Journal 2004 |
| Risk, 3 dice vs 2 | Defender loses 2: 37.2%; split: 33.6%; attacker loses 2: 29.3% | Attacker-favorable baseline for combat odds (computed) |
| Farkle bust | 1 die 66.7%; 2: 44.4%; 3: 27.8%; 4: 15.7%; 5: 7.7%; 6: 2.3% | Push-your-luck risk curve (computed, standard scoring) |
| Zombie Dice cup | 6 green (3B/2F/1S), 4 yellow (2/2/2), 3 red (1B/2F/3S); brains/die 0.50/0.33/0.17 | EV per draw color (official components) |
| Point-salad paths | within ~10–15% VP/action of each other | [contested origin — community heuristic] |
| Action-compression premium | +25–50% over summed parts | [contested folk range] |
| Length targets | filler ≤30; family 30–60; medium-light euro 20–30; euro 60–120; heavy 90–180+ min | Industry/BGG usage; medium-light figure: Piechnick |
| Downtime | (n−1) × mean turn length; >~2 min idle/round = fix it | Arithmetic; fixes: simultaneous play, off-turn payouts |
| Co-op win rate | ~40% first-time; 60% for legacy sessions (Leacock, LoG 2016); 50–70% community band [contested] | Difficulty calibration reference; target-setting → `board-game-solo-coop-design` |
| Win-rate CI (p=0.5) | n=10 → ±31 pp; n=20 → ±22; n=50 → ±14; n=100 → ±10; n=400 → ±5 | 95% CI half-width = 1.96·√(p(1−p)/n) |
| Detecting a gap | Two strategies vs each other (two-arm, two-sided, 80% power): 10-pp gap (45 vs 55) ~390 plays/arm; 55 vs 50 ~1,570/arm | Why 10 playtests can't balance anything; one strategy vs a known 50% baseline (one-sample) needs ~½ of this → `board-game-playtesting` §H |
| First-player advantage | Track first-player win rate; >~55–60% → compensate later seats | [contested folk threshold] |
| Engagement floor | Trailing players need ≥ ~5% win chance | Piechnick |

## Common pitfalls

- **Balancing on 10 plays.** ±31 pp of noise; you're reading tea leaves. Model for balance; playtest for
  perceived balance and breakage.
- **Average-only design.** Two randomizers with equal means and different shapes play differently; check
  tails per session, not EV alone.
- **Balancing by adding rules instead of numbers.** No tuning knob remains. Put an adjustable number on
  every component (Piechnick).
- **Strictly-worse outcomes.** Sword 2/2 vs Spear 3/3 at equal cost feels like theft; make weaker results
  *different*, with some upside.
- **Pass/fail output randomness on big stakes.** Decide-then-roll failure with no mitigation = agency loss;
  prefer input luck, fail-forward, or hidden-information contests (Piechnick).
- **Naked catch-up mechanics.** Visible leader taxes/handouts read as anti-meritocratic (Isle of Skye
  income example); hide them in general arithmetic.
- **Catch-up overcorrection.** If trailing becomes the optimal strategy, players sandbag; cap the
  rubber-band's strength.
- **Runaway leader via uncapped engine.** Every income/production loop needs scarcity, a cap, proportional
  pressure, or an early end trigger; check with rank-correlation tracking.
- **Kingmaking & failed politics.** Politics-as-catch-up fails if the table won't bash the leader;
  elimination + visible scores breeds kingmakers.
- **Spreadsheet false precision.** Elaborate models invalidated by the next revision; keep the model coarse,
  then guess → play → adjust (Piechnick: "don't make a science of it"; the public outplaytests you by
  orders of magnitude).
- **Memory-based hidden scoring.** Obscuring the leader via memory (Small World's face-down VP) is a chore;
  use structurally hidden info (Waterdeep's hidden Lords).
- **Length creep.** Compiling identical rounds to reach box time; cut rounds until testers ask whether it's
  too short (Piechnick).

## Reference files

- `references/probability-tables.md` — LOAD when computing specific dice/card odds, comparing distribution
  shapes, or writing AnyDice/spreadsheet formulas. Contains verified tables (2d6, 3d6, pools, exploding,
  4dF, hypergeometric anchors, Risk, Farkle, Yahtzee) and push-your-luck EV method.
- `references/balance-playbook.md` — LOAD when executing cost/power budgeting, point-salad calibration,
  intransitive (RPS) design, symmetric-vs-asymmetric decisions, or feedback-loop diagnosis. Contains worked
  examples and the feedback-lever catalog.
- `references/pacing-scaling-difficulty.md` — LOAD when setting game-length/turn-time budgets, scaling
  across player counts, building difficulty dials, or validating win rates statistically (CI tables, sample
  sizes, Monte Carlo recipe).

## Related skills

- `board-game-mechanisms` — choose mechanisms before pricing them; tension sources this skill quantifies
- `board-game-design-theory` — why balance serves experience: fairness perception, agency, decision quality
- `board-game-playtesting` — protocols and instruments that gather the data this skill analyzes
- `board-game-solo-coop-design` — automa/co-op structure; owns win-rate target-setting, whose logs this skill validates
- `board-game-prototyping` — fast iteration loops for testing numeric changes
- `board-game-rules-writing` — expressing odds, restrictions, and catch-up rules clearly
