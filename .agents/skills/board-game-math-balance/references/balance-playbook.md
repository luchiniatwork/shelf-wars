# Balance Playbook — Worked Procedures

Step-by-step balancing procedures with worked examples: cost curves, power budgets, point-salad
calibration, intransitive design, symmetric vs asymmetric balance, and the feedback-lever catalog.

Load this file when: pricing components, calibrating scoring paths, designing counter relationships, or
diagnosing runaway-leader/kingmaking problems.

---

## 1. Effort accounting (Strain) & LCD conversion (Piechnick)

**Christian Strain, "Finding Balance Before Playtesting," League of Gamemakers (2017)** — balance
mathematically *before* playtesting ("Tesla method" vs Edison's brute iteration):
- Effort (e) = turns to acquire, starting from nothing. Free red card = 1e. Blue card costing two reds =
  3e (pick up red, pick up red, spend). If one turn gathers 2 gold, gold = 0.5e, so the blue card should
  cost 4 gold.
- Adjust for supply & demand: the scarcer of two equal-e resources is worth more *when it does something
  the other can't*.
- Playtests then test *perceived* balance, which players systematically misjudge (told to "roll close to
  average," players pick 2 dice over 10, though 10 dice is far more reliable).

**Daniel Piechnick (daniel.games, "Balance")** — convert everything into the game's lowest-common-
denominator resource to compare values; actions/turns are costs (a "free" card still costs a card; an
action costing 2× with 2× reward is *better* — both consume one turn). Counterweights to over-mathing
(also Piechnick, same article — hold both truths):
- "Don't make a science of it." Almost all power is context-dependent; the correct level often *seems*
  outrageously strong — "don't baulk at making things three times stronger."
- An option chosen only ~25% of the time is still balanced enough if worth considering.
- A *hand* of cards averages out individual imbalance; zero-cost cards are still balanced by the hand slot.
- You will never fully balance it; the public plays orders of magnitude more than you and *will* find what
  you missed. Balance by **changing numbers, never adding rules** — put a tunable number on every
  component (Radlands camps carry a corner number; weaker camps grant a larger starting hand).

## 2. Cost-curve fitting — worked example

Procedure: (1) pick LCD currency, (2) tabulate components, (3) fit curve, (4) flag outliers, (5) reprice.

Example (invented card game, cost in gold, power in converted-VP — labeled example, not a real game):

| Card | Cost | Power (VP-equiv) | Fit: power = 2·cost + 1 | Residual |
|---|---|---|---|---|
| Peasant | 1 | 3 | 3 | 0 |
| Soldier | 2 | 5 | 5 | 0 |
| Knight | 3 | 8 | 7 | +1 |
| Ballista | 4 | 12 | 9 | **+3 → overcosted power / underpriced** |
| Elephant | 5 | 9 | 11 | −2 → overpriced |

The linear fit `power = 2·cost + 1` (echoing the Hearthstone vanilla heuristic *stats ≈ 2×cost + 1*
[community heuristic]) exposes Ballista and Elephant immediately. Fixes: Ballista to cost 5–6 or power 10;
Elephant to power 11 or cost 4.

Pricing premiums & discounts on top of the curve:
- **Action compression** (2 effects, 1 action): +25–50% over the summed parts [contested folk range].
  Rationale: the turn, not the gold, is the real cost (Piechnick).
- **Area/multi-target effects**: ≥ linear in targets hit; global effects (hit *all*) priced at the top of
  the band — they scale with player count and board state.
- **Flexibility** (modal cards, choose-one): premium for option value, ~10–20% [folk].
- **Discounts**: restrictions (class-only), telegraphing (enters tapped, delayed), setup requirements.
- **Saturation**: the 20th axe ≉ 20× the 1st (Piechnick); duplicate effects have diminishing value — price
  the *marginal* copy, not the first.

CCG-derived invariants (Magic design practice, Mark Rosewater columns): no infinite loops (output ≤ input
of the same currency), no strictly-better cards at equal cost, multi-effect cards split the budget so each
mode is weaker than a focused card. Dominion community anchors: Village 3, Smithy 4, Market/Laboratory 5 —
and the "Silver test": a cost-5 card should beat buying Silver in most decks [community heuristic,
contested]. Baselines drift with power creep — re-derive from *your* game's set, don't import blindly.

## 3. Point-salad calibration — worked example

Feld-style design, 5 scoring paths, 40 actions per player per game. Estimate realistic output for a
competent player, then compute VP/action:

| Path | Total VP | Actions spent | VP/action | vs median |
|---|---|---|---|---|
| Farming | 55 | 14 | 3.93 | +15% |
| Trading | 42 | 12 | 3.50 | +2% |
| Building | 50 | 15 | 3.33 | −2% |
| Monastery | 30 | 10 | 3.00 | −12% |
| Shipping | 20 | 5 | 4.00 | +17% |

Median ≈ 3.43. Target band: all paths within ~10–15% of median [contested origin — community heuristic].
Farming (+15%) and Shipping (+17%) breach the band; Monastery (−12%) is borderline.

Knobs, in order of preference:
1. **Reward size** (Farming 55 → 50 VP).
2. **Cost** (Shipping actions 5 → 6).
3. **Scarcity** (limit Farming slots per round — competition taxes the path).
4. **Synergy slots** (give Monastery a combo hook with Building, raising its effective yield without
   touching its face value).

After tuning, re-verify: no path is strictly ordered for *all* board states (else the salad is a script).
Sanity-check with greedy-bot Monte Carlo: each bot hard-commits to one path; final scores should land
within ~15% with no path winning >35% of sims (4–6 paths). Then humans test perceived balance.

Exemplar: *Point Salad* (AEG, 2019) — 108 scoring conditions, veggie counts scaled by player count,
flip-a-point-card-to-veggie as a pivot valve between drafting and scoring economies.

## 4. Intransitive balance (RPS triangles) vs transitive power

**Intransitive (cyclical) balance:** A beats B, B beats C, C beats A. No dominant strategy; counterplay is
positional. Use for factions, unit types, strategies (infantry > cavalry > archers). Design targets:
- Each matchup should be decisive enough to feel real (≈ 55–65% for the advantaged side [folk band]) —
  matchups at exactly 50/50 are indistinguishable from transitive equality and kill the texture.
- Across the meta, each option's *average* win rate vs the field should sit in the viability band
  (≈ 45–55%); a triangle where everyone is equal vs the field but every matchup is 60/40 is the ideal.
- Odd numbers of options avoid pairing deadlocks; classic games extend RPS to 5+ cycles (Rock-Paper-
  Scissors-Lizard-Spock; as a curiosity, RPS-101 by David Lovelace: 101 gestures, each beating 50).
- Pokémon's 18-type chart is the commercial apex of intransitive networks.

**Nontransitive dice (Efron's dice, Bradley Efron, via Martin Gardner 1970):** dice can be cyclical too —
A = {4,4,4,4,0,0}, B = {3,3,3,3,3,3}, C = {2,2,2,2,6,6}, D = {1,1,1,5,5,5}, where each die beats the next
with P = 2/3 (C beats A only 5/9). Useful as a mechanic for "no best pick" components.

**Transitive power ladders** (strict A > B > C) are correct only where escalation is the point: tech trees,
weapon tiers. There, balance means *cost* scaling with rank, not denying the rank order.

Evaluation method: scripted-bot round robin. Each strategy/faction pair plays ≥1,000 sims (±3 pp at 95% CI per 1,000 sims; ~6,800 sims for ±1.5 pp);
build the matchup matrix; then check (a) every option's field-average in the viability band, (b) every
matchup off 50/50 by at least ~5 pp for texture. Sirlin's framing (*Playing to Win*, sirlin.net):
balance = maximizing the number of viable options, and unchecked positive loops ("slippery slope") are the
enemy of viable counterplay.

## 5. Symmetric vs asymmetric balance

| | Symmetric | Asymmetric |
|---|---|---|
| Balance cost | Low: one system, mirrored | High: budget 3–5×; every pairing is a matchup |
| Content feel | Low (everyone same) | High (distinct factions = replayability) |
| Failure mode | Mirror boredom | Untestable matrix explosion, dominant faction |
| Exemplars | Chess, Puerto Rico | Cosmic Encounter (1977), Root (2018), Scythe |

Asymmetric procedure:
1. Give each faction a power budget in the LCD currency; all kits sum within ±10% of each other [folk
   threshold] *before* unique abilities; price abilities on top.
2. Mirror-test each kit against a "vanilla" faction to isolate ability power.
3. Round-robin bots for the matchup matrix (see §4); humans for feel.
4. Patch by numbers, not rules; version every change; track per-faction win rate per player count
   (imbalance is often count-dependent).
5. Social balancing is a legitimate layer: Cosmic Encounter's 50+ aliens are balanced partly by table
   politics — but only if your game *has* negotiation. Stegmaier's Scythe balance process was
   spreadsheet-plus-playtest-data driven (Stonemaier Games design blog).

## 6. Feedback-loop engineering — lever catalog

Positive loop = success breeds success (engine, income, territory) → snowball/runaway leader.
Negative loop = success breeds resistance → rubber-banding (*Characteristics of Games*, Elias/Garfield/
Gutschera 2012, treats this as a core axis; Mario Kart's position-scaled items + AI adaptation is the
canonical dynamic-difficulty example — and the canonical example players *resent* when overt).

| Problem | Lever | Exemplar | Risk |
|---|---|---|---|
| Runaway leader | Structural turn-order compensation: last place acts first where it matters | Power Grid (last place buys resources first, at lower prices; "stay behind then leap" is core strategy) | Incentivizes stalling |
| Runaway leader | Upkeep/proportional penalty: growth triggers cost steps | Suburbia (population crossings tax income/reputation) | Feels like punishment if naked |
| Runaway leader | Proportional effects: "all opponents lose half X" hits leader hardest | — (general pattern, Piechnick) | Can feel targeted |
| Runaway leader | Ramps & big moves: trailing players keep a theoretical path | Family Feud double-points final round; Scrabble bingo +50 | Cheapens early play if too strong |
| Runaway leader | Early end trigger: end the game before the leader locks | Race for the Galaxy (12-card tableau trigger) | Games feel truncated if mistuned |
| Runaway leader | Obscured leader | Waterdeep's hidden Lords (structural) — good; Small World's face-down VP (memory test) — bad | Memory-based hiding is a chore |
| Leader-bashing fails | Politics: robbers/attack cards only work if the table targets the leader | Catan robber; Waterdeep attacks | Kingmaking if table refuses |
| Snowball | Scarcity cap: congestion, diminishing returns, market exhaustion | Agricola action scarcity | Over-tight = frustration |
| Checked-out trailers | Engagement floor: keep ≥ ~5% win chance alive (Piechnick) | — | — |

Diagnostic metrics:
1. **Rank-correlation tracking**: record each player's rank at 25/50/75% of game vs final rank over 10–20
   plays/sims. Consistent early lock-in → add negative pressure; leader changing every round → agency is
   noise, add weight to early play.
2. **Margin distribution**: log final-score gaps. Healthy games show most margins within ~10–20% of the
   winner's score [folk band]; blowouts signal missing catch-up, photo-finishes-every-time signal overt
   rubber-banding.
3. **Elimination audit**: any player who cannot win should lack the power to decide who does. Mitigations:
   hidden scores, simultaneous reveals, multiple end conditions, self-directed goals for trailers.
4. **Sandbagging test**: is deliberately trailing ever optimal? If yes, the catch-up is too strong.

Catch-up placement rule (Piechnick): hide the mechanism inside general arithmetic, never as a naked
score-based handout (negative example: Isle of Skye's income-per-player-behind).

## 7. Balance workflow summary

1. Model: effort accounting → cost curve → path EVs → distribution shapes. Coarse is fine.
2. Simulate: bots for matchup matrices and path win rates; 10k sims = ±1 pp.
3. Playtest: humans for perceived balance, fun, breakage. Log winner seat, strategy, margin, length.
4. Patch numbers only; one variable per iteration; re-fit the curve after each batch.
5. Accept the viability band. Ship with tunable numbers (or a living FAQ) — the public will outplaytest
   you by orders of magnitude and find the rest.
