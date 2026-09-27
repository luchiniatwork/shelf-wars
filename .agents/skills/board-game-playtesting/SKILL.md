---
name: board-game-playtesting
description: Design and run board game playtesting programs — self-play simulation, guided tests, and blind waves — with session protocols, feedback instruments, logging, recruitment, statistical humility, and kill criteria. Use when the user says "playtest my game", "blind playtesting", "write a playtest feedback form", "how many playtests do I need", "is my game ready to pitch", "recruit playtesters", "playtest protocol", "testers couldn't learn the rules", or "should I shelve this design". Covers what each format (self/guided/blind/remote) can and cannot measure, one-goal-per-session protocol, question design without leading questions, session logging, Unpub/Protospiel/online recruitment, blind-test kit contents, rules-usability testing, and small-sample interpretation. For prototypes/PnP use board-game-prototyping; for numeric balance changes use board-game-math-balance; for rulebook text use board-game-rules-writing; for solo/co-op difficulty calibration use board-game-solo-coop-design.
---

# Board Game Playtesting

## When to use / when not to use

Use this skill when the user needs to:
- Decide which playtest format to run (solo sim, guided, blind, remote) or what a result actually proves.
- Plan a session: goal, protocol, observation, debrief, logging.
- Build feedback instruments: surveys, question banks, fun-rating tracking.
- Recruit testers: local groups, conventions, online blind-test pools, PnP communities.
- Assemble a blind-test kit, run a wave, or interpret small-sample data.
- Decide whether a design is ready to pitch, or whether to shelve/kill it.

Do NOT use this skill for:
- Building the prototype, PnP files, or digital versions → `board-game-prototyping`.
- Deciding what to change numerically (cost curves, probabilities, pacing math) → `board-game-math-balance`.
- Writing the rulebook (structure, teach order, terminology) → `board-game-rules-writing`.
- Whether the core loop is worth testing at all (MDA, fun kinds, decision quality) → `board-game-design-theory`.
- Automa/solo difficulty win-rate calibration → `board-game-solo-coop-design`.

## Core principles

1. **Every session answers one question.** Name it before inviting anyone ("does 4p downtime stay tolerable?", "is the bidding legible to first-time players?"). Sessions without a goal produce anecdotes, not data (Stegmaier frames the goal for testers up front).
2. **Match the format to the question.** Self-play proves functionality; guided tests prove engagement; only blind tests prove the rulebook and the unbiased experience. No format substitutes for another.
3. **Observe first, ask second.** Body language, hesitation, phone-checking, and engagement dips are the signal (Engelstein: the biggest late-cycle insights are behavioral). Save deep discussion for the debrief; never interrupt flow mid-game (Laurie, Stegmaier).
4. **Testers report symptoms; designers prescribe cures.** Engelstein's playtester paradox: "always listen to your playtesters" / "never listen to your playtesters" — they are reliable that something is wrong and how it felt, unreliable at prescribing fixes (Stegmaier: ask what happened, why, and how it felt — "playtesters raise questions; developers propose answers").
5. **One variable per iteration.** Once the core loop holds, change exactly one system per build so effects are attributable. Early thrash is tolerated; late-stage multi-change rebuilds are how balance regressions ship.
6. **Log everything, version everything.** No version + no log = the session never happened. Cardboard Edison writes down *every word* of feedback even when they expect to discard it (Levandowski).
7. **Small samples produce hypotheses, not proof.** One group breaking a strategy means "investigate," not "nerf." Detecting a 60%-win strategy vs a fair 50% needs ~190 games (binomial, 80% power) — you will never have that; act on trends, repetition across independent groups, and structural analysis instead.
8. **Escalate tester hostility.** Self → friends/family ("friendly" tests) → strangers ("unfriendly" tests) → target market → repeat groups → mechanics/theme experts (Caputo). Friends-only data is supportive bias, not signal.
9. **The rulebook is a component under test.** In blind tests every question testers ask is a rulebook bug — even when the answer is printed in the book (Stegmaier). Patterns of identical misplay across groups indicate a rules/UX problem, not player error.
10. **Test both extreme player counts.** Auction/market/bidding/deduction mechanisms notoriously break at 2p; downtime and chaos spike at max count (Caputo). A game tested only at its sweet spot is untested.
11. **Readiness and kill criteria are decided with numbers, not vibes.** Stegmaier's bar: ≥3 blind waves, ratings all 8–10/10, remaining feedback is fine-tuning only. If the trend line won't go there, shelve it and move to another design.

