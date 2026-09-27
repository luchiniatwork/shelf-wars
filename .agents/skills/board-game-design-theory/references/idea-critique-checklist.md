# Idea Critique Checklist — Systematic Diagnostic for a Board Game Idea or Prototype

Load when asked to critique, score, or diagnose a game idea. Works at three fidelity levels: written pitch, rules draft, played prototype. At lower fidelity, ask the designer for the missing answers rather than assuming them — do not flatter, do not invent.

## How to run

1. Restate the idea in one sentence (fantasy + core action). If you can't, that is finding #1.
2. Work through the 10 sections below in order. Each item is scored: **2 = pass, 1 = risk, 0 = fail**. Every 0 or 1 gets a named failure sign and the smallest fix that could raise it.
3. Check the auto-fail red flags first (end of document) — any one of them caps the verdict at "major redesign".
4. Report per-section scores, total (/100), verdict band, then a fix list ordered by leverage. Cite the framework behind each diagnosis (MDA, Johnson, Laurie, Fristoe, Schell…). Vague encouragement is a report failure.

## Section 1 — Core experience & fantasy (MDA / LeBlanc)

1.1 Target aesthetics named: 2–3 of LeBlanc's 8 kinds of fun chosen deliberately (Sensation, Fantasy, Narrative, Challenge, Fellowship, Discovery, Expression, Submission, +Competition). Fail: "it's fun" with no kind specified. Fix: pick primaries, then audit every mechanism against them.
1.2 One-sentence fantasy exists: who the player *is* and what they *feel*. Fail: sentence describes components or mechanisms, not experience. Fix: write the experience-first pitch (BGDL: theme-first, mechanism-first, and experience-first are all valid starts, but the pitch must be experience-shaped).
1.3 Aesthetics agree with weight/length: epic Fantasy promised at filler weight, or Submission relaxation at 3-hour length, is a mismatch. Fix: rescope promise or product.
1.4 Dynamics named per aesthetic: each target aesthetic has a concrete dynamic that will produce it ("tense" ← a race the leader can lose). Fail: aesthetics asserted, mechanism hoped-for. Fix: MDA mapping (SKILL.md §B).
1.5 Hook: one sentence a stranger would repeat. Fail: hook is "it's like X but with Y" minus a reason. Fix: sharpen the single novel dynamic.

## Section 2 — Decision audit (Meier/Johnson/Laurie)

2.1 Decision test: the designer can describe a hard, typical-turn choice unprompted. Fail: Candy Land problem — no real choice on a normal turn. Fix: add a meaningful tradeoff to the core action.
2.2 Decision density: typical turn has ~3 salient options (Laurie; 11 → paralysis). [contested — audience-dependent] Fail: 1 (rote) or 10+ (overload). Fix: delete rote branches; phase-chunk or cut options.
2.3 Impact + information: key choices are both consequential and informed. Fail: guesses (no info) or puzzles (fully computable). Fix: leak partial information; add hidden info or uncertainty (Laurie).
2.4 Variation in value: options are visibly unequal across game states (Laurie principle 3). Fail: all choices equivalent → illusory. Fix: differentiate payouts, costs, timing.
2.5 Perceivable consequence: results of decisions are visible within a turn or two (Church: intention → consequence → anticipation). Fail: "did that matter?" Fix: feedback on components — tracks, reveals, state changes.

## Section 3 — Tension sources

