# 04 — Stage-1 Prototype: Solo Sim Plan

> **Updated to v0.5 (2026-09-29).** Originally written pre-sim for v0.1;
> the Monte Carlo campaign (`05`–`09`) has since answered two of the four
> original questions (demand pressure, dominant-strategy smell) and
> resolved the persist-vs-discard micro-rule (persist one quarter, v0.2).
> What remains for the physical build is what sims cannot measure: flow
> with human hands, rules completeness as written, ergonomics, duration.
> All numbers below are v0.5 (4 ad slots/segment; 3rd chip = 4 R&D actions
> + 6c; persist).

Doctrine: this build is a **question-answering machine**, not a mini final
game. Ugly, ~$5, one evening to build. No polish before the loop works.

## The Stage-1 questions (post-sim scope)

1. **Does the funnel resolve fast and unambiguously with human hands?**
   Target: income < 3 min/quarter, zero unresolvable ties, ladder printed
   on the market sheet.
2. **Is the quarter anatomy complete as written in `rules-v0.5.md`?**
   Every "wait, what happens now?" is a rules gap — log it, don't improvise
   silently.
3. **Do the components work physically?**
   Price dials, 3 chip slots per line card, 4-slot market rows, the persist
   row, table footprint. Fiddliness is data.
4. **What does a quarter cost in wall-clock time?**
   Solo pace → extrapolate 3p/4p against the 100–120 min target.
