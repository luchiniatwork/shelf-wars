# Automa Design — Patterns, Principles, and Worked Example

Load this when designing or auditing an actual solo opponent: building the deck, choosing the AI
pattern, writing tiebreak rules, or running an upkeep audit.

## 1. The Automa Factory canon

The Automa Factory approach comes from **Morten Monrad Pedersen**. Jamey Stegmaier commissioned him to
build the Viticulture solo mode in February 2014; Morten founded Automa Factory about a year later. The
team has since produced official solo modes for 30+ titles including Scythe, Wingspan, Tapestry, Terra
Mystica, Gaia Project, Patchwork Anniversary, Glen More II, Tokaido, and most Stonemaier releases.
("Automa" is Italian for automaton — chosen because the first was built for Viticulture, set in Italy.)
Source: automafactory.com/about.

**The six guiding principles** (verbatim structure, paraphrased text, automafactory.com/about):
1. An artificial opponent — the Automa — takes the place of a human player in a multiplayer game.
2. The human player must play by the same rules as in the multiplayer game.
3. The important player interactions must be simulated — including keeping the win/lose criteria.
4. The player must face the same decisions as in multiplayer.
5. The player must not make choices on behalf of the Automa, except in rare cases (cooperative element
   or strong thematic reason).
6. The Automa rules must be as streamlined as possible while achieving the above — remove internal
   opponent state that does not directly affect the player. (Canonical example: the Scythe Automa has
   no player mat.)

Audit any solo-mode design against these six lines verbatim; they catch 80% of bolt-on failure.

## 2. What solo players demand (BGG community, via Jeff Cornelius, League of Gamemakers 2016)

1. **As close to multiplayer as possible** — same decisions, same board pressure.
2. **Challenging** — most common desired win rate in Cornelius's survey: **25–30%** [contested:
   self-reported preference, 2016].
3. **Limited upkeep** — tolerated only if "not a huge amount more than the original game."
4. **An actual win condition** — explicit rejection of pure "beat your previous high score" modes.

Corollary: if you ship score-chase, attach a threshold ("win = 75+ VP at Standard") so the mode still
has a binary outcome.

## 3. AI pattern catalog (choose one primary, hybridize sparingly)

| Pattern | How it works | Upkeep | Fidelity | Exemplars | Use when |
|---|---|---|---|---|---|
| Priority-list action cards | Card reveals an action + ordered fallbacks + tiebreak arrows/icons | Very low | Medium | Scythe, Wingspan, Viticulture automas | Default for euros with action spots/majorities |
| Deck-as-timer bot | Threat/opponent advances when its deck cycles; player races it | Very low | Low | many PnP solo modes | The opponent is pacing, not competing |
| Race-track scoring bot | Automa advances VP on a fixed or card-modified schedule | Minimal | Low | small-card-game solo modes | Score-race games with little board interaction |
| Flowchart bot | Multi-page decision tree per faction | Very high | High | COIN series (Volko Ruhnke, GMT) | Wargame audience that tolerates admin for fidelity |
| State-tracking bot | Bot keeps resources/hand/board position like a player | High | Highest | Mage Knight's dummy+variant play, some 18xx solos | Only when interaction demands real state |
| App-driven AI | App runs enemy logic, spawns, and scripting | Zero table admin | High | Mansions of Madness 2e (2016), Imperial Assault "Legends of the Alliance" app (2017), Journeys in Middle-earth (2019), Descent: Legends of the Dark (2021), XCOM (2015) | Campaign/narrative co-ops; when overlord seat is a barrier |
| Multi-role solo | One player controls 2–3 full roles | None extra | Exact | official Pandemic solo variant: 3 roles share one hand, 7-card limit, "archive" for shared cards | Co-ops where the multiplayer game IS the puzzle |

**Upkeep vs. fidelity is the trade.** COIN flowcharts prove you can buy fidelity with admin; the Automa
Factory line proves most euro audiences won't pay that price. Pick your audience's tolerance first.

## 4. Anatomy of a good automa card

