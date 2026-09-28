# 02 — Design Spec (v0.1, locked at Stage-1 entry)

Frame: 3–4 players · 5–6 quarters · ~100–120 min · cash = VP.
Core mechanism: **worker placement**. 1 core + 4 supporting systems
(demand market, funnel resolution, production, marketing). One randomizer
(demand deck, input-side). One scoring funnel (cash).

## Quarter structure

1. **Forecast (input luck)** — trend marker auto-advances one step on the
   4-attribute loop; new customer cards dealt face-up into segments.
2. **Price reveal (the ceremony)** — all players secretly set one price dial
   (1–6) per product line; reveal simultaneously. ~30 seconds; the game's
   poker heartbeat. Once per quarter.
3. **Action phase** — single-exec placement turns around the table.
4. **Income** — deterministic funnel resolution, segment by segment (ladder
   below). Players resolve their own sales simultaneously.
5. **Upkeep** — unsold widgets stay on the shelf (they block next quarter's
   production). No cash penalties, no depreciation bookkeeping.

## The five action spaces

| Space | Effect |
|---|---|
| **R&D** | Take an attribute chip / retool a product line (max 2 lines, 2–3 chips each; the 3rd chip costs 2 actions — compression premium) |
| **Factory** | Produce up to capacity at 2c/widget **or** expand capacity +1 for 4c (start 2, max 5) |
| **Marketing** | Place 2 ads (1c each) into segment ad slots |
| **Campaign** | Place 1 ad **and** nudge the trend marker one step (Option B — see decision record) |
| **Market Research** | Peek at the top of the demand deck (mitigation currency for input luck) |

## Income resolution ladder (printed on the board)

For each customer, in segment order, among sellers who:

1. have ≥1 **ad in that segment** (know you), and
2. whose product **covers the customer's attribute set** (want you), and
3. whose **price ≤ customer's max** (afford you) —

the sale goes to: **lowest price → most ads in segment → start-player
marker.** Fully countable before it happens; zero dice.

## The market

- 3 segments at 3p: **Budget / Mainstream / Enthusiast** (+ **Corporate**
  at 4p as a scaling pressure-valve).
- Customer cards show: segment, 1–2 attribute wants (icons), max price.
- **Ad slots: 3 per segment.** Full segment → placing bumps the **oldest
  opponent ad** (suggested interim rule). Slot-blocking turns marketing
  into worker-placement-style contention and self-regulates awareness
  without a decay rule.
- **Trend**: customers wanting the hot attribute pay **+1 over printed
  max**. Marker auto-advances each quarter; Campaign nudges it.

## Inventory

- Shelf cap **6** widgets (per-player).
- Unsold widgets occupy slots → next quarter's production is throttled
  (opportunity cost, not cash loss — respects loss aversion).
- Inventory is worth **0 at game end** → the final-quarter fire sale is
  *emergent*, not scripted (no liquidation rule).

## Arc & ending

| Phase | Quarters | Texture |
|---|---|---|
| Growth | Q1–2 | Few customers; engines spin up |
| Peak | Q3–4 | All segments contested; price wars; 4th exec online (fixed milestone, Q3) |
| Saturation | Q5–6 | Demand deck visibly depletes → "market matures"; fat Q6 demand for the finale |

End trigger: quarter track + deck depletion (hybrid, both legible).
Winner: most cash. No conversion, no hidden scoring.

## Catch-up & feedback-loop policy

No naked catch-up rule (anti-pattern). Structural counterweights to the
money→production→money loop: shelf cap, 3 ad slots/segment, finite
customers per quarter, depletion clock. If playtests show blowouts, fix
order: tighten shelf cap → trim final-quarter demand → *only then* consider
a challenger rule.

---

## Decision record

### Critique score (idea-critique checklist, written-pitch fidelity)

**89/100 — Strong.** No auto-fail red flags.
Section scores: Fantasy 9 · Decisions 10 · Tension 10 · Arc 9 · Victory 9 ·
**Feedback loops 6** (weakest) · Agency/luck 10 · **Complexity budget 7** ·
Player types 10 · Commercial 9.
The two weak sections drove the subsystem diet below and the playtest
instrumentation (see 03).

### Subsystem diet (bloat audit)

Acid test: *does this rule create a decision, or perform maintenance?*
Maintenance rules were cut first.

| Cut / change | Rationale |
|---|---|
| ✂ Inventory depreciation | Shelf cap already punishes overproduction; second punishment paid in bookkeeping |
| ✂ Ad decay rule → **3 ad slots + bump-oldest** | Converts maintenance into blocking decisions; caps monopoly |
| ✂ Scripted liquidation quarter | Emergent fire sale (inventory = 0 at end) is a better climax, one fewer "remember" rule |
| ✂ Exec-growth economy → fixed Q3 milestone | Engine subgame was fighting the market game |
| Product lines **capped at 2** | Uncapped lines were a complexity multiplier on the price reveal |
| Challenger discount → **deferred to playtest** | Bolt-on catch-up is an anti-pattern; test structural caps first |
| Trend-shaping → **Option B: merged into Campaign space** | One space, one sentence: "1 ad + nudge." Preserves the market-*making* verb at near-zero rules cost. Escape hatch: if nudge use <10% of marketing actions, delete the clause |

Post-diet shape: 1 core + 4 supporting; 5 action spaces (inside working
memory budget); teach ≈ 15 min for a ~110 min game (~14%, inside tolerance).

### Teach plan (≈15 min)

1. Goal + funnel — "know you, want you, afford you; most cash wins" (2 min)
2. Quarter anatomy: forecast → price reveal → execs → income (4 min)
3. Five spaces, one sentence each (4 min)
4. Walk one income resolution with example cards (3 min)
5. Trend schedule + saturation end (2 min)

Everything else (bump, ties, endgame) lives on the player aid, not in the teach.

### Known risks to instrument

- **Ad-slot bumping** is the newest, least-proven rule — watch for final-
  quarter kingmaking (bumping the leader's ad to hand a segment to third
  place). Fallback: restrict bump targets or cap bumps.
- **3p politics** — open cash + undercutting can let a dead player pick the
  winner late. Multiple segments dilute it; watch in 3p tests.
- **Runaway leader** — structural caps are the bet; instrument rank at
  Q2/Q4 vs. final (see 03).
