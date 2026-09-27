# Co-op Antipatterns — Quarterbacking, Semi-Coop Traps, Difficulty Failure Modes

Load this when diagnosing why a co-op plays badly: one player dominates, endings feel spiteful or flat,
difficulty feels unfair, or the group is bored/snowballed.

## 1. Quarterbacking / the alpha-player problem

**Definition.** An alpha gamer "can figure out the moves required to achieve a goal for everyone and then
attempts to guide the other players to that goal" — telling everyone what to do and sucking out the fun
(Christian Strain, "I, Alpha Gamer," League of Gamemakers 2014). Mike Selinker calls it **"the Pandemic
problem"** (noting it neither originated with nor always afflicts Pandemic): "Sometimes one player wants
to run the game for everyone. A good co-op design knows this is a possibility and figures out something
that gets in the way of that" (LoG 2016).

**Who it hits hardest.** Leacock: most common with mismatched skill levels and with strangers (convention
pickup games), less among established groups; "I don't think it can be eliminated altogether." Design
goal = raise the cost of quarterbacking, not perfect elimination.

**Structural model — break a leg of the tripod.** Quarterbacking needs all three:
1. **Perfect shared information** — one brain can see the whole position.
2. **Symmetric capability** — anyone can do anyone else's job, so directing costs nothing.
3. **Unlimited communication** — directing is free and instant.
(A fourth accelerant: low per-player cognitive load, so one brain *can* compute everyone's turn.)

### Mitigation catalog (mapped to the leg it breaks)

| Mitigation | Breaks | Exemplar | Note |
|---|---|---|---|
| Hidden own-hand info | Info | Hanabi (Bauza, 2010) — you see every hand but your own; clues cost limited tokens | Clue tokens also tax communication |
| Channel-limited comms | Comms | The Crew (Sing, 2019) — radio token reveals exactly one card fact per hand | Silence is the default state |
| Communication ban + split controls | Comms + symmetry | Magic Maze (Lapp, 2017) — no talking; each player owns one movement direction | Physical dependence forces engagement |
| Real-time pressure | Comms (by compression) | Space Alert (Chvátil, 2008, 10-min soundtrack), Escape: The Curse of the Temple (2012), Fuse (2015) | Planning outruns speech bandwidth |
| No-value communication | Comms | The Mind (2018) — play cards ascending, no talk about values | Pure version; party-weight |
| One-way/asymmetric info | Info | Mysterium (2015) — ghost may only send vision cards | One role structurally cannot be directed |
| Simultaneous secret commit | Comms | Just One (2018) — clues written secretly, duplicates cancel | Directing is mechanically impossible |
| Personal stakes / secret goals | Symmetry (stakes) | Dead of Winter (2014) — secret personal objective, possible betrayer | Selinker's fix: "encourage self-interest" |
| Traitor possibility | Info + stakes | Battlestar Galactica (2008), Shadows over Camelot (2005) | Open solving risks feeding the enemy |
| Long-haul ownership | Stakes | Pathfinder ACG — your deck persists; giving away the Sword of Awesome costs YOU | Selinker, LoG 2016 |
| Physical ownership devices | Comms (norms) | Pandemic: The Cure (2014) — each player rolls their own dice; Leacock: "I've never seen a player reach across the table and roll another player's dice!" | Cheap, stackable on any design |
| Per-player cognitive load | 4th leg | Spirit Island (2017) — each spirit's turn is complex enough that computing four turns exceeds one brain | The heavy-euro solution |
| Rules-level communication limits | Comms | Strain's own design rule: advice only from adjacent players | Works but feels artificial unless themed |

**When to accept quarterbacking:** teaching/family games where a mentor dynamic is desired (Hawthorne
reports never seeing it as a problem in Mice and Mystics' all-ages context), and intentionally
hierarchical designs. Name the tradeoff in the design diary instead of pretending it's solved.

## 2. Semi-cooperative traps

Source baseline: Tom Jolly, "Making Semi-Cooperative Games Work," LoG 2015.

- **The fatal flaw — reverse kingmaker.** If players can lose individually but the group losing reads as
  a shared "tie," a player who can't win may tank everyone: "if everyone loses, then it's a tie!" Any
  semi-coop with an everyone-loses state must answer this in the rules.
- **Competition eats cooperation.** Jolly's law from his own prototypes: when both are present, "the
  competitive elements will always rule the cooperative elements." Budget cooperation incentives
  accordingly, or stop calling it a co-op.
- **Fixes that work:** (a) remove the everyone-loses conclusion; (b) escape/stash mechanism — bank your
  winnings and leave, so one spiteful player can't burn your stake; (c) embed cooperation inside a normal
  competitive game (trading in Catan/Bohnanza) instead of bolting competition onto a co-op.
- **Individual-winner co-op variant caution:** point-scored "co-op with a winner" (Legendary's scoring,
  Castle Panic's Master Slayer) reintroduces leader-tanking — the leader may let the team nearly die to
  farm kills. If you ship it, cap the farming (shared-failure threshold close and visible).
- **Traitor-specific traps:** betrayer under-powered pre-reveal (BSG balance work), revealed-traitor
  downtime, and suspicion paralysis in groups that over-accuse. Give the traitor pre-reveal subversion
  actions and the group a mechanical accusation cost.

## 3. Difficulty and tension failure modes

| Failure mode | Signature in playtests | Root cause | Fix |
|---|---|---|---|
| Flat difficulty | "Turn 1 felt like turn 10" | Threat constant; no ratchet | Scheduled escalation step (Pandemic epidemic: rate up + spike + discard recycle) |
| Difficulty spike | Smooth then sudden wall | Step function too steep or all dials stacked at one point | Spread escalation; cap single-step jumps |
| Snowball fail | Early bad luck → certain loss felt by mid-game, game continues | No stabilization tools; no fast-loss exit | Give comeback levers post-escalation; let doomed runs end fast (Hawthorne: "lose quickly… allows them time to try again") |
| Already-lost-but-playing | Loss certain ~45 min before it registers | Hidden doom math | Make clocks visible; end or telegraph |
| Routine threat | Group solves the AI by play 3 | Predictable, non-varied challenges | Variety of enemies/content (Hawthorne); well-ruled randomness to kill "I calculated all odds" play (Trzewiczek) |
| Difficulty-morale mismatch (campaign) | Legacy group tilts after 2 losses | Irreversible sessions + standard difficulty | Target ~2:1 win:loss for campaign sessions (Leacock) |
| No-target tuning | "Is it too hard?" debates with no numbers | No win-rate target chosen | Pick a target first (see SKILL.md table: designer-stated first-play targets span 0–75%) |

**Detection discipline.** Log win/lose, margin, and *the turn the outcome felt decided* for every test.
The felt-decision turn, not the final score, exposes snowball and already-lost failures. Watch players
rather than trusting self-reports (Leacock: phones out = disengagement; leaning in and talking = the
system works).

## 4. The engagement checklist (what good looks like)

From the LoG expert panel (Hawthorne / Trzewiczek / Selinker, 2016):
- Dynamic artificial tension that is "more than just a puzzle being solved by a group" — enough varied,
  interacting challenges that the puzzle can't be pre-solved (Hawthorne).
- Each player has a unique, meaningful contribution — but roles must not hard-script every round
  (Trzewiczek's Robinson Crusoe soldier who "spends 2 hours sending his worker on the Hunting action" is
  the anti-model).
- Replay variety: "different victory conditions, different headaches, different resources. Always
  different" (Selinker).
- Alternating hope and fear (Leacock): after every escalation beat, the players should hold a tool that
  could plausibly stabilize them.
