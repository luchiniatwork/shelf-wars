# 03 — Balance Pass (numbers v0.1)

Caveat (Piechnick's rule): these are v0.1 starting values chosen so **every
component carries a tunable number**. The model finds structural problems;
playtests find real ones. Each knob names the metric that tunes it.
Fixes change numbers, never add rules.

## 1. Economy baseline (LCD = one exec-action)

A competent action should be worth ~2–3 cash in expectation.

| Parameter | v0.1 | Notes |
|---|---|---|
| Production cost | 2c/widget, flat | Shelf cap already throttles volume — don't punish twice |
| Factory space | Produce ≤ capacity @2c **or** expand +1 for 4c | Compressed engine: one space, no upgrade system |
| Capacity | start 2, max 5 | |
| Ads | 1c each | Free marketing isn't a decision |
| Starting cash | 10c | Q1 spend (2 widgets + 2 ads = 6c) leaves a real third-exec choice |

## 2. Price bands & segment margins

| Segment | Wants | Max price | Margin (cost 2) | Role |
|---|---|---|---|---|
| Budget | 1 attribute | 2–3 | 0–1 | Volume floor; dumping (price 1 = −1) clears shelf |
| Mainstream | 2 attributes | 3–5 | 1–3 | **The battleground** — most cards live here |
| Enthusiast | 2 attributes | 4–5 (v0.3; was 5–6) | 2–3 | Low volume, high margin, R&D-gated |
| Corporate *(4p only)* | 1 attribute | 4 | 2 | Scaling pressure-valve, not a core system |

**Trend premium: +1** over printed max for customers wanting the hot
attribute. Quantifies the Campaign nudge at ~1–3c expected value → prices
Campaign (1 ad + nudge) against Marketing (2 ads). Both tunable by one
number each.

## 3. R&D combinatorics (4 attributes: A/B/C/D)

| Product | Covers single-want | Covers double-want |
|---|---|---|
| 2 chips | 2/4 = 50% | 1/6 ≈ 17% |
| 3 chips | 3/4 = 75% | 3/6 = 50% |

The 3rd chip roughly **triples** Mainstream coverage — the strongest single
upgrade in the game, and (sim iteration 2) the only *permanent* asset in the
funnel, so it compounds over the full arc. Priced at **4 actions** (v0.3;
2 actions = 80% bot dominance, 3 = 99% over 6 quarters). The Enthusiast
band carried the rest of the fix (5–6 → 4–5).

## 4. Demand deck = clock + scarcity engine

Fixed composition, shuffled; dealt on a growth curve (visible market
expansion + legible end trigger):

| Quarter (3p) | Q1 | Q2 | Q3 | Q4 | Q5 | Q6 | Total |
|---|---|---|---|---|---|---|---|
| Customers | 5 | 7 | 9 | 11 | 12 | 13 | **57** |

- Segment mix: ~40% Budget / 40% Mainstream / 20% Enthusiast.
- Attribute seeding: each attribute on ≥45% of two-want cards per
  quarter-slice — no dead attributes, no scripted R&D path.
- **The scarcity ratio is THE knob.** Competition comes from multiple
  sellers eligible for the *same* customer, not raw totals.
  **Target metric: 1–2 unsold widgets per player per quarter mid-game.**
  Below 1 → demand too rich, undercutting toothless → trim curve / tighten
  shelf. Above 2 → too punishing → trim capacity growth first (cheapest lever).

## 5. Income sanity & score feel

Mid-game competent quarter: ~3 sales × ~2 margin ≈ 6c net → final scores
**~30–60c**. Denominations 1/5/10/20; totals < 100; no conversion math.
Close-game target: **last place ≥ 60–70% of leader** (Fristoe floor) —
tuned by the scarcity knob, not a catch-up rule.

## 6. Player-count scaling

| | 3p | 4p |
|---|---|---|
| Segments | 3 | 3 + Corporate |
| Deck | 57 | ~74 (+30%) |
| Ad slots/segment | 3 | 3 (tighter blocking = free) |
| Shelf cap | 6 | 6 |

Downtime: 4p × 4 execs × ~25s placements ≈ 7 min action phase; income
simultaneous. Budget ≈ 12 min/quarter × 6 + setup ≈ **100–110 min** —
inside the euro band.

## 7. Randomness & loops audit

- One randomizer (demand deck, input-side) ✓; Research space = its
  mitigation currency ✓; price reveal is hidden information, not luck ✓.
- Positive loop counterweights: shelf cap, 3 ad slots, finite customers,
  depletion clock. No naked catch-up rule ✓.

## 8. Playtest instrumentation (log every play)

| Metric | Watch for | Response |
|---|---|---|
| Rank at Q2 / Q4 vs. final | Early rank locks in → snowball | Tighten caps / trim curve |
| First-player win rate | >55–60% [contested folk threshold] | Compensate later seats (start-player marker is a tie-break lever) |
| Unsold widgets/player/quarter | outside 1–2 band | Scarcity knob (deck curve) |
| Campaign-nudge usage | <10% of marketing actions | Delete the nudge clause (Option B escape hatch) |
| Price-1 dump frequency | >20% of sales | Scarcity miscalibrated |
| Last/leader cash ratio | <60% | Structural caps insufficient → reconsider challenger rule |

## 9. Full knob sheet

Production cost **2** · capacity **2→5** / expand **4c** · shelf **6** ·
ad cost **1** · ad slots **3** · trend premium **+1** · 3rd chip **3
actions** (v0.2, sim-validated) · execs **3** (+1 at Q3) · start **10c** ·
quarter curve **5/7/9/11/12/13** · segment price bands · deck size per
count **57/74**.

Sim verdicts (see `05-sim-results-v0.1.md`): 3rd chip at 2 actions was a
dominant strategy (80% bot win rate); ad cost 0 unleashes the coverage
leader (71–94%); production cost 1 helps the premium strategy (80–90%);
raising price bands starves the discount strategy. All four rejected —
keep v0.2 values.

Iteration-2 verdicts, full 6Q game (see `06-sim-results-v0.2.md`, read its
errata): chip3 3 → 4 was necessary but NOT sufficient (its 45/50 was a
sim-script artifact); E-band 5–6 → **4–5** stands; trend premium +2
rejected (self-reinforcing); demand-volume boost rejected (eligibility is
the choke); retaliation worth ~14pp to challengers.

Iteration-3 verdicts (see `07-sim-results-iter3.md`): the real lever is
cash — **3rd chip = 4 actions + 6c** (knife-edge 5/6/7c = 86/63/0% Spike).
Rejected: sale-cap, 5 attributes, E-wants-3, random trend, line upkeep,
campaign-creates, prodcost 1 (×3), late inflation, start-cash 14.
Deflation is structural (faucet ≈ cost floor); options: ×5 presentation
scaling, demand-creation redesign (v0.5), or accept brutality.
