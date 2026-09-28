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
| Status | **v0.1** — pre-prototype; Stage-1 solo sim is the next step |

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
- `rules-v0.1.md` — one-page rules reference for the solo sim

## Changelog

| Version | Date | Change |
|---|---|---|
| v0.1 | 2026-09-28 | Initial package: brainstorm → spec → math → Stage-1 plan |

## Open decisions (owner: designer)

- Price reveal: secret-simultaneous (current) vs. open pricing action (lighter)
- 2p support in the box: undecided (dummy demand deck is the fallback)
- Unsold customers: discard at end of income (current recommendation) vs. persist one quarter
- Final title (Shelf Wars is placeholder energy)
