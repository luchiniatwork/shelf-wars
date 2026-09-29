# 08 — v0.5 Plan: The Economy Redesign (demand creation)

Status: **TESTED AND FALSIFIED** — see `09-sim-results-v0.5.md`. Creation
converts at ~10% through the eligibility funnel (demand volume was never
the choke); the fix that shipped in v0.5 is **4 ad slots per segment**, an
eligibility-side change found during the validation runs. This file is kept
as the record of the hypothesis and why it failed.

## Goal

Fix the structural deflation: today the faucet (sales) scales only with
eligibility (~50–60% of a fixed market), while every sink scales with
player investment. v0.5 makes **marketing create demand**, so the money
supply grows when players invest in growth — the FCM property our current
awareness-only model lacks.

This formally **revives Option A from the subsystem diet**
(`02-design-spec.md`). The diet deferred it because no evidence then
justified the rules weight; ~20 sim configs later, the evidence exists.
The diet's other cuts stand.

## The core mechanic: Campaign becomes the creation verb

| Space | v0.4 | v0.5 proposal |
|---|---|---|
| Marketing | Place 2 ads (1c each) | unchanged |
| Campaign | Place 1 ad + trend nudge | **Place 1 ad + create 1 customer** |

The trend nudge is the sacrificial verb: bots used it ~1.2×/game, the
escape hatch was already armed, and Campaign needs room to pay rent. (Open
question 1 below.)

**How creation works:**

1. You place an exec on Campaign (1 ad as usual, 1c).
2. You **choose a segment** and draw from its **growth pile** — a small
   separate deck (~6 cards per segment; random wants/max within the
   segment's band).
3. The created customer goes **face-up into the "next quarter" area** of
   the market board — visible to everyone immediately.
4. At next quarter's forecast, it joins the row. It is a normal customer
   in every way: same funnel, same ladder, same persistence rule.

## Why this doesn't just feed the creator (anti-self-serve design)

The naive sim version (create in your own segment, effective immediately)
went Spike 100%. Three mechanisms break the self-serve:

1. **Maturity delay.** Created demand enters *next* quarter's row, not this
   one. The creator cannot capture it with the ad they just placed and the
   position they already hold — they must still be standing when it lands.
2. **Public visibility.** From the moment of creation, all players see the
   incoming customer and have a full round to contest it: bump the
   creator's ads, retool coverage, or price to undercut. Creation becomes
   table information, not private equity.
3. **Random wants.** The creator picks the *segment*, not the wants — so
   they can't print a customer only their line covers. (Stricter variant
   if needed: draw from the base demand deck, not a growth pile.)

The funnel is unchanged. A created customer is exactly as contestable as a
dealt one — creation grows the pie, it doesn't slice it for you.

Expected residual self-capture: ~40–60% (creator knows the segment and can
pre-position). That's a *feature*: marketing needs positive expected ROI or
nobody buys it. The sim pass criterion is that self-capture doesn't
translate into a leader lock.

## Faucet/sink model (projection)

Volume: Campaign costs an exec + 1c ad; with 3–4 execs, realistic usage is
~1 creation per seat per quarter from Q2 → **+2–3 customers/quarter,
+12–18 per game (3p)** vs 57 base ≈ **+25–30% demand**.

At ~3.5c average: **+45–60c of faucet per game**. The deflation gap
measured in sim was ~15–45c — creation at this dosage flips the economy
net-positive without flooding it.

| Metric (3p) | v0.4 sim | v0.5 target |
|---|---|---|
| Table total (from 30c) | 10–25c | **45–70c** |
| Unserved customers / game | ~27 of 57 | 15–20 of ~70 |
| Unsold widgets, midgame | 1.25–1.67 (in band) | 1–2.5 (no flooding) |
| Spike win rate | 63% | ≤65% (creation must not become the new rush) |
| Q2-leader-wins | 20% | ≤40% |

## Physical implementation

- **Growth piles**: 3 small decks (~6 cards each) beside the market board,
  one per segment. Creator picks the segment, draws the top card, places it
  face-up in the **"next quarter" row** printed on the market sheet.
  (+18 cards to the manifest; no new rules objects.)
- The base demand deck is untouched → the saturation clock is stable.
  (Rejected variant: pull creations from the base deck — zero new
  components, but it eats the clock and shortens the game as players market
  more. Wrong trade.)
- Teach cost: +1 rule ("Campaign also builds a customer for next quarter").
  The funnel story absorbs it naturally: marketing literally creates
  customers.

## Sim validation plan (executed — results in `09-sim-results-v0.5.md`)

1. Implement in `sim/shelf_wars_sim.py`: pending-creation pool → joins
   next quarter's row; wants drawn from segment band; reuse the existing
   `--campaign-creates` flag (redefine with maturity delay).
2. Update bot policies so all three archetypes use Campaign (Discounter
   swaps 1 Marketing → Campaign from Q3; Engine from Q5; Spike already
   campaigns). This also tests whether creation lifts the weaker scripts.
3. Batches (500 runs each, v0.4 base: chip3 = 4 actions + 6c, E 4–5,
   persist, retaliation on):
   - creates 1, maturity delay 1 quarter — primary
   - creates 2 — flooding check
   - creates 1 with self-serve bias (creator picks 1 want) — robustness
     check on the random-wants safeguard
4. Pass criteria: the target table above. Fail paths pre-named: flooding
   (cap creations/game), self-serve (add a creation cooldown per segment),
   Spike-rush (creation gated behind... nothing — re-examine).

## Scope discipline

v0.5 is **one system change**: demand creation + validation. It is not: a
rebalance of v0.4 numbers (they stand), not 4p tuning, not new segments,
not the bankruptcy floor (still a table-feel question).

## Risks

- **Creation flooding** → scarcity knob dies (unsold > 2.5). Mitigation:
  hard cap 1 creation/seat/quarter (already implied by exec economy; make
  it explicit if sim shows abuse).
- **Self-serve residual** → creation becomes the new Spike rush. Sim
  variant 3 tests the bias case directly.
- **Teach creep**: +1 rule is affordable; +2 is not. If creation needs a
  second rule (cooldowns, caps), simplify before shipping.
- **Clock stability**: growth piles must not interact with the demand
  deck's depletion trigger.

## Open questions for the designer

1. **Does the trend nudge survive?** Proposal: removed (Campaign = 1 ad +
   create). Alternative: Campaign = 1 ad + choose {nudge | create} —
   keeps both verbs but re-raises teach cost and the self-reinforcement
   risk the sim flagged. My recommendation: remove; the trend stays
   schedule-driven chaos you adapt to rather than steer.
2. **Growth pile composition**: mirror base segment bands exactly, or
   skew growth cards slightly generous (+1 max price) to make creation
   reliably worth the exec?
3. **Creation visible from setup or only from Q2?** (Q1 creation means
   turn-1 analysis load; Q2 keeps the opening clean.)