3.1 Named tension: at least one of scarcity, timing race, spatial contest, hidden information, social pressure, risk/reward (Costikyan's uncertainty sources as the checklist). Fail: none — multiplayer solitaire risk. Fix: introduce shared scarcity or a clock.
3.2 Double-bind: a typical turn makes the player want two incompatible things. Fail: single-axis optimization. Fix: force opportunity cost (actions spent on X can't go to Y).
3.3 Opponent relevance: other players' actions change my best move (interaction — even indirect: drafting, markets, blocking). Fail: fully parallel play. Fix: shared pools, contention, or negotiation.
3.4 Escalating stakes: tension rises through the session (scarcity tightens, engines race, clock depletes). Fail: uniform pressure. Fix: staged decks, depletion, scaling payouts.
3.5 Risk/reward asymmetry: at least one triangular choice (safe-small vs risky-big — Schell's Triangularity). Fail: all options same variance. Fix: add a push-your-luck or gambit path.

## Section 4 — Session arc (Schell interest curve)

4.1 Opening legibility: first-turn decisions are understandable without knowing the whole game; subgoals orient players (Fristoe). Fail: analysis of the entire board on turn 1, or "do anything" paralysis. Fix: scripted first turns, starting hands, subgoal prompts.
4.2 Midgame peak: interaction and scarcity crest mid-session. Fail: turns N≈turn 1 in texture. Fix: engine growth, board contraction, age/epoch stages.
4.3 Endgame convergence: game state visibly closes; final turn contains a real decision for every live player. Fail: end is bookkeeping. Fix: conversion pressure (resources → points), end-trigger race.
4.4 Climax placement: the most dramatic moment is near the end, not the middle. Fail: winner obvious ⅓ in. Fix: late-scaled scoring, hidden points, catch-up (→ §6).
4.5 Length discipline: "ends one turn too soon" (Piechnick); players can NOT complete everything they wanted. Fail: all paths fully achievable → game too long or too loose. Fix: shorten by a round; tighten the economy.

## Section 5 — Victory & scoring

5.1 Behavior-spec alignment: the victory condition rewards exactly the behavior the fantasy promises (Fristoe: explicit goal = real goal; the party-game warning). Fail: optimal play contradicts the intended fun. Fix: re-point scoring at the desired behavior.
5.2 Structure chosen deliberately: race / competition / elimination / sudden death / objectives / hybrid (taxonomy: SKILL.md §E). Fail: "highest points win" by default without considering alternatives. Fix: match structure to aesthetic (races for drama, competitions for engines).
5.3 End trigger legibility: players can read roughly how much game remains. Fail: surprise ending or unreadable trigger. Fix: visible clocks, depletion tracks.
5.4 Score feel: totals ≤10 or aids provided (Fristoe granularity rule); scoring math limited to addition for mass audiences; multipliers used sparingly. Fail: "math-problem finale." Fix: tracks, staged scoring, component-encoded math.
5.5 Standings visibility chosen: hidden/open/hybrid deliberately traded off (hidden = losers stay invested; open = leader politics work). Fail: hidden scores in a game that needs leader-bashing. Fix: hybrid — public track + hidden end bonus.

## Section 6 — Standings, feedback loops & elimination

6.1 No runaway leader: positive loops have a counterweight (negative loop, scaling costs, table politics). Fail: mid-game winner locks. Fix: catch-up patterns (→ `board-game-math-balance` for the math; experience rule: hide the catch-up inside arithmetic).
6.2 No dead-man-walking: a trailing player retains ~5%+ win path or meaningful alternate goals until late (daniel.games floor). Fail: losers spectate. Fix: self-directed goals, spoilers, shorter tail.
6.3 Elimination justified: if players can be eliminated, the game ends within minutes for them or elimination is the point (Fristoe's bad action-arc warning). Fail: 45 minutes of sitting out. Fix: partial elimination (penalties), spectator roles, or cut it.
6.4 No kingmaking: a player out of contention cannot unilaterally pick the winner. Fail: endgame attacks are decisive and arbitrary. Fix: hidden scores, simultaneous reveals, multiple end conditions.
6.5 Close-game engineering: last place typically ≥60–70% of winner's score (Fristoe). Fail: routine blowouts. Fix: scaling costs, rubber-banding inside systems, shorter game.

## Section 7 — Agency & luck

7.1 Decision ownership: players attribute outcomes to their choices, even under luck (Laurie's core requirement). Fail: "the dice decided." Fix: mitigation options (rerolls, modifiers, dice-as-resources — catalog in `board-game-math-balance`).
7.2 Input luck preferred: randomness lands before decisions, not after (Engelstein). Fail: commit-then-roll pass/fail on key actions. Fix: roll-then-assign, or price output luck with mitigation.
7.3 Loss aversion respected: punishments ≈half the weight of equivalent rewards (Kahneman & Tversky; λ≈2.25 [approx.]). Fail: harsh take-that in a light game. Fix: convert penalties to forgone gains.
7.4 Mitigation currency: a way to buy out of bad luck exists (tokens, powers, rerolls). Fail: naked variance on high-stakes rolls. Fix: add a fate economy.
7.5 Skill expression: better players win more over repeated sessions. Fail: win rate uncorrelated with experience. Fix: deepen decision tree, reduce output luck.

## Section 8 — Complexity budget & elegance

8.1 Declared weight matches audience: target BGG weight named (evergreen center ≈2.10, Stegmaier 2019). Fail: "for everyone" + heavy systems. Fix: pick the audience; cut or simplify.
8.2 Rule-by-rule yield: every rule buys decision depth ≥ its cognitive cost. Fail: rules that exist for simulation flavor only (Meier's research rule). Fix: Saint-Exupéry subtraction pass.
8.3 Consistency: mechanics apply uniformly (Laurie principle 4); exceptions countable on one hand. Fail: case-by-case rulings. Fix: unify timing/wording (→ `board-game-rules-writing`).
8.4 Subsystem focus: one good game, not two fighting ones (Covert Action Rule, Meier via Johnson). Fail: two loops competing for attention. Fix: pick the focus; demote the other to support.
8.5 Teach time proportionate: teach ≤ ~10–15% of session length for gateway/family [contested — community heuristic]. Fail: 30-minute teach for 45-minute game. Fix: strip systems before writing rules.

## Section 9 — Player-type & audience coverage

9.1 Four-type test: what Sue, BUTCH, Aimeyj, and Raphael each do all session is nameable (Domeny). Fail: a type has nothing. Fix: add their hook (info access, high-variance route, off-meta path, discoverable corners) or declare the narrower audience.
9.2 Psychographic anchor: at least two of {Achiever, Explorer, Socializer, Killer} / {Timmy, Johnny, Spike} served deliberately (Bartle 1996; Rosewater 2002). Fail: single-type product with mass-market ambitions. Fix: add a second hook or reposition.
9.3 Spike integrity: chance limited enough that decisions matter (Sue/Spike). Fail: luck-dominant outcomes in a strategy pitch. Fix: input luck + mitigation.
9.4 Social load matches frame: negotiation/talk requirements match the group's likely mood (Fellowship aesthetic). Fail: forced table talk in an optimization euro, or silence in a party game. Fix: retune interaction level.
9.5 Replay motivation: a reason to play again within a week exists (variable setups, asymmetric powers, discovery, skill climb — Koster: fun persists while there's pattern left to learn). Fail: one-solve puzzle. Fix: variability or strategic depth.

## Section 10 — Commercial shape (experience-level only; deep analysis → `board-game-market-analysis`)

10.1 Player count: core box supports a wide count credibly; evergreen average max = 5, no evergreen is 2p-only (Stegmaier 2019). Fail: 2p-only with mass-market plan. Fix: scaling design or accept niche.
10.2 Session length matches segment: filler ≤30m / family 30–60m / euro 60–120m; evergreen mean ≈45m. Fail: 90m party game. Fix: cut a round/system or reposition.
10.3 Flow preserved at max count: downtime handled (simultaneous play, off-turn engagement). Fail: sequential turns × 5 players. Fix: simultaneous selection (Laurie method 10).
10.4 Endgame trigger is point/progress-based (Stonemaier tenet 10), not exhaustion. Fail: "play until bored." Fix: add a clock.
10.5 One-line retail pitch survives contact: a store clerk can sell it in 15 seconds (experience promise + one mechanism + player count/time). Fail: pitch needs the whole rules summary. Fix: simplify the experience promise, not just the words.

## Auto-fail red flags (any one caps verdict at "major redesign")

- A typical turn offers no meaningful decision (2.1 = 0).
- One dominant strategy survives the audit (2.4 + 9.5 both 0).
- Winner knowable by halfway with no catch-up and >⅓ of playtime remaining (4.4 + 6.1 both 0).
- Players routinely ask "when does it end?" or "what can I even do?"
- The explicit goal rewards behavior opposite the stated fun (5.1 = 0).
- Eliminated players idle >15 minutes (6.3 = 0).

## Verdict bands

| Total /100 | Verdict | Action |
|---|---|---|
| 80–100 | Strong | Prototype now (→ `board-game-prototyping`); protect what scored 2 |
| 60–79 | Promising with risks | Fix the 0s first, retest the section, then prototype |
| 40–59 | Major redesign | Rework core loop/arc/victory before any prototype |
| <40 | Shelve or restart | Restart from the fantasy (§1) with a different core dynamic |

## Reporting format

Per section: score, the worst item, the smallest fix. Then: total, band, red flags, and a 3–5 item fix list ordered by leverage (cheapest big improvement first). Close with what the idea genuinely has going for it — one concrete strength, not a compliment sandwich.
