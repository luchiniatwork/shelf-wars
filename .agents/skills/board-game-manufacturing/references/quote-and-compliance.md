# Quote, Compliance & Freight — Deep Reference

Load when preparing an RFQ, comparing manufacturers, planning QC, doing compliance markings, or planning freight/fulfillment. Sources: Panda GM process & guidebooks, PrintNinja Resource Center, James Mathe (2013, via Wayback), League of Gamemakers ("Kickstarter Homework Lesson 1: Quotes and Setting Prices", Jeff Cornelius), Stonemaier Games blog, Wikipedia/USITC/CPSC for regulatory.

---

## 1. RFQ spec sheet (template)

Send to 3–10 manufacturers; request quotes at **3 run sizes (e.g., 1,500 / 2,000 / 3,000)**. Expect clarification questions; full quotes ~5–6 weeks (LoGM). Never let the printer assume — write "ivory core 350gsm, not grey core," "2.0mm greyboard box," exact Pantone C.

| Field | Spec to fill |
|---|---|
| Game title / SKU | |
| Box | Type (2-piece telescoping), dims L×W×H mm, greyboard mm, wrap finish, interior print? |
| Game board | Folded size, unfolded size, folds, paper gsm on greyboard, finish, double-sided (yes — always) |
| Cards | Per deck: count, size mm, stock (core + gsm), finish, corner radius, 4/4 or 4/1 color |
| Punchboards | Count, dims, thickness mm, finish, dieline reuse note |
| Wooden bits | Per item: shape, dims mm, color/finish (paint/silkscreen/engrave), qty/game |
| Dice | Size, material, stock vs custom faces, engraving/printing |
| Plastic minis | Sculpt count, material (PVC/HIPS/ABS), height, base type, STP/STEP files available? |
| Tray/insert | Vacuum-formed / pulp / cardboard; cavity sketch attached |
| Rulebook | Trim size, page count (multiple of 4), paper gsm, binding, 4/4 |
| Other | Bags, bands (latex-free), stickers, shrinkwrap, easy-peel request |
| Markings | Age label, CE/UKCA, UPC, country of origin, addresses |
| Quantities | 1,500 / 2,000 / 3,000 (or campaign-driven) |
| Terms | Incoterm (EXW/FOB/DDP), payment schedule, proof stages included, spare % |

Include diagrams/photos/renders for unusual parts (LoGM used SketchUp renders for a grooved 3-part track).

## 2. Manufacturers & brokers

| Company | Type / location | MOQ | Notes |
|---|---|---|---|
| Panda GM | Manufacturer (Canadian-owned, Shenzhen plant) | 1,500 | 400+ publishers, 57M+ games; factory reps on site; 6-step pipeline with PPC/MPC air-shipped free; template generator |
| LongPack Games | Manufacturer (Shanghai) | ~1,000–1,500 | Similar 6-step flow; mini painting tiers |
| Whatz Games | Manufacturer (China) | ~1,000–1,500 | Established board-game plant |
| PrintNinja | US-fronted broker, China offset | 500 decks | Instant online calculator; strong file-prep education |
| Ludo Fact | Manufacturer (Germany) | ask | EU production — tariff/lead-time hedge |
| Cartamundi | Manufacturer (Belgium) | ask | Playing-card giant |
| Hero Time | Manufacturer (China, Hersh Glueck) | ask | QC/communication-focused pitch |
| AdMagic | US front (uses MeiJia, China) | ask | Mathe's chart |
| BangWee / Wingo / GPI | China plants | 500 (BangWee) | Mathe's picks list; BangWee cheap but "wood & dice sub-par" |
| 360 Manufacturing | — | — | Mathe's chart warns: delays, errors |

Mathe's maintained "Hitchhiker's Guide to Game Manufacturers" chart (Wayback) is the canonical comparison; his picks: Panda, LongPack, Wingo, BangWee, GPI. Always get current quotes — MOQ is the most variable number in the industry.

## 3. Quote workflow, payment & vendor management

