# 06 — Sim Results v0.2 (iteration 2: full game + retaliation)

> **⚠ ERRATA (added 2026-09-28):** this iteration's headline config
> (chip3 = 4 actions → Engine 45 / Spike 50) was contaminated by a bot-script
> bug: Spike's script spent only 3 R&D actions, so its 3rd chip never
> landed at chip3 = 4 — the measured "balance" was a crippled strategy, not
> working knobs. The corrected lever (3rd chip = 4 actions **+ 6c cash**) and
> all superseding conclusions are in `07-sim-results-iter3.md`. Still valid
> here: persist adoption, retaliation-helps-challengers, trend-premium +1,
> E-band 4–5 direction, the economy-leak analysis, and the Discounter autopsy.

Date: 2026-09-28 · Sim: `sim/shelf_wars_sim.py` (iteration 2) · 500 runs/config
What changed vs iteration 1: v0.2 rules by default (chip3 = 3 actions, persist),
**full 6-quarter game** (57 customers, curve 5/7/9/11/12/13), and
**retaliation-capable bots** (undercut comparable rivals to a cost floor;
prefer bumping the cash leader's ads). Same caveat as before: structural
signal from scripted policies, not human balance.

## Headline: the compressed game hid a full-game imbalance

| Config (6Q, persist, retaliation on) | D / E / S win % | Q2-lock | Table total |
|---|---|---|---|
| v0.2 as-written (chip3 = 3, E 5–6) | 0 / 0.6 / **99.4** | 78.6% | 25.6c |
| chip3 = 4, E 5–6 | 6 / 32 / 62 | — | 15.7c |
| **chip3 = 4, E-band 4–5 (→ v0.3)** | **5 / 45 / 50** | **26.4%** | 17.6c |

The 4-quarter compression let Spike's 3-action chip investment balance out;
over 6 quarters it amortizes to nothing. **Coverage is the only permanent
asset in the funnel** (ads churn, prices reset quarterly, chips never leave)
— it compounds, and the late fat quarters amplify it. This is the runaway
engine the design feared, and the sim caught it before the table did.

## What fixed it (and what didn't)

| Experiment | Result | Verdict |
|---|---|---|
| 3rd chip = 4 actions | Spike 99→62% | **Adopted (v0.3)** |
| E-band 5–6 → 4–5 (premium margin nerf) | +chip3=4 → Engine 45 / Spike 50 | **Adopted (v0.3)** |
| Retaliation ON vs OFF (at D config) | Engine 45% vs 31%; Spike 50% vs 62% | **Politics is worth ~14pp to the challenger — human tables will fight the leader for free. Do NOT add mechanical rubber-banding before human data.** |
| Trend premium +1 → +2 | Spike 78% | **Rejected** — nudge + premium is self-reinforcing for the coverage leader. Keep +1. |
| Scrap rule (broke seats liquidate widgets 1c) | No win-rate movement; floors bankruptcy only | Deferred — a feel rule, not a balance rule. Decide at the table. |
| Demand boost (+1–2 Mainstream/quarter) | No buoyancy; unserved customers rise | **Rejected** — eligibility, not demand volume, is the choke. |
| Ad cost 0 (at D config + retaliation) | Economy grows (+9.6c table), Engine 42 / Spike 58 — **but Discounter 0%**: free blanket coverage kills the Budget archetype; unsold widgets 2.28 (over band) | Not default. Logged as a **table experiment**: "free-ads variant" |

## The Discounter autopsy (known limit)

Pure-Budget is non-viable in the 6Q game under **every** tested config:
B margins (0–1 at production cost 2) cannot fund 6 quarters of 1c ads.
Raising B bands backfires (widens premium eligibility). Interpretation:
Budget is a **portfolio leg, not a strategy** — fine if mixed B+M lines
work for humans, and Engine (mid-price volume) is proof the volume side of
the board is playable. **Stage-2 question: does a mixed B+M strategy beat
pure M?** If pure-B should be viable, the lever is B-segment customer
*volume*, not price bands.

## The economy leak, located

Winners' trajectories now grow mid-late (Engine 5.5→6.8; Spike dips then
6.0→8.5) but the table still nets negative (17.6c from 30c). The leak is
**ad churn**: ~9.7 leader-bumps + ordinary bumping force constant re-buys,
eating ~50–60% of sales revenue at 1c/ad. Free ads fix the economy but cost
the Budget archetype (see table). Options ranked for human testing:

1. Keep 1c ads (v0.3 default) — archetype diversity first, accept a tight
   economy (FCM is also tight).
2. Table-test the free-ads variant — growing economy, premium-heavy meta.
3. If neither feels right: 4 ad slots/segment (less churn) is the untested
   middle path.

## Snowball check

Q2-leader-wins: 78.6% (broken config) → **26.4% (D config)** — healthy.
Unsold widgets midgame 1.83 — inside the 1–2 band. Undercuts 0.7/game,
leader-bumps ~9.7/game (churn economy confirmed), nudges ~1.2/game
(bots use the nudge slightly more in the long game — still watch).

## Rules clarifications added this iteration

- Trend premium stays **+1** (self-reinforcement at +2).
- 3rd chip progress may be paid **across quarters** (already in rules-v0.2).
- Bankruptcy: scrap-for-1c is the leading candidate floor; sim shows it
  doesn't distort balance either way.

## ~~Proposed v0.3 numbers~~ (superseded — see errata)

3rd chip = 4 actions was under-protective; v0.4 corrects to **4 actions +
6c cash**. E-band 4–5 stands.

## Limitations

Scripted policies; Discounter-bot is an extreme pure strategy (humans mix);
retaliation is formulaic (real politics is richer and meaner); no 4p/
Corporate modeling; Research still unmodeled. All balance claims are
structural: they say "these numbers can support a real game," not "these
numbers are balanced."

## Next

Physical Stage-1/2 with `rules-v0.3.md` + `prototype/customers-full-3p-v0.3.csv`.
The sim has answered what sim can answer; the rest is table work.
