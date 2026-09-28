# Shelf Wars — Rules Reference v0.1 (Stage-1 solo sim)

Half-page rules for the proof-of-concept build. Anything not covered here
is a **gap** — log it, pick an interim ruling, keep playing.

## Goal

Run the most profitable widget company. **Most cash after the final quarter
wins.** A customer buys from you only if they **know you** (your ad in
their segment), **want you** (your product covers all their attribute
icons), and **can afford you** (your price ≤ their max price).

## Setup

- Market sheet: 3 segments (Budget / Mainstream / Enthusiast), 3 ad slots
  each, trend loop (A→B→C→D) with marker on A.
- Demand deck: shuffle each quarter pile; place Q1 face-down.
- Per seat: 10c, 4 execs (use 3 until Q3), 2 product-line cards, 10 widget
  cubes, 9 ad cubes, shelf space for 6 widgets.
- Each seat: build one starting product line (2 chips of choice), set its
  price dial.

## Quarter anatomy

1. **Forecast** — advance trend marker one step. Deal this quarter's
   customers face-up into their segment rows.
2. **Price reveal** — set one price (1–6) per product line (solo sim: set
   per seat in turn, ignoring other dials).
3. **Actions** — single-exec placement, rotating seats, until all execs
   are placed.
4. **Income** — resolve sales (ladder below), segment by segment: Budget,
   then Mainstream, then Enthusiast. Collect cash.
5. **Upkeep** — unsold widgets stay on the shelf. Discard unsold customers.

## Action spaces

- **R&D** — take 1 attribute chip onto a product line (max 2 lines;
  a line's 3rd chip costs 2 actions total).
- **Factory** — produce widgets at 2c each into free shelf slots, up to
  capacity (start 2); **or** expand capacity +1 for 4c (max 5).
- **Marketing** — place 2 ads (1c each) into segment ad slots.
- **Campaign** — place 1 ad (1c) **and** move the trend marker one step
  (either direction).
- **Research** — look at the top 3 cards of the demand deck; return in any
  order.

**Ad slots:** 3 per segment. Full → your placement **bumps the oldest
opponent ad** (returned to its owner).

## Income resolution ladder

Each customer, in segment order, considers sellers who pass all three:

1. **Ad** in this segment
2. Product **covers** all the customer's attribute icons
3. **Price ≤ customer's max** (+1 to max if the customer wants the
   trend-marked attribute)

Among eligible sellers: **lowest price → most ads in this segment →
start-seat order** wins the sale. Seller collects the price; widget leaves
the shelf; customer discarded.

## End

After Q4 income (compressed sim), most cash wins. Shelf inventory is
worthless.

## Interim rulings (proposed — validate in sim)

- Bump targets: oldest **opponent** ad only; a segment full of your own
  ads is full to you.
- Production: only into free shelf slots.
- Unsold customers: discard (do not persist).
- Ties beyond the ladder: start-seat order, rotating each quarter.