1. RFQ with full spec sheet → clarification questions → quotes at 3 quantities (~5–6 weeks total, LoGM).
2. Compare **total landed cost**: unit price + tooling (dies, molds, setup) + proofs + freight terms. EXW (factory door) ≠ FOB (on ship) ≠ DDP (delivered, duties paid).
3. Payment rhythm (Mathe): **50% down + setup fees; final bill before the printer ships.** Wire fees $20–40. Never 100% up front.
4. Vendor vetting (Liminal via Stonemaier): beware Yes-Men ("we can do anything") and Cool Chads (apathetic); video-call before committing; watch how they handle language misunderstandings; be hyper-specific; **consolidate changes** — weekly tweak-drips get you dropped; after calls, have the manufacturer summarize decisions by email.
5. Timeline reality (Mathe): full process ~1 year; production 60–90 days; ocean 21–30 days; +≥7 months if custom plastics (Panda).

## 4. Production pipeline & QC gates

Panda's 6-step pipeline (industry-representative):

1. **Quote** → 2. **Design Verification** (prepress; common failures: RGB, low-res, spot colors, dielines in art) → 3. **PPC** (pre-production copy: printed components air-shipped free + non-printed part samples, video-call review) → 4. **Mass Production + MPC** (first full copy incl. shrinkwrap — last checkpoint) → 5. **Assembly** (final QC; Panda promises 99% defect-free + free spare components) → 6. **Shipping**.

QC practices:
- Get a white-box/physical sample early (Mathe: FedEx $100–300, worth it).
- **Play the PPC** — color, cut alignment, token pop-out, card snap, box fit.
- Verify the MPC including shrinkwrap, collation, inserts, spares.
- Third-party pre-shipment inspection (SGS, QIMA, TÜV) against the approved PPC when no factory rep is on site. Mathe's horror stories: paper swapped for card stock to lower bids, misprints, QC staff writing on components.
- Contract for defect remedy and spare components up front.

## 5. Compliance matrix

| Market | Regime | What it requires |
|---|---|---|
| EU (toys) | Toy Safety Directive + **EN 71** (14 parts; 71-1 mechanical/physical, 71-2 flammability, 71-3 migration of elements; 71-6 age-warning symbols) | **CE mark** = manufacturer's self-declaration backed by test evidence (affixing non-compliantly is a criminal offence); Declaration of Conformity; a TSD **authorised representative** is optional; EU distributor address on box |
| EU (all consumer products, incl. non-toys) | **GPSR (EU 2023/988, in force 13 Dec 2024)** | Binds 14+ hobby games that fall outside the toy regime: mandatory EU-established **responsible economic operator** (manufacturer, importer, authorised representative, or fulfillment service provider) — name, postal + electronic address on product/packaging; traceability duties; accident/risk reporting via the **Safety Business Gateway** (see §8) |
| EU (toys, incoming) | **Toy Safety Regulation (TSR)** — adopted by Parliament 25 Nov 2025; replaces the Directive | Wider chemical bans (endocrine disruptors, PFAS), per-toy **digital product passport**; transition window (~4.5 years) before it applies — TSD/EN 71 remains the operative regime meanwhile [dates provisional — verify entry into force] |
| UK | UKCA (largely mirrors EN 71) | **CE alone is legal in GB indefinitely** — Product Safety and Metrology etc. (Amendment) Regulations 2024 extended CE recognition incl. the Toys (Safety) Regulations 2011; UKCA optional (sticky-label/importer flexibility); UK distributor + importer addresses |
| US | **ASTM F963** (toy standard) + **CPSIA** for children's products | "Children's product" = intended primarily for ≤12 years → mandatory third-party CPSC-accepted lab testing, Children's Product Certificate, tracking labels; lead ≤90ppm surface coatings, ≤100ppm substrate |
| Canada | CCPSA / Toys Regulations SOR-2011-17 | Bilingual labeling; similar testing expectations |

Key operational rules:
- **Age labeling drives the regime.** Industry standard for hobby games: 13+ / 14+. But CPSC judges intent by packaging, promotion, and common recognition — a label can't launder an obviously child-aimed product.
- Panda's guidance: games marked 13 and under may face customs/distributor demands for EN71/UKCA/ASTM F963 test results regardless of strict legal need. Mathe calls testing sold for adult hobby games "a racket" **[contested — his opinion; mandatory for children's products]**.
- Small-parts warnings: 0–3 symbol ≥10mm height, black/white/red, unaltered; warning triangle taller than the word "Warning". Approved texts: "Warning: Not suitable for children under 36 months" and "CHOKING HAZARD — Small parts. Not for children under 3 years."
- Manufacturers (Panda) can broker third-party testing, but **the publisher retains legal responsibility**.
- Box-bottom markings: player count, time, age, UPC (pure black, 5mm clearance for lot number), publisher/distributor/importer addresses, "Made in [country]".

