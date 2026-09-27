# Session Protocols — scripts, logs, cadence, kill criteria

Load this file when planning or running any playtest session: solo simulation, guided test, blind wave, stress test, or rules-usability test. For surveys and question banks see `feedback-instruments.md`; for recruiting and kit assembly see `recruitment-and-kits.md`.

---

## 1. Solo / self-simulation protocol

Purpose: prove the core loop functions before spending anyone else's time (Stegmaier: "I can smooth out the big rough patches on my own before subjecting anyone else to an early prototype").

**Setup:** control 2–3 seats with distinct, simple heuristics ("seat A always buys the cheapest engine card; seat B hoards; seat C plays greedily for points"). Hidden information: deal hands face-down and only look at the active seat's hand, or play open-handed and note the bias in the log.

**Script (30–60 min):**
1. Write the one question for the session ("can a full game be completed without rules contradictions?").
2. Explain each turn out loud as you play it — anything you cannot explain cleanly is a rulebook/flow bug; log it.
3. Play to completion. Do not redesign mid-session; log change ideas under "For Next Time."
4. Log: turn count, duration, any dead ends, any rules contradiction, first impressions of pacing.

**What solo play can prove:** loop functionality, rules-flow completeness, setup logistics, component ergonomics, rough duration, obvious math breakage.
**What it can never prove:** fun, social dynamics, true balance, clarity to a newcomer. Do not let 20 solo sessions substitute for one guided test.

---

## 2. Guided session script (designer present)

Total time: teach 10–20 min + play + debrief 10–15 min. Announce the expected duration and honor it (Laurie: testers whose time is disrespected don't return, and don't give feedback).