## How to apply it

### A. Choose the format

| Format | Measures | Cannot measure | Valid when |
|---|---|---|---|
| Solo / self-simulation (you run 2–3 seats) | Core-loop functionality, rules-flow bugs, setup logistics, rough duration | Social dynamics, true balance (you know hidden info), fun, rules clarity for newcomers | From first playable build onward; always before spending other people's time (Stegmaier) |
| Guided (designer at the table) | Engagement, pacing/downtime, emotional spikes (joy/frustration/confusion), emerging strategies, component usability, targeted hypotheses | Unaided rulebook comprehension; unbiased opinion (your presence breeds politeness) | Once solo-stable; the workhorse of mid-development |
| Blind (rules-only, no designer contact) | Rulebook clarity, iconography, setup intuitiveness, unbiased first impression | Early-stage breakage (wastes testers); deep strategy balance on its own | When the game is fun and functional and focus shifts to balance + intuitiveness (Stegmaier's trigger) |
| Remote blind (PnP / TTS / Tabletopia) | Scale, geographic spread, repetition volume | Physical usability: footprint, fiddliness, legibility are obscured digitally (Stegmaier treats digital as strictly secondary) | Late-stage waves; always re-verify conclusions physically before manufacturing |

### B. Run the session (guided)

1. **Before:** write the session goal; confirm stage-appropriate testers and player count; freeze a versioned build; print log sheet + feedback forms.
2. **Opening (2 min):** state the goal and stage ("testing balance of the two engines; components are placeholder"); give time expectation — and honor it. If the session collapses, stop early and talk it through; you are not required to finish every game (Laurie).
3. **Teach:** just enough to start; layer rules as they become relevant; never front-load everything or narrate design justifications (Laurie).
4. **During:** observe silently. Log every rules question (with interim ruling), hesitation, phone-checking, confusion, and engagement dips — including the quietest player. If someone breaks an element, let them demonstrate it once, then steer away; if they keep exploiting it, remove the element from play (Stegmaier).
5. **Debrief (10–15 min):** favorite part → least favorite part → one change (MVP icebreaker trio), then targeted probes from the question bank (`references/feedback-instruments.md`), then "would you play again?" and "would you buy it if it were available?" (Caputo).
6. **After:** complete the log same day; set notes aside ~1 day before implementing (Stegmaier); make ONE change; bump the version; update the card sheet and rulebook together.

Full scripts (solo, guided, blind, stress test), log templates, and journal structure: load `references/session-protocols.md`.

### C. Instrument the feedback

- Never ask leading or yes/no-only questions ("Is my game not awesome?!" teaches you nothing — Laurie). Replace "did you have fun?" with **perceived time** ("How long did you feel you were playing?" vs the clock — Rockholz).
- Ask for specifics, not adjectives: "Cards 2, 8, 19, and 54 felt too expensive," not "some cards felt expensive" (Stegmaier's example).
- Collect a **1–10 fun rating per session** (Stegmaier's standing metric; readiness = all 8–10). For emotional-arc detail, add per-round pulse checks or post-game peak/trough recall [community practice — no canonical named method].
- Written forms before verbal discussion where possible: writing is harder to self-censor, and shy testers contribute (Laurie; Kathleen Mercury's WINQ form: Works / Improvement / New ideas / Questions).
- Question bank, survey templates, rubrics, and NPS-for-games: load `references/feedback-instruments.md`.

### D. Log and iterate

- Minimum log fields: game + rules version, date, format, player count, tester names/experience, teach time, game length (actual + perceived), final scores/outcome, setups/factions used, every rules question + interim ruling, observed behavior, broken elements, fun rating, would-play-again / would-buy, pain points, planned change.
- Named exemplars: Brad Brooks logged *Letter Tycoon* play length, scores, and which letter tiles each player bought to expose over/under-powered powers; Peter Vaughan's *What the Food?!* (LoGM) finished balancing with a small core group of repeat testers playing weekly [group size unverified].
- Cadence: early stage — fast multi-change thrash, idea → playable in <1 week [community maxim]; mid — one variable per build, weekly or faster; blind waves — batch all changes *between* waves, never mid-wave (MVP), 3 sessions within 3 weeks per wave (Stegmaier).

### E. Blind-test waves (Stegmaier protocol)

1. Entry gate: fun + functional in guided tests; rulebook drafted to near-final; components legible without you.
2. Screen lead testers with a quiz for the skill that matters: reporting what happened, why, and how it felt. Stonemaier maintains ~130 paid, credited lead playtesters selected this way; each runs their own group.
3. Wave setup: detailed brief — timeline (3 sessions within 3 weeks), confidentiality, urgent-question channel, quantitative survey after each session + written report at the end, compensation (store credit or PayPal).
4. Hold ALL reports until the wave closes — reading early reports produces partial-picture processing (Stegmaier). Then process, implement changes, re-wave. Minimum 3 waves before calling a game ready.
5. Kit contents and recruitment channels: load `references/recruitment-and-kits.md`.

### F. Recruit

Ladder (Caputo's People approach): self → friends/family → local meetups/FLGS → conventions (Unpub events; Protospiel — reciprocity norm: give as much time as you take) → online pools (Break My Game: 500+ virtual events/yr, 4,000+ member Discord; Protospiel Online; Cardboard Edison's directory) → target market (kids' games need kids) → repeat groups (strategy games need one group playing 10+ times) → mechanics/theme experts. Full directory, outreach templates, compensation norms: `references/recruitment-and-kits.md`.

### G. Rules-comprehension (usability) testing

- Core instrument: the blind test. Variants: teach-back (testers teach the game back from the book), summarization (read book, explain the game), look-up timing (watch how long answers take to find — MVP).
- Etiquette: observe silently; intervene only when the answer isn't in the book; every intervention is a rulebook fix item (MVP).
- Repeated identical misplay across independent groups = rewrite or restructure that rule; do not fix comprehension by accreting exceptions.

### H. Statistical humility

| Claim you want to make | Games needed (binomial, α=.05, 80% power) |
|---|---|
| A strategy wins 70% vs a fair 50% | ~40 |
| 65% vs 50% | ~80 |
| 60% vs 50% | ~190 |
| 55% vs 50% | ~780 |

You will never have 190 logged games of one build. Therefore: single-session outliers are hypotheses, not noise (they often flag edge cases that resurface); balance on repeated independent reports + score-correlation analysis (correlate final scores with strategies used — Caputo), never on one table's result; report numbers with their n.

### I. Readiness vs kill criteria

**Ready to pitch/publish when ALL hold:** ≥3 blind waves complete; ratings all 8–10/10 with feedback reduced to fine-tuning (Stegmaier); ≥1 stranger per table says "would buy" (Caputo); a repeat group still chooses the game after 10 plays; both extreme player counts pass; your own gut agrees (Stegmaier pairs data with gut).

**Shelve/kill signals** [synthesis of the above, inverted — no single canonical source]: ratings plateau ≤6–7 across ≥2 full waves with no upward trend; zero would-buy across 3+ consecutive stranger tables; the repeat group stops choosing it before play 5; the only fix requires becoming a different game; you have dreaded working on it for weeks (Stegmaier's rut response: keep multiple designs and switch). Shelving = archive the last version + notes; it is reversible, and many designers return after months.

## Key numbers & heuristics

| Value | Heuristic | Source |
|---|---|---|
| 1 | Goal per session; variables changed per build (post-core) | Stegmaier; community consensus |
| 10–20 cards | First playable build of a planned 100-card game | Stegmaier, 2023 |
| ≥30 | Playtests before pitching a publisher | Caputo, LoGM (his "minimum population size in statistics" rationale is a misapplication of the CLT rule of thumb [contested as statistics; fine as a floor]) |
| 100+ | Playtests behind a published design | Peter Vaughan, LoGM |
| ≥3 | Blind waves minimum before "ready" | Stegmaier |
| 8–10/10 | Session ratings at readiness, feedback fine-tuning only | Stegmaier |
| 3 sessions / 3 weeks | Per blind wave, per lead tester | Stegmaier |
| ~130 | Stonemaier paid lead playtesters, quiz-screened | Stegmaier, 2023 |
| 10+ | Plays by one group to expose solvability in strategy games | Caputo |
| ≥1 | "Would buy it" per table before pitching | Caputo |
| 2 extremes | Always test lowest and highest player counts | Caputo |
| ~1 day | Set notes aside before processing | Stegmaier |
| ~40 / ~190 / ~780 | Games to detect 70/60/55% win-rate edges | Binomial power calc [derived, approximate] |
| 500+ / 4,000+ | Break My Game virtual events per yr / Discord members | breakmygame.com |
| — | "Test until you stop making changes, then 20 more" | Community maxim [unattributed, contested] |

## Common pitfalls

- **Friends-and-family-only testing:** supportive bias and sugar-coated feedback read as false confidence. Counter: Caputo's "unfriendly playtests" — strangers, then target market.
- **Defending the design:** explaining why a critic is wrong mid-debrief kills honesty. Levandowski's stages (LoGM): every designer passes through "I don't need feedback" → confirmation bias → "here's why you're wrong" → "everyone is right!" → disciplined "I'll think about it." Never tell a tester they're wrong; assume they're right about *how they felt* and file it (Laurie).
- **Changing 5 things at once:** effects become unattributable; balance regressions ship undetected. One variable per build once the core holds.
- **Asking "did you have fun?":** unactionable and invites politeness. Use perceived-time, favorite/least-favorite/one-change, and strategy walk-throughs (Rockholz).
- **Soliciting solutions instead of symptoms:** "what should I change?" yields contradictory prescriptions. Extract what/why/how-it-felt (Stegmaier); fixes are your job (Engelstein paradox).
- **Ignoring the least engaged player:** the quiet or disengaged tester is your most diagnostic data point — engagement dips are exactly what fun ratings hide. Watch phones, side conversations, and who stops leaning in.
- **Statistical overreach:** nerfing a strategy off one table's result, or dismissing single outliers that flag real edge cases.
- **Unstructured game-night testing:** rules changed mid-session on a whim, no version, no log, feedback of "it was fun." Unrepeatable and wasted.
- **Letting the exploit run:** after a broken element is demonstrated, continued exploitation invalidates the rest of the session (Stegmaier) — steer away or remove it.
- **Interrupting flow:** mid-game design debates alter everyone's perception of the game. Notes now, debrief later (Laurie, Stegmaier).
- **Rulebook by accretion:** patching comprehension failures with exceptions instead of restructuring; measure look-up time and misplay patterns instead.
- **Premature blind testing:** sending an unstable game to blind testers burns goodwill and measures nothing — blind waves start when the game is already fun and functional (Stegmaier).
- **Overrunning the clock:** sessions that drag past the promised length cost you feedback and future testers (Laurie).

## Reference files

- `references/session-protocols.md` — load when planning or running any session: full solo/guided/blind scripts, stress-test protocol, log & journal templates, iteration cadence, kill-criteria worksheet.
- `references/feedback-instruments.md` — load when building surveys or debrief questions: Rockholz's 10 questions with purposes, question-hygiene rewrites, WINQ, fun-rating instruments, post-session and blind-wave survey templates.
- `references/recruitment-and-kits.md` — load when recruiting testers or assembling blind-test kits: channel directory (Unpub, Protospiel, Break My Game, Protospiel Online, PnP communities), screener design, outreach templates, compensation norms, consent & privacy, kit checklist, tester tracking.

## Related skills

- `board-game-prototyping` — what you bring to the session: build fidelity, versioning, PnP kits.
- `board-game-rules-writing` — the rulebook your blind test is actually testing.
- `board-game-math-balance` — turning balance findings into cost/probability changes; win-rate targets.
- `board-game-design-theory` — what "fun" and "interesting decisions" mean before you measure them.
- `board-game-solo-coop-design` — automa difficulty and co-op-specific test protocols.
- `board-game-publishing` — what "ready to pitch" means on the publisher side.
- `board-game-market-analysis` — comparable titles for calibrating would-buy feedback.
- `board-game-accessibility` — catching access barriers testers won't articulate (colorblind double-coding, cognitive load).
