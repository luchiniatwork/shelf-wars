---
name: board-game-manufacturing
description: >-
  Component specs, print-file prep, manufacturer quotes, costing, MOQ, compliance, freight and fulfillment for physically producing a board game. Use when the user says "manufacture my game", "get a quote from Panda GM / PrintNinja / LongPack", "what size should my cards / box be", "prepare print files (CMYK, bleed, 300dpi)", "how much does it cost to produce a board game", "MSRP multiplier", "MOQ", "EN71 / CE / ASTM F963 / CPSIA compliance", "age labeling", "sea freight / HS code / tariffs", "fulfillment or 3PL partner", or "plastic-free / FSC components". Covers card/punchboard/box specs, finishes, wooden bits, mini materials and mold costs, the proofing ladder (digital to PPC to MPC), the 5x MSRP heuristic, RFQ spec sheets, QC/inspection, and sustainability. For prototypes use board-game-prototyping; for campaign shipping/VAT/pledge managers use board-game-crowdfunding; for pricing vs comparables use board-game-market-analysis; for licensing/royalties use board-game-publishing.
---

# Board Game Manufacturing & Production

Manufacturing is where design decisions become irreversible tooling. Your job: specify everything, price from the distribution chain, size the box for the pallet, decide the age label deliberately, and climb every proofing gate before the boat sails.

## When to use / when not to use

Use this skill when the user needs to:
- Choose component specs: card sizes/stocks/finishes, punchboard, boards, boxes, wooden bits, dice, minis materials, trays, rulebook format.
- Prepare print files for a manufacturer (CMYK, bleed, dielines, resolution) or pass a prepress check.
- Build an RFQ/spec sheet, choose a manufacturer or broker (Panda GM, LongPack, Whatz, PrintNinja, Ludo Fact, Cartamundi), and interpret quotes/MOQs.
- Cost a game (landed cost, MSRP multiplier), plan proofing (digital → physical → PPC → MPC), QC and third-party inspection.
- Handle compliance (EN71/CE, UKCA, ASTM F963/CPSIA, GPSR, age labeling, small-parts warnings) or freight/customs/fulfillment (HS codes, FCL/LCL, 3PL, FSC/sustainability).

Do NOT use this skill for:
- Prototype-fidelity printing (The Game Crafter, PnP, sleeve inserts) → `board-game-prototyping`.
- Campaign logistics: pledge tiers, stretch goals, pledge managers, backer shipping/VAT → `board-game-crowdfunding`.
- MSRP positioning vs comparable titles, distribution economics → `board-game-market-analysis`.
- Licensing vs self-publishing, contracts, royalties → `board-game-publishing`.
- Rulebook content/teach → `board-game-rules-writing` (this skill covers rulebook *physical* specs only).

## Core principles

