# Pacing, Player-Count Scaling & Difficulty Statistics

Game-length targets, turn-time budgets, player-count scaling patterns, solo/co-op difficulty calibration,
and the statistics of validating balance from finite data.

Load this file when: setting box time, fighting downtime, scaling a design across player counts, building
difficulty dials, or deciding what playtest data can and cannot prove.

---

## 1. Length & pacing targets (community consensus, BGG weight 1–5)

| Class | BGG weight | Box time | Notes |
|---|---|---|---|
| Filler | 1–1.5 | ≤30 min (some 5–15) | Rules in one breath; 2-minute teach |
| Family | 1–2 | 30–60 min | Kids' games 10–30 min |
| Medium-light euro | 2–2.5 | 20–30 min (Piechnick: medium-light should aim here) | Most "weeknight" euros overshoot this |
| Euro / mid-weight | 2.5–3.5 | 60–120 min | |
| Heavy | 3.5–5 | 90–180+ min | |

Rules of thumb:
- Length tracks weight; a shorter game can just be played twice (Piechnick, daniel.games/game-length).
- "A good game ends one turn too soon." For ramping games: long enough to reach *some* of the biggest
  stuff; if a player can follow all paths to their end, the game is too long.
- Don't compile identical rounds to pad length. Keep shortening until playtesters ask whether it's too
  short — that question is the signal of correct length.
- Expect first plays to run well over box time (teach + lookups); box time should reflect an experienced
  group. Teach+setup reserve of ~10–20% is a common planning figure [folk].

## 2. Turn-time budgets

Master equation: **minutes = players × turns/player × seconds/turn ÷ 60**.

Worked examples:
- 60-min 4p euro at 25 turns/player → 36 s/turn available.
- 30-min 5p family game at 10 turns/player → 36 s/turn.
- If your measured mean turn is 60 s, that 5p game is 50 min, not 30 — change turns, players, or length.

Measured-turn data comes from playtests (time a sample of turns per player count). Levers when over budget:
- Shrink the per-turn menu (~3–5 meaningful options; more invites analysis paralysis — the 7±2 citation is
  [contested] in this context; treat 3–5 as practitioner consensus, not psychology).
- Deliver new information (card draw, market refresh) at the **end** of the turn so players plan during
  others' turns.
- Sequence phases so only the active subsystem needs attention.
- Simultaneous play where possible (see §3).
- Fixed-action allowances (Pandemic = 4 actions; Tikal = 10 AP) make turn time predictable — estimate
  total decisions ≈ actions × turns × rounds, and verify each action's EV per action-point. Attacks on an
  opponent's action efficiency = "Net Action Advantage."

Downtime arithmetic: sequential idle per round = (n−1) × mean turn length. 5 players × 60 s = 4 min idle.
If idle exceeds ~2 min/round at max count, apply the fixes above or restructure to simultaneous play.

## 3. Player-count scaling patterns

