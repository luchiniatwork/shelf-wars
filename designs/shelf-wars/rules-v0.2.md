# Shelf Wars — Rules Reference v0.2 (post-sim)

Changes from v0.1 (validated by greedy-bot Monte Carlo, see
`05-sim-results-v0.1.md`):

1. **A product line's 3rd chip costs 3 R&D actions** (was 2 — dominant
   strategy at 2).
2. **Unsold customers persist one quarter**, then are discarded (was:
   discard immediately — nearly halved unserved demand).
3. Rules clarifications the sim forced: cheapest covering line sells;
   bump oldest *opponent* ad only; production into free slots only; trend
   advances from Q2; ads persist until bumped.

## Goal

Run the most profitable widget company. **Most cash after the final quarter
wins.** A customer buys from you only if they **know you** (your ad in
their segment), **want you** (your product covers all their attribute
icons), and **can afford you** (your price ≤ their max price).

## Setup

- Market sheet: 3 segments (Budget / Mainstream / Enthusiast), 3 ad slots
  each, trend loop (A→B→C→D) with marker on A.
- Demand deck in quarter piles (Q1 face-down).
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
  A line's **3rd chip costs 3 R&D actions** (spend them across quarters if
  you like; the chip lands on the 3rd).
- **Factory** — produce widgets at 2c each into free shelf slots, up to
  capacity (start 2); **or** expand capacity +1 for 4c (max 5).
- **Marketing** — place 2 ads (1c each).
- **Campaign** — place 1 ad (1c) **and** move the trend marker one step
  (either direction).
- **Research** — look at the top 3 cards of the demand deck; return in any
  order.

**Ad slots:** 3 per segment, ads persist until bumped. Full segment → your
placement **bumps the oldest opponent ad** (returned to its owner). A
segment holding only your ads is full to you.

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

- **Bankruptcy is a dead state** (0 cash → no useful action). Candidate
  answers: loan rule / scrap inventory for 1c / accept the brutality.
  Instrument in Stage-2; do not patch casually.
- Campaign nudge value (bots used it 0.5×/game; if humans also ignore it,
  delete the clause per the Option-B escape hatch).
