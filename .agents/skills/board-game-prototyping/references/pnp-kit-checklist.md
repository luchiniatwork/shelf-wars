# Print-and-Play (PnP) & Remote Blind-Test Kit — Package Spec

Load this when packaging a print-and-play, a remote blind-test kit, or a reviewer/publisher prototype package. Session protocol, wave cadence, and feedback-form design live in `board-game-playtesting`; this file owns the *package*.

## Package contents checklist

- [ ] `rulebook.pdf` — near-final; blind testing tests the book as much as the game (Stegmaier: every tester question is a rulebook bug, even when the answer is in it). Authoring → `board-game-rules-writing`.
- [ ] `cards.pdf` — one deck per file or clearly sectioned; backs file if duplex.
- [ ] `board.pdf` — tiled for home printers with overlap/tape marks.
- [ ] `tokens.pdf` — counters, tiles, trackers.
- [ ] `player-aids.pdf` — reference cards; these do disproportionate work in unaided play.
- [ ] `README.txt/pdf` — assembly instructions + what testers must supply.
- [ ] `manifest.pdf` — component | qty | file | page — doubles as your pre-manufacturing estimation doc.
- [ ] `feedback form` — linked Google Form (or equivalent) with a **version field**.
- [ ] `changelog.txt` — one line per build.
- [ ] Version + date in the footer of EVERY pdf page; version in every filename.

## File specs (home-printer reality)

- PDF everywhere; 300 dpi at final size.
- **Dual paper sizes:** design text/rulebook pages to a ~190×260 mm safe area so one file prints correctly on both A4 and US Letter; card sheets deliberately exceed that height (see Card layout) since both papers are ≥279 mm tall. If layout still forces a choice, ship both variants.
- **Print at 100% / actual size** — never "fit to page" (scale drift breaks card sizes and sleeve fit). Put this instruction, verbatim, on page 1.
- **No bleed at home:** white gutters between cards, no edge-to-edge color — consumer printers can't print to the edge and cut errors expose neighbors. Bleed (3 mm) is for POD/manufacturing paths only.
- **Card layout:** 9 poker-size cards (63×88 mm) per page in a 3×3 grid with ~2 mm gutters — the community-standard PnP sheet. The block is ~193×268 mm: over the 260 mm safe-area height, it fits A4 (297 mm) comfortably but US Letter (279 mm) leaves only ~5–6 mm top/bottom margins — verify printer minimum margins, or fall back to 2×3 (6/page) for Letter-only kits. Compute other card sizes from this grid math, not the safe area.
- **Duplex backs:** verify flip-edge (long vs short) with one test sheet; symmetric backs survive sheet rotation.
- **Low-ink variant:** white backgrounds, no full-bleed panels, icons over art — testers' ink budgets gate participation.
- **Accessibility:** double-code (icon + color) everything color-only; colorblind-safe palettes → `board-game-accessibility`.

## Assembly instructions (write them for a stranger)

1. Print at 100%; check the printed 63×88 mm reference box with a ruler before printing all pages.
2. Cut order: sheets → strips → cards (trimmer recommended; scissors acceptable).
3. Sleeve option: paper inserts in opaque sleeves over backing cards (your testers who own sleeves get a shuffleable deck).
4. Boards: tile pages, tape back seams, fold.
5. **Tester-supplied items list** — be explicit: N× d6, pawns/meeples in N colors, ~40 cubes, scissors, tape, optional sleeves. If they'd need to buy it, redesign the kit or supply it.
6. Estimated assembly time (testers bail when "30 minutes" is actually 2 hours).

## Remote blind-test kit extras

- Written instructions up front: purpose = *test the rulebook*; no contacting the designer mid-game; if stuck, guess, note it, continue (MVP Board Games etiquette).
- One urgent-questions channel that does NOT become a FAQ crutch; log every question.
- Confidentiality expectations in one paragraph (no public posts/images without permission).
- Schedule expectation per Stegmaier's wave cadence: 3 sessions within 3 weeks; survey after each session; hold all reports until the wave closes (protocol detail → `board-game-playtesting`).
- Compensation/incentive stated up front (copy of the published game, credit, or payment).
- Optional 5–10 min setup video for complex setups; the rulebook must still stand alone.

## Distribution checklist

- [ ] Single zip: `GameName_v0.7.2_PnP_2025-03-04.zip`, plus a Drive/Dropbox folder for updates.
- [ ] Link tested in an incognito window (permissions!).
- [ ] Digital alternative offered (Screentop.gg / Playingcards.io / Tabletopia / TTS build — see `digital-platforms.md`) for testers who can't print.
- [ ] Tracking sheet: tester | date sent | version sent | feedback due | received (your own CRM; do not rely on memory).
- [ ] Version freeze for the duration of the wave — mid-wave edits produce multi-version garbage data.
- [ ] Confirmation the feedback form records version automatically or asks for it.

## Common PnP failure modes

- **Ink-hog design:** full-bleed art on 120 cards → nobody prints it. Low-ink variant is not optional.
- **Fit-to-page shrinkage:** cards at 94% don't fit sleeves; players trim to different sizes and decks become marked.
- **Silent scope:** tester discovers they need 60 cubes and 8 dice after printing; the supplies list belongs on page 1 of the README.
- **Assembly-time lie:** over ~45–60 min of cutting suppresses completion rates [community observation — no canonical study]; offer the digital build as the escape valve.
- **Rulebook as afterthought:** the kit's real test article is the book; a PnP wave with a draft-quality rulebook measures nothing.
