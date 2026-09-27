# Probability Tables & Tools

Verified dice/card distribution tables, AnyDice snippets, spreadsheet formulas, and the push-your-luck
EV method. All percentages re-derived computationally unless marked otherwise.

Load this file when: computing specific odds, choosing a distribution shape, writing AnyDice or
spreadsheet formulas, or pricing a random effect.

---

## 1. Dice sums

### 2d6 (the "Catan model")
36 equiprobable outcomes. Catan prints these as pips on hex tokens; 6 and 8 are the contested spots.

| Sum | Ways | P(exact) | P(≥) |
|---|---|---|---|
| 2 | 1 | 2.78% | 100% |
| 3 | 2 | 5.56% | 97.2% |
| 4 | 3 | 8.33% | 91.7% |
| 5 | 4 | 11.11% | 83.3% |
| 6 | 5 | 13.89% | 72.2% |
| 7 | 6 | 16.67% | 58.3% |
| 8 | 5 | 13.89% | 41.7% |
| 9 | 4 | 11.11% | 27.8% |
| 10 | 3 | 8.33% | 16.7% |
| 11 | 2 | 5.56% | 8.3% |
| 12 | 1 | 2.78% | 2.78% |

Mean 7, SD 2.415. P(6 or 8) = 27.8%. Design notes: Catan makes the modal roll (7, once per ~6 rolls)
produce *nothing* — it fires the Robber, converting the most frequent outcome into interaction.

### 3d6
Mean 10.5, SD 2.958. P(8–13) ≈ 67.6%.

| Sum | Ways (of 216) | P | | Sum | Ways | P |
|---|---|---|---|---|---|---|
| 3 / 18 | 1 | 0.46% | | 7 / 14 | 15 | 6.94% |
| 4 / 17 | 3 | 1.39% | | 8 / 13 | 21 | 9.72% |
| 5 / 16 | 6 | 2.78% | | 9 / 12 | 25 | 11.57% |
| 6 / 15 | 10 | 4.63% | | 10 / 11 | 27 | 12.50% |

P(≥16) = 4.63%, P(≥15) = 9.26%. Matching a d20 crit rate on 3d6 needs ranges: "≥16" ≈ nat-20 (5%),
"≥15" ≈ 19–20 (10%).

### Flat vs bell: d20 vs 3d6
Both mean 10.5. d20: uniform 5% per face, SD 5.77. 3d6: near-normal, SD 2.96.

| Threshold | d20 | 3d6 |
|---|---|---|
| P(≥10) | 55% | 62.5% |
| P(≥11) | 50% | 50% |
| P(≥16) | 25% | 4.63% |
| Extreme (nat 20 / 3 or 18) | 5% | 0.46% |
| Effect of a +1 modifier | flat 5 pp everywhere | up to ~12.5 pp at the mean, ~1–3 pp at tails |

Consequences: flat = swingy, luck-dominant, modifiers feel weak; bell = reliable, skill-dominant, each +1
matters most at mid targets. This is why D&D (d20) feels heroic-swingy and GURPS (3d6) feels gritty.
Also: P(≥1 six in 4d6) = 1 − (5/6)⁴ = **51.8%**; P(double-6 in 24 rolls of 2d6) = 1 − (35/36)²⁴ ≈
**49.1%** — the de Méré problem (1654) that launched probability theory (Pascal–Fermat correspondence).

## 2. Dice pools (success counting, binomial)

Roll N dice, count faces ≥ target. Mean = N·p, SD = √(N·p·(1−p)). Three tuning knobs: dice count, target
number, successes required. Example: 5d6 counting 5–6 (p=1/3, Shadowrun-style) averages 1.67 successes.

P(≥1 success), by pool size N:

| N | p=1/2 (4+ on d6) | p=1/3 (5+ on d6) | p=1/6 (6 only) |
|---|---|---|---|
| 1 | 50% | 33.3% | 16.7% |
| 2 | 75% | 55.6% | 30.6% |
| 3 | 87.5% | 70.4% | 42.1% |
| 4 | 93.8% | 80.2% | 51.8% |
| 5 | 96.9% | 86.8% | 59.8% |
| 6 | 98.4% | 91.2% | 66.5% |
| 8 | 99.6% | 96.1% | 76.7% |