5. **The v0.5 feel questions** (log, don't fix mid-play): does the ×5
   rescale feel better? Does scrap-for-1c ever trigger? Does the nudge get
   used?

**Answered by sim — do not re-test physically:** demand-curve pressure
(unsold 1.15/seat/quarter, in band) and fixed-policy balance (Spike 47 /
Discounter 31 / Engine 22). Physical solo balance signal is noise by
comparison; the sim remains the balance authority.

**Stage 1 cannot answer:** fun, real balance, price-reveal poker (hidden
info is fake when you hold all three hands), kingmaking feel, clarity to a
newcomer. Don't judge the game emotionally off solo runs — judge whether
it *runs*.

## Component list (~$5)

| Component | Build | Qty |
|---|---|---|
| Customer cards | Index cards: segment letter, 1–2 attribute letters, max price | 32 (compressed) + 57 (full) |
| Attribute chips | Cardboard squares, letters A/B/C/D | 16 (4× each) |
| Product line cards | Index cards, 3 chip slots drawn, price in pencil; note "3rd chip: 4 actions + 6c" | 6 (2 per seat) |
| Market board | Sheet of paper: 3 rows (B/M/E), **4 ad-slot boxes each**, persist row, trend loop (A→B→C→D) in corner, income ladder printed | 1 |
| Ad tokens | **12 cubes per seat color** (4 slots × 3 segments) | 36 |
| Widgets | 10 cubes per seat color (different shape from ads) | 30 |
| Execs | 4 pawns per seat (use 3 until Q3) | 12 |
| Money | Poker chips (1/5/10/20) — see ×5 note below | — |
| Trend + quarter markers | Coins | 2 |

**Money scale:** build at **×5 from session 1** — prices 10–30, production
10/widget, ads 5, expand 20, 3rd chip 30c, start 50c. `09` recommends it,
ratios are identical so sim results carry verbatim, and chips make the
scale a declaration rather than a rebuild. If it feels worse at the table,
revert by announcement. Record the verdict in the session log.

Decks are already data: `prototype/customers-4q-v0.3.csv` (32-card
compressed) and `prototype/customers-full-3p-v0.3.csv` (57-card full game,
curve 5/7/9/11/12/13 — no v0.5 deck changes). The CSVs later feed
nanDECK/Component.Studio verbatim. Label everything **v0.5**.

## Deck composition (compressed build record)

The 32-card compressed deck is built from `customers-4q-v0.3.csv`; the
seeding rules below are the record of how it was composed.

| Quarter | Deal | Budget (1-want) | Mainstream (2-want) | Enthusiast (2-want, 5–6) |
|---|---|---|---|---|
| Q1 | 5 | 2 | 2 | 1 |
| Q2 | 7 | 3 | 3 | 1 |
| Q3 | 9 | 4 | 3 | 2 |
| Q4 | 11 | 4 | 5 | 2 |

Seeding: single-wants split evenly A/B/C/D; double-wants spread across all
6 pairs, no pair twice in one quarter.

## Self-play protocol

**Three seats, fixed heuristic policies** — same archetypes as the sim
bots, so qualitative surprises are comparable (kills decision fatigue too):

- **Seat 1 "Discounter"** — 2-chip lines, Budget/Mainstream ads, prices at
  band floor.
- **Seat 2 "Engine"** — capacity to 3 before max production, Mainstream
  focus, mid prices.
- **Seat 3 "Spike"** — rush 3-chip line (4 actions + 6c), Enthusiast ads,
  band-ceiling prices, Campaign-nudges toward its own attribute.

**Session plan (≤5 sessions, one written question each):**

| # | Build | Question |
|---|---|---|
| 1–2 | Compressed 4Q | Funnel speed + ambiguity; rules-gap harvest |
| drills | Between runs | Edge cases below, constructed deliberately |
| 3–4 | Full 6Q | Duration extrapolation; ergonomics; does Discounter *feel* viable (qualitative cross-check vs sim, not numeric) |
| 5 (optional) | Grief drill | One seat plays pure ad-churn/bump denial — can it lock a seat out of a segment? (structural probe of the 3p kingmaking question) |

**Session loop (target ≤75 min compressed; record actuals for full):**
run the quarter cycle as written (`rules-v0.5.md`). Set prices per seat in
turn, ignoring other seats' dials — the hidden-info leak is accepted and
noted in the log; price-reveal poker is a Stage-2 question.

Explain each turn out loud as you play — anything you cannot explain
cleanly is a rulebook/flow bug; log it. No mid-session redesign: change
ideas go on the "For Next Time" list; one variable per build from here on.

**Edge-case drills (construct deliberately):**

- Exact price + ad-count tie → does the ladder always terminate
  (start-seat order)?
- Full 4-slot segment where your own ad is oldest → bump oldest *opponent*
  ad only; a segment holding only your ads is full to you.
- Shelf full at production → produce only into free slots.
- Persisted customer alongside the new deal → does the trend premium
  (+1 to max) apply cleanly? Second consecutive unsold quarter → discard.
- 3rd chip: actions spread across quarters; 6c (30c at ×5) due when the
  chip lands.
- A customer nobody covers → unsold.

**Open items under test (do not "fix" in play without logging):**

- Economy feel — tight by design (see `09` final accounting); ×5 is the
  first lever, not rules.
- Bankruptcy floor — scrap-for-1c is the leading candidate (sim: no
  distortion); log every moment it would have triggered and how it felt.
- Campaign nudge usage — bots used it ~1.2/game; log yours. If you ignore
  it too, it's a cut candidate.
- Creation module — shelved with evidence (`09`); do not reintroduce.

## Log every run

No log = the session never happened. Fields:
version · session question · quarter timings (actual) · unsold/player/
quarter · price-floor dump count · nudge uses · scrap triggers · cash at
Q2/Q4/final · gap-list entries + interim rulings · ergonomic/fiddliness
notes · "For Next Time" list.

Unsold average: log it, but divergence from the sim's 1.15/seat/quarter
flags policy-fidelity drift (you playing the seats unlike the bots), not a
balance problem.

## Exit criteria → Stage 2

- Full session without rules collapse; gap list resolved into written
  rules (→ `rules-v0.6.md`)
- Income < 3 min/quarter with the ladder printed on the market sheet
- Duration extrapolation lands in (or near) the 100–120 min band
- ×5 decision recorded; scrap rule written in or cut
- No seat wins by >2× the loser across 2–3 full runs (smell test only)

Then stop soloing. Every remaining question — price-reveal sweat, 4p
downtime, bump-rule kingmaking feel, lean-in during income, nudge value
for humans — is a human question.

## Stage-2 preview (ugly functional, ~$25)

Sleeves + paper inserts for the deck, label-paper market board, and a 4th
seat. Questions shift to the human ones: price-reveal sweat, 4p downtime,
bump-rule kingmaking at 3p, whether people lean in during income or check
phones, and nudge value for humans. One variable per build from there on;
batch changes between waves, never mid-wave.
