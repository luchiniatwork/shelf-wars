# Shelf Wars — Rules Reference v0.3 (post full-game sim)

Changes from v0.2 (validated by iteration-2 Monte Carlo over the full
6-quarter game, see `06-sim-results-v0.2.md`):

1. **A product line's 3rd chip costs 4 R&D actions** (was 3 — coverage is
   the only permanent asset and compounded over the full arc).
2. **Enthusiast max prices are 4–5** (was 5–6 — premium margin nerf; brings
   mid-price volume to parity).
3. Trend premium confirmed at **+1** (+2 tested: self-reinforcing).

## Goal

Run the most profitable widget company. **Most cash after the final quarter
wins.** A customer buys from you only if they **know you** (your ad in
their segment), **want you** (your product covers all their attribute
icons), and **can afford you** (your price ≤ their max price).

## Setup

- Market sheet: 3 segments (Budget / Mainstream / Enthusiast), 3 ad slots
  each, trend loop (A→B→C→D) with marker on A.
- Demand deck in quarter piles (Q1 face-down): full game = 57 customers on
  the curve 5/7/9/11/12/13 (`prototype/customers-full-3p-v0.3.csv`).
- Per seat: 10c, 4 execs (use 3 until Q3), 2 product-line cards, 10 widget
  cubes, 9 ad cubes, shelf space for 6 widgets.
- Each seat: build one starting product line (2 chips of choice), set its
  price dial.

## Quarter anatomy

1. **Forecast** — from Q2 onward, advance the trend marker one step. Deal
   this quarter's customers face-up into segment rows (alongside any
   persisted customers from last quarter).
2. **Price reveal** — set one price (1–6) per product line.
3. **Actions** — single-exec placement, rotating seats.
4. **Income** — resolve sales (ladder below), segment by segment: Budget,
   then Mainstream, then Enthusiast.
5. **Upkeep** — unsold widgets stay on the shelf. Customers unsold for the
   **second consecutive quarter** are discarded.

## Action spaces

- **R&D** — take 1 attribute chip onto a product line (max 2 lines).
  A line's **3rd chip costs 4 R&D actions** (spend across quarters; the
  chip lands on the 4th).
- **Factory** — produce widgets at 2c each into free shelf slots, up to
  capacity (start 2); **or** expand capacity +1 for 4c (max 5).
- **Marketing** — place 2 ads (1c each).
- **Campaign** — place 1 ad (1c) **and** move the trend marker one step
  (either direction).
- **Research** — look at the top 3 cards of the demand deck; return in any
  order.

**Ad slots:** 3 per segment, ads persist until bumped. Full segment → your
placement **bumps the oldest opponent ad**. A segment holding only your ads
is full to you.

## Income resolution ladder

Each customer, in segment order, considers sellers who pass all three:

1. **Ad** in this segment
2. Product **covers** all the customer's attribute icons
3. **Price ≤ customer's max** (+1 to max if the customer wants the
   trend-marked attribute)

Among eligible sellers: **lowest price → most ads in this segment →
start-seat order** wins the sale. If you have several covering lines, your
**cheapest** covering line sells. Seller collects the price; the widget
leaves the shelf.

## End

After the final quarter's income, most cash wins. Shelf inventory is
worthless.

## Customer composition reference (deck building)

Budget (wants 1 attribute, max 2–3) ~40% · Mainstream (2 attributes,
max 3–5) ~40% · Enthusiast (2 attributes, **max 4–5**) ~20%.

## Open issues under test (do not "fix" in play without logging)

- **Bankruptcy floor**: scrap inventory for 1c is the leading candidate
  (sim: no balance distortion either way). Add only if the dead state
  feels bad at the table.
- **Free-ads variant** (ads cost 0): grows the economy but kills the
  pure-Budget archetype in sim. Table-test as a variant only.
- **Pure-Budget viability**: sim says Budget is a portfolio leg, not a
  solo strategy. Watch whether mixed B+M beats pure M at the table.
- **Campaign nudge usage** (bots: ~1.2/game). Escape hatch still armed.
- If the economy still feels tight after human tests: try **4 ad slots per
  segment** (less churn) before touching ad cost or production cost.