Design use: pools give soft caps — doubling dice never doubles certainty. Raising the target number shifts
the whole curve; raising successes-required tightens variance relative to mean.

## 3. Exploding dice

Reroll-and-add on the max face. EV = base mean × n/(n−1):

| Die | Base mean | Exploding mean | Gain |
|---|---|---|---|
| d4 | 2.5 | 3.33 | +33% |
| d6 | 3.5 | 4.20 | +20% |
| d8 | 4.5 | 5.14 | +14% |
| d10 | 5.5 | 6.11 | +11% |
| d12 | 6.5 | 7.09 | +9% |
| d20 | 10.5 | 11.05 | +5.3% |

**Target-number paradox:** exploding d4 reaches ≥6 at 18.8% vs exploding d6 at 16.7% — small dice spike
more often relative to their range. Exemplars: Savage Worlds, Deadlands, L5R. Price exploding effects
with the new mean AND the long right tail (players remember the 24-point d6).

## 4. Fudge/Fate dice (4dF)

Each dF = {−1, 0, +1}. 4dF: mean 0, SD ≈ 1.63, range −4..+4.
P(+4) = P(−4) = 1/81 ≈ 1.2%; P(≥+3) ≈ 6.2%; P(0) ≈ 23.5%; P(−1..+1) ≈ 63%.
Use when you want modifiers to dominate and luck to whisper.

## 5. Cards: hypergeometric model (sampling without replacement)

P(k of K desired cards in n draws from N-card deck) = C(K,k)·C(N−K,n−k) / C(N,n).
**Do not use binomial (with-replacement) math for draws — a known error.**

Anchors, 60-card deck, 7-card opening hand (computed):

| Copies in deck | P(≥1 in opener) | P(≥1 by draw 10) |
|---|---|---|
| 1 | 11.7% | 16.7% |
| 4 | 39.9% | 52.8% |
| 8 | 65.4% | 79.0% |
| 12 | 80.9% | 91.3% |

Mana-base anchors (computed): 24 lands/60 → P(≥2 in opener) = 85.7%; 17/40 (Limited) → 89.5%;
37/99 (Commander, free mulligan effect excluded) → 81.4%. Hence the design rule: include **8–12
functionally identical cards** for effects you need every game; 4 copies is "sometimes."

MTG manabase math by Frank Karsten (ChannelFireball articles) applies the same model to colored-source
requirements — the reference point for "90% consistency" targets [thresholds contested by format].

**Deck thinning:** removing cards raises remaining density, but per-card effects are small (~1–2 pp per
pair thinned from a mid-game deck). The real value is compounding and removing *bad* draws (Dominion's
Chapel). Practical value of MTG fetchland thinning specifically is [contested].

**Shuffle cycles (deckbuilders):** a bought card is seen ≈ (deck size ÷ hand size) draws per shuffle;
early purchases compound across shuffles — price acceleration accordingly.

### Other useful card anchors
- Love Letter (16 cards): 5 Guard, 2 each Priest/Baron/Handmaid/Prince, 1 each King/Countess/Princess —
  deduction works because the distribution is memorizable.
- 52-card opener: P(≥1 ace in 5 cards) = 34.1%; P(pair in 5-card poker hand) = 42.3%.

## 6. Named-game combat & luck tables

**Risk, attacker 3d6 vs defender 2d6 (per roll, computed):** defender loses 2 armies 37.2%, each loses 1
33.6%, attacker loses 2 29.3%. Attacker-favorable; the defender's tie-wins rule only partly offsets
numerical advantage.

**Farkle bust probability (standard scoring: 1s, 5s, triples, straight, three pairs — computed):**

| Dice rolled | P(bust) |
|---|---|
| 1 | 66.7% |
| 2 | 44.4% |
| 3 | 27.8% |
| 4 | 15.7% |
| 5 | 7.7% |
| 6 | 2.3% |

**Yahtzee:** P(5-of-a-kind on one roll) = 6/6⁵ = 0.077%; within a 3-roll turn ≈ 4.6% [widely published].

