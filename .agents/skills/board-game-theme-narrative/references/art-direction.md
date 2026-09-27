# Art Direction — Deep Reference

Load when commissioning art, writing artist briefs or style guides, or budgeting illustration and graphic
design. Print-file technical specs (bleed, CMYK, DPI, dielines) belong to `board-game-manufacturing`; this
file covers the creative/commercial side.

## 1. Roles to staff (don't conflate them)

| Role | Owns | Notes |
|------|------|-------|
| **Illustrator** | Box cover, card/board art, world imagery | Paid per illustration type (see §4) |
| **Graphic designer** | Iconography, card layouts, rulebook layout, box layout, logo | Distinct discipline from illustration; Stegmaier treats them as separate hires (KS Lesson #3, "Art and Graphic Design") |
| **Art director** (often the publisher/designer at small scale) | Style guide, briefs, consistency across hundreds of pieces | On indie projects this is you; BGDL episodes: "Art Direction in Games with Nolan Nasser", "Scott Rogers on Tips and Tricks for Art Direction" |
| **Sculptor** | Miniatures, custom meeples | Stonemaier contracts cover "illustrations and sculpts big and small" |

Art *is* marketing: theme+hook sells the first copy (SKILL.md principle 1), and the box/cover is the hook's
largest surface. Stegmaier's named artist bench: Beth Sobel, Jacqui Davis, Jakub Rozalski, Mr Cuddington —
distinctive, consistent, box-forward styles.

## 2. Writing the brief (per piece or per batch)

Include, in this order:
1. **World summary** — 3–5 sentences: setting, mood, era, tech/magic level, tone references.
2. **Subject spec** — what is depicted, from what angle, doing what; in-world nouns only.
3. **Function in play** — where the piece appears (card that is read at distance? board space under player
   hands? box front on a shelf?) and what gameplay info must stay legible. Art must never fight usability
   (coordinate palettes/icons with `board-game-accessibility`).
4. **Style anchors** — 2–4 reference images or named works ("mood, not imitation"); point to the artist's
   own portfolio pieces you liked.
5. **Hard constraints** — dimensions/aspect, bleed and safe zones (from `board-game-manufacturing`),
   palette limits, anything that must NOT appear (IP conflicts, cultural sensitivities per consultant).
6. **Deliverables & milestones** — sketch → rough color → final, with the contract's revision stages
   (§3) mapped onto them.

## 3. Commissioning process (Stonemaier model — verified from the published template)

1. **Gauge interest & availability**; discuss the project.
2. **Provide a scope estimate** (rough counts per illustration type up front).
3. **Request 1–2 prepaid sample illustrations** specific to the game — "I prepay for these samples, and
   there is no further commitment in place at this time." This is the cheap test of fit.
4. **Share cost ranges per illustration type with total counts.** Leverage: "if you're paying an artist for
   several months' worth of work, that is often invaluable to them, as that's easier for them than finding a
   new project every week." Volume = negotiating value.
5. **Send a short, plain-language contract.** Verified Stonemaier terms:
   - **Ownership:** publisher owns all rights to product-specific illustrations — "they are the creator of
     that thing, but I am the owner of it." Missing ownership clauses "caused quite a bit of frustration."
     Expect some artists to decline work-for-hire ownership; respect it and decide.
   - **Artist's license back:** beginning no earlier than the game's **official announcement**, artist gets
     limited usage for self-promotion, personal display, and custom prints. Rationale: anti-spoiler timing.
   - **Duration/territory/media:** indefinite, worldwide, print and digital.
   - **Payment:** invoices paid on the artist's request/schedule for completed work ("whenever you ask me to
     pay you, I'll pay you right away"); rate is $X per "standard illustration," other types negotiated.
     Royalties only occasionally ("our margins are already very tight").
   - **Revisions:** up to **2 revision stages** per illustration; additional stages = additional fees; fixes
     to meet original spec are free. Publisher may have another artist perform revisions if necessary.
   - **Art book:** publisher holds first right of refusal; pays artist **10% royalty on revenue** if made.
   - **Derivative works:** **5% of revenue** from non-board-game uses (film/TV etc.), excluding digital ports
     of the game.
   - **Infringement:** artist indemnifies publisher; artist warrants originality and copyright compliance.

## 4. Budget ranges

| Item | Range | Source quality |
|------|-------|----------------|
| Total pre-revenue spend, premium title | $150,000 all-in for Wingspan (art + graphic design + manufacturing + freight) before Jan 2019 first sale | Verified (Stegmaier) |
| Card illustration | ~$50–$500+ per card, artist/scope dependent | [contested] community-quoted ranges |
| Box cover / key art | ~$1,000–$5,000+ | [contested] community-quoted ranges |
| Graphic design (full game) | commonly low-thousands USD for a midweight title | [contested] community-quoted |
| Cultural consultant | flat project fee; hire at final-files stage | process verified (§5 of resonance reference); fees vary |

Budget heuristics: card count × per-card rate dominates illustration cost — scope discipline (fewer unique
illustrations, smart reuse via graphic design) is the main lever. Get the total counts into the negotiation
early (process step 4).

## 5. Style guide contents (keep it short and visual)

- World pillars: 3–5 adjectives + 1 paragraph.
- Do/don't image board (mood, palette, lighting).
- Palette + typography locks (coordinate with accessibility palettes).
- Recurring motifs/icons and their meanings.
- Character/culture design rules from the cultural consultant (binding, not advisory).
- Named anti-references: styles you explicitly don't want.

## 6. Finding and selecting artists

- Portfolio hunt where board-game artists show work: ArtStation, Instagram, BGG game pages (artist credits),
  publisher art credits; Stegmaier maintains a public list ("200+ Artists and Graphic Designers Whose Work I
  Love").
- Select on *consistency and throughput* as much as peak quality: a 170-card game needs an artist who can
  hold a style across months of work.
- Test with the prepaid samples (§3 step 3) before committing the full scope.
- Never ask for free "spec" samples — prepaying is the industry norm and the reputational minimum.

## 7. Common commissioning failures

- **No ownership clause** → disputes when the game succeeds; fix contract first.
- **Art spoiled pre-announcement** → artist promo rights must start at announcement, not delivery.
- **Revision infinity** → cap at 2 stages, then paid; spec-misses free.
- **Scope creep without repricing** → illustration counts change = renegotiate totals, don't absorb silently.
- **Illustrator doing graphic design (or vice versa)** → different skills; budget both.
- **Art that breaks play** → illegible iconography, value-only color coding; loop in
  `board-game-accessibility` before final art lock.