1. **Underspecification = cheapest default.** The modal failure is "I expected X, got Y" (Liminal via Stonemaier): unspecified card stock arrives grey-core, boards arrive thin. Specify every component in metric — dims, stock/gsm, finish, Pantone C where color-critical, qty — and never let the factory assume.
2. **Price from the chain, not from hope.** Stegmaier: MSRP = 5× manufacturing cost (benchmarked at the 5,000-unit price), adjusted for freight, royalties, discounts. Mathe: 5–6× *landed* cost. Distribution baseline (Stegmaier 2025): $10 production → distributor pays $20 → retailer pays $25 → consumer pays $50. [Sources agree on magnitude, disagree on base — see Key numbers.]
3. **Design the box for the pallet.** Sea freight prices by volume, not weight. Stegmaier: 48 cartons/pallet at 6 games/carton vs 4 → $3.47 vs $5.21 freight per game — $52,200 over 30,000 copies. Box = largest component + ~15mm in each dimension, and no larger; oversized boxes also increase component damage (top-to-bottom movement).
4. **Run size picks the print method.** Digital/POD 1–500; sheet-fed offset ~250–10,000 (PrintNinja: "short or mid-range runs"); web offset 10,000+. Consolidated Chinese plants (Panda, LongPack, Whatz): MOQ typically 1,000–1,500. First print run: 1,500–2,500 copies (Mathe; of 80 new products through his fulfillment house in 2012, only 22 sold >500 retail units).
5. **The age label is a regulatory decision, not marketing.** CPSIA: a "children's product" is one intended primarily for ≤12 years → mandatory third-party lab testing, tracking labels, Children's Product Certificates. Hence the industry-standard 13+/14+ label on hobby games. But a label can't launder an obviously child-aimed product — CPSC judges packaging, promotion, and common recognition.
6. **Dielines are tooling.** Each unique die-cut = a new die (~$300/punch die, Mathe 2013). Reuse one dieline across every punchboard; submit dielines as a separate PDF or layer, never embedded in art (they drive the cutting mold).
7. **Climb the whole proofing ladder.** Digital/prepress proof → physical "white box" sample → Pre-Production Copy (PPC) → Mass-Production Copy (MPC, first fully finished copy incl. shrinkwrap — the last checkpoint). Play the PPC like a customer. Every skipped gate is a defect discovered after freight.
8. **Print files obey the Basic Five (Panda Graphic Design Guidebook):** (1) PDFs, (2) CMYK only — never RGB, (3) ≥300 ppi, (4) ≥3mm bleed AND ≥3mm safe margin on every side, (5) black text in pure black (C0 M0 Y0 K100) set to overprint — rich black misregisters thin text. Most prepress rejections: RGB art, low-res images, spot colors, dielines in art layers.
9. **Payment follows risk (Mathe):** 50% down + setup fees, balance due before the printer ships. Never 100% up front. Wire fees ~$20–40.
10. **QC is contractual, not hoped for.** Panda's model: factory reps on site, 99% defect-free promise, spare components included free. On any plant, commission third-party inspection (SGS, QIMA, TÜV) for runs you can't babysit — pre-shipment, against an approved-sample standard.
11. **Consolidate communication with the factory.** Video-call before committing; beware Yes-Men ("we can do anything") and Cool Chads (apathetic) (Liminal). Batch changes — weekly tweak-drips get you deprioritized. After every call, have the manufacturer email a written summary of decisions.
12. **Sustainability is a spec, not a vibe.** FSC-certified paper/wood, paper-pulp trays, reduced/plastic-free packaging are increasingly demanded by backers and EU retailers — and must be requested at RFQ time, not retrofitted.

## How to apply it

### A. Fix the component manifest first

Build the manifest before any quote: item | dims (mm) | stock/gsm | finish | colors (Pantone C if critical) | qty/game | per-player scaling. Default picks when the user has no constraints:

| Component | Default spec | Notes |
|---|---|---|
| Cards | Poker 63.5×88.9mm, 300–310gsm black core, linen finish, 2.5mm corner radius | 54/press sheet (Panda) — counts near sheet multiples cost less |
| Punchboard | 1.5–2.5mm, linen finish; tokens ≥8×8mm, ≥6mm between dielines | Board ≤ box −15mm; reuse one dieline |
| Box | 2-piece telescoping, 2mm greyboard, matte lamination | Largest component + ~15mm; freight-sized |
| Wooden bits | 8mm cubes, 16mm meeples, screen print or laser engrave | Wood preferred over plastic for meeples (Stegmaier) |
| Minis | PVC (soft) or HIPS/ABS (hard); detail ≥0.4mm | Steel molds $3,000–5,000 each (Mathe 2013) — avoid unless justified |
| Rulebook | Saddle-stitched, 100–150gsm, page count multiple of 4 | Sized to fit box (or deliberately smaller, e.g., Libertalia 165×240mm) |

Full tables (all card sizes, cores, finishes, minis materials, box sizes, tray options): load `references/component-specs.md`.

### B. Prepare print files (prepress checklist)

