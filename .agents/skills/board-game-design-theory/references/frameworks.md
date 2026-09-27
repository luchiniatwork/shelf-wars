# Frameworks Reference — Core Game Design Theory & Player Experience

Extended catalog for `../SKILL.md`. Load when you need full definitions, exemplars, and mappings. Sources are cited inline; research provenance at the end. Numbers that are folklore are flagged [contested].

---

## 1. MDA framework (Hunicke, LeBlanc & Zubek, 2004)

Origin: "MDA: A Formal Approach to Game Design and Game Research," AAAI Workshop on Challenges in Game AI, 2004. Robin Hunicke and Robert Zubek wrote the prose; Marc LeBlanc supplied the concepts (per LeBlanc's own site, 8kindsoffun.com).

- **Mechanics**: rules, basic actions, algorithms, components.
- **Dynamics**: run-time behavior of mechanics acting on player input and each other.
- **Aesthetics**: emotional responses evoked in the player.
- **Directionality**: the designer builds M → D → A; the player experiences A → D → M. This asymmetry is the framework's core lesson: you cannot directly design feelings, only the rules that produce them.
- **Eight aesthetics** (the paper's phrasing): Sensation (sense-pleasure), Fantasy (make-believe), Narrative (drama), Challenge (obstacle course), Fellowship (social framework), Discovery (uncharted territory), Expression (self-discovery), Submission (pastime). The paper also mentions a ninth: **competition**.
- **Criticism** (Wikipedia, flagged under-cited): the list is arbitrary and mechanic-centric; weak for experience-first design. Treat as industry-standard vocabulary, not settled science [contested].

### Board-game usage

Tabletop translation: Mechanics = rulebook + components; Dynamics = table talk, races, blocking, snowballs, negotiation metas; Aesthetics = what players say afterwards ("tense", "hilarious", "epic"). Practical loop: (1) pick 2–3 target aesthetics; (2) name the dynamics that must exist; (3) choose mechanics (hand off to `board-game-mechanisms`); (4) verify with unprompted player language in playtests.

## 2. Marc LeBlanc's 8 kinds of fun — with tabletop exemplars

LeBlanc's own phrasings (8kindsoffun.com) differ slightly from the MDA paper; both given.

| Kind of fun | LeBlanc's tag | Dynamic that must exist | Tabletop exemplars |
|---|---|---|---|
| Sensation | Game as sense-pleasure | Tactile/visual delight; dexterity | Wingspan (eggs, dice tower), Flick 'em Up, dexterity games |
| Fantasy | Game as make-believe | Players inhabit a role/world | Cosmic Encounter, Root, Twilight Imperium |
| Narrative | Game as unfolding story | Events chain into a tellable story | Pandemic Legacy, Betrayal at House on the Hill, Above and Below |
| Challenge | Game as obstacle course | Skill growth visible; near-losses | Spirit Island, Through the Ages, Terraforming Mars |
| Fellowship | Game as social framework | Talking/reading people is gameplay | Diplomacy, Codenames, The Resistance |
| Discovery | Game as uncharted territory | Hidden content worth uncovering | Charterstone unlocks, Tainted Grail exploration, legacy envelopes |
| Expression | Game as soap box (MDA paper: "self-discovery") | Choices reveal/reflect the player | Dixit, Fiasco-style story games, faction-crafting |
| Submission | Game as mindless pastime | Low-stakes relaxation; ritual | Azul, Can't Stop, Quacks of Quedlinburg |

Usage: most successful designs anchor 1–2 primaries (e.g., Catan = Challenge + Fellowship) and support with 1–2 secondaries. Audit the box cover, theme, and mechanisms for agreement — a Submission-priced, Submission-weighted game marketed as epic Fantasy disappoints both audiences.

## 3. Jesse Schell — *The Art of Game Design: A Book of Lenses*

Book facts: Jesse Schell (CMU/Schell Games); 1st ed. 2008 (~100 lenses), 2nd ed. 2014 (113 lenses), 3rd ed. 2019. Each "lens" is a set of questions for inspecting a design. Lenses most load-bearing for tabletop work (names; numbering differs by edition — do not cite numbers):

- **Lens of the Interest Curve** — plot player interest over time: hook → rising peaks with rests → climax → resolution. The single most useful lens for session-arc work (§8 below).
- **Lens of Flow** — is challenge tracking skill? Where are the boredom/anxiety gaps?
- **Lens of Meaningful Choice** — are choices real? (See §11.)
- **Lens of Triangularity** — give players asymmetric risk/reward choices: safe-small vs risky-big. Tabletop embodiment: push-your-luck (Can't Stop), expensive-but-efficient vs cheap-now actions.
- **Lens of Endogenous Value** — why do players want the things the game says they want? Points must feel worth wanting.
- **Lens of the Elemental Tetrad** — mechanics, story, aesthetics, technology (components) must reinforce one theme.
- **Lens of Holographic Design** — every element should imply the whole; cut elements that don't.
- **Lens of Emergence** — simple rules, complex behavior (§7).
- **Lens of Surprise / Lens of Fun / Lens of Curiosity** — emotional spice checks.
- **Lens of Fairness / Lens of Challenge / Lens of Skill vs Chance** — competitive-integrity checks.
- **Lens of Simplicity and Complexity** — spend complexity where it buys depth (§7).

Schell's framing definition: a game is "a problem-solving activity approached with a playful attitude" — useful gate test for dry optimization puzzles.

## 4. Player psychographics

### 4.1 Bartle taxonomy (Richard Bartle, 1996)

"Hearts, Clubs, Diamonds, Spades: Players Who Suit MUDs" (1996). Quadrants: acting vs interacting × players vs world.

| Type | Suit | Wants | Board-game catering |
|---|---|---|---|
| Achiever | Diamonds | Points, measurable progress, mastery | Victory tracks, achievements, efficiency engines |
| Explorer | Spades | Discovery, systems, lore | Tech trees, hidden content, variant maps, lore |
| Socializer | Hearts | Relationships, talk, shared moments | Negotiation, co-ops, party mechanisms, table talk |
| Killer | Clubs | Dominance over other players | Direct conflict, take-that, area control, king-of-the-hill |

Caveats: designed for MUDs/MMOs, not tabletop; types describe *motivations in a session*, not fixed personalities; players blend. The Bartle Test (Andreasen & Downey, 1999–2000) had 800,000+ completions by Oct 2011 — evidence the model resonates, not that it is validated science.

### 4.2 MTG psychographics (Mark Rosewater, 2002+)

From Rosewater's "Timmy, Johnny, and Spike" (magicthegathering.com, March 2002); Melvin and Vorthos added by Rosewater in 2007 (the term Vorthos coined earlier by Matt Cavotta, "Snack Time with Vorthos," Aug 2005); female variants Jenny/Tammy introduced by Rosewater in March 2015.

- **Timmy/Tammy** — big moments, splashy swings, fun over winning. Serve: big combos, dramatic dice, table-flipping plays.
- **Johnny/Jenny** — self-expression, clever off-meta wins, combos nobody saw. Serve: modular systems, weird build paths (League's "Aimeyj" — see below).
- **Spike** — winning, proving skill. Serve: low luck variance, clear skill expression, draftable depth.
- **Melvin/Mel** — appreciates elegant mechanics as such. Serve: clean systems, clever interlocks.
- **Vorthos** — flavor and world. Serve: theme-mechanism resonance (hand off to `board-game-theme-narrative`).

### 4.3 League of Gamemakers four types (Michael Domeny, 2015)

Tabletop-native mapping ("Designing for the Four Types of Gamers," Oct 2015):

- **Sue** — makes a straight line for the victory condition; wants decisions that matter and full information. Design: limit chance's weight; put rules info on components/reference cards. Sue is your ideal rulebook proofreader.
- **BUTCH** — must win BIG. Design: allow high-risk/high-reward routes; let others progress even when attacked.
- **Aimeyj** (pronounced Amy) — wants to win unconventionally. Design: multiple viable paths; if Aimeyj can't find an off-meta strategy, suspect the game is on rails (a race to do "the one winning thing" fastest).
- **Raphael** — explores the world, may not try hard to win. Design: discovery content, flavorful corners.

Design test: name what each of the four does in your game for 90 minutes. If one has nothing, you've defined your audience narrower than the box claims.

### 4.4 Quantic Foundry motivation models (Nick Yee)

Two distinct models — do not conflate:

- **Video-game Gamer Motivation Model**: six clusters — **Action, Social, Mastery, Achievement, Immersion, Creativity**. Useful as a generic checklist of motivational hooks, but it is *not* derived from board-gamer data.
- **Board Game Motivation Model** (quanticfoundry.com, Jan 12 2017 reference chart; analysis post Apr 27 2017): **11 motivations in 4 clusters**, identified by cluster analysis of board-gamer survey data — **Conflict** (+ Social Manipulation: deception, bluffing, negotiation), **Immersion** (+ Aesthetics), **Strategy** (+ Systems Discovery, Need To Win), **Social Fun** (+ Cooperation, Chance, Accessibility). Survey n > 90,000 (91,035 in the April 2017 analysis; 1.1% non-binary respondents). Design-relevant findings: video-game "Competition" splits into Need To Win / Conflict / Social Manipulation / Cooperation for tabletop; Conflict is the most gender-polarized motivation (3.5× more men than women as primary); Accessibility and Social Fun top women's primary motivations; Discovery tops older gamers (36+).

Tabletop takeaway: direct conflict is optional, so audit which of the four clusters your game serves — a Strategy-only design leaves the Social Fun majority unserved. Per-motivation baseline scores are [contested — do not quote specific numbers without the source].

## 5. Flow theory (Mihaly Csikszentmihályi)

Origin: *Beyond Boredom and Anxiety* (1975). Flow = full absorption, action-awareness merging, distorted time sense, autotelic reward. Six components (Nakamura & Csikszentmihályi): intense concentration; merging of action and awareness; loss of self-consciousness; sense of control; time distortion; intrinsically rewarding experience. Plus: immediate feedback and a perceived chance to succeed.

Board-game applications:

- **Flow channel**: challenge/skill axes; boredom below, anxiety above. A game played 10 times by the same group must scale its challenge (asymmetric handicaps, scenario difficulty, deeper strategic layers) or players exit the channel.
- **Difficulty dials** must be explicit and honest (cross-ref `board-game-solo-coop-design` for win-rate calibration).
- **Session length**: flow requires sustained attention; downtime is the enemy — sequential turns at high player counts break flow (downtime math lives in `board-game-math-balance`; experience-level fixes: simultaneous play, off-turn engagement, end-of-turn draws).
- **Teach load vs flow**: nothing kills flow like a 40-minute rules lecture; the first turn must be playable within minutes of opening the box (cross-ref `board-game-rules-writing`).

## 6. The interesting-decisions doctrine

- **Sid Meier's dictum**: commonly rendered "a game is a series of interesting decisions." Soren Johnson (7 years at Firaxis, 2000–2007) quotes it in *Game Developer* (Jan 2009 issue; designer-notes.com, May 2009) as "a good game is a series of interesting choices." Attribute to Meier via Johnson.
- **Luke Laurie** (League of Gamemakers, 2014): "A tabletop game, at its core, is a structure for making decisions, with a feedback system for rewarding those decisions." And: "Even when luck is involved, we like to believe that our successes are the result of the decisions we have made."
- **Greg Costikyan**, "I Have No Words & I Must Design" (1994): a game is "a form of art in which participants, termed players, make decisions in order to manage resources through game tokens in the pursuit of a goal." Decision-centric definition; pairs with his *Uncertainty in Games* (MIT Press 2013): 11 uncertainty sources sustain tension even without dice — other players' minds are the randomizer (catalog in `board-game-mechanisms`).
- **Doug Church, Formal Abstract Design Tools** (Gamasutra, July 1999): **intention** (player can form a plan), **perceivable consequence** (feedback makes the result legible), **anticipation**. A decision without perceivable consequence teaches nothing.

### Sid Meier's other rules (via Soren Johnson, Game Developer Jan 2009 issue; designer-notes.com, May 2009)

1. **Double it or cut it by half** — iterate in large steps to stake out design space; small tweaks waste limited iterations.
2. **One good game is better than two great ones** ("Covert Action Rule") — two sub-games competing for attention destroy each other (his Covert Action; counter-examples Pirates! and X-COM work because sub-games are short and serve one clear focus).
3. **Do your research after the game is done** — players shouldn't "have to read the same books the designer has read."
4. **The player should have the fun, not the designer or the computer** — the player must "always be the star"; consequences the player can't understand are not fun.

### Soren Johnson, "When Choice is Bad" (Game Developer May 2013 issue; designer-notes.com, July 2013)

- Equation: **(total fun) = (meaningful decisions) / (time played)**.
- Every choice costs one of three things: **too much time** (Risk's army placement vs Dice Wars' auto-placement), **too much complexity** (5 techs vs 50; Blizzard held ~12 units/faction across StarCraft, Warcraft 3, StarCraft 2, explicitly removing old units to make room), **too much repetition** (static option menus produce stale favorites; Atom Zombie Smasher and FTL create variety *by limiting* choice — the emergent-variety argument).

## 7. Depth, complexity, elegance, emergence

- **Depth**: the size of the discoverable decision/strategy space that survives repeated play. **Complexity**: the cognitive load of rules and state-tracking. Quality target: maximize depth per unit of complexity ("depth-to-complexity ratio"; community consensus, echoed by Knizia — see `board-game-mechanisms` digest).
- **Elegance** test: can any rule be removed without shrinking the strategy space? Saint-Exupéry's subtraction principle is the working standard.
- **Emergence**: simple rules → unscripted complex behavior. Canonical example: Conway's Game of Life (1970). Tabletop: Go (near-minimal rules, vast depth); Magic's unintended card combos; negotiation metas in Diplomacy. Design for emergence by making *systems interact* rather than scripting outcomes.
- **Complexity budget** (Johnson's cognitive-load argument): players have finite attention (Miller 1956: 7±2 chunks; Cowan 2001: ~4±1). Every subsystem, exception, and icon spends it. Audit: list every rule; for each ask what decision depth it buys; cut negative-yield rules first.
- **Warning sign**: complexity that exists to serve simulation/realism rather than decisions (Meier's research rule, §6).

## 8. Engagement curves & session arc

Schell's **interest curve** shape for quality entertainment: initial hook → period of rising interest with peaks and rests → climax → brief resolution. Applied to a board-game session:

| Phase | Share [contested — heuristic] | Design job | Failure sign |
|---|---|---|---|
| Setup/teach | before play | Get to first decision fast | Players check phones during teach |
| Opening | ~first 25% | Legible first decisions; subgoals orient (Fristoe) | "I don't know what to do" on turn 1–2 |
| Midgame | ~middle 50% | Escalation: scarcity bites, interaction peaks, engines race | Nothing changes; turns feel identical |
| Endgame | ~last 25% | Convergence; every live player has a real final decision | Leader uncatchable with rounds left; "when will it end?" |
| Resolution | minutes | Fast, dramatic scoring | 15-minute arithmetic finale (Fristoe's "math-problem finale") |

Arc tools: escalation (engine growth, deck stages like 7 Wonders ages), depletion clocks, board contraction, staged scoring (triangular/square curves so late > early — Fristoe), end triggers that fire while outcomes are still contested. Piechnick's bar: "a good game ends one turn too soon" — leave players wanting one more turn.

## 9. Victory-condition design (extended)

Base taxonomy after Fristoe's goals/scoring articles (League of Gamemakers, Sep–Oct 2015) and Engelstein & Shalev's "Game End & Victory" category (*Building Blocks of Tabletop Game Design*, CRC Press 2019):

1. **Races** — first to a target (Catan 10 VP; Root 30 VP). Scoring is usually hidden-by-framing (movement on a track). Simple, dramatic, leader-hunting friendly.
2. **Competitions** — highest score at a fixed end (Terra Mystica, Agricola). More room for interesting scoring systems; risk of opaque standings.
3. **Elimination** — last player standing (Chess, King of Tokyo). Peak drama, worst dead-time. Fristoe's warning: elimination "leads to a pretty bad action arc" — power shrinks as the game ends.
4. **Sudden death / instant win** — override conditions (Twilight Struggle: DEFCON suicide, Europe control, 20 VP; Root's Dominance cards swap the race for objectives mid-game). Permanent background tension; must be signposted or it feels arbitrary.
5. **Objective/checklist** — complete a set of goals (Pandemic's 4 cures). Subgoals double as engine rewards (Fristoe: subgoal rewards "tend to help build a player's engine").
6. **Hybrid** — race + competition mixes, point salads (Wingspan, 7 Wonders). Multiple paths satisfy more psychographics but need EV calibration (→ `board-game-math-balance`).

Scoring-system dials (Fristoe, "Game Elements: Scoring," Oct 2015):

- **Hidden vs open scores**: hidden keeps losers invested and prevents mid-game computing; open enables leader-bashing and catch-up politics. Hybrid (part public, part revealed at end) is common. Failure: attacking the wrong "leader" in hidden-score games (Fristoe); compare Piechnick's criticism of Small World's face-down VP — it degrades into a memory test.
- **Granularity**: totals >10 → players need aids (Agricola's score sheets). Low scores make each point precious; high scores give the designer finer balance control.
- **Scaling over time**: flat lines are fine; rising (triangular: 1,3,6,10…; square: 1,4,9…) push importance late. "You don't want the graph to go down to the right" — that kills buildup.
- **Multipliers**: exciting but swingy; Fristoe's target: last place ≥60–70% of first place.
- **Math load**: keep to addition; avoid subtraction/negatives for mass audiences; hide complex math in components (grids, tracks).

Stonemaier's 12 Tenets (Jamey Stegmaier, Sep 2012) — a publisher's victory/experience checklist: quick setup/easy to learn; balances not checks for close games; conflict not hostility; choices not luck; scalability; unique production/creation; variable turn order; fast pace/smooth flow; **multiple paths to victory**; **point-based end-game trigger**; reasonable duration; replayability.

## 10. Feedback loops at the experience level

(Math of loop tuning belongs to `board-game-math-balance`; this section is about felt experience.)

- **Positive loop (success breeds success)** → snowball, runaway leader. Experience: leader exhilarated, table deflated; losers mentally check out. Monopoly is the canonical cautionary example (positive loop + elimination + output luck = miserable arc for everyone but the winner).
- **Negative loop (success breeds resistance)** → rubber-banding, close finishes. Experience: permanent tension — but players resent *overt* rubber-banding (Mario Kart's blue-shell problem). Hide catch-up inside arithmetic: ramps, proportional effects, politics, structural turn-order advantages, obscured leader (patterns catalogued in `board-game-math-balance`).
- **Design bar**: a player who cannot win still needs agency — self-directed goals, spoilers-with-purpose, or a short remaining clock. Never let a player know they've lost with a third of the game left (§10 in SKILL.md).
- **Engagement floor**: ~5% win probability keeps a trailing player invested (daniel.games [contested]).

## 11. Meaningful vs illusory choice

Taxonomy synthesized from Johnson (2009/2013), Laurie (2014 AP series; 2016 "Good Games – Hard Choices"), Church (1999):

| Type | Definition | Detect | Fix |
|---|---|---|---|
| Meaningful | Impactful + informed; intent and perceivable consequence both present | Players argue about the best move afterward | Protect |
| Rote | Best option obvious given goals | Turns run on autopilot | Automate/delete; or destabilize context |
| Illusory | Options differ in name, not outcome | Swapping choices changes nothing | Vary values visibly (Laurie P3) |
| Guess | Impact without information | Players shrug; blame luck | Leak partial info, forecasting, tells |
| Puzzle | Information complete, answer computable | Slow AP turns; alpha player solves | Add uncertainty/hidden info (Laurie M4) |
| Overload | Real choice buried under option count | Turn time balloons | Cut to ~3 salient options; phase-chunk |
| Hollow agency | Consequence invisible to player | "Did that do anything?" | Perceivable consequence (Church) |

Barry Schwartz's *The Paradox of Choice* (2004; TED 2005) is Laurie's psychological warrant: more options ≠ more satisfaction.

## 12. Why game ideas fail — synthesis

The recurring fatal patterns, each traceable to a framework above:

1. **No decisions** (Candy Land problem): the turn structure offers nothing impactful+informed. Test: SKILL.md §C audit finds zero meaningful classes.
2. **No tension**: no scarcity, race, contest, or uncertainty source; multiplayer solitaire. Test: nothing forces a player to want two things at once.
3. **No arc**: interest curve flat; turn N plays like turn 1. Test: remove the score track and players can't tell how far in they are.
4. **Solved/illusory depth**: dominant strategy collapses choice (Aimeyj test fails).
5. **Agency swamped**: output luck or chaos decides outcomes; players stop owning results (Laurie).
6. **Two games fighting** (Covert Action Rule): split attention.
7. **Arc ends early**: leader locked by midgame; kingmaking fills the vacuum.
8. **Wrong audience match**: weight/length misaligned with declared players (evergreen center of gravity: ~45 min, weight ~2.10 — 2019 snapshot, n=14; 2022 n=21 update in `board-game-market-analysis`).
9. **Designer fun, not player fun**: lore/simulation serving the author (Meier rule 4).
10. **Goal mismatch**: explicit victory condition rewards behavior opposite to the players' real goal (Fristoe's party-game warning).

## Sources & provenance

Fetched and extracted for this skill: Wikipedia articles "MDA framework", "Bartle taxonomy of player types", "Flow (psychology)"; Marc LeBlanc's 8kindsoffun.com; Soren Johnson's designer-notes.com ("GD Column 5: Sid's Rules", May 2009; "GD Column 25: When Choice is Bad", July 2013); League of Gamemakers (Luke Laurie, "Designing Games to Prevent Analysis Paralysis" parts 1–2, Feb 2014; Laurie, "Good Games – Hard Choices"; Teale Fristoe, "Game Elements: Goals" Sep 2015 and "Game Elements: Scoring" Oct 2015; Michael Domeny, "Designing for the Four Types of Gamers" Oct 2015); Stonemaier Games ("The 12 Tenets of Board Games", Sep 2012; "The Magic Formula for Publishing an Evergreen Tabletop Game", Dec 2019). Quantic Foundry via Wayback Machine (quanticfoundry.com Jan 12 2017, "Board Game Motivation Model: Handy Reference Chart & Slides"; Apr 27 2017, "The Primary Motivations of Board Gamers: 7 Takeaways") for the Board Game Motivation Model structure and demographics. Cross-referenced sibling research digests in this repo (mechanisms, math-balance, theme-narrative) for Costikyan, Engelstein & Shalev, Elias/Garfield/Gutschera, Knizia, Piechnick, and Leacock win-rate targets. Book knowledge cited without page-level verification: Schell (editions/lens counts), Koster (*A Theory of Fun*, 2004 — "fun is just another word for learning"), Kahneman & Tversky (1979; λ≈2.25 from the 1992 cumulative model), Miller (1956), Cowan (2001), Schwartz (2004).
