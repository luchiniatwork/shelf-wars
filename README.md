# shelf-wars

A collection of expert **board game design skills** for [Pi](https://github.com/badlogic/pi-mono), covering the full journey of designing a great and commercially successful tabletop game:

> idea → mechanisms → math & balance → theme → prototype → playtest → rules → market fit → manufacturing → crowdfunding → publishing

## Skills

| Skill | What it covers |
|---|---|
| `board-game-design-theory` | Player-experience frameworks (MDA, 8 kinds of fun, Schell's lenses, psychographics), interesting decisions, agency, depth vs complexity, session arc, victory conditions, idea critique |
| `board-game-mechanisms` | The mechanism taxonomy with tension sources, player-count scaling and exemplars; combining mechanisms into a core loop; where mechanical innovation comes from |
| `board-game-math-balance` | Dice/card probability, expected value, cost curves & power budgets, point-salad calibration, intransitive balance, feedback loops, pacing, player-count scaling, win-rate statistics |
| `board-game-theme-narrative` | Theme-mechanism resonance, worldbuilding, naming & trademark, art direction, IP licensing, cultural sensitivity, representation |
| `board-game-prototyping` | Prototype lifecycle stages, physical materials, digital platforms (TTS/Tabletopia/Screentop/Playingcards.io), print-and-play kits, iteration discipline |
| `board-game-playtesting` | Self/guided/blind test protocols, feedback instruments & question design, recruitment, session logging, statistical humility, kill criteria |
| `board-game-rules-writing` | Rulebook anatomy, teach order, terminology discipline, examples of play, player aids, iconography, edge cases, localization-ready writing, living FAQ |
| `board-game-manufacturing` | Component specs (cards/punchboard/minis/boxes), print file prep, manufacturers & quoting, MSRP≈5x landed-cost economics, MOQ, EN71/ASTM/CPSIA/GPSR compliance, freight & fulfillment |
| `board-game-publishing` | Licensing vs self-publishing vs work-for-hire, royalties & contracts, sell sheets, pitching etiquette, conventions, BGG & reviewer ecosystem, realistic designer economics |
| `board-game-crowdfunding` | Pre-launch funnel, funding-goal math, campaign page anatomy, pledge tiers, stretch goals, shipping/VAT/tariffs, pledge managers, fulfillment, post-campaign operations |
| `board-game-market-analysis` | Market sizing & segments, comparable-title method, pricing architecture, distribution margins, positioning statements, trend radar |
| `board-game-solo-coop-design` | Automa/AI opponent design (Automa Factory principles), upkeep budgets, difficulty dials & win-rate calibration, co-op structures, quarterbacking mitigation, loss-condition pacing |
| `board-game-accessibility` | Colorblind-safe palettes & double coding, vision/cognitive/physical/emotional access (Meeple Like Us framework), language independence, socioeconomic access, inclusive art & language |

Each skill is a directory with an always-loaded `SKILL.md` (core principles, procedures, key-number tables, pitfalls) plus deep `references/*.md` files loaded only when needed. Skills cross-reference each other for routing.

## How the skills are discovered

Skills live in **`.agents/skills/`** — the [Agent Skills](https://agentskills.io/specification) standard location — and load through three redundant mechanisms:

1. **Project auto-discovery** (no install): Pi discovers project `.agents/skills/` from the working directory through its ancestors, stopping at the repo root. Clone, `cd shelf-wars`, run `pi`. Other harnesses implementing the Agent Skills spec use the same location.
2. **Project settings** (belt and suspenders): `.pi/settings.json` explicitly declares the resource root for Pi versions/configurations where explicit resource lists are preferred:
   ```json
   { "skills": [".agents/skills"] }
   ```
3. **Package install**: `package.json` declares the same root for `pi install` (dot-prefixed roots must be listed directly, not found via glob):
   ```json
   "pi": { "skills": [".agents/skills"] }
   ```
   ```bash
   pi install git:github.com/<your-remote>/shelf-wars   # remote
   pi install ./path/to/shelf-wars                      # local checkout
   ```

**Project trust:** project `.agents/skills` and `.pi/settings.json` are trust-protected resources. On first interactive run in this repo, Pi prompts for project trust — approve it (and save the decision with `/trust`). Headless runs (`pi --print`, `--mode json/rpc`) cannot prompt: pass `--approve` or the skills are silently skipped. If you add or edit skills mid-session, run `/reload`.

Then use naturally ("help me balance my deck-builder", "write my rulebook", "plan my Kickstarter") or force with `/skill:board-game-math-balance`. Discovery is verified end-to-end: a natural request (no file paths) triggers the matching skill automatically.

## How this was built

Researched and authored by AI subagent fleets with adversarial review:

1. **Research** — 10 parallel agents ran multi-angle web research across the design domain (designer blogs, publisher resources, manufacturer guides, textbooks, BGG community, postmortems).
2. **Authoring** — 13 parallel agents each re-researched one subdomain and wrote a skill (13 `SKILL.md` + 35 reference files, ~6,200 lines).
3. **Adversarial review** — 6 critic agents attacked the collection: three fact-checkers verified ~100+ checkable claims against fresh sources; a coverage-gap analyst checked the lifecycle contract; a format critic validated the Agent Skills spec; a veteran-industry adversary hunted survivorship bias and outdated facts (e.g. adding EU GPSR compliance). Per-skill fixer agents then applied verified corrections.

Numeric folklore is flagged `[contested]` where sources disagree. `research/` holds the provenance: `skill-taxonomy.md` records the scope contract, and the `*.md` digests are the raw research notes the agents produced (kept for fact-check traceability; the skills themselves are the distilled product).

## Skill format

Follows the [Agent Skills specification](https://agentskills.io/specification). The repo is a standard Pi package (`package.json` with a `pi.skills` manifest pointing at `.agents/skills/`), installable via npm or git.
