# 01 — Concept: Product Marketing as a Game

> Origin: brainstorm for a game where players run companies that build and
> sell "widgets" — widgets have attributes, demand, prices, marketing — with
> an income phase (round-end or triggered) where widgets sell or don't.

## The core design problem

The game lives or dies on the **income round** — the moment all systems
collide. Two classic failure modes:

1. **Bookkeeping homework** — players watch one person do math.
2. **Opaque lottery** — players feel sold-or-not was decided by the game,
   not by them.

Everything in this design is organized around avoiding those two.

## The clarity backbone: the 3-step funnel

Every sale answers three questions, in order, printed on the board:

1. **Do they know you exist?** → marketing (awareness)
2. **Do they want what you built?** → attributes matching demand
3. **Will they pay your price?** → price vs. willingness-to-pay

One-sentence teach: *customers must know you, want you, and afford you.*
Every action maps to exactly one funnel step → no orphan subsystems; the
bloat check is built in.

## The engagement principle: visible demand, deterministic resolution

Exemplars:

- **Food Chain Magnate** — marketing places demand tokens *physically on the
  map*; "dinnertime" resolution is 100% deterministic. Everyone can count who
  buys what before it happens. Drama comes from *committed decisions
  colliding*, not from the reveal.
- **Smartphone Inc.** — secret simultaneous price/production planning, then
  fast deterministic market resolution.
- **Container** — player-set prices, closed player-driven economy.

Rule: randomness enters in *what demand appears* (input luck, before
commitments), never in *whether a sale closes* (output luck). No dice at
sale time.

## Idea modules considered

- **Demand as a public, manipulable object** — tokens/cards in customer
  segments on a shared market board. Countable, contestable, finite.
- **Create vs. capture demand** — marketing *creating* demand (FCM-style,
  aggressive) vs. *capturing* it (awareness race). Resolution: both, via the
  Campaign space (see spec).
- **Attributes as matching, not math** — 2–4 icon attributes; sale = visual
  set-matching, zero arithmetic.
- **Discrete price tiers (1–6)** — never a continuous dial; anti-AP.
  Undercut rule: cheapest eligible seller wins → emergent price wars.
- **Income triggers considered** — fixed cadence (flat), deck depletion
  (anticipation), player-triggered "earnings call" (timing decision).
- **Inventory pressure** — shelf cap (opportunity cost, loss-aversion-safe)
  rather than cash penalties.
- **Catch-up philosophy** — structural caps (shelf size, finite customers,
  ad slots) instead of bolt-on rubber-banding.

## Failure modes designed against

- **Multiplayer solitaire** → demand is shared and contestable, always.
- **Math-problem finale** → cash = VP; totals < 100; no conversion step.
- **Two-games-fighting** → the market game is the core; the company engine is
  demoted to a single capacity track.
- **Runaway leader** → one shelf can only eat so much of the market per
  quarter; money→production→money is capped by components, not rules.

## Three sketch shapes (by weight)

| Weight | Shape |
|---|---|
| Light (~45 min) | Face-up customer row; Build (2 icons) / Advertise / Price actions; round-end income = cheapest matching widget sells |
| **Mid-heavy (chosen)** | FCM-lite: marketing places demand/awareness into shared segments; deterministic ladder resolution; trend track; quarterly price reveal |
| Heavy | Smartphone-style hidden simultaneous planning + persistent campaigns + depreciation + segment unlocks |