1. Get the manufacturer's **own dielines/templates** (Panda has a template generator) — never hand-draw dielines.
2. Export PDFs, CMYK, ≥300ppi, 3mm bleed + 3mm margin everywhere; box/board fronts need 18mm wrap-around bleed.
3. Text: pure black K100 overprint; no text rasterized into art (kills localization — Stegmaier).
4. Dielines and special-fx (spot UV, foil, emboss) as separate single-ink files/layers.
5. Cards: one multi-page PDF, fronts in order, common back last; multiple backs → separate fronts/backs PDFs. Card backs must be rotationally symmetric (sheets rotate 180° across copies).
6. Rulebook PDF: single pages (no two-page spreads), page count multiple of 4, larger gutter if 32+ pages.
7. Pantone spot colors only where color-critical (they add cost); everything else process CMYK.

### C. Get quotes (RFQ process)

1. Send the complete spec sheet to 3–10 manufacturers/brokers; ask for **3 run sizes** (e.g., 1,500 / 2,000 / 3,000). Expect clarification questions; full quotes take ~5–6 weeks (League of Gamemakers).
2. Compare on total landed cost, not unit price: add tooling, setup, proofs, freight terms (EXW vs FOB vs DDP).
3. Vet the vendor (video call, written summaries, reference publishers). Never accept "we can do anything."
4. Spec sheet template + manufacturer/broker comparison + payment terms: load `references/quote-and-compliance.md`.

### D. Cost and price (worked example, Stegmaier 2022)

Tuscany expansion: manufacturing $6.50 → 5× = $32.50; freight $3/unit → landed $9.50 → MSRP bumped to $35. Distributors buy at 60% off ($14) → $4.50/unit profit over $9.50 landed — not sustainable alone; direct/webstore margins carry the difference. If freight is heavy, use 6–8× on manufacturing or 5× on landed instead.

### E. Run the proofing gates

| Gate | What it is | Your job |
|---|---|---|
| Design verification | Manufacturer prepress check | Fix RGB/low-res/spot-color/dieline-in-art rejections |
| Physical / white-box sample | Unprinted-structure or digital proof copy, FedEx ~$100–300 (Mathe) | Verify size, construction, component fit — worth it |
| PPC | Near-final printed components, air-shipped (free from Panda) + samples of non-printed parts | Play it fully; check color, finish, cut alignment, token pop-out |
| MPC | First full mass-production copy incl. shrinkwrap | Last checkpoint — verify assembly, inserts, spares |

### F. Compliance (decision tree)

