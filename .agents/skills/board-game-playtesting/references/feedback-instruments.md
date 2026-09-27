# Feedback Instruments — question banks, surveys, rubrics

Load this file when building a playtest survey, preparing debrief questions, or converting raw feedback into design actions. For session scripts see `session-protocols.md`; for tester-facing kit documents see `recruitment-and-kits.md`.

---

## 1. Question hygiene (rules before instruments)

1. **No leading/loaded questions.** "Is my game not awesome?!" / "Wasn't combat exciting?" teach you nothing and manufacture confirmation bias (Laurie).
2. **No bare yes/no items.** Every yes/no question hides the "why" you actually need.
3. **Symptoms, not solutions.** Testers are reliable about what happened and how it felt, unreliable at prescribing fixes (Engelstein's playtester paradox: "always listen to your playtesters" / "never listen to your playtesters"). Stegmaier's instruction to testers: share **what happened, why it happened, and how it made you feel** — do not redesign the game.
4. **Specifics over adjectives.** Stegmaier's canonical example: useless = "There were a few cards that felt too expensive"; useful = "Cards 2, 8, 19, and 54 felt too expensive."
5. **Both polarities.** Collect what works AND what doesn't — knowing what to keep is as valuable as knowing what to change (Stegmaier dropped testers who only praised).
6. **Written before verbal.** Forms first, discussion second — writing resists peer anchoring and gives shy testers a channel (Laurie).

### Leading → neutral rewrites

| Leading / useless | Neutral / useful |
|---|---|
| "Did you have fun?" | "How long did you feel like you were playing?" (compare to the clock — Rockholz) |
| "Was the game balanced?" | "Can you explain why the winner won?" + log final scores |
| "Isn't the engine-building satisfying?" | "Walk me through your strategy this game." |
| "Was it too long?" | Actual length vs stated expectation + "where, if anywhere, did your attention drift?" |
| "Did you like the cards?" | "Name any cards you always wanted and any you never wanted." |
| "Were the rules clear?" | (Blind test) log every question asked + every misplay; don't ask at all |

---

## 2. Rockholz's 10 Insightful Playtest Questions (Gamasutra/Game Developer, 2014)

A debrief bank engineered to replace "did you have fun?". Pick 3–5 per session matched to the session goal.

| # | Question | What it measures |
|---|---|---|
| 1 | How much time did you *feel* like you were playing for? | Engagement via perceived-time compression (the "did you have fun" replacement) |
| 2 | Did you feel you were making friends or enemies with the other players? | Whether the social atmosphere matches your design intent (co-op that feels competitive = misaligned mechanisms) |
| 3 | Could you play again without looking at the rules? | Rules learnability and mnemonic design |
| 4 | What was your strategy? | Whether the game presents legible strategic paths; "I didn't have one" = strategies aren't surfacing |
| 5 | How far in advance could you predict opponents' moves? | Depth vs predictability; fully predictable → tic-tac-toe effect (solved, stale) |
| 6 | To what extent did you react to opponents' moves? | Meaningful interaction vs multiplayer solitaire |
| 7 | Can you explain why the victorious player won? | Win attribution: informed decisions vs coin-flips; also whether players had enough opponent information |
| 8 | How much did you feel in control of the outcome? | Agency vs randomness calibration for your target audience |
| 9 | Did anything hold you back from seeing your plans through? | Resource starvation, counter-play frustration; the same complaint repeated = flashing red light |
| 10 | Name the game you've played most similar to this one. | Market-fit proxy; reveals what players use as mental scaffolding for learning your game |

---

## 3. Structured written instruments

### Icebreaker trio (MVP Board Games) — every debrief, any stage
1. What was your favorite part?
2. What was your least favorite part?
3. If you could change one thing, what would it be?

### WINQ form (Kathleen Mercury, built on Stanford d.school feedback methods)
Four written quadrants, usable mid-game without stopping play:
- **W**orks — what's functioning and fun (protect this)
- **I**mprovement — what needs work
- **N**ew ideas — what you'd add or change
- **Q**uestions — what's confusing

Process: the designer prepares ≥3 targeted questions for testers beforehand; both designer and testers fill forms; the designer writes a self-reflection summarizing how feedback will be incorporated.

### Per-session survey (Stegmaier's blind-wave core fields)
Consistent every session, plus 2–3 game-specific items:
```
name | email | playtester names at table | player count | session length |
winning/losing details (scores, margin) | rating 1–10 | bad | good
```
Add per build: the 1–2 hypotheses this wave is testing ("did the new market card get bought at 2p?").

### Fun-rating instruments
- **Per-session 1–10** (Stegmaier): the standing metric; readiness = consistently 8–10 with fine-tuning-only feedback.
- **Perceived time** (Rockholz Q1): felt vs clock time; engagement compresses time.
- **Per-round pulse / emotional-arc mapping** [community practice — no canonical named method]: a 1–5 rating per round/phase, or post-game recall of peak and trough moments, to locate *where* the fun curve sags (e.g., a mid-game downtime trough).
- **NPS-for-games** (borrowed instrument): 0–10 "likelihood to recommend"; promoters 9–10, passives 7–8, detractors 0–6; NPS = %promoters − %detractors. Value is in the trend across waves and the mandatory follow-up "why?" — not the absolute number.
- **Pull questions** (Caputo): "Would you play again?" and "Would you buy it if it were available?" — ≥1 would-buy per table is the pre-pitch bar.

---

## 4. Blind-wave final report template (tester-facing)

```
1. Sessions played (dates, player counts, durations)
2. Rules questions you could NOT resolve from the book (list every one)
3. Rules you played wrong and discovered later (list every one)
4. What happened: the 3 most memorable moments (good or bad) — what, why, how it felt
5. Balance: what strategy won and why; anything that felt unbeatable or useless
6. Specifics: name exact cards/tiles/rules that felt too strong, too weak, too expensive
7. Rating 1–10, and what would move it +1
8. Would you play again? Would you buy it? Why / why not?
```

Designer-side reminders: tell testers to use intuition when stuck (guess, note, continue — Stegmaier); require misplayed rules to be reported explicitly (patterns of identical misplay = rules/UX problem, not player error); hold all reports until the wave closes before reading any (Stegmaier).

---

## 5. From feedback to action — the processing rubric

1. **De-duplicate and cluster** across the wave: one complaint from five groups > five complaints from one group.
2. **Classify each item:** bug (rules/math broken) · usability (book/icon/UX) · balance (dominant/weak strategy) · taste (preference, not defect).
3. **Convert to hypothesis:** "Cards 2, 8, 19, 54 feel expensive" → hypothesis "engine cards overpriced at 2p" → test with ONE changed variable next build.
4. **Weight by tester fit:** target-market testers' taste complaints outrank experts'; mechanics experts' balance complaints outrank casuals'. A party-game complaint from a heavy-euro player is data about audience, not about the game.
5. **Watch the trend, not the point:** small samples make single-session means meaningless (see SKILL.md §H power table). Act on repeated independent reports and score–strategy correlation (Caputo: correlate final scores with strategies used to detect dominant lines).
6. **Log decisions:** every implemented change gets version, date, hypothesis, result. Also log feedback you *rejected* and why — it resurfaces, and you'll want the reasoning (Cardboard Edison writes everything down even when they expect to discard it).

### Feedback-reception failure stages (Levandowski, LoGM "The Stages of Playtesting")
Recognize where you are; the goal is stage 5:
1. "I don't need feedback. I know my game!" → fix: get feedback at all.
2. "That was good feedback — it agreed with me!" (confirmation bias) → fix: write everything down.
3. "Here's why you're wrong…" (ego; theory-vs-practice) → fix: assume they're right about how they felt; try the idea before dismissing it.
4. "Everyone is right!" (contorting the game for every comment) → fix: some feedback is wrong for this game; trying costs one session, contorting costs the design.
5. "I'll think about it." — record verbatim, consider later, decide with data.
