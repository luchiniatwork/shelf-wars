# Component Specs — Deep Reference

Load this when the user asks about any specific physical component. All dimensions metric-first. Sources: Panda GM Graphic Design Guidebook v4 (2022) & Component Guidebook, PrintNinja Printing Resource Center, James Mathe "10,000 Feet to Publishing a Board Game" (2013), League of Gamemakers real RFQ sheets, Stonemaier Games blog. Where a value is community convention rather than a manufacturer spec, it is marked.

---

## 1. Cards

### 1.1 Standard sizes

| Name | mm | inches | Cards per press sheet (Panda) | Typical use / exemplars |
|---|---|---|---|---|
| Poker (standard) | 63.5×88.9 | 2.5×3.5 | 54 | Default choice; Magic, most deck games |
| Bridge | 57×87 | 2.24×3.43 | 60 | Narrow hands (many cards held) |
| Tarot | 70×120 | 2.75×4.75 | — (PrintNinja menu) | Large art cards; tarot decks |
| Standard European ("euro") | 59×91 | 2.32×3.58 | 45 | FFG "Standard European" sleeve size |
| Mini European | 44×67 | 1.73×2.64 | 84 | FFG "Mini European"; compact decks |
| Mini American | 41×63 | 1.61×2.48 | — | FFG "Mini American" [secondary source — community/FFG nomenclature] |
| Mini square | 51×51 | 2×2 | 110 | |
| Square | 70×70 | 2.75×2.75 | 56 | |

- Mathe's shorthand: EURO family = 59×91 & 44×67; USA family = 63×88 & 57×87.
- PrintNinja customs: any size 1.5–6.9″.
- **Standard corner radius: 2.5mm** (Panda).
- **Press-sheet economy:** card counts near sheet multiples (54/45/84…) waste less paper and cost less. Design deck counts toward them.

### 1.2 Stocks & cores

| Stock | gsm | Notes |
|---|---|---|
| Blue core | 280 | Economy (PrintNinja); standard "casino-grade" feel |
| Coreless standard | 300 | |
| Black core | 310 | High opacity (no see-through at edges) |
| Black core plus | 330 | Max opacity (PrintNinja menu) |
| Coreless plus | 350 | |
| Ivory core | e.g. 350 | Chinese-printer jargon; premium |
| Grey core | — | The cheap default you get if you don't specify (Liminal via Stonemaier) |
| White PVC | 450 | Waterproof (PrintNinja) |

- Typical card stock: 275–300gsm multi-ply (Mathe); 300–310gsm is the common premium target.
- Colored cores (blue/black) prevent edge see-through; specify core AND gsm explicitly: "ivory core 350gsm, not grey core."

### 1.3 Finishes & coatings

