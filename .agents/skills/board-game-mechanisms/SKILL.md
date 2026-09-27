---
name: board-game-mechanisms
description: >-
  Board game mechanism taxonomy and selection. Covers the experience created, tension source, player-count scaling, exemplars, and combination partners for major mechanisms (worker placement, deck/bag building, drafting, area control, tile-laying, push-your-luck, roll-and-write, engine building, trick-taking, auctions, network building, action points, programming, simultaneous selection, hidden roles, legacy/campaign, dice mitigation, rondels, mancala, tech trees, polyomino, markets). Use when picking or combining mechanisms, building a core loop, checking player-count fit, auditing bloat, or seeking innovation via recombination/inversion/constraint changes. Triggers: "which mechanism should I use", "combine X with Y", "is my game too bloated", "how does X scale at 2 players", "games that use X", "build a core loop". For experience frameworks/victory conditions use board-game-design-theory; for probability/EV/balance math use board-game-math-balance; for automa/co-op use board-game-solo-coop-design.
---

# Board Game Mechanisms: Taxonomy & Selection

A mechanism is a reusable rule pattern that creates a repeatable kind of decision. When advising a designer: translate their target experience into a tension source, then into a mechanism (or proven combination) that delivers it at the intended player count and complexity budget.

## When to use / when not to use

Use for:
- Choosing a core or supporting mechanism ("which mechanism should I use", "worker placement or drafting for this?")
- Combining mechanisms into a core loop; checking whether a pairing is proven or clashing
- Auditing a design for mechanical bloat ("too many systems", "takes 40 minutes to teach")
- Player-count fit of a specific mechanism at minimum/maximum count
- Finding canonical exemplar games to study for a mechanism
- Generating mechanical novelty via recombination, inversion, or constraint changes

Not for (route there instead):
- Experience frameworks (MDA, kinds of fun, lenses), agency, victory conditions, idea critique → `board-game-design-theory`
- Probability, expected value, cost curves, point-salad calibration, difficulty win-rates → `board-game-math-balance`
- Automa/AI opponents, co-op structure, quarterbacking fixes → `board-game-solo-coop-design`
- Dexterity/memory accessibility, colorblind double-coding → `board-game-accessibility`
- Theme-mechanism resonance and naming → `board-game-theme-narrative`
- Validating choices in test sessions → `board-game-playtesting`

## Core principles

