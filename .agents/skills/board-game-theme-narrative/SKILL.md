---
name: board-game-theme-narrative
description: >
  Theme, narrative, and immersion for board game design. Use when the user wants to choose or change a game's
  theme ("theme-first or mechanism-first?", "does this theme fit these mechanisms?", "reskin my game",
  "pasted-on theme"), build a world ("write flavor text", "card names", "worldbuilding", "lore"),
  design campaign/legacy story arcs, name a game ("help me name my board game", "can I trademark this title"),
  commission art ("art direction", "artist brief", "how much does board game art cost"), weigh licensed IP vs
  original IP, or audit cultural sensitivity, representation, and historical-theme risk. For player-experience
  theory (MDA, kinds of fun, decision quality) use board-game-design-theory; for mechanism selection and
  taxonomy use board-game-mechanisms; for colorblind palettes, double coding, and language independence use
  board-game-accessibility; for pitching, contracts, and royalties use board-game-publishing; for theme as
  market positioning use board-game-market-analysis.
---

# Board Game Theme, Narrative & Immersion

## When to use / when not to use

Use when the task is about the fiction, presentation, or identity of a game: picking a theme, testing
theme-mechanism fit, writing flavor text/card names/lore, designing campaign or legacy narrative, naming a
game, directing or commissioning art, evaluating an IP license, or checking cultural/representation risk.

Do NOT use for:
- Choosing or tuning mechanisms themselves → `board-game-mechanisms`
- Fun/decision-quality theory, victory conditions → `board-game-design-theory`
- Rulebook wording, terminology discipline, examples of play → `board-game-rules-writing` (this skill owns
  *what* the terms mean in-world; that skill owns *how* the rulebook teaches them)
- Colorblind palettes, double coding, physical/cognitive access → `board-game-accessibility`
- Pitching the theme to publishers, sell sheets, royalty contracts → `board-game-publishing`
- Theme as positioning/pricing/comparable titles → `board-game-market-analysis`
- Print-file prep and art technical specs (bleed, CMYK, DPI) → `board-game-manufacturing`

## Core principles

1. **Theme sells the first copy; mechanisms sell the rest.** Theme, hook, and box drive purchase and
   marketing; mechanisms drive reviews, replay, and evergreen status. Industry adage; treat as practitioner
   consensus, not law [contested origin]. Screen for both, as publishers do (Stonemaier rejects submissions
   that duplicate an existing title *mechanically or thematically* — a winemaking game is dead on arrival
   because Viticulture exists).
2. **Verisimilitude, not realism.** Anchor fiction to real-world reference points (size, temperament,
   encumbrance) so players suspend disbelief; never simulate reality's tedium. Framework: Anthony Rando &
   Eric Cesare, "Reality Check: Verisimilitude in Game Design" (League of Gamemakers, 2014). Equivalent to
   Magic: The Gathering's "top-down design."
3. **Every core mechanism needs a one-sentence in-world justification.** Simultaneous selection = "a food
   fight happens in the blink of an eye" (*What the Food?!*). If you can't write that sentence, the mechanism
   is theme-independent — acceptable for light games, fatal for immersive pitches.
4. **Use in-world nouns for currencies and win conditions.** *Expedite* changed its win condition from 100 VP
   to $100M because abstract VP broke the CEO fantasy [contested — source not located; community-cited case].
   Prefer "money/influence/sanity" over "points" wherever the fiction supports it.
5. **Scale effects to in-world severity.** In *Bad Roommate*, sanity loss is proportional to offense severity
   (borrowed sweater ≪ wrecked car). Numbers are lore.
6. **Asymmetry must instantiate the trope.** In mash-up games (*Smash Up*, *Legendary*), each faction's
   mechanisms must reflect the essence of its trope — the "toybox appeal" only pays off when the toys play
   like what they are (Dan Letzring, League of Gamemakers).
7. **Keep ludic incentives consistent with the fiction's directives.** Ludonarrative dissonance (Clint
   Hocking, 2007, re *BioShock*; formalized by Frédéric Seraphine, Univ. of Tokyo 2016, as opposition between
   *incentives* and *directives*) occurs in tabletop when scoring rewards behavior the theme condemns — e.g.,
   a conservation game that pays you to exploit species.
