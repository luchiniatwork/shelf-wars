# Board Game Design Skill Taxonomy

Thirteen skills covering the full lifecycle of designing a great and commercially
successful board game. Each skill owns a disjoint scope; cross-references route
between them. Trigger descriptions are written for automatic model selection.

| # | Skill | Owns | Defers to |
|---|-------|------|-----------|
| 1 | `board-game-design-theory` | Player-experience frameworks (MDA, kinds of fun, lenses), interesting decisions, agency, depth vs complexity, session arc, victory conditions, idea critique | mechanisms, math-balance |
| 2 | `board-game-mechanisms` | Mechanism taxonomy, tension sources, player-count scaling, exemplars, combining into a core loop, mechanical innovation | design-theory, math-balance |
| 3 | `board-game-math-balance` | Probability, expected value, cost curves, point-salad calibration, intransitive balance, feedback loops, pacing, player-count scaling, difficulty win-rates | mechanisms, playtesting |
| 4 | `board-game-theme-narrative` | Theme-mechanism resonance, worldbuilding, naming, art direction, IP licensing, cultural sensitivity, representation | market-analysis, rules-writing |
| 5 | `board-game-prototyping` | Prototype stages, physical materials, digital platforms (TTS/Tabletopia/Screentop), PnP kits, iteration discipline | playtesting, manufacturing |
| 6 | `board-game-playtesting` | Self/guided/blind tests, session protocols, feedback instruments, recruitment, logging, kill criteria, usability testing | prototyping, math-balance |
| 7 | `board-game-rules-writing` | Rulebook anatomy, teach order, terminology discipline, examples of play, player aids, iconography, edge cases, localization-ready writing | playtesting, accessibility |
| 8 | `board-game-manufacturing` | Component specs, print file prep, manufacturers & quotes, costing (MSRP ~5x), MOQ, compliance (EN71/ASTM/CPSIA), freight & fulfillment | crowdfunding, market-analysis |
| 9 | `board-game-publishing` | Licensing vs self-publishing vs work-for-hire, pitching & sell sheets, conventions, contracts & royalties, BGG/media ecosystem | crowdfunding, market-analysis |
| 10 | `board-game-crowdfunding` | Pre-launch funnel, funding-goal math, page anatomy, pledge tiers, stretch goals, shipping/VAT/tariffs, pledge managers, fulfillment, post-campaign | manufacturing, publishing |
| 11 | `board-game-market-analysis` | Market segments, comparable-title method, pricing architecture, positioning, distribution economics, trends | publishing, design-theory |
| 12 | `board-game-solo-coop-design` | Automa/AI opponents, difficulty dials & win-rate calibration, co-op structure, quarterbacking mitigation | math-balance, design-theory |
| 13 | `board-game-accessibility` | Colorblind-safe palettes, double coding, cognitive/physical/vision access, language independence, socioeconomic access, inclusive art | rules-writing, theme-narrative |

## Authoring conventions

- Directory package: `.agents/skills/<name>/SKILL.md` (+ optional `references/*.md`),
  the Agent Skills standard location so harnesses discover the skills both when
  working inside this repo and when installing it as a Pi package.
- SKILL.md = the always-loaded instruction: core frameworks, key numbers,
  checklists, and explicit pointers for when to load each reference file.
- References carry bulk catalogs/tables/examples.
- All claims specific: named frameworks with originators, numeric heuristics,
  named exemplar games. Contested numbers flagged `[contested]`.