1. **Markets first**: US? EU? UK? Canada? Each adds markings; decide before box art is final.
2. **Age label**: genuinely for kids ≤12 (US) → CPSIA third-party testing regime. Hobby game → 13+/14+ label and ASTM F963/EN71 testing is customary for retail/distributor acceptance even when not legally mandated [contested: Mathe calls printer-sold testing for adult games "a racket"; legally mandatory only for children's products].
3. **EU (toys)**: EN 71 (71-1 mechanical, 71-2 flammability, 71-3 element migration) under the Toy Safety Directive; CE mark with Declaration of Conformity (manufacturer's self-declaration backed by test evidence; a TSD authorised representative is optional); EU distributor address on box. **UK**: CE suffices indefinitely in GB (2024 regulations extended CE recognition incl. the Toys (Safety) Regulations 2011); UKCA optional. **US**: ASTM F963 + CPSIA for children's products (lead ≤90ppm coatings, ≤100ppm substrate, tracking labels, CPC).
4. **GPSR covers non-toys too (EU)**: GPSR (EU 2023/988, in force Dec 2024) binds ALL consumer products — hardest for 14+ hobby games that fall outside the toy regime: an EU-established responsible economic operator (manufacturer, importer, or authorised representative) with name/address on product or packaging is mandatory before sale.
5. **Small parts**: 0–3 age-warning symbol ≥10mm, unaltered colors; approved text: "Warning: Not suitable for children under 36 months" / "CHOKING HAZARD — Small parts. Not for children under 3 years."
6. **Box bottom markings**: player count, time, age, UPC (pure black + 5mm clearance), publisher + distributor/importer addresses, "Made in [country]" (customs requires origin).

Full compliance matrix, GPSR/recall duties, marking rules, and testing workflow: `references/quote-and-compliance.md`.

### G. Freight & fulfillment (quick path)

- Sea LCL (priced by volume/CBM) for <~half a container; FCL flat per container; air only for samples/PPCs and emergency restocks (a multiple of sea cost). Ocean transit China→US/EU ~21–30 days port-to-port (Mathe).
- US HTS 9504.90.60.00 "games played on boards of a special design" — base duty 0%. **2025 tariffs on China-made games moved 20% → 145% peak, settling at 30% after a 90-day pause** (Stegmaier's worked math used the 54% snapshot: ~$10M production → +$5M exposure). Charged on manufacturing cost, paid by the importer; tariff legality was challenged in court, with a possible refund path for duties paid [volatile — verify current rates/status before quoting landed cost].
- Incoterms: FOB is the common default; DDP for EU so the VAT-inclusive price is final (Stonemaier).
- 3PL by region (Stonemaier 2024): US — Miniature Market, Fulfillrite, Quartermaster; EU — Spiral Galaxy; Canada — Asmodee Canada; AU/NZ/Asia — Aetherworks. Factory pre-packing cuts fulfillment cost; keep SKU count low (per-item fees + mispicks).

### H. Production QC

- Contract for spare components and a defect remedy; Panda promises 99% defect-free + free spares.
- Third-party pre-shipment inspection (SGS, QIMA, TÜV) against the approved PPC, especially without factory reps on site.
- Print both sides of player boards (one-sided boards warp — Mathe); air holes in bags; easy-peel shrink; label/number punchboards.

## Key numbers & heuristics

| Value | Heuristic | Source |
|---|---|---|
| 5× | MSRP ≈ 5× manufacturing cost (benchmarked at 5,000 units), adjusted | Stegmaier 2022 [contested base: Mathe multiplies *landed* cost ×5–6; Stegmaier allows 6–8× manufacturing or 5× landed] |
| $10→$20→$25→$50 | Production → distributor → retailer → MSRP chain | Stegmaier, "The Math of Tariffs" 2025 |
| 60–65% / ~50% | Distributor discount off MSRP / direct-retailer discount | Stegmaier 2022; Mathe 2013 |
| 1,000–1,500 | Typical MOQ, consolidated Chinese plants | Panda (1,500), LoGM |
| 500 | PrintNinja MOQ (decks); offset sensible from ~250 sheet-fed | PrintNinja |
| 1,500–2,500 | First print run ceiling — don't be talked into more | Mathe 2013 |
| 63.5×88.9mm / 70×120mm | Poker / tarot card sizes | PrintNinja |
| 54 / 45 / 84 | Cards per press sheet: poker 63×88 / euro 59×91 / mini 44×67 | Panda GM |
| 280–310gsm | Card stock: blue core 280 (economy) → black core 310–330 (max opacity) | PrintNinja |
| 1.5–2.5mm | Punchboard thickness range (60pt chipboard ≈1.5mm; box greyboard ~2mm) | LoGM, Panda, Mathe |
| 3mm / 3mm / 300ppi | Bleed / safe margin / resolution, all print files | Panda Basic Five |
| 18mm / 15mm | Wrap-around bleed on box & board fronts / box wrap | Panda |
| 8×8mm / 6mm | Min token size / min gap between dielines | Panda |
| $300 / $3,000–5,000 | Punch die / plastic mini steel mold (2013 dollars; magnitude "thousands per mold" is consistent) | Mathe 2013 |
| >10,000 units | Pre-painted minis become economical | Panda |
| ≥7 months | Extra timeline for custom plastics | Panda |
| 50% + balance | Deposit + setup fees; balance before shipment; wire $20–40 | Mathe 2013 |
| 5–6 weeks | Quote turnaround; request 3 quantities | LoGM (Cornelius) |
| 60–90 days / 21–30 days | Mass production / ocean transit | Mathe 2013 |
| 48 cartons/pallet | Stegmaier's freight worked example; $3.47 vs $5.21/game at 6 vs 4 games/carton | Stegmaier [cartons/pallet varies with carton size; Mathe: 300–600 games/pallet] |
| 0% + 30% (post-pause 2025) | US base duty for HTS 9504.90.60.00 + 2025 China tariff: 20%→145% peak→30% after 90-day pause (Stegmaier's article used the 54% snapshot) | USITC HTS; Stegmaier 2025 [volatile — verify current rates] |
| ≤12 years / 90ppm / 100ppm | CPSIA "children's product" threshold; lead limits coatings/substrate | CPSIA (2008) |
| Multiple of 4 | Rulebook page count; saddle-stitch default | Mathe; Panda |
| 22 of 80 | New products (2012, Mathe's fulfillment house) that sold >500 retail units | Mathe, "Board Games by the Numbers" |

## Common pitfalls

- **Grey-core surprise**: underspecified stock → factory ships the cheap default. Specify "ivory/black core, exact gsm" (Liminal).
- **Prepress rejection loop**: RGB, <300ppi, spot colors, dielines embedded in art (Panda's most common design-verification failures).
- **Glossy boards/cards**: overhead-light glare at the table — Stonemaier's original Tuscany mistake. Matte or linen for play surfaces; never gloss.
- **One-sided player boards warp** (Mathe). Always print both sides.
- **Asymmetric card backs** reveal 180° sheet rotation between copies — design rotationally symmetric backs.
- **Dieline sprawl**: every unique die-cut is new tooling; reuse one dieline across all boards.
- **Minis undercuts & multi-color sculpts**: undercuts force multi-part molds + factory assembly; color variants = mold resets. Avoid undercuts; use stock snap bases; exaggerate facial features (min detail ~0.4mm).
- **Oversized boxes**: freight bleed ($1.74/game swing) plus more component damage; ~50% of gamers discard expansion boxes anyway (Stonemaier poll).
- **Change-drips**: weekly tweaks → manufacturer disengages. Batch changes into consolidated revisions.
- **SKU sprawl**: add-ons/variants multiply fulfillment errors and per-item fees.
- **Testing upsell confusion**: paying for lab tests on an adult hobby game that doesn't legally need them [contested — Mathe: "a racket"; distributors/customs may still demand EN71/ASTM results for ≤13 labels].
- **Run-size errors**: overprinting burns cash (Mathe's 22/80 stat); underprinting starves evergreen demand (Wingspan 25th printing, Scythe 28th).
- **Tariff/geopolitical exposure**: China-centric production faced 2025 US tariffs swinging 20%→145%→30% within months; mitigations: regional manufacturing, EU production (Ludo Fact), pass-flat pricing (Stegmaier).
- **Origin/marking omissions**: no "Made in" line, missing EU distributor address, altered 0–3 warning graphic → customs holds and retail rejection.

## Reference files

- `references/component-specs.md` — Load when the user asks about ANY specific component: all card sizes with press-sheet counts, core/stock/finish menu, punchboard & dieline rules, board construction, standard box sizes with exemplars, wooden bits, dice, minis materials (PVC/HIPS/ABS/resin) with mold economics, trays/inserts, rulebook physical specs.
- `references/quote-and-compliance.md` — Load when preparing an RFQ/quote comparison, choosing a manufacturer or broker, planning QC/inspection, doing compliance markings & GPSR/recall duties (EU/UK/US/Canada), or planning freight/customs/fulfillment/sustainability. Includes the fill-in spec-sheet template.

## Related skills

- `board-game-prototyping` — prototype-fidelity builds, POD, PnP kits, component-count estimation before manufacturing.
- `board-game-crowdfunding` — funding-goal math, stretch goals, pledge managers, backer shipping/VAT/tariff handling.
- `board-game-market-analysis` — comparable-title pricing, positioning, distribution economics.
- `board-game-publishing` — licensing vs self-publishing, contracts, royalties, conventions.
- `board-game-rules-writing` — rulebook content and teach (this skill covers only its physical specs).
- `board-game-accessibility` — component legibility, double coding, language independence that survive manufacturing.
- `board-game-theme-narrative` — art direction that must survive CMYK, Pantone, and localization constraints.