- **Linen emboss** (crosshatch texture): Stegmaier recommends for cards, mats, boxes, boards — slides less, feels premium. Avoid only with tiny art detail or reflective foil.
- **Matte vs gloss lamination:** never glossy on boards/cards/mats — overhead-light glare (Stonemaier's original Tuscany mistake). Gloss is acceptable on box covers for shelf pop.
- **Special effects** (Panda): spot UV (raised shiny coating), metallic ink, foil stamping, emboss/deboss, scratch-off (legacy games). Each effect = separate file or layer in a single ink color.
- Varnish vs lamination: varnish is the cheaper baseline; lamination (matte/gloss film) is more durable and premium.
- "Border black" for card borders: C40 M0 Y0 K100 (Panda guidebook).

### 1.4 Deck file submission

- One multi-page PDF, fronts in order, common back as the last page. Multiple backs → separate fronts PDF and backs PDF (Panda).
- **Card backs must be rotationally symmetric** — sheets rotate 180° between copies in production, and asymmetric backs reveal it.
- Dielines/round-corner guides come from the manufacturer's template generator, never hand-drawn.

---

## 2. Punchboard & tokens

- **Thickness:** 1.5–2.5mm industry range. LoGM real spec: "60-pt chipboard" ≈1.5mm for mats/tokens. Linen finish typical (Mathe).
- **Geometry rules (Panda):**
  - Min token ~8×8mm; smallest edge of any shape ≥3mm.
  - ≥6mm between any two dielines.
  - Each token needs its own 3mm bleed + 3mm margin.
  - Board must be ≥15mm smaller in length & width than the box top.
  - "Whole board dieline" must match the contract size exactly.
- **Dielines = tooling:** submitted as a separate PDF or layer, never embedded in art layers (they drive the die-cut mold). Each unique die-cut layout = new tooling cost (~$300/die, Mathe 2013) → **reuse one dieline across multiple boards**.
- Label/number every board ("Board 1 of 3") for QC and collation.
- Front edges come out slightly rounded; **back art must be mirrored** relative to front.

## 3. Game boards

- 18mm wrap-around bleed on the front; double-sided boards: back 3mm smaller per side (Panda).
- Panda max board size: 700×1000mm.
- **Always print both sides** — single-sided boards warp (Mathe). Applies to player boards too.
- Folding boards are scored wraps over greyboard; more folds = more cost and warp risk.

## 4. Boxes

### 4.1 Construction

- Standard: two-piece telescoping box (top + bottom), printed wrap over **greyboard ~2mm** (Panda example template: 235×156×50mm in 2mm greyboard). 18mm bleed, 15mm wrap-around.
- **Size rule:** box ≥15mm larger in each dimension than the largest component — and no larger. Extra air = freight cost + component damage (top-to-bottom movement; inserts only help side-to-side — Stegmaier).
- ~50% of gamers discard expansion boxes (Stonemaier poll) — consider expansion content sized to fit the base-game box ("One Box to Rule Them All" argument).

### 4.2 Common retail box sizes (nominal, mm — verify against current SKUs)

| Approx. size | Class / exemplar |
|---|---|
| ~130×180×40 | Small card-game box |
| 235×156×50 | Panda template example (small-medium) |
| ~254×254×51 (10×10×2″) | Medium square family game |
| ~295×242×76 | Catan-class rectangle |
| ~296×296×72 | Ticket to Ride / Wingspan-class big square |
| ~370×300×98 | Scythe-class heavy box |

Publishers converge on a few shelf-friendly footprints; freight efficiency (cartons/pallet) matters more than matching an exact size.

### 4.3 Box-bottom markings checklist

- Player count, play time, age label.
- UPC/EAN barcode, pure black, +5mm clearance for lot number (GS1 barcode required by fulfillment/retail; hobby SKUs via HMA).
- Publisher address; EU requires a distributor address; UK requires distributor + importer.
- "Made in [country]" — customs requires country of origin on the box.
- 0–3 age-warning graphic if applicable (see compliance reference).

## 5. Wooden bits

- Standard sizes (LoGM real quote spec): cubes 8mm; meeples 16mm standard / 24mm large; discs 10/15mm. Standard bits range 8–20mm (Mathe).
- Cut methods: machine-cut or laser-cut from sheet wood/acrylic (acrylic slightly pricier).
- Decoration: paint, stains, ink washes, **silkscreen (screen print)** for flat faces, **laser engraving** (adds "deluxe" feel), heat transfer.
- Stegmaier: gamers prefer wood over plastic for meeples/custom resources; request rounded-corner dice; latex-free rubber bands.

## 6. Dice

- Custom molded dice rarely pay off below ~2,000 games (Mathe). Instead: silkscreen or heat-transfer on stock dice, or customize one face of resin dice to share molds.
- Engraved lines on custom dice/trays ≥3mm wide (Panda tray guidance, same principle).

## 7. Plastic miniatures

### 7.1 Materials

| Material | Type | Traits | Use |
|---|---|---|---|
| PVC | Soft plastic | Flexible; thin parts need ≥1.5mm sections | Mass-market minis, board-game standard |
| HIPS | Hard plastic | Crisp detail; thin sections ≥0.6mm diameter | Detailed minis |
| ABS | Hard plastic | Rigid, durable | Structural parts |
| POM / acrylic | Hard plastic | Specialty | Small precision parts |
| Resin | Cast | Low tooling cost, high per-unit, brittle | Small-run / hobby minis [community convention] |
| Metal | Cast | ≥0.2mm detail possible, heavy | Niche hobby |

### 7.2 Design rules (Panda Component Guidebook)

- Detail floor ≥0.4mm recommended (the eye resolves ~0.2mm; exaggerate facial features).
- Thin sections (weapons, tails): ≥0.6mm diameter hard plastics, ≥1.5mm PVC.
- **Avoid undercuts** — they force multi-part molds + factory assembly and blow budgets.
- Same sculpt in multiple colors = mold resets = cost; use stock snap bases (20/25/50mm).
- Submit STP/STEP (preferred) or STL.
- Pre-painted minis only economical >10,000 units.

### 7.3 Mold economics & timeline

- Steel injection mold: $3,000–5,000 setup per figure (Mathe 2013); "thousands per mold" is the consistent magnitude across sources.
- Cost estimate ~2 weeks per sculpt; optional 2–4 weeks optimization; plan **≥7 months extra** for custom plastics (Panda).

## 8. Trays & inserts

| Type | Notes |
|---|---|
| Vacuum-formed plastic | ~0.9mm thick, black default, optional clear lid; submit 2D/3D design + STP/STEP; engraved lines ≥3mm wide |
| Paper-pulp | Sustainable alternative; higher tooling cost, longer lead |
| Cardboard | Cheapest |

- Stegmaier: inserts help side-to-side movement, not top-to-bottom — minimize headroom.

## 9. Rulebooks (physical specs)

- **Saddle-stitch binding is the board-game default**; also perfect-bound, spiral, casewrap.
- **Page count must be a multiple of 4.** Submit single pages, no two-page spreads; larger gutter margin if 32+ pages.
- Paper: 100–150gsm, 4/4 CMYK (Mathe); layout/design $500–2,000 (2013).
- Size to the box: full-box booklets are unwieldy — Libertalia used 165×240mm deliberately smaller than its box (Stegmaier).
- No text rasterized into art — kills localization (Stegmaier). Localization = new plates; keep text on live layers.

## 10. Print-file prep master checklist (Panda "Basic Five" + extras)

1. PDFs. 2. CMYK only. 3. ≥300ppi. 4. ≥3mm bleed AND ≥3mm safe margin every side (18mm wrap on box/board fronts). 5. Black text pure K100, overprint.
6. Dielines separate (file or layer), from manufacturer templates. 7. Special-fx layers single-ink. 8. Trim tolerance ±1mm (Panda). 9. Cards as multi-page PDFs. 10. Rulebook pages multiple of 4.