1. **Experience first, mechanism second** (MDA — Hunicke, LeBlanc & Zubek 2004). Name the feeling (scarcity sweat, compounding growth, table drama), then pick the mechanism that manufactures it. Never pick by fashion.
2. **Every mechanism must name its tension source**: scarcity, blocking, hidden information, probability, time pressure, or other players' minds. Costikyan's 11 uncertainty sources (*Uncertainty in Games*, 2013) include player unpredictability — luck-free games stay tense because opponents are the randomizer.
3. **One mechanism owns the turn structure.** Supporting mechanisms must feed its inputs or consume its outputs; a subsystem touching neither is bloat.
4. **Mechanism budget: 1 core + 2–3 supporting** [contested — community consensus across designer blogs, no named originator]. The binding constraint is teachability and depth-per-rule, not the count.
5. **Prefer input luck over output luck** (Engelstein, Ludology/GameTek). Input = roll, then decide how to use it (The Castles of Burgundy) — preserves agency. Output = decide, then roll to see if it worked (Risk) — needs mitigation: rerolls, pip modifiers, conversion powers.
6. **Player count is a hard gate.** Auctions fail below 3p, social deduction below 5p, open drafting thins at 2p, sequential turns choke at 5–6p. Check both ends before committing.
7. **Novelty = recombination, inversion, or constraint change** — not invention from nothing. Clank! = deck-building × board; Hanabi = inverted hand information; Welcome To = Yahtzee minus dice → 1–100 players. First-to-market with a genuinely big idea dominates its category (League of Gamemakers, "The Next Big Idea in Tabletop Gaming": D&D, Magic, Dominion).
8. **Elegance = depth ÷ rules.** Knizia: "out of the simplicity, a second level of depth." Saint-Exupéry: "perfection is achieved… when there is nothing left to take away." Cut any rule that adds no decisions.
9. **Design the driving mechanism and the rest of the game in parallel** — each constrains the other (League of Gamemakers, "Parallel Design": Trajan's mancala-rondel, 7 Wonders' drafting, Puerto Rico's role selection).
10. **Study exemplars for failure modes, not just rules.** Every major mechanism has 2–4 canonical games that teach its edge cases (see `references/mechanism-catalog.md`).

## How to apply it

### A. Select a mechanism (checklist)

1. Name the target aesthetic: scarcity sweat / growth / opponent-reading / spatial puzzle / gambling thrill / social drama / long-horizon narrative.
2. Map aesthetic → tension source → candidate mechanisms:

| Target experience | Tension source | Candidate mechanisms |
|---|---|---|
| Sweaty "can't do everything" | Limited actions, blocking | Worker placement, action points, rondel, mancala |
| Growth / compounding power | Invest now vs. score now | Deck/bag/pool building, engine/tableau, tech trees |
| Reading opponents | Hidden info, simultaneity | Drafting, simultaneous selection, auctions, trick-taking |
| Spatial puzzle | Contested space | Tile-laying, polyomino, area control, network building |
| Gambling thrill | Probability vs. greed | Push-your-luck, dice drafting, roll-and-write |
| Social drama | Trust, hidden allegiance | Hidden roles, traitor, negotiation, voting, deduction |
| Long-horizon narrative | Permanence | Legacy, campaign, unlockable content |

3. Player-count check at BOTH ends (quick table below; per-mechanism detail in the catalog).
4. One-sentence teach test: can you state the core action in one sentence?
5. Luck profile: input vs. output; attach mitigation tech if output.
6. Interaction level vs. audience: shared race (low) / blocking & denial (medium) / direct conflict (high).
7. Elegance test: does it earn its rules weight? If not, kill it.
8. Filter survivors through Stonemaier's 12 Tenets (Stegmaier): quick setup, easy to learn, balances-not-checks, conflict-not-hostility, choices-not-luck, scalability, unique production, variable turn order & smooth flow, multiple paths to victory, point-based end trigger, reasonable duration, replayability.

### B. Build the core loop

1. Pick the ONE core mechanism that owns the turn.
2. Close the resource loop: **generate → convert → score.** Every currency must be earnable, spendable, and scarce.
3. Attach only supporting mechanisms that feed core inputs or consume core outputs (proven pairings in `references/combinations.md`).
4. At most one primary randomizer; any further luck needs mitigation tech.
5. Funnel all subsystems into one scoring system (two max, with one being a loss condition).
6. Playtest the loop solitaire first (Fristoe: experiment with the bare mechanic), then layer interaction.
7. Add downtime control last: simultaneous selection, single-action turns, short phases.

### C. Engineer novelty (full playbook with dated examples in `references/combinations.md`)

1. **Recombination** — port a proven mechanism onto a new substrate (deck-building onto a map → Clank!, 2016).
2. **Inversion** — flip the default assumption (see opponents' hands, not yours → Hanabi, 2010).
3. **Constraint change** — remove one degree of freedom (no hand rearrangement → Scout, 2019; fixed hand order → Bohnanza, 1997).
4. **New substrate/tech** — permanence (Risk Legacy, 2011), sealed envelopes (Gloomhaven, 2017), app-checked logic (Alchemists, 2014).

### D. Audit for bloat

1. List every subsystem. For each, write which core-loop input it feeds or output it consumes. Can't answer → cut candidate.
2. Count "remember/except" rules — Stegmaier's playtest red-flag words; each signals rules weight without decisions.
3. Teach-time test: if the teach exceeds the audience's tolerance, cut systems before simplifying them.
4. Precedent [unverified — source not locatable]: Engelstein reportedly cut faction goals, an economy system, and a tension track from *The Expanse* — they pushed complexity past the target audience without adding interest.

## Key numbers & heuristics

| Claim | Value | Source |
|---|---|---|
| Mechanism budget | 1 core + 2–3 supporting | Community consensus [contested] |
| Printed taxonomy size | ~196 mechanisms in 13 categories | Engelstein & Shalev, *Building Blocks of Tabletop Game Design* (2019) |
| BGG crowd taxonomy | ~51 mechanisms (2014 citation); much larger now — treat any exact count as a snapshot [contested] | BGG wiki/community |
| Sources of uncertainty | 11 | Costikyan, *Uncertainty in Games* (2013) |
| System parts of a game | 8: Goal, Actions, Resources, Acquisition, Scoring, Elimination, Uncertainty, Interaction | Teale Fristoe, League of Gamemakers (2015) |
| Auction viability | Needs 3+ players; weak below 3 | Community consensus; Knizia auction trilogy practice |
| Social deduction viability | Needs 5+ players (The Resistance: 5–10) | Publisher specs + consensus |
| Card drafting at 2p | Thin; use dummy hand or official 2p variant (7 Wonders) | Community consensus |
| Shared dice-pool sizing | 2n+1 dice per round for n players (5/7/9 at 2/3/4p) | Sagrada (2017) rules |
| 2d6 bell curve | 7 = 6/36 ≈ 16.7%; 6 or 8 = 5/36 ≈ 13.9% each | Catan dice math |
| Action-point budgets | Pandemic: 4/turn; Tikal: 10/turn | Rules |
| Small World conquest cost | 2 tokens for empty region + 1 per defensive piece | Rules |
| Pandemic Legacy campaign | 12 in-game months × ≤2 attempts = 12–24 sessions | Daviau & Leacock (2015) |
| Welcome To player count | 1–100 (flip-and-write removed dice AND player cap) | Publisher (2018) |
| Player elimination | Avoid once session length is non-trivial: eliminated players sit idle, game length becomes erratic, and it forces cruelty on the group | Fristoe, "Game Elements: Elimination", League of Gamemakers (paraphrase) |

Player-count quick gate (details per mechanism in catalog):

| Mechanism family | Fails/thins at | Fix |
|---|---|---|
| Auctions | <3p (no competition) | Once-around or sealed formats; fixed-price market |
| Social deduction / traitor | <5p | Route to hidden-objective or semi-coop designs |
| Open card drafting | 2p | Dummy hand, 2p variant, or tile/factory drafting (Azul) |
| Sequential worker placement | 5–6p (downtime) | Split boards (Viticulture seasons), simultaneous reveals |
| Area majority | 3p (kingmaking) | Tight map, scoring every round, or 4p+ recommendation |
| Engine building | Any, if no contestable space | Add shared races/markets to avoid multiplayer solitaire |

## Common pitfalls

- **Mechanical bloat** — subsystems with no core-loop role. Manifests as 30+ minute teaches, "remember/except" rules, playtesters forgetting a system exists.
- **Analysis paralysis** — too many equal options per turn (big AP budgets, big hands). Manifests as exploding turn-time variance.
- **Multiplayer solitaire** — engine/deck builders and roll-and-writes with no contestable space. Fix with shared races, drafting, or shared markets.
- **Runaway leader** — compounding engines with no cap or catch-up; winner obvious at the 60% mark.
- **3-player area-control kingmaking** — two players over-contest one region while the third sweeps the rest.
- **Auction misvaluation & stalls** — novices can't price lots; open formats develop "waiting out" stalls. Use once-around (Ra), one-god bids (Cyclades), or demand-scaled markets (Power Grid).
- **Synergy-free drafting** — if a pick doesn't change the value of remaining cards, it's distribution, not drafting (Nerdlab, Card Drafting deep dive). Cards must be interdependent.
- **Quarterbacking** — co-op/traitor designs where one alpha player directs others → `board-game-solo-coop-design`.
- **Elimination downtime** — eliminated players sit out while the rest keep playing (Fristoe's core weakness: players want to play); the longer the game, the worse the cost.
- **Meta-dominated social deduction** — veterans steamroll; mitigate with asymmetric information (Avalon) or mid-game reveals (Battlestar Galactica).
- **Legacy ceiling** — one group per copy; the post-campaign state must still function (Charterstone's solution).
- **Dexterity/memory gating core scoring** — excludes players; keep to side systems or party contexts → `board-game-accessibility`.
- **Push-your-luck odds blindness** — players misestimate bust odds; surface them through repeated small rounds (Incan Gold), not single big ones.

## Reference files

- `references/mechanism-catalog.md` — Load when the user asks about a SPECIFIC mechanism (what it feels like, tension, scaling, exemplars, partners), or needs the full taxonomy table. The bulk per-mechanism data lives there.
- `references/combinations.md` — Load when combining mechanisms, designing a core loop from scratch, hunting for innovation, or auditing bloat. Synergy patterns, loop recipes, and the recombination/inversion/constraint playbook live there.

## Related skills

- `board-game-design-theory` — MDA, kinds of fun, interesting decisions, agency, victory conditions, idea critique
- `board-game-math-balance` — probability, EV, cost curves, feedback loops, pacing, difficulty tuning
- `board-game-solo-coop-design` — automa/AI opponents, difficulty dials, co-op structure, quarterbacking
- `board-game-accessibility` — dexterity/memory/cognitive/vision access, double coding
- `board-game-theme-narrative` — theme-mechanism resonance, naming, representation
- `board-game-playtesting` — protocols and instruments for validating mechanism choices
- `board-game-prototyping` — building testable versions of the chosen mechanisms
- `board-game-market-analysis` — format trends and comparable-title positioning
