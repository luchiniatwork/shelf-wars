# 07 — Sim Results, iteration 3 (root-cause hunt + v0.4 numbers)

Date: 2026-09-28 · Sim: `sim/shelf_wars_sim.py` (iteration 3) · 500 runs/config
Planned scope: v0.3 regression gate, 4p + Corporate test, Portfolio bot,
basin check. **Actual course:** the regression gate failed, exposed two sim
bugs and one contaminated iteration-2 conclusion, and the iteration became a
root-cause hunt for the real balance lever. That is exactly what regression
gates are for.

## ⚠ Errata for `06-sim-results-v0.2.md` (read first)

The v0.3 headline (chip3 = 4 actions, E-band 4–5 → Engine 45 / Spike 50)
was **contaminated by a bot-script bug**: Spike's script spent only 3 R&D
actions, so at chip3 = 4 its 3rd chip *never landed* — the "balance" was
Spike playing crippled, not the knobs working. Corrected findings here.

Valid from iteration 2: persist customers, retaliation-helps-challengers,
trend-premium +1 (not +2), E-band 4–5 direction (kept in v0.4).

## Sim bugs found & fixed this iteration

1. **No exec cap enforced** — Spike's Q2 script listed 4 actions at 3
   execs. Fixed: `acts[:execs]` truncation; scripts now priority-ordered.
2. **Fixed-investment R&D scripts** — bots couldn't complete chips whose
   cost exceeded their scripted action count (crippled Spike at chip3 ≥ 4,
   Engine at chip3 ≥ 4). Fixed: invest-until-done with a market fallback.
3. **Division by zero** when all seats end at 0c (last/leader metric).

## The lever hunt (all 500-run batches; base = 3p, persist, retaliation on)