### Before
- [ ] One session goal written down ("is 4p downtime tolerable?", not "general feedback")
- [ ] Testers match the stage: friends for early thrash; strangers/target market for validation (Caputo's friendly → unfriendly ladder)
- [ ] Player count chosen deliberately; extreme counts scheduled as their own sessions
- [ ] Build frozen and versioned (`v0.7.1`); rulebook and card sheet match the build
- [ ] Log sheet + written feedback forms printed; pens

### Opening (say this)
> "Thanks for testing. This is version 0.7. The goal today is to find out whether the two engines are balanced — I'm not testing the art or components, which are placeholder. The game takes about 75 minutes. Ask rules questions any time; save design suggestions for the end — I'll ask for them."

Giving testers the goal focuses their attention (Stegmaier asks testers to ask the designer what they're trying to get out of the playtest); naming the stage prevents art feedback on an ugly prototype (Laurie: state theme, mechanics, and stage of development; give players an out if it isn't for them).

### Teach
- Teach just enough to start; layer rules as they become relevant ("in two turns we'll enter the end phase — here's how scoring works") (Laurie).
- Never narrate design history or justifications — it biases judgment and wastes table time.
- Compare to games the table knows only to accelerate the teach, then stop referencing them.

### During — observation checklist
Log, silently:
- Every rules question asked + the interim ruling given (each is a rulebook fix item — Stegmaier)
- Hesitation before turns; repeated re-reading of a card/icon
- Engagement dips: phone-checking, side conversations, leaning back; **who** and **when** (the least engaged player is your most diagnostic data point)
- Emotional spikes: laughter, groans, visible frustration, "wait, what?" moments (Stegmaier observes for joy/frustration/confusion)
- Downtime: longest wait between turns, and what caused it
- If a broken element appears: let it be demonstrated once, then steer play away; if the player keeps exploiting it, physically remove the element (Stegmaier)
- Do NOT: explain why a rule exists, defend choices, take notes so conspicuously that the table performs for you

### Debrief script (10–15 min, in this order)
1. **Icebreaker trio** (MVP Board Games): "Favorite part? Least favorite part? If you could change one thing, what?"
2. **Targeted probes** for today's goal, from the question bank in `feedback-instruments.md` (e.g., for balance: "What was your strategy? Can you explain why the winner won?").
3. **Pull questions:** "Would you play again?" → "Would you buy it if it were available?" (Caputo: ≥1 yes per table is the pitching bar).
4. **Written forms** collected before extended open discussion, so loud voices don't anchor the quiet ones.
5. Thank testers; tell them what happens next ("one change, then v0.8").

### Abort criteria
Stop a session early when: the game has collapsed (unrecoverable rules contradiction), a player is miserable, or the goal is already answered. Say so, convert to a discussion, and log it as a valid (often highly informative) session. You are not required to finish every game (Laurie).

---

## 3. Playtest journal & session log

### Journal structure (Mike, LoGM "Dear Diary: Keeping a Playtest Journal")
Per entry:
- **Header:** game, version, date, players (names + count), location/format
- **Set-up:** first sessions — full setup procedure; later — only deviations from standard
- **Results:** scores, how mechanisms played out, players' own impressions of how their play went, start/end time (phase-level durations if pacing is under test)
- **For Next Time:** rule changes that would have improved that session; setup changes; reminders
- **Catch-all:** questions to ponder, brainstorms, art/UI notes

Rule: get through the whole game without mid-session changes so effects on duration and balance stay trackable.

### Session log (spreadsheet header row)

```
date | game | rules_version | format (solo/guided/blind/remote) | location |
player_count | testers (+experience) | teach_time | game_length_actual | game_length_perceived |
scores_outcome | setup_factions | rules_questions (+interim rulings) | observed_behavior |
broken_elements | fun_rating_1_10 | would_play_again | would_buy | pain_points | planned_change
```

Named exemplars: Brad Brooks logged *Letter Tycoon* play length, scores, and which letter tiles each player bought — exposing over/under-powered letter powers (he dropped a discard-frequency metric when it proved uninformative: prune log fields that stop earning their keep). Peter Vaughan (LoGM, *What the Food?!*) logged name/length/date/final scores and finished balancing with a small core group of repeat testers playing weekly [group size unverified].

---

## 4. Stress test protocol (Michael Domeny, LoGM, 2015)

Purpose: find breakage a "normal" game hides. Strip theme, run the bare system, deliberately try to break it — one mechanic at a time.

**Setup:**
1. Recruit the full player count; repeat the protocol at each player count the game supports.
2. Identify victory condition(s).
3. Assign ONE player a single path to victory; they dedicate every decision and resource to it.
4. All other players are "control" — they play a balanced, normal strategy.

**Problem areas to investigate (checklist):**
- [ ] **Trickle scoring** — compensation/drip points or resources outside the main mechanic becoming a viable path on their own
- [ ] **Multipliers** — multiplication (worse: squaring) in scoring math running away
- [ ] **Catch-up mechanics** — usable by players not in last place, or when last is only slightly behind
- [ ] **Player-count scaling** — "take 3 gold from each other player" is fine at 2p, backbreaking at 6p

The stress test finds problems; it does not prescribe fixes.

---

## 5. Blind wave protocol (Stegmaier model)

**Entry gate (all required):** core loop proven fun in guided tests; rulebook near-final; components legible without explanation; you are shifting focus to balance + intuitiveness.

**Wave structure:**
1. Screen lead testers by quiz: the target skill is reporting what happened, why it happened, and how it felt — in writing. (Stonemaier: ~130 paid, credited lead testers; each runs their own group of ~1–4 additional players.)
2. Send the brief: timeline (3 sessions within 3 weeks), confidentiality expectations, channel for urgent blocking questions only, per-session quantitative survey + one written report at the end, compensation (Stonemaier: choice of store credit or PayPal).
3. Survey fields per session (Stegmaier's consistent core): name, email, player count, length, winning/losing details, 1–10 rating, bad, good, playtester names — plus 2–3 game-specific data points.
4. **Do not read reports as they arrive.** Wait until the wave closes; early reports produce partial-picture processing (Stegmaier).
5. Process: read all reports; note repeated independent complaints (signal) vs one-off opinions (hypotheses); implement changes; set aside ~1 day first if emotions are involved.
6. Re-wave. Minimum 3 blind waves before calling a game ready — often more.

**Ready when:** ratings all 8–10/10 AND remaining feedback is fine-tuning only, cross-checked with your own gut from the table (Stegmaier).

**Campaign/legacy games:** recruit testers committed to the full campaign and raise compensation significantly (Stegmaier).

**Video recordings:** Stegmaier tried recorded sessions for *Charterstone* and found them not useful without excellent A/V setups [contested — other designers rely on video; treat as optional, never a substitute for written reports]. If you record, get written recording consent from every player (and a parent's for minors) before the camera goes on — see `recruitment-and-kits.md` §6.

---

## 6. Rules-comprehension (usability) test variants

| Variant | Procedure | What it isolates |
|---|---|---|
| Blind rules-only | Kit + book, zero designer contact (see §5) | Whole-book clarity, setup intuitiveness |
| Teach-back | Tester reads the book, then teaches the game back to you or a second group | Structure/teach order failures |
| Summarization | Tester reads, then explains the game in their own words | Misread core concepts |
| Look-up timing | Mid-game, make testers find answers in the book themselves; time them (MVP) | Indexing, cross-referencing, term consistency |

Etiquette (MVP): observe silently; intervene only when the answer is not in the book; every intervention = one fix item. If several independent groups misplay the same rule identically, restructure the rule — don't append exceptions.

---

## 7. Iteration cadence by stage

| Stage | Change scope | Cycle | Notes |
|---|---|---|---|
| Early (solo/friendly) | Multi-change thrash acceptable | Daily–weekly; idea → playable <1 week [community maxim] | Attribution doesn't matter yet; velocity does |
| Mid (guided, core holds) | ONE major system per version | Weekly or faster; every build versioned + changelog (version / date / hypothesis / one change / result) | Preserve old versions — you will revert |
| Late (blind waves) | Batch ALL changes between waves; nothing mid-wave | 3 sessions / 3 weeks per wave; process → change → re-wave | Never tweak a build currently being evaluated by testers or a publisher — branch instead (MVP) |

Process rhythm per significant session: log same day → set aside ~1 day (Stegmaier) → implement one change → update rulebook + card data together → bump version.

---

## 8. Kill-criteria worksheet

No single canonical source defines kill thresholds; these operationalize the inverse of the sourced readiness criteria (Stegmaier, Caputo) plus community practice. Review after each wave.

| # | Signal | Threshold → action |
|---|---|---|
| 1 | Ratings plateau | Median ≤6–7 across ≥2 full blind waves with flat trend → rebuild core loop or shelve |
| 2 | No purchase pull | 0 "would buy" across 3+ consecutive stranger tables (Caputo's bar inverted) → shelve or reposition |
| 3 | No repeat pull | Repeat group stops choosing the game before play 5 (vs Caputo's 10+ target) → depth problem; redesign or shelve |
| 4 | Fun lives in a doomed element | Testers' favorite feature is one you must cut (license, cost, manufacturing) → pivot or shelve |
| 5 | The fix is a different game | Every viable solution changes the core audience/length/weight → start the new design; archive this one |
| 6 | Designer burnout | Weeks of dreading the work (Stegmaier's rut response: keep multiple designs going and switch) → pause, don't delete |

**Shelving protocol:** archive the final version + changelog + a one-page "state of the design" memo (what worked, open problems, hypotheses untested). Shelving is reversible — Stegmaier explicitly keeps multiple designs in flight and returns after breaks. Announce shelving to active testers and thank them; tester goodwill survives shelved games, not ghosting.
