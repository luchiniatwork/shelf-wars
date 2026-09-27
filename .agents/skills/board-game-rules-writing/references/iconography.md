# Iconography, Card Layout & Information Hierarchy

Load this when designing icons, symbols, card layouts, player aids, or board visual hierarchy — or auditing a game's game-facing graphic communication. Palette-level colorblind work (specific safe color sets, simulation testing) belongs to `board-game-accessibility`; this file owns symbol *system* design.

## Icon system principles

1. **Icons compress, they don't encrypt.** An icon's job is to speed recognition of something the player already knows — not to replace teaching. If players must memorize an icon before it means anything, the icon is overhead (Selinker's *Gloria Mundi* failure: "one symbol cannot do the work of ten"). Stegmaier: prefer **text on cards** over icon combos; icons should need no appendix.
2. **Double-code everything color-dependent**: color + shape/pattern/text label, always (Brian Chandler, Colorblind Games). ~4.5% of players (8% of men, 0.5% of women — Colour Blind Awareness) cannot rely on hue.
3. **Rotationally readable**: cards get read upside-down across a table. ColorADD fails this — its blue and red symbols differ only by rotation (criticized by Colorblind Games); it is also proprietary and requires rote memorization.
4. **Budget the icon count.** Under ~6 icons: self-explanatory with first-use text. **10+ icons → full icon legend** on the rulebook's last page AND on every player aid (Meeple Mountain). Every icon in the legend gets a one-line text gloss.
5. **One icon = one meaning, system-wide.** No recycling a symbol for a different concept on a different component (Tweet's maxim applied visually).
6. **Text fallback**: if an icon needs a "see rulebook" marker, the icon system has failed — *Bang!*'s book icon is the canonical anti-pattern. Overflow text goes to an appendix (*Apiary*) or component backs (*Tokaido*), not to a decipherment step mid-turn.

Exemplars to study:
- *Tussie Mussie* — background patterns double-code suit color.
- *The Isle of Cats* — cat ear/tail feature shapes double-code color.
- *Fantastic Factories* — symbol + color pairing on dice and cards.
- ArtiSlime-style quadruple coding: color + component-color icons + written name + diagram dot.

## Card anatomy (Joseph Z. Chen, "Anatomy of a Card", 2017)

| Zone | Hand cards | Market/display cards | Tableau cards |
|---|---|---|---|
| Name | Top, largest text | Top, largest | Top or banner |
| Cost | **Top-left** — visible when the hand is fanned | **Bottom edge** — thumbs cover the bottom; cost is irrelevant once acquired (*Dominion*) | Top-left or banner |
| Effect text | Middle/bottom, readable in hand | Middle | Must be readable **from across the table** |
| Type signal | Color **and** icon/label (never color alone) | Same | Same |

- MTG's top-right mana cost is the deliberate outlier (playtested in *Future Sight* against a left-edge layout); do not copy it without a hand-fan test of your own.
- **Hand-visibility test**: fan 8 cards in one hand. Every piece of information needed for the play decision must survive the fan. Whatever is hidden moves to the top-left or gets cut from the decision.
- Keep per-card text under ~2 short sentences for gateway/family games; heavier games still cap effect text at what fits at 9–10 pt minimum on the card face.

## Readability specs (print-applied)

| Element | Standard | Source |
|---|---|---|
| Body text | ≥10 pt (heads 16 pt bold / sub-heads 12 pt); go larger, never smaller | Meeple Mountain practitioner template; "~9–10 pt minimum" folklore [contested] |
| Body font | Legible sans/serif (Calibri/Arial class); thematic fonts for headings only | Meeple Mountain, Unpub |
| Contrast | ≥4.5:1 body text; ≥3:1 large text (≥18 pt / 14 pt bold) and meaningful icons | WCAG 2.1 applied to print |
| Backgrounds | No critical text on busy art; solid or scrim panel behind rules text | Meeple Like Us teardown consensus |
| Distance text | Tableau/board text must survive the across-the-table test (~1 m); *Hanabi* teardown is the cautionary case | Meeple Like Us |
| Emphasis | Bold = key terms at first instance; italics = examples/notes; never underline; no all-caps runs (*Magic Realm* is the failure case) | Stonemaier Style Guide; Lim bold-first-instance compromise |

## Player aids (Board Game Business top-5, in priority order)

1. **Use symbols** (with a legend on the aid).
2. **Visually distinct** from the rulebook and from other aids — players grab the right sheet.
3. **White space** — an aid packed edge-to-edge reads as a wall.
4. **Max one double-sided card** per player.
5. **No walls of text** — fragments, arrows, and numbered sequences, not paragraphs.

Content: turn sequence (numbered), binding constraints ("once per turn", hand limits), icon glossary, scoring summary. The aid is a **reminder device for Backe's third audience (returning players)** — if it teaches, it's doing the rulebook's job badly.

## Information hierarchy on boards

- Most-used information biggest and highest-contrast (League of Gamemakers, prototyping graphic-design priorities — the same law applies to final boards).
- Track spaces, zones, and icon callouts get text labels at first use even when an icon is present.
- Board text follows the same rotation rule as icons: orient for the players who read it most, or make it readable from two sides.
- Setup diagrams in the rulebook must match the board's final art exactly — a diagram drawn from a prototype board is a blind-test failure generator.

## Audit checklist

- [ ] Every color-coded element also coded by shape/pattern/text?
- [ ] Every icon rotationally readable and unique system-wide?
- [ ] Icon count ≤9, or legend present in rulebook back matter + all aids?
- [ ] Hand-fan test passed on hand cards; across-the-table test passed on tableau/board text?
- [ ] Zero "see rulebook" icons; overflow text in appendix/component backs?
- [ ] Contrast ≥4.5:1 body, ≥3:1 icons; no rules text on busy, un-scrimmed art?
- [ ] Player aids: one per player, ≤1 double-sided card, turn sequence + constraints + legend present?
