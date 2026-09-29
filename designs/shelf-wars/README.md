# Shelf Wars (working title)

A mid-euro/heavy board game about **product marketing**. Players run widget
companies fighting for shelf space in a shared, fully visible market.
Build it, hype it, price it — the market shows no mercy.

| Spec | Value |
|---|---|
| Players | 3–4 (sweet spot: 4) |
| Length | ~100–120 min |
| Target weight | BGG ~2.9–3.3 |
| Core mechanism | Worker placement (3 execs/quarter, 4th from Q3) |
| Supporting systems | Demand market · funnel sales resolution · production/inventory · marketing/awareness |
| Randomizers | One: the demand deck (input-side only) |
| Scoring | Cash = VP (no endgame conversion) |
| Status | **v0.5** — structurally validated (3rd chip 4 actions + 6c; 4 ad slots/segment); sim campaign declared complete. Next: physical Stage-1/2 |

The spine of the design is the **sale funnel**, printed on the board:

> Customers must **know you** (ad in their segment) → **want you**
> (your product covers their attribute set) → **afford you**
> (price ≤ their max). Most cash wins.

Every action in the game feeds exactly one funnel step, which is both the
teach and the built-in bloat check.

## Files

- `01-concept.md` — design exploration: core problem, principles, exemplars
- `02-design-spec.md` — the locked design + decision record (critique & subsystem diet)
- `03-balance-pass.md` — numbers v0.1: economy, price bands, deck math, knob sheet
- `04-stage1-prototype.md` — component list + self-play protocol + exit criteria
- `05-sim-results-v0.1.md` — Monte Carlo iteration 1 (compressed game): chip3 2→3, persist adopted
- `06-sim-results-v0.2.md` — iteration 2 (full game + retaliation) — **partly contaminated; read with its errata banner**
- `07-sim-results-iter3.md` — iteration 3 (root-cause hunt): the real lever (3rd chip = 4 actions + 6c), 15+ knob verdicts, deflation analysis
- `08-economy-redesign-v0.5-plan.md` — demand-creation plan (**tested and falsified**; kept as record)
- `09-sim-results-v0.5.md` — iteration 4: creation falsified, **ad slots 3→4 adopted** (best balance of the campaign), eligibility-gate taxonomy
- `rules-v0.5.md` — **current** rules reference (4 ad slots/segment)
- `rules-v0.4.md`, `rules-v0.3.md`, `rules-v0.2.md`, `rules-v0.1.md` — archived drafts
- `prototype/customers-4q-v0.3.csv` — 32-card compressed deck
- `prototype/customers-full-3p-v0.3.csv` — 57-card full 3p deck
- `sim/` — deckgen + Monte Carlo sim (reproducible)

## Changelog

| Version | Date | Change |
|---|---|---|
| v0.1 | 2026-09-28 | Initial package: brainstorm → spec → math → Stage-1 plan |
| v0.2 | 2026-09-28 | Post-sim: 3rd chip = 3 actions (was dominant at 2); customers persist 1 quarter; 5 rules clarifications from sim (see `05-sim-results-v0.1.md`) |
| v0.3 | 2026-09-28 | Post full-game sim: 3rd chip = 4 actions (coverage compounds over 6 quarters); Enthusiast band 4–5; trend premium confirmed +1 (see `06-sim-results-v0.2.md`) |
| v0.4 | 2026-09-28 | Iteration 3: regression gate caught contaminated v0.3 (chip never landed in sim). Real lever found: 3rd chip = 4 actions **+ 6c cash** — knife-edge 5c/6c/7c = 86/63/0% Spike (see `07-sim-results-iter3.md`) |
| v0.5 | 2026-09-28 | Iteration 4: demand-creation plan falsified (eligibility, not volume, is the choke). **Ad slots 3→4 adopted**: Spike 47 / Discounter 31 / Engine 22 — best balance of the campaign (see `09-sim-results-v0.5.md`) |

## Open decisions (owner: designer)

- Price reveal: secret-simultaneous (current) vs. open pricing action (lighter)
- 2p support in the box: undecided (dummy demand deck is the fallback)
- ~~Unsold customers: discard vs persist~~ → **resolved v0.2: persist one quarter** (sim)
- Bankruptcy floor: scrap-for-1c is leading candidate (sim: no balance distortion) — Stage-2 feel question
- Economy feel: tight by design; ×5 presentation rescale is the first lever, not rules
- Campaign nudge usage: bots ~1.2/game; cut for humans if equally ignored
- Creation module: shelved with evidence (`09`); may return as promo/variant
- Final title (Shelf Wars is placeholder energy)