8. **Worldbuild through components, not prose.** Distribute lore across card titles, flavor text, component
   shapes, and board geography; never wall-of-text in the rulebook. *Hansa Teutonica* player boards are
   shaped like desks; *Euphoria*'s board art shows the tunnels you dig.
9. **Match title tone to game weight.** Uncommon/complex words signal heavy games (*Tzolk'in*, *Twilight
   Imperium*); pun titles only for light games under 30 minutes (Mike Domeny, League of Gamemakers).
10. **Assume "you don't know what you don't know."** Fictional worlds are not exempt from cultural harm —
    "nothing is created in a vacuum... our biases have a tendency to cause harm anyway" (Isaac Childres,
    Frosthaven update). Hire cultural consultants proactively, at final-files stage.
11. **Representation is a design decision, not a demographic guess.** Among top-200 BGG games (2018), 94% of
    designers were white men (Elizabeth Hargrave). Broaden who designs and who is depicted; never reason from
    "women like pretty/low-conflict games"-style stereotypes.
12. **First-time designers build original IP.** Licensed IP brings approvals, royalties, style-guide
    constraints, and no brand equity for you. Original IP compounds: every game you publish grows an asset
    you own.

## How to apply it

### A. Choose the design's starting point
All three entries have produced all-time-great games (Gabe Barrett / Board Game Design Lab). Diagnose which
the user has, then stress-test it:
- **Theme-first** (e.g., Jeff Cornelius's *Threads*, designed "for knitters"): require domain immersion
  first — learn the field's terminology and practice before mapping mechanisms. Test: an insider should say
  "the designer gets it" even if they aren't one.
- **Mechanism-first**: require a theme pass before pitching. Run the resonance audit (B) and rename all
  currencies/win conditions in-world (principle 4).
- **Experience/hook-first** (define audience + target feelings, e.g., "heroic, paranoid"): derive theme and
  mechanisms to serve the feeling; Schell's experience-first method (*Art of Game Design*).

### B. Theme-mechanism resonance audit (run per core mechanism)
1. Can you justify the mechanism in one thematic sentence? (food-fight test)
2. Are win conditions/resources named in-world? (Expedite test)
3. Do relative costs/effects match in-world scale? (sweater-vs-car test)
4. Do factions' mechanisms reflect their trope's essence? (toybox test)
5. Could the game be trivially reskinned? If yes, theme is decorative — fine for light/abstract positioning
   (*Love Letter* reskins endlessly by design), a red flag for immersive/campaign pitches.
6. Any place where optimal play contradicts the fiction? (Hocking/Seraphine dissonance check — principle 7)

Deep paired examples and fixes → load `references/resonance-and-worldbuilding.md`.

### C. Worldbuilding pass
- Name every card/space in-world first, mechanically-generic second (or never).
- Flavor text: one line, voice-consistent, only where it adds character; skip it on frequently-read
  reference surfaces.
- Put lore into geography (board layout tells the world's story) and component shape before prose.
- Leave benign abstractions unexplained (dice-as-time-elapsed in Catan); explain only what players ask about.
- Backstory-first characters: enumerate archetypes/backstories/traits, then derive mechanisms from them
  (*Campaign Trail* method).

### D. Narrative & campaign design
- Definition (Stegmaier, 2021): a campaign game is "designed specifically to be played over multiple
  sessions with some connecting narrative and persistent elements." Design **micro endings** (pause points,
  episode cleanup/setup) and a **macro ending** (overarching goal).
- Budget engagement honestly: players average ~2 campaign games/year and have ~3 sitting unplayed; ~70% have
  abandoned a campaign; ~30:1 non-campaign:campaign play ratio (Stegmaier 2021 surveys). A campaign structure
  is not itself a selling point — "excitement... is largely dependent on the game itself (theme, mechanisms),
  not the inclusion of a campaign."
- Design for 2–4 players (91% of campaign play); include solo anyway (only 6–20% primarily solo, but
  Stegmaier calls solo "a necessity" — coordinate with `board-game-solo-coop-design`).
- Favor **emergent** story beats (mechanism-generated anecdotes) over scripted ones; scripted arcs belong in
  legacy/campaign containers with micro endings.

### E. Naming procedure
1. Generate 10+ candidates; crowdsource more from playtesters/social (Teale Fristoe, League).
2. Filter: 1–2 words ideal — "every word you use above a single word is minus points" (Peter Vaughan).
3. Check tone-weight match (principle 9); no puns unless light and <30 min.
4. Check collisions: BGG database, app stores, web search, domain availability; unambiguous vs. near-names
   (counterexample: "Summoner Wars" vs. "Summoners War").
5. Check trademark: games fall in Nice Class 28; search USPTO/EUIPO registers before falling in love.
6. Provisionally title early so playtesters can reference it; get objective feedback (Brad Brooks: "what
   resonates with you might not with others").
Full gauntlet + trademark/IP-licensing detail → load `references/naming-and-ip.md`.

### F. Art direction quickstart
- Write a brief per piece: subject, mood, world anchors, style references, technical specs (specs from
  `board-game-manufacturing`), and how the piece is used in play.
- Commission the Stonemaier way: scope estimate → 1–2 **prepaid** sample illustrations → cost ranges per
  illustration type with total counts (offer months of work as leverage) → short plain-language contract.
- Contract must-haves: publisher owns product-specific art (creator ≠ owner); artist self-promotion/print
  rights only **after official announcement** (anti-spoiler); up to 2 revision stages per illustration; pay
  invoices on the artist's schedule; 10% royalty if an art book is made; 5% of non-board-game derivative
  revenue (Stonemaier template, verified).
Full brief template, budget ranges, style-guide contents → load `references/art-direction.md`.

### G. Sensitivity & representation pass
1. List every real-world culture, history, identity, and religion your theme/art touches — including
   "fantasy" ones that map to real groups (Childres: fiction is not exempt).
2. Screen for colonial-fantasy defaults (games that ask players to "reenact colonialism" — Luke Winkie,
   The Atlantic 2021). Consider inverted premises (*Spirit Island*: you play the island's spirits repelling
   invaders; invader pieces are white to break light=good coding).
3. Hire a cultural consultant at final-files stage (Stonemaier, Tapestry expansion #2; Childres, Frosthaven
   with James Mendez Hodes; Kate Edwards for *Fled*). Brief: internal consistency of depicted cultures, no
   harmful co-option of real-world terms, collaborative fixes. Frame: "less harm and more joy."
4. Representation: vary depicted gender/ethnicity/age/body in art; check count ratios on cards; never
   justify theme choices by demographic stereotype (Hargrave/Bezdenejnih-Snyder).
5. Historical themes: decide explicitly between simulation, respectful treatment, and entertainment framing;
   state your stance in the rulebook/designer notes.

### H. Reskin risk test (before publisher pitch or theme change)
- If mechanisms reference theme-specific nouns (names, places, objects in card text), a retheme forces
  mechanism rewrites → flag as reskin-fragile.
- Trope-bound asymmetry (principle 6) resists reskin by design — a feature for immersion, a bug if the
  publisher wants a different license.
- Theme-independent cores reskin cleanly (*Love Letter*'s 16-card core has carried dozens of licensed
  editions). Decide deliberately which architecture you want.

## Key numbers & heuristics

| # | Heuristic | Value | Source |
|---|-----------|-------|--------|
| 1 | Title length | 1–2 words ideal | Peter Vaughan, League of Gamemakers |
| 2 | Pun-title ceiling | Light games, <30 min play time | Mike Domeny, League of Gamemakers |
| 3 | Trademark class for games | Nice Class 28 (USPTO/EUIPO) | trademark practice; file ~$250–$350/class [contested — fees change; check current schedule] |
| 4 | Campaign engagement | ~2 campaign games played/yr; ~3 unplayed backlog; ~30:1 non-campaign:campaign ratio | Stegmaier 2021 surveys |
| 5 | Campaign completion | ~70% have abandoned a campaign; only 21–29% completed every one started; 30% of abandoners feel regret | Stegmaier 2021 surveys |
| 6 | Campaign player counts | 91% play campaigns at 2–4p; solo-primary 6% (ambassador) vs 20% (reader) | Stonemaier Ambassador vs reader surveys, 2021 |
| 7 | Wingspan pre-revenue spend | $150,000 total (art + graphic design + manufacturing + freight) before Jan 2019 first English sale | Stegmaier |
| 8 | Wingspan thematic content | 170 unique bird cards in base game; signed partly because "the theme directly inspired the mechanisms" | Stegmaier |
| 9 | Designer demographics | 94% of top-200 BGG game designers were white men (2018) | Elizabeth Hargrave |
| 10 | Gamer motivations survey | n>90,000; 72.7% male, 26.0% female, 1.1% other | Nick Yee, Quantic Foundry, Apr 2017 |
| 11 | Artist revisions | Up to 2 revision stages per illustration, then extra fees | Stonemaier artist contract |
| 12 | Artist extras | Art-book royalty 10% of revenue; derivative non-game media 5% of revenue | Stonemaier artist contract |
| 13 | Card illustration rates | Community-quoted ~$50–$500+ per card illustration; box covers ~$1,000–$5,000+ | [contested — community ranges, vary widely by artist/scope] |
| 14 | Licensed-IP royalty | Community-quoted ~8–14% of net sales to licensor, plus approvals | [contested — practitioner consensus, deal-specific] |

## Common pitfalls

- **Pasted-on theme / wallpaper:** mechanisms untouched by fiction; breaks the moment a player asks "why am
  I doing this in-world?" Survivable only in light/abstract-positioned games.
- **Ludonarrative dissonance (tabletop form):** scoring incentives reward what the fiction condemns
  (Seraphine's incentive-vs-directive split is the diagnostic).
- **Realism instead of verisimilitude:** simulating tedium (wool regrowth, bathroom breaks) instead of
  anchoring believability. VST ≠ realism (Rando & Cesare).
- **Tone-weight mismatch:** heavy mechanisms under a pun title; light chaos under an epic name. Misleads
  buyers, tanks reviews.
- **Wall-of-text lore:** worldbuilding dumped into rulebook passages instead of distributed across card
  titles, flavor, component shape, and board geography.
- **Reskin breakage:** theme-specific nouns hard-wired into mechanism text; a publisher retheme demands a
  redesign.
- **Colonial/appropriation blind spots:** colonizer-fantasy defaults; "it's just fantasy" fallacy. Fix with
  inverted premises and cultural consultants, proactively not reactively.
- **Demographic stereotyping:** "female-friendly theme" reasoning; individual preference ≫ demographic
  generalization.
- **Campaign fatigue as market risk:** buyers already own ~3 unplayed campaign games and finish ~1 in 4–5
  they start; a campaign badge alone sells nothing.
- **Licensed-IP seduction:** approvals, royalties, and zero equity; a trap for first-time designers
  (practitioner consensus; BGDL licensed-IP episodes with Daryl Andrews, Nolan Nasser).
- **Historical-accuracy whiplash:** marketing "accuracy" while sanitizing the era's harms — critics punish
  both directions. Pick a stance and disclose it.
- **Theme redundancy at the publisher gate:** pitching a theme the publisher already owns (winemaking →
  Viticulture) is rejection regardless of mechanism quality.

## Reference files

- `references/resonance-and-worldbuilding.md` — load when auditing theme-mechanism fit, writing lore/flavor,
  designing campaign/legacy narrative arcs, assessing reskin risk, or reviewing sensitivity case studies.
- `references/art-direction.md` — load when commissioning art, writing artist briefs or style guides, or
  budgeting illustration/graphic-design work.
- `references/naming-and-ip.md` — load when naming a game, checking trademark/searchability, or evaluating a
  licensed-IP deal vs original IP.

## Related skills

- `board-game-design-theory` — MDA, kinds of fun, decision quality, victory conditions, idea critique
- `board-game-mechanisms` — mechanism taxonomy, tension, combining into a core loop
- `board-game-rules-writing` — terminology discipline, rulebook anatomy (takes your in-world nouns as input)
- `board-game-accessibility` — colorblind-safe palettes, double coding, language independence, inclusive art
- `board-game-market-analysis` — themes that sell, positioning, comparable titles
- `board-game-publishing` — pitching themed games, sell sheets, contracts & royalties, advances
- `board-game-crowdfunding` — campaign-page anatomy and tier structure your theme must serve
- `board-game-solo-coop-design` — solo modes for campaign/narrative games
- `board-game-manufacturing` — art file specs, print prep for commissioned art
