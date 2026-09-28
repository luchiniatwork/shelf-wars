# Shelf Wars — Rules Reference v0.4 (post iteration-3 sim)

Changes from v0.3 (see `07-sim-results-iter3.md`; supersedes parts of
`06-sim-results-v0.2.md`, which was based on a contaminated sim run):

1. **A product line's 3rd chip costs 4 R&D actions *and* 6c cash.**
   Sim proof across ~20 configurations: permanent coverage is the dominant
   asset and action cost alone never balances it (99%+ at any action price);
   the cash price is the only lever that works. Knife-edge: 5c too cheap
   (86%), 7c kills the strategy (0%) — **6c** it is.
2. Enthusiast max prices stay **4–5**; trend premium stays **+1**.
3. Everything else unchanged from v0.2/3 (persist, ad slots/bump, shelf 6,
   ads 1c, production 2c, start 10c, execs 3→4 at Q3).

## Goal

Run the most profitable widget company. **Most cash after the final quarter
wins.** A customer buys from you only if they **know you** (your ad in
their segment), **want you** (your product covers all their attribute
icons), and **can afford you** (your price ≤ their max price).

## Setup

- Market sheet: 3 segments (Budget / Mainstream / Enthusiast), 3 ad slots
  each, trend loop (A→B→C→D) with marker on A.
- Demand deck in quarter piles (Q1 face-down): full game = 57 customers on
  the curve 5/7/9/11/12/13 (`prototype/customers-full-3p-v0.3.csv` — still
  valid; bands unchanged).
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
  A line's **3rd chip costs 4 R&D actions + 6c** (actions may be spread
  across quarters; the 6c is due when the chip lands).
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

## Open issues under test (do not "fix" in play without logging)

- **Economy feel**: sim shows a structurally tight (deflationary) economy.
  If it feels bad at the table, first try **presentation scaling ×5**
  (identical ratios, bigger-feeling numbers); the deeper fix is
  demand-creation design (v0.5), not cost-side knobs (15+ rejected).
- **Bankruptcy floor**: scrap inventory for 1c is the leading candidate
  (sim: no balance distortion).
- **Campaign nudge usage** (~1.2/game by bots). Escape hatch armed.
- **Pure-Budget viability**: portfolio leg in sim. Watch mixed B+M play.