## 6. Freight & customs

- **Sea LCL**: priced by volume (CBM), not weight — box size is the lever. **FCL**: flat per 20ft/40ft/40HC container. Mathe (2013): a $50 game × 2,000 units ≈ $3,000–4,000 China/Europe→warehouse + a few hundred in customs fees; 21–30 days ocean.
- **Air**: a multiple of sea cost; for samples, PPCs, emergency restocks only.
- **Pallet math**: Stegmaier's worked example — 48 cartons/pallet; 6 games/carton → $3.47/game freight vs 4/carton → $5.21 ($52,200 swing on 30,000 copies). Mathe: 300–600 games/pallet. Cartons/pallet depends on carton size — optimize carton dims with the factory.
- **HS codes**: US HTS **9504.90.60.00** "games played on boards of a special design" — base duty Free (0%). **2025 tariffs on China-made games moved 20% → 145% peak, settling at 30% after a 90-day pause** (Stegmaier's article used the 54% snapshot: ~$10M 2024 production spend → potential +$5M); charged on *manufacturing cost*, paid by the importer. Tariff legality was challenged in court, with a possible refund path for duties paid [volatile — verify current rates/status before committing landed costs]. Confirm EU classification/duty with your customs broker (TARIC).
- **Customs bond**: US formal entries (>$2,500) require one (single-entry or continuous); forwarders/brokers usually roll it in, but DIY first-timers hit it as a surprise cost (CBP entry rules).
- **Incoterms**: FOB common default; **DDP for the EU** so the VAT-inclusive price is final (Stonemaier). Use a customs broker/freight forwarder (ARC Global cited by Stonemaier).
- Tariff-chain math (Stonemaier 2025): pass-flat ($10→$15 production → MSRP $50→$55) vs full multiplier (→$75). Mitigations: regional manufacturing (Earthborne Rangers model), EU production (Ludo Fact).

## 7. Fulfillment & 3PL

- Regional picks (Stonemaier "Current State of Worldwide Fulfillment", 2024): US — Miniature Market, Fulfillrite, Quartermaster Logistics; EU — Spiral Galaxy (full-service VAT); Canada — Asmodee Canada; AU/NZ/Asia — Aetherworks.
- Factory pre-packing (game fully collated/shrunk) cuts fulfillment cost.
- GS1 barcodes required by fulfillment/retail; hobby SKUs via HMA. Keep SKU/add-on count low — per-item fees + mispicks.
- Latin America/Africa parcels unreliable → forwarders (Shipito, MyUS).
- Direct-sale baseline (Stonemaier 2025): $10 production vs $50 consumer price, minus ~$20 fulfillment subsidy; Stonemaier 2024 sales mix: ~55% distributors/retailers, just under 30% direct.

## 8. Recalls & incident reporting (post-market duties)

Market access is half the duty — a defect surfacing after shipping triggers affirmative reporting obligations.

- **EU — GPSR Arts. 19–20**: on a serious accident caused by the product, or on discovering a safety risk, economic operators must notify market-surveillance authorities via the **Safety Business Gateway**, cooperate on corrective action (withdrawal/recall), and inform affected consumers. Traceability duty: know who supplied you and who you supplied.
- **US — CPSA §15(b)**: a manufacturer, importer, or distributor must report to the CPSC **immediately** (within 24 hours) when a product fails to comply with an applicable rule/ban, contains a defect that could create a substantial product hazard, or creates an unreasonable risk of serious injury or death. Failure to report draws civil and potentially criminal penalties.
- **Prep before first shipment**: lot/batch identification (CPSIA tracking labels already required for children's products), retained PPC/MPC and inspection reports, a spare/replacement-parts channel, and a written recall plan with customer-contact paths.

## 9. Sustainability

- FSC-certified paper/wood available from major plants (Panda et al.) — request at RFQ.
- Paper-pulp trays instead of vacuum-formed plastic (higher tooling, longer lead).
- Plastic-free / reduced-plastic packaging increasingly demanded by backers and EU retailers; avoid PVC where a substitute exists.
- Right-size boxes (freight = volume = emissions), consolidate SKUs, include spare parts to reduce replacement shipments.
- Verify any specific sustainability claim (recycled content, "plastic-free") with the manufacturer in writing before marketing it.