**Zombie Dice (official components):** cup = 6 green (3 brains/2 feet/1 shotgun), 4 yellow (2/2/2),
3 red (1 brain/2 feet/3 shotguns). Per-die EV (ignoring footprint re-draws): green 0.50 brains, yellow
0.33, red 0.17; shotgun risk per die 1/6, 1/3, 1/2.

## 7. Push-your-luck EV method (Pig as canonical model)

Pig: first to 100; roll d6, add to turn total; roll 1 = lose turn total; hold = bank. Computed EVs:
hold-at-20 ≈ **8.14 points/turn** (hold-at-21 the same; hold-at-25 ≈ 8.0). The simple EV-max rule is
"hold at ~20"; the true optimal policy is score-relative (roll more when behind, hold when ahead),
computed via value iteration by **Neller & Presser, "Optimal Play of the Dice Game Pig," UMAP Journal
25(1), 2004**.

Procedure for your own push-your-luck mechanism:
1. Enumerate the wager: continue cost (bust probability × stake lost) vs continue gain (payout distribution).
2. Compute EV at each decision state (spreadsheet recursion or AnyDice), not just the "average roll."
3. Make the bust odds *slightly* worse than players intuit — players systematically misestimate (that's the
   fun), but the house edge of each wager must be intentional.
4. State-dependence: wagers near a win threshold skew optimal play; check endgame states separately.

Incan Gold/Diamant works the same way: expected gems of continuing vs realized gems of leaving, with risk
rising as trap cards accumulate.

## 8. Tools

### AnyDice (anydice.com, by Jasper Flick) — verified syntax
```
output 2d6
output 3d6 named "3d6"
output 1d20
output [explode 1d6]                 \ reroll-and-add on max \
output [highest 3 of 4d6]            \ also lowest / middle \
output [count {5,6} in 5d6]          \ dice pool, successes on 5-6 \
output 5d{0,0,1}                     \ same pool, custom faces \
output [lowest 1 of 2d20]            \ disadvantage \
```
Predefined functions: `explode`, `highest/lowest/middle N of DICE`, `count VALUES in SEQUENCE`,
`absolute`, `maximum of`, `sort`, `reverse`. Custom functions: `function: NAME { ... result: ... }`.
Use the "At least"/"At most" view buttons for threshold tables; export CSV for spreadsheets.
Docs: anydice.com/docs (function library verified 2026-09).

### Spreadsheet formulas (Excel / Google Sheets)
- Hypergeometric: `=1-HYPGEOM.DIST(0, 7, 4, 60, FALSE)` → 0.399 (4-of in 60, 7-card opener).
- Binomial pool: `=1-BINOM.DIST(0, 5, 1/3, TRUE)` → 0.868 (≥1 success, 5 dice, p=1/3).
- Combinations: `=COMBIN(60,7)`.
- Win-rate CI: `=1.96*SQRT(0.25/n)` (worst case p=0.5).
- Cost-curve regression: `=LINEST(power_range, cost_range)` or scatter + trendline; flag residuals.

### Simulations
Monte Carlo in Python (numpy) for anything stateful (push-your-luck, combat chains, VP races) —
10,000 runs gives ±1 pp at p=0.5. See `pacing-scaling-difficulty.md` for the bot recipe.
Hypergeometric calculators: Stat Trek, cardgamecalculator.com (TCG-oriented).

## 9. Distribution-shape cheat sheet

| Shape | Feel | Use for | Exemplar |
|---|---|---|---|
| Single die (flat) | swingy, readable | family games, big stakes, crits | d20 attacks |
| 2d6 triangular | moderate, legible (pips) | resource generation, movement | Catan |
| 3d6+ bell | reliable, mastery | skill checks where investment should pay | GURPS |
| Dice pool | success-counting, soft caps | opposed/contested resolution | Shadowrun, Storyteller |
| Exploding | rare spikes, hope | crits, underdog moments | Savage Worlds |
| 4dF | tight around 0 | modifier-dominated resolution | Fate |
| Card draw | deck memory, buildable | engine consistency, combos | Dominion |
| Bag/tile draw | dwindling, forecastable | push-your-luck with known contents | Quacks of Quedlinburg |
