# Co-op Difficulty Architecture — Escalation, Dials, Calibration, Scaling

Load this when building the escalation curve, choosing difficulty dials, writing a calibration plan, or
scaling a co-op/solo design across player counts.

## 1. The Pandemic dissection (exemplar; all numbers from the official Z-Man rulebook)

**Win/lose.** Win by curing all 4 diseases. Lose on any of three independent clocks:
1. **8 outbreaks** (position collapse),
2. **cubes of a needed color exhausted** (resource bleed-out),
3. **player deck exhausted** (hard timer — "your team runs out of time").
Independent clocks force triage: you cannot over-invest in one defense.

**The escalation engine.** The infection rate marker starts on the leftmost "2" space (2 infection cards
per turn). An Epidemic card does three steps in order:
1. **Increase** — advance the infection rate marker one space (pressure ratchets permanently),
2. **Infect** — draw the BOTTOM card of the infection deck; that city jumps to 3 cubes (a brand-new hot
   spot, spike not trickle),
3. **Intensify** — reshuffle ONLY the infection discard pile and put it back ON TOP of the deck (known
   hot zones are guaranteed to re-flare).
This is the canonical escalation step: rate + spike + memory. The discard-recycle is the crucial,
most-copied idea — the threat deck has memory, so tension concentrates where players already feel pain.

**The difficulty dial.** Build the player deck with **4, 5, or 6 Epidemic cards = Introductory,
Standard, Heroic** (base deck: 48 city cards + 5 event cards + chosen epidemics, split into matched
piles with one epidemic per pile so epidemics spread through the session). Same rules, same length —
only the density of escalation beats changes. This is the model for "quantity dial, named tiers."

**Setup calibration.** 9 cities seeded: 3 cities × 3 cubes, 3 × 2, 3 × 1 (18 cubes) — the opening board
always contains one near-outbreak triage problem per cube level.

**Official solo adaptation (2013+ rulebook insert).** One player runs **3 roles sharing a single hand**
(hand limit still 7), with a face-up "archive" area to store/retrieve city cards via Share Knowledge;
the Researcher role is removed. Lesson: for co-ops, solo can be *role-multiplexing* instead of an automa
— the game system itself is the opponent.

## 2. Difficulty dial catalog

| Dial type | What you change | Exemplar | Caution |
|---|---|---|---|
| Quantity knob | Density/count of threat cards, enemies, rounds | Pandemic 4/5/6 epidemics | Cleanest; first choice |
| Stat knob | Enemy strength, VP bonuses, HP | Automa tier VP bonuses; Gloomhaven monster stat tables per scenario level 0–7 | Keep tables printed, not computed |
| Resource knob | Player starting assets, hand size, actions | common in scenario setups | Feels like handicap; label as tier |
| Timer knob | Rounds, clock length, deck size | deck-out timers; real-time lengths | Interacts with snowball: shorter timer = harsher early luck |
| Rules knob | Extra enemy powers, new exceptions | Spirit Island adversary levels I–VI | Use sparingly; each fork doubles test surface |
| Information knob | Open hands, revealed threat draws | "play open-handed for first game" | Good as teaching setting, poor as shipped tier |

**Formula exemplar.** Gloomhaven: recommended scenario level = **average party level ÷ 2, rounded up**,
then ±1 per group taste; monster stats, trap damage, and gold conversion all key off the resulting
level 0–7. One number drives the whole stat table — players self-select challenge without the designer
forking rules (Gloomhaven rulebook, 2017).

**Published-rating exemplar.** Spirit Island assigns each adversary/level a **difficulty rating 1–10**,
letting groups compose a target number from adversary choice + level + scenario (Spirit Island rulebook,
2017). Publishing the scale turns difficulty into community-comparable data.

## 3. Win-rate calibration worksheet

**Step 1 — pick the target from structure, not vibes:**

