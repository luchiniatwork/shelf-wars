# 05 — Sim Results v0.1 (greedy-bot Monte Carlo)

Date: 2026-09-28 · Sim: `sim/shelf_wars_sim.py` · Deck source: `sim/deckgen.py` →
`prototype/customers-v0.1.csv` (physical build) — the sim **samples the deck
space** per run (fixed per-quarter composition; randomized attribute
assignment and band prices) after single-deck results proved hyper-sensitive
to per-card price assignment.

## What this can and cannot say

Greedy scripted bots (Discounter / Engine / Spike), 4-quarter compressed
game, 500 runs per config. This tests **structure**: dominant-policy smells,
knob directions, economy shape. It does **not** test fun, the price-reveal
poker (bots set prices by formula, no retaliation), rules comprehension, or
true human balance. Win-rate CI ±4.4pp at n=500; fixed policy skill also
confounds the spread. Treat every number as "structural signal to verify
with humans," per model-first-playtest-second doctrine.

## Headline findings (ranked by leverage)

1. **The 3rd chip's action cost is THE balance lever.** At 2 actions,
   Spike (premium 3-chip rush) wins **80.2%**. At 3 actions:
   **Discounter 35.4 / Engine 23.0 / Spike 41.6** — a three-way race.
   → **v0.2: 3rd chip costs 3 actions.** (Math pass predicted; confirmed.)
2. **Unsold customers should persist one quarter.** Persist halves unserved
   demand (12.5 vs 17–22 of 32), grows the economy, and Q2-leader-wins drops
   to a healthy 39%. → **v0.2: customers persist one quarter, then discard.**
3. **The 1c ad cost is load-bearing as a leader-brake.** At ad cost 0,
   Spike wins 71–94% regardless of chip3 cost — free awareness lets the
   coverage leader blanket every segment. The 1c tax slows the winner's
   expansion. → **Keep ads at 1c.**
4. **Production cost 1 rejected** (twice): cheaper production compounds with
   high prices (Spike 80–90%). → Keep production at 2c.
5. **Raising price bands backfires** (B 3–4 or M 4–6): higher max prices
   widen eligibility for premium sellers and starve the Discounter
   (Spike 51–69%). → Keep bands B 2–3 / M 3–5 / E 5–6.

## Metrics at the recommended config (chip3=3, adcost 1, persist)

| Metric | Result | Target | Verdict |
|---|---|---|---|
| Win rates (D/E/S) | 35.4 / 23.0 / 41.6% | no dominant policy | ✓ (Engine trails; watch) |
| Unsold widgets/seat/quarter, midgame | 1.67 | 1–2 | ✓ scarcity calibrated |
| Unserved customers/game | 12.5 of 32 | lower is looser | watch |
| Mean final table total | 16.1c (from 30c) | growth | ✗ see economy note |
| Last/leader cash ratio | 0.33 | 0.60–0.70 | ✗ confounded by fixed bot skill — human tests decide |
| Q2 leader wins | 39% | <~60% | ✓ no early lock-in |
| Campaign nudges/game | 0.5 | usage check | bots barely nudge — Option-B escape hatch stays open for human tests |
| Price-1 dumps/game | 0.16 | <20% of sales | ✓ |

## The economy note (top open issue)

Every config runs deflationary in sim (table total 14–23c from 30c). Three
confounds before touching any knob: (a) bots are undisciplined — they
produce into shelves they can't sell through and re-buy ads they don't need;
(b) the 4-quarter compression cuts the fat Q5–6 payoff quarters where
engines cash in; (c) fixed policy skill exaggerates both poverty and spread.
**Decision: do not tune the economy on bot data.** Stage-2 human games
decide; if it still reads deflationary, the first levers are a steeper
demand curve (more customers late) or a starting-cash bump — not production
cost or ad cost (both unleashed the leader in tests).

## Rules gaps the sim forced (proposed clarifications, now in rules-v0.2)

- A seat with several covering lines sells its **cheapest** covering line.
- Bumping: oldest **opponent** ad only; a segment full of your own ads is
  full to you.
- Production only into free shelf slots.
- Trend advances at forecast from Q2 onward (Q1 uses the setup marker).
- Ads persist across quarters until bumped.
- **Bankruptcy is a dead state**: at 0 cash every space is dead (produce
  costs, ads cost, R&D earns nothing alone). Engine-bot died this death in
  early runs. Open design question: loan rule / asset-scrap (return widget
  for 1c) / accept FCM-style brutality. Instrument in Stage-2 human tests.

## Limitations (for the record)

Scripted policies, no real hidden-information play, Research space
unmodeled, 4p/Corporate segment unmodeled, 4-quarter compression, no
per-round ad-churn tuning. Balance claims are structural, not statistical.

## Proposed next iterations

1. Full 6-quarter / 57-card sim with the recommended v0.2 rules (re-check
   economy + Engine viability with the Corporate segment off).
2. Retaliation-capable bots (undercut the segment leader; bump leader's
   ads) — tests whether human-like politics fixes the Engine gap.
3. Then, and only then, human Stage-2 with the physical v0.2 build.