| Pattern | Exemplar | Effect |
|---|---|---|
| Simultaneous drafting/phases | 7 Wonders | ~30 min constant at 3–7p; downtime ≈ 0 |
| Off-turn engagement | Catan, Machi Koro (payouts on others' rolls) | Idle time becomes attention time |
| Two-sided / sectioned boards | Small World (4 maps), Power Grid (regions = player count) | Congestion constant |
| Component-count scaling | Sagrada dice = 2n+1; Point Salad veggie counts per count | Scarcity constant |
| Route/zone restrictions | Ticket to Ride: double routes banned at 2–3p | Blocks degenerate openness |
| Resource refresh tables | Power Grid per-count refresh rates | Economy pressure constant |
| Round-count scaling | Fewer rounds at high counts | Length constant |
| Nearest-neighbor interaction | Attacks/trades only with neighbors | Politics constant |

Failure modes by count:
- **2p**: auctions/trading go flat (no bid competition [folk]); zero-sum makes catch-up math harsher;
  many playtests happen here — verify it works.
- **3p**: kingmaking peak in conflict/area-control — two players over-fight one region, the third sweeps
  the rest. Mitigate with congestion, per-pair interaction limits, or hidden scores.
- **4p**: sweet spot for auctions and trading (Catan tuned for 4).
- **5–6p**: downtime doubles; Catan's 5–6p extension adds a "special building phase" between turns —
  an official admission that turn structure, not content, is the scaling problem.

Scaling checklist: (1) downtime computed at max count; (2) congestible resources scaled; (3) 2p variant
verified; (4) real turn times measured per count; (5) interaction graph decided (everyone vs neighbors).

## 4. Solo/co-op difficulty calibration

Target win-rate bands:
- **Matt Leacock**: ~**40% win rate for first-time groups**; 60% for *legacy-style sessions* (LoG "Win
  Ratios in First Time Cooperative Play", 2016) and a 2:1 win:loss target for legacy (2017 interview) — the
  player should lose the first game(s) and feel mastery closing the gap. Target-setting itself →
  `board-game-solo-coop-design`.
- Community bands for replayable co-ops run **~50–70%** [contested — varies by source and audience;
  family co-ops higher, "hard" co-ops lower; Ghost Stories has a notorious sub-20% reputation [contested
  community estimate]].

Dial design:
- Ship ≥3 difficulty knobs (Pandemic: 4/5/6 Epidemic cards). Difficulty should scale threat *density*, not
  just numbers-on-monsters (Leacock's "cardboard antagonist": card/dice-driven threat engine).
- Tension should oscillate in waves, not ramp monotonically — peaks and breathers.
- Solo modes inherit the same win-rate band; the dial belongs in the automa/threat deck
  (→ `board-game-solo-coop-design` for construction).
- Tune by logging win/loss **and margin** per configuration over dozens of plays, never by feel.

## 5. The statistics of playtesting (what data can prove)

95% CI half-width on a win rate, worst case p=0.5 (half-width = 1.96·√(p(1−p)/n)):

| n plays | ± pp |
|---|---|
| 5 | 44 |
| 10 | 31 |
| 20 | 22 |
| 30 | 18 |
| 50 | 14 |
| 100 | 10 |
| 400 | 5 |

Sample sizes to *detect* a true win-rate gap, **two strategies vs each other (two-arm**, two-sided 5%, 80% power, computed):
- 55% vs 50%: ~1,570 plays per arm (one-sided: ~1,230/arm).
- 60% vs 50%: ~390 per arm.
- A 10-pp gap between two strategies (45 vs 55): ~390 per arm.

**One strategy vs a known 50% baseline (one-sample)** needs roughly half: 55% vs 50% ≈ 780 plays (one-sided ≈ 620) — that is the table in `board-game-playtesting` §H; the 2× difference vs the figures above is test design, not disagreement.

Consequences:
- **You cannot statistically balance on 10 plays.** "30 playtests = statistical minimum" is [contested —
  arbitrary]; 30 plays is still ±18 pp.
- Use models (EV, bots, Monte Carlo) for fine balance distinctions; use humans for perceived balance, fun,
  and breakage (the Strain/Piechnick division of labor).
- Log per play: winner seat, strategy, margin, length, dead elements, stalemates. Change ONE variable per
  iteration.
- Track first-player win rate; if >~55–60% [folk threshold], compensate later seats (extra resource, bid,
  or turn-order advantage).
- Games-user-research guidance for surveys: ~100 responses ≈ ±10%, diminishing returns past ~400.
- The public plays orders of magnitude more games than your test group and *will* find imbalances you
  missed (Piechnick) — ship with tunable numbers and a living FAQ.

## 6. Monte Carlo bot recipe

For VP races, push-your-luck, combat chains, faction matchups — anything stateful:

```python
import random

def play_game(strategy_a, strategy_b):
    # simulate one game; return winner ("A"/"B"/"draw")
    ...

def win_rate(n=10_000):
    random.seed(42)
    wins = sum(play_game("greedy_farm", "greedy_trade") == "A"
               for _ in range(n))
    p = wins / n
    ci = 1.96 * (p * (1 - p) / n) ** 0.5   # n=10k -> ±1 pp at p=0.5
    return p, ci
```

Bot ladder: (1) random legal moves (sanity: no crashes, length in range); (2) greedy per-path bots
(does any single-minded strategy dominate?); (3) heuristic bot with adaptive play (the bar the others must
clear). 10,000 sims give ±1 pp at p=0.5; 1,000 give ±3 pp — cheap enough to run per patch. Then confirm
the top and bottom of the sim ranking with human pods, because bots measure exploitability, not fun.
Tabletop Simulator + scripted setups and Discord playtest servers accelerate the human side.