| Structure / audience | Designer-stated target | Source |
|---|---|---|
| Brutal learning-arc co-op | 0% first-play win ("I want them to lose, always") | Antoine Bauza (Ghost Stories), LoG 2016 |
| Light family co-op | 40% first-play win | Justin De Witt (Castle Panic), LoG 2016 |
| Core co-op, first play | ~40% (and "a good chance you lose on your first try") | Matt Leacock (Pandemic), LoG 2016/2017 |
| Story-chapter co-op | 70% (avoid replaying chapters) | Jerry Hawthorne (Mice and Mystics), LoG 2016 |
| Deck-campaign co-op | 75%; "people don't like losing anywhere near as much as they say they like it" | Mike Selinker (Pathfinder ACG), LoG 2016 |
| Legacy/campaign sessions | ~2:1 win:loss (~67%) | Leacock & Daviau practice, LoG 2017 |
| Solo vs. automa (self-reported want) | 25–30% win rate | BGG solo community via Cornelius, LoG 2016 [contested] |

Note the spread: 0–75% across respected designers. The target is a *positioning decision* (who is the
audience, what is the retry cost), then an engineering spec.

**Step 2 — instrument:** every logged play records setting/dial values, player count, win/lose, final
margin, turns played, and the turn the outcome *felt* decided. (Statistics of the resulting log —
sample sizes, confidence — are `board-game-math-balance`'s job; rule of thumb here: ≥ ~10 logged plays
per dial setting before moving a knob [contested].)

**Step 3 — move one dial at a time.** Batch tests per configuration; never change two knobs between
batches or you can't attribute the delta.

**Step 4 — protect the learning arc.** Trzewiczek's Robinson Crusoe model: early plays should be losses
*that teach one named lesson each* (weather → shelter; animals → weapons). If testers lose but can't
name what to do differently, difficulty is noise, not arc.

**Step 5 — ship named settings.** Rulebook states the tiers, which is Standard, and where first-timers
start. Include a "lost badly? drop one tier" line — losing groups rarely self-modulate without
permission.

## 4. Player-count scaling methods

1. **Write the per-round budget, not the per-player budget.** For each count n: team actions per round
   = n × actions/player; system pressure per round = f(n). In Pandemic both sides scale with n (each of
   the n turns ends with an infection step), so the action:infection ratio is count-independent — yet
   coordination cost and total held cards are not. Community still debates which count is hardest
   [contested] — the lesson is that "constant ratio" ≠ "constant difficulty."
2. **Per-player quotas in threat text.** "Spawn 1 enemy per hero," "place X per player" (Spirit Island
   adversary effects frequently scale per player). Prevents the classic failure: flat spawn counts that
   overwhelm 2p and bore 5p.
3. **Scale what players trivialize, tax what they complicate.** More players = more board coverage and
   role coverage (buff for the system), but slower information passing and travel (debuff). A scaling
   table that only adds hit points misses both.
4. **Gloomhaven method:** monster count AND stats scale with player count via printed setup tables per
   count — zero mid-game math.
5. **Hand-economy check.** In card-driven co-ops, total cards held = n × hand limit (Pandemic: 7 each),
   so cure/set collection gets easier with count while matching-location coordination gets harder. Test
   the extremes (2p and max) first — that's where the math breaks.
6. **Solo at low counts.** If your co-op advertises 1–4p, decide and document: role-multiplexing
   (Pandemic official solo: 3 roles, one shared hand) vs. automa (euro model). Ship one intentionally;
   don't let "play two characters" emerge by accident.

## 5. Session-shape budget

- Escalation beats should land at predictable fractions of session length (Pandemic's pile-splitting
  guarantees epidemics distribute through the deck). Place beats at roughly 1/4, 1/2, 3/4 of the timer.
- Alternate hope/fear (Leacock): after each beat, players should gain or already hold a stabilizing tool.
- Endgame: the final 20% of the timer should have the highest loss-probability density — design the last
  clock to be the loudest (deck-out visible, outbreak track near 8).
- Fast-loss exit: a doomed position should end the session within ~10 minutes, not grind (Hawthorne's
  chapter-retry logic).
