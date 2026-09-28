# 04 — Stage-1 Prototype: Solo Sim Plan

Doctrine: this build is a **question-answering machine**, not a mini final
game. Ugly, ~$5, one evening to build. No polish before the loop works.

## The four Stage-1 questions

1. **Does the funnel resolve fast and unambiguously?**
   Target: income < 3 min/quarter, zero unresolvable ties.
2. **Does the demand curve create pressure?**
   Target: 1–2 unsold widgets per player per quarter in mid-game.
3. **Is the quarter anatomy complete?**
   Every "wait, what happens now?" is a rules gap — log it, don't improvise
   silently.
4. **Does a fixed heuristic policy dominate?**
   One seat winning every sim by a mile = dominant-strategy smell; fix
   before humans see it.

**Stage 1 cannot answer:** fun, real balance, price-reveal poker (hidden
info is fake when you hold all three hands), kingmaking. Don't judge the
game emotionally off solo runs — judge whether it *runs*.

## Component list (~$5)

| Component | Build | Qty |
|---|---|---|
| Customer cards | Index cards: segment letter, 1–2 attribute letters, max price | 32 (4-quarter compressed game) |
| Attribute chips | Cardboard squares, letters A/B/C/D | 16 (4× each) |
| Product line cards | Index cards, 3 chip slots drawn, price in pencil | 6 (2 per seat) |
| Market board | Sheet of paper: 3 rows (B/M/E), 3 ad-slot boxes each, 4-attribute trend loop in corner | 1 |
| Ad tokens | 9 cubes per seat color | 27 |
| Widgets | 10 cubes per seat color (different shape from ads) | 30 |
| Execs | 4 pawns per seat | 12 |
| Money | Poker chips or paper track (1/5/10/20) | — |
| Trend + quarter markers | Coins | 2 |

**Start the spreadsheet on day one** — one row per customer card (segment,
wants, max price). The deck is data; the CSV later feeds
nanDECK/Component.Studio verbatim. Label everything **v0.1**.

## Deck composition v0.1 (3-seat sim, 4 quarters)

| Quarter | Deal | Budget (1-want) | Mainstream (2-want) | Enthusiast (2-want, 5–6) |
|---|---|---|---|---|
| Q1 | 5 | 2 | 2 | 1 |
| Q2 | 7 | 3 | 3 | 1 |
| Q3 | 9 | 4 | 3 | 2 |
| Q4 | 11 | 4 | 5 | 2 |

Seeding: single-wants split evenly A/B/C/D; double-wants spread across all
6 pairs, no pair twice in one quarter. (Compressed game: 4 quarters, not 6
— the loop question doesn't need the full arc.)

## Self-play protocol

**Three seats, fixed heuristic policies** — kills decision fatigue *and*
smoke-tests dominant strategies:

- **Seat 1 "Discounter"** — 2-chip lines, Budget/Mainstream ads, prices at
  band floor.
- **Seat 2 "Engine"** — capacity to 3 before max production, Mainstream
  focus, mid prices.
- **Seat 3 "Spike"** — rush 3-chip line, Enthusiast ads, band-ceiling
  prices, Campaign-nudges toward its own attribute.

**Session loop (target ≤75 min):** run the quarter cycle as written
(`rules-v0.1.md`). Simulate the price reveal by setting prices per seat in
turn, ignoring other seats' dials — accept the leak; real reveal poker is
a Stage-2 question.

**Edge-case drills (between games, construct deliberately):**

- Exact price + ad-count tie → does the ladder always terminate?
- Full segment where your own ad is oldest → suggested rule: bump oldest
  *opponent* ad only.
- Shelf full at production → suggested rule: produce only into free slots.
- A customer nobody covers → unsold.

**Open micro-rule to settle in sim:** unsold customers — **discard at end
of income** (recommended: quarters stay independent, deck curve stays the
sole demand driver) vs. persist one quarter (try only if Q1 feels too
swingy).

**Log every run** (no log = the session never happened):
version · quarter timings · unsold/player/quarter · price-1 dump count ·
nudge uses · cash at Q2/Q4/final · gap-list entries + interim rulings.

## Exit criteria → Stage 2

- Full session without rules collapse; gap list resolved into written rules
- Income < 3 min/quarter with the ladder printed on the market sheet
- Unsold average in the 0.5–3 band (else: deck-curve knob, nothing else)
- No seat wins by >2× the loser across 2–3 runs

## Stage-2 preview (ugly functional, ~$25)

Sleeves + paper inserts for the deck, label-paper market board, restore
the full 6-quarter curve and a 4th seat. Questions shift to the human ones:
price-reveal sweat, 4p downtime, bump-rule kingmaking at 3p, and whether
people lean in during income or check phones. One variable per build from
there on; batch changes between waves, never mid-wave.
