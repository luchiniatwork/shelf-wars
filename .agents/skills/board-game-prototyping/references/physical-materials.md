# Physical Materials, Pipelines & Estimation — Deep Reference

Load this when buying or building physical prototypes, setting up a data-merge card pipeline, estimating component quantities before manufacturing, or setting up versioning/changelog discipline.

## Bill of materials & costs (community cost guides; verify current prices)

| Item | Approx. cost | Use |
|---|---|---|
| Index cards | ~$3/100 (~$10/1000) | Stage-1 cards; counters |
| Full-sheet label paper | ~$10–15/100 sheets | Boards on chipboard; tiles; repositionable (low-tack) elements |
| Opaque card sleeves (Dragon Shield Matte, UltraPro, KMC) | ~$5–10/100 | The stage-2 workhorse; avoid penny sleeves (rip mid-shuffle) |
| Backing cards | ~$0 | Old MTG/CCG commons or poster board inside sleeves for stiffness |
| Bulk wooden meeples | ~$10/100 (10 colors) | Pawns, workers |
| Bulk d6 | ~$10–15/100 | Dice, counters, cubes-substitute |
| Polyhedral dice sets | ~$10 for ~7 sets | Special dice needs |
| Wooden cubes/discs | a few $/bag | Resources, trackers |
| Personal paper trimmer (scrapbooking aisle) | ~$20 | Cutting hundreds of cards without scissor-cramp |
| Cutterpillar trimmer | ~$30–60 | Stegmaier's card-cutting tool |
| Chipboard 0.022–0.030″ | a few $/sheet | Board/tile backing under label paper |
| Bead-organizer bit box | ~$5–15 | Sorted cubes/pawns/tokens (Whirling Derby, LoGM) |
| Blank game boards / education-store stock | varies | Boards + Unifix cubes, fake money, lamination |

Free bits: cannibalize thrift-store and failed-prototype games. Keep everything — prototypes are iterative, parts are permanent infrastructure.

## Build recipes by component

**Cards — three levels:**
1. *Index-card scrawl* (stage 1): marker on index card; sleeve optional. Change = cross out.
2. *Sleeve + insert* (stages 2–3): print inserts on plain paper → cut → insert into opaque sleeve over a backing card. Shuffleable, durable, opaque, and a content change costs one reprinted sheet (Whirling Derby, LoGM).
3. *Print-on-demand* (stage 3–4): The Game Crafter (US) or MakePlayingCards — documented cases: Stones of Fate full prototype ~$16, deck-only less (Luke Laurie); Energy Empire ~$60–70/copy at ~500 components; Campaign Trail 9 copies at $80. Glossy POD copies measurably help games get noticed at cons (Laurie) — but only after counts stabilize, or POD cost punishes iteration.

**Boards:**
- *Cardstock + scotch tape* (LoGM method): print in letter-size panels, tape the back seams so it folds — fully usable for dozens of tests, cheap to reprint weekly.
- *Label paper on chipboard* (stage 3+): full-sheet label on 0.022–0.030″ chipboard; feels like a real board.
- *Blank board + low-tack labels*: reposition elements without reprinting the board.

**Tiles/tokens:** label paper on chipboard, cut with the trimmer; keep tokens ≥10 mm (manufacturing floor commonly quoted as ~8×8 mm with ≥6 mm dieline gaps, attributed to Panda GM [unverified — no citable spec sheet] — prototype inside final constraints or you'll redesign later).

**Boxes (con stage):** Vaughan's stage-3 audience expects a box; a labeled white mailer or DIY chipboard box suffices (LoGM has a DIY prototype-box guide).

## Data-merge pipelines (the iteration engine)

**Spreadsheet schema (single source of truth):** one row per card; columns at minimum: `id, name, deck/type, cost, rules_text, flavor, icon, art_ref, count, version, status`. Component manifest (non-card items) lives in a second sheet of the SAME file so content and counts version together.

| Tool | Cost | Strengths | Notes |
|---|---|---|---|
| nanDECK | Free | CSV-driven scripting; exports print PDFs; direct TTS save export (DECK directive); command-line builds | Windows-native (runs under Wine elsewhere); steepest learning curve, most power |
| Component.Studio | ~$9.99/mo at research time | Google Sheets → components in browser; pushes to The Game Crafter and TTS; PnP PDF export | Subscription; fastest for non-programmers |
| Inkscape | Free | Vector design; extensions for card sheets | Manual merge; pair with a script for large decks |
| Affinity Designer + Publisher | One-time purchase | Publisher's data merge → print-ready files | Stegmaier-equivalent pro route without Adobe subscription |
| Adobe InDesign | Subscription | Stegmaier's own pipeline (with HP color laser + Cutterpillar) | Overkill unless already owned |

**Print specs for home/POD prototypes:** 300 dpi; design with ~2–3 mm bleed only when the print path supports it — for home printers use *white gutters between cards and NO bleed* so cutting errors don't expose adjacent cards; 300 gsm cardstock if the printer feeds it; duplex card backs: print one test sheet first and check flip-edge alignment (long-edge vs short-edge) before printing 20 pages wrong.

## Component quantity estimation (pre-manufacturing)

1. **Manifest worksheet:** item | dimensions | qty per game | per-player scaling rule | max simultaneous need | sheet/pack source.
2. **Card math:** group by deck and size. Press-sheet check (Panda GM): 63×88 mm poker = 54/sheet; 44×67 mm mini = 84/sheet. Totals near sheet multiples are cheaper at manufacturing; a 55-card poker deck costs a second sheet.
3. **Bits formula:** (max simultaneous need per player × max player count) + ~10% spares. Example: 12 wood cubes/player at 5p → 60 + 6 = 66.
4. **Per-player scaling rule:** write it now (e.g., "remove 8 cards per missing player below 4p") — player-count scaling is the classic thing prototypes forget and playtests expose (auction/bidding/deduction games notoriously break at 2p — Caputo).
5. **Footprint sanity:** sum the laid-out area of board + player boards + market rows; if a 4p layout needs > ~90×120 cm, expect table-fit complaints from testers in small apartments.
6. Defer final specs, quotes, MOQ, and compliance to `board-game-manufacturing`.

## Versioning & change discipline

**Scheme:** `vMAJOR.MINOR.PATCH` — MAJOR: system/mechanism change; MINOR: content/balance change; PATCH: text/clarity fix. Stage-1/2 builds churn MAJOR freely; from stage 3, one MAJOR or MINOR system per build.

**Changelog entry (one line per build):**
`v0.7.2 | 2025-03-04 | hypothesis: 4p downtime too high | changed: simultaneous reveal for market phase (was clockwise) | result: downtime cut ~40%, kingmaker risk appeared → watch next 3 sessions`

**File naming:** `GameName_v0.7.2_cards_2025-03-04.pdf` — version AND date, always; archives never deleted (you will revert).

**Branch rule:** the build a publisher/reviewer/blind wave is evaluating is frozen; iterate on a copy (MVP Board Games). Merge learnings only after their evaluation closes.

**Manifest sync:** every build that changes component counts updates the manifest in the same commit/edit; the manifest is the source for eventual manufacturing quotes.

**Kill/hibernate rule:** keep a one-line "why we stopped" note when shelving a prototype — resurrected projects with no autopsy repeat their death.