A priority-list card should carry, in reading order:
1. **Primary action** in one icon/line ("claim the leftmost available action spot in row A").
2. **Fallback chain** ("if unavailable, claim leftmost in row B; else score 2 VP") — never "your choice."
3. **Tiebreak geometry** printed on the card or board: arrows, compass priority, nearest/leftmost rules.
4. **Scoring/momentum line** if the bot accrues points ("advance 3 on the score track").
5. Optional **escalation hook**: a reshuffle icon or a card that ratchets the bot's rate mid-game.

Deck construction:
- Size typically ~10–25 cards (Tokaido automa pack: 23 cards plus solo rulebook and per-character
  reference guides — Stonemaier, 2025). Small decks cycle = readable rhythm; add a reshuffle beat to
  reset and escalate.
- Skew the action mix toward the multiplayer game's *interaction* actions, not its internal-engine ones.
- One-card lookahead (current card visible until the next automa turn) is the standard
  predictability/variability compromise — players can plan around it but can't see beyond it.

## 5. Difficulty tiers that don't fork the rules

- Ship **3–5 named tiers** (e.g., the community-standard easy → expert ladder).
- Vary **quantities**: starting assets, per-turn VP bonus, cards drawn per cycle, timer length.
- Do NOT vary **rules structure** per tier (new powers, new exceptions): each structural fork doubles the
  teach/test surface. If a tier needs new enemy behavior, make it a separately named scenario/variant.
- Publish which tier is "Standard" and tell first-timers where to start.

## 6. Worked example: automa for a worker-placement euro

Assume: 8 shared action spots, a shared card market, area majorities, end at round 8, most VP wins.

1. **Interaction list**: spot-blocking, market denial, majority contest, round-clock pressure.
2. **Minimum simulation**: bot places 2 blockers/round on spots (no workers/resources tracked — principle
   6); bot buys/removes the top market card when its card says so; bot claims majority presence via a
   simple "place a cube in the region with fewest player cubes" rule; round clock unchanged.
3. **Driver**: 16-card priority-list deck. Card faces: "Block spot priority A→B→C" (×6), "Take top market
   card matching icon X else Y" (×4), "Place majority cube" (×4), "Score 2 VP + reshuffle" (×2).
4. **Tiebreaks**: clockwise from first-player marker; leftmost; fewest-cubes. Zero player choices for the
   bot (principle 5).
5. **Tiers**: Standard = as above; Easy = bot blocks 1/round, no market denial; Hard = bot scores +1 VP
   per card; Expert = Hard + bot starts with 2 majority cubes. Quantities only.
6. **Upkeep audit**: draw 1 card, place ≤2 pieces, maybe score. Target ≤ 20–30 s. If any card takes
   > 45 s to resolve, split or simplify it.
7. **Principle check** (section 1): same human rules ✓, interactions simulated ✓, same decisions ✓, no
   choices-for-bot ✓, streamlined state ✓.
8. **Test**: 10+ logged solo plays per tier [contested sample-size heuristic]; track win rate against
   the target band (see coop-difficulty-architecture.md) and ask testers the upkeep question directly.

## 7. Upkeep audit checklist (run before every external test)

- [ ] One deck to draw from (two max). No cross-referencing tables mid-turn.
- [ ] No hidden bot state the human must remember or track.
- [ ] Every tie has a printed geometric/positional tiebreak.
- [ ] Bot turn resolvable in ≤ ~30 s; total bot admin ≤ ~20% of session time [contested targets].
- [ ] Bot actions readable at a glance (icons + ≤ 2 lines of text per card).
- [ ] Win/lose vs. the bot is explicit and scored exactly once, at game end.
- [ ] The bot cannot illegally occupy/claim things (write the exception rules explicitly).

## 8. Frequent automa bugs found in blind tests

- Ambiguous fallback chains ("if unavailable" without defining availability timing).
- Tiebreaks that reference hidden or bot-owned information the player can't verify.
- Escalation reshuffles that accidentally repeat the same 3-card cycle (predictable loop).
- Difficulty tiers that quietly change rules, causing players to mix tier rules mid-campaign.
- Bot turns that front-load admin at round start, creating a 2-minute dead beat each round.
