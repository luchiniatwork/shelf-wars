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
| Status | **v0.2** — bot-sim validated structurally; Stage-1 physical solo sim is the next step |

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
- `05-sim-results-v0.1.md` — greedy-bot Monte Carlo: findings, knob verdicts, open issues
- `rules-v0.2.md` — **current** rules reference (post-sim)
- `rules-v0.1.md` — archived first draft
- `prototype/customers-v0.1.csv` — 32-card customer deck (source of truth)
- `sim/` — deckgen + Monte Carlo sim (reproducible)

## Changelog

| Version | Date | Change |
|---|---|---|
| v0.1 | 2026-09-28 | Initial package: brainstorm → spec → math → Stage-1 plan |
| v0.2 | 2026-09-28 | Post-sim: 3rd chip = 3 actions (was dominant at 2); customers persist 1 quarter; 5 rules clarifications from sim (see `05-sim-results-v0.1.md`) |

## Open decisions (owner: designer)

- Price reveal: secret-simultaneous (current) vs. open pricing action (lighter)
- 2p support in the box: undecided (dummy demand deck is the fallback)
- ~~Unsold customers: discard vs persist~~ → **resolved v0.2: persist one quarter** (sim)
- Bankruptcy floor: loan rule / scrap-for-1c / accept brutality — Stage-2 question
- Final title (Shelf Wars is placeholder energy)