| Experiment | Spike win % | Verdict |
|---|---|---|
| v0.3 as-shipped (chip3 = 4 actions) | **99.8%** | Under-protective (see errata) |
| chip3 = 3 or 5 actions | 97.8–99.6% | Action cost alone never balances |
| Sale-cap 2–3 per segment/quarter | 100% | Rejected (effect size ~3pp; doesn't pay rent) |
| 5 attributes | 98.2% | Rejected |
| Enthusiast wants 3 attributes | 95.4% | Rejected |
| Random trend start | 100% | Trend schedule was NOT the driver |
| **3rd chip = 4 actions + cash price** | 5c → 86% · **6c → 63%** · 7c → 0% | **THE LEVER. Knife-edge at 6c (start 10c).** |
| Line upkeep 1–2c/quarter | 98% / economy flatlines | Rejected both ways |
| Campaign creates demand (N=1) | 100% | Rejected: created demand feeds its creator |
| Upkeep + creates + chip3-cash | 0% Spike, table at 2.6c | Overcorrects into dead economy |
| chip3 = 1 action + 5c (simplification test) | 3.2% Spike | Overcorrects (Q1 liquidity kill) |
| prodcost 1 (3rd test, under chip3-cash 6) | 98.4% | Rejected forever: scales the coverage leader's revenue |
| Late-market inflation (Q5–6 pay +1) | 70.8% | Rejected: flows proportional to existing win-share |
| Sale-cap 2 under chip3-cash 6 | 65.6% | ~3pp for a rule — rejected as default |
| Start-cash 14 | Spike 99.8% at cash 6 | More runway helps the rusher most; **keep 10c** |

## Validated configuration (→ v0.4)

3p, persist, retaliation on, B 2–3 / M 3–5 / E 4–5, shelf 6, ads 1c,
production 2c, start 10c, trend +1, **3rd chip = 4 R&D actions + 6c cash**:

| Policy | Win % | Read |
|---|---|---|
| Spike (premium 3-chip rush) | 63–65% | Strong, beatable; the premium path is a real commitment |
| Engine (capacity + mainstream) | 26–30% | Viable challenger |
| Discounter (pure budget) | 4–8% | Portfolio leg, not a strategy (robust across ALL configs) |

Q2-leader-wins 20–21% (no early lock-in) · unsold widgets 1.25–1.67
midgame (in band) · undercuts + leader-bumps active (politics working).

**Interpretation caution (unchanged, important):** win rates rank *scripts*,
and the script order (Spike > Engine > Discounter) may be a skill order.
What is robust is structural: free permanent coverage dominates ~20
configurations; cash-pricing it is the only lever that ever moved it
without killing something else. Human retaliation (worth ~14pp in sim)
should compress 63/28/8 further. Do not tune further on bot data.

## The unsolved structural problem: deflation

Every configuration ever run ends with the table **poorer than it started**
(10–25c from 30c). The design has **one faucet and four sinks**:

| Flow | Mechanism | Scales with player investment? |
|---|---|---|
| Faucet: customer sales | bank pays your price | only via eligibility, which caps ~50–60% of demand served |
| Sink: production | 2c/widget | yes |
| Sink: ads | 1c each, churned (≈10 bumps/game force re-buys) | yes |
| Sink: capacity expansion | 4c | yes |
| Sink: 3rd chip | 4 actions + 6c | once |

Ceiling math (3p, 57-card deck, avg max price ≈ 3.5c): faucet ceiling at
impossible-perfect play ≈ 57 × 3.5 ≈ 200c; realistic faucet (50–60% served)
≈ 90–110c for the whole table; sinks to achieve that ≈ 125–145c
(40 widgets × 2c + 30–42c ads + 8–12c expands + 6–12c chips). Net ≈ one
player's starting stake, negative. Ten+ buoyancy knobs all failed the same
way: raising the faucet (bands, demand volume, inflation) flows to the
eligibility leader; cutting sinks (prodcost 1, free ads) compounds the
coverage leader. **The faucet doesn't scale with player investment; the
sinks do.** Marketing-as-awareness only redistributes a fixed pie — FCM
survives brutality because its marketing grows the pie. That is the shape
of every rejected lever, and why the problem is structural, not numeric.

Compounding effects: score trajectory points down (arc flattened); early
revenue is a larger share of a shrinking money supply (Q2-leader stickiness
and deflation are the same disease); the starting 10c dominates lifetime
cash, over-weighting openings. Confounds: bots are wasteful (humans will
land less negative) but the ceiling argument is play-independent; fixed
script skill inflates spread, not the sum — the sum is the claim.

Options, in order of recommendation:

1. **Presentation scaling: multiply all money ×5** (prices 10–30, cost 10,
   ads 5, chip3 30c, start 50c). Identical ratios — the sim results carry
   verbatim — but scores *feel* like an economy (25–175 range). Zero
   structural risk. Cheap to test at the table.
2. **Demand-creation redesign (v0.5 question):** the faucet must scale with
   marketing investment (the FCM lesson; our Option-A verb deferred at the
   diet stage). Naive version feeds the creator — the design problem is
   *targeting*. Human design call, informed by sim.
3. **Accept the brutal economy** (FCM posture): legitimate for the heavy
   segment if positioned as a knife-fight. Not recommended without (1).

Also note: the deflation is *partly* bot indiscipline (bots produce into
unsellable shelves). Human play will read richer than the sim shows — but
the faucet-ceiling math is real regardless. Table decision, instrumented.

## Robust cross-config findings (keep)

- Ad cost 1c is a leader-brake; 0 unleashes the coverage leader.
- Production cost 2 is structural; 1 empowers the leader in every regime.
- Raising any price band widens premium eligibility → starves Budget.
- Trend premium +1 (not +2). Persist customers. Retaliation helps challengers.
- Pure-Budget is a portfolio leg, not a strategy, in every configuration.
- 4p + Corporate runs mechanically clean; **balance claims deferred** until
  the 3p core survives humans (scaling test was not the priority after the
  regression failure).

## v0.4 numbers (adopted in `rules-v0.4.md`)

3rd chip = **4 R&D actions + 6c** · E-band 4–5 · everything else as v0.2/3.
Open for the table: economy feel (option 1 vs 3), bankruptcy floor,
nudge usage, Portfolio-style mixed play (the 4p Portfolio bot is built and
ready for a future iteration once 3p stabilizes).
