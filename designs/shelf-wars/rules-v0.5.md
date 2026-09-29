# Shelf Wars — Rules Reference v0.5 (eligibility fix)

Change from v0.4 (validated by sim iteration 4, see `09-sim-results-v0.5.md`):

1. **Ad slots: 4 per segment** (was 3). One number, no new rules. Effect:
   Discounter archetype viable for the first time (31% bot win share),
   Spike 65% → 47%, economy +25%. Awareness was the over-constrained gate.

The demand-creation plan from `08-economy-redesign-v0.5-plan.md` was
**tested and falsified** (random created demand converts at ~10% through
the coverage/price funnel — demand volume was never the choke). No growth
piles, no creation rule. The trend nudge stays (balance-neutral; keeps
Campaign distinct from Marketing).

## Goal

Run the most profitable widget company. **Most cash after the final quarter
wins.** A customer buys from you only if they **know you** (your ad in
their segment), **want you** (your product covers all their attribute
icons), and **can afford you** (your price ≤ their max price).

## Setup

- Market sheet: 3 segments (Budget / Mainstream / Enthusiast), **4 ad slots
  each**, trend loop (A→B→C→D) with marker on A.
- Demand deck in quarter piles (Q1 face-down): full game = 57 customers on
  the curve 5/7/9/11/12/13 (`prototype/customers-full-3p-v0.3.csv` — still
  current; no v0.5 deck changes).
- Per seat: 10c, 4 execs (use 3 until Q3), 2 product-line cards, 10 widget
  cubes, **12 ad cubes** (4 slots × 3 segments), shelf space for 6 widgets.
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

**Ad slots:** **4 per segment**, ads persist until bumped. Full segment →
your placement **bumps the oldest opponent ad**. A segment holding only
your ads is full to you.

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

## Presentation option (apply to the physical build if numbers feel small)

Multiply all cash values ×5 (prices 10–30, production 10/widget, ads 5,
expand 20, 3rd chip 30c, start 50c). Identical ratios — sim results carry
verbatim. Decide after the first table session.

## Open issues under test (do not "fix" in play without logging)

- **Economy feel**: tight by design (see `09-sim-results-v0.5.md` final
  accounting). First lever is the ×5 rescale above, not rules.
- **Bankruptcy floor**: scrap inventory for 1c (sim: no distortion).
- **Campaign nudge usage**: if humans ignore it like bots (~1.2/game),
  cut it — Campaign becomes 1 ad + a small fee rebate, or fold into
  Marketing.
- **Creation as texture**: shelved as an economy fix; may return as a
  promo/variant module with the evidence file attached.
