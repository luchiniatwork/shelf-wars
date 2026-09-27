# Pricing & Margin Economics

Load this file when pricing anything (MSRP, KS reward, webstore), modeling channel revenue, or deciding distribution vs direct vs crowdfunding. Every table cites its source; figures marked [contested] or hearsay are directional only.

## 1. The distribution chain (Stegmaier, "The Math of Tariffs", April 2025)

Baseline for a $50-MSRP game, per unit:

| Node | Pays | Receives | Keeps (gross) | Why |
|---|---|---|---|---|
| Manufacturer | — | $10 from publisher | production margin | China consolidated plants (Panda, LongPack) |
| Publisher | $10 production | $20 from distributor | ~$10 before freight/royalty/sunk costs | Funds reprint, art amortization, salaries |
| Distributor | $20 | $25 from retailer | ~$5 | Warehousing, sales force, retailer net-terms risk |
| Retailer | $25 | $50 from customer | ~$25 gross → single digits net | Pre-paid shelf inventory risk, rent, staff, discount headroom |
| Customer | $50 (MSRP) | the game | — | Street price often 15-25% below MSRP |

Rules derived from the chain:
- Publisher revenue in distribution ≈ **35-40% of MSRP** (distributor discount 60-65%; direct-retailer discount 45-50% — Stegmaier 2022).
- Retailer's 2× markup is structural, not greed: $1,000 of capital stocks 40 games at $25 and returns $2,000 only if *all* sell (Stegmaier 2025). Tariffs/cost rises erode this arithmetic immediately.
- If your landed cost forces MSRP above the comp cluster's ceiling, the game cannot enter distribution — change components or change channel; do not "price it anyway".

## 2. Margin comparison by channel (per $50 list price, $10 production, $2.50 freight)

| Channel | Buyer pays | Publisher gross per unit | Costs still owed | Notes |
|---|---|---|---|---|
| Distribution | $50 | ~$20 (60% off) | landed $12.50, royalty, sunk | Volume channel; evergreen reach; publisher profit ≈ $5-7.50/unit |
| Direct retailer | $50 | ~$25-27.50 (45-50% off) | landed $12.50, royalty | Few retailers buy direct; usually needs free shipping |
| Webstore direct | $50 (+shipping) | ~$50 minus fulfillment | fulfillment ~$20 real vs ~$10 charged (Stegmaier 2025), platform fees, payment ~3% | Tuscany example: $14/unit webstore profit vs $4.50 via distribution (Stegmaier 2022) |
| Crowdfunding | ~$39-45 (KS price, $50-MSRP game) | pledge − ~8-10% fees [community consensus] | landed, fulfillment subsidy, pledge-manager fees | Funds the print run itself; see §4 |
| Convention/direct sales | $40-50 | full price | booth cost, travel, stock hauling | Marketing as much as margin |

Channel reality check (Stonemaier 2024 actuals): ~55% of sales through distribution/retail, <30% direct, remainder localization partners; 58% of their survey respondents buy primarily from retailers; Wingspan sold >90% of units via distribution. Direct-only strategies forfeit this volume — that is a valid choice (CMON/Awaken Realms prove crowdfunding-native works) but must be chosen with open eyes.

## 3. The MSRP multiplier rules [sources agree on magnitude, disagree on base]

| Rule | Formula | Source |
|---|---|---|
| Stegmaier | MSRP ≈ 5× manufacturing (at 5,000-unit cost), then adjust for freight, royalties, discounts; 6-8× when freight-heavy | 2022 |
| Mathe | MSRP = (total printing + shipping + fees ÷ units) × 5-6 — i.e., 5-6× *landed* | 2013 |
| Hoyt (Foxtrot) | MSRP ≥ 5× landed cost to sell through distribution and fund a reprint | 2016 |

Recoup math at the 5× rule (Hoyt 2016):
- Sell ~50% of the print run → recoup costs.
- Sell out → nearly double your money → *just* funds the reprint (this is the treadmill, not profit).
- At ~4.16× manufacturing (ignoring freight): ~84% sell-through needed to recoup; "very few games sell 16,000 copies."

Worked example (Stegmaier 2022, Tuscany expansion): manufacturing $6.50 → ×5 = $32.50; freight $3/unit → landed $9.50 → MSRP raised to $35. Distributor buys at 60% off ($14) → $14 − $9.50 landed = $4.50/unit publisher profit — not sustainable alone (can't fund a reprint unit); webstore/direct margins ($14/unit) carry the difference. Lesson: **distribution margins alone are thin; hybrid channels subsidize them.**

## 4. Crowdfunding price architecture (Stegmaier, KS Lesson #201)

Formula: KS core reward = (MSRP − 40%) + shipping subsidy, then "9-ify" (round to nearest 9; KS Lesson #92 — psychological pricing).

| MSRP | Recommended KS core reward (assumes ~$10 US shipping subsidy) |
|---|---|
| $30 | $25 |
| $35 | $29 |
| $40 | $34 |
| $50 | $39 |
| $60 | $49 |
| $70 | $55-59 (heavier items need higher subsidy) |
| $80 | $65-69 |

- Yields ~$20-30 profit/unit at the $10-manufacturing baseline, before KS+payment fees (~8-10%), art/design, freight, and pledge-manager costs.
- Backers expect 10-20% under MSRP (Stegmaier) — the discount *is* the pitch; funding comes from margin structure, not underpricing below the per-unit loss line.
- Mathe's 2013 KS price anchors (inflate for today): 1-deck card game $9-19; light family/party $20-39; typical 3-lb 12″×12″ game $50-60; big-box up to $99.
- Sell-through reality (Mathe, 2012, n=80 new products through his fulfillment house): only 22 sold >500 retail units. First print runs: 1,500-2,500 units (Mathe 2013).
- Post-campaign sell-through playbook (PrintNinja): keep selling from the KS page (edit it on the final day — it freezes at close), open a webstore immediately, then pursue retail with retail-standard packaging (UPC, standard box, no KS-exclusive branding on the retail SKU).

## 5. Deluxe, exclusives, and direct-only SKUs

- KS-exclusive deluxification breaks distribution: Scythe metal mechs would need >$100 MSRP in retail → direct-only product (Stegmaier).
- Dual-SKU strategy (standard retail + deluxe direct) adds a third SKU (upgrade pack); SKU proliferation confuses consumers years later.
- Retailers dislike publisher-exclusive deluxe versions — Stegmaier's preference: one deluxe-feeling standard box + à-la-carte add-ons ("The Deluxe Dilemma", 2020).
- A $100+ KS core reward concentrates lifetime sales into the 30-day campaign window; retail sell-through of the same product is structurally weaker afterwards (market already absorbed).

## 6. Tariff scenario math (Stegmaier, April 2025; +54% US tariff on Chinese goods at publication)

Pass-flat up the chain: $10→$15 production → distributor $25 → retailer $30 → MSRP $55. Full-multiplier pass-through would put the same game at $75 MSRP — which the market rarely tolerates; hence margin compression lands on every node. Publisher scale context: Stonemaier spent ~$10M on production in 2024 → tariffs implied ~+$5M. Treat tariff/cost volatility as a permanent padding factor in pricing, not a one-off (freight rates and exchange rates behave the same way).

## 7. Royalty context (for margin completeness — details belong to `board-game-publishing`)

Designer royalties (Mathe): 3-5% of MSRP, 5-6% of wholesale, or 20-25% of net profit. Price the game as if the royalty exists even when self-publishing — it disciplines the multiplier.

## 8. Pricing procedure (checklist)

1. Landed cost/unit at realistic quantity (from `board-game-manufacturing` if unknown).
2. Floor check: MSRP ≥ 5× landed (or Stegmaier's adjusted 5× manufacturing).
3. Ceiling check: comp-cluster price band (see `references/comp-title-method.md`); above it needs visible component justification.
4. Channel prices: distribution MSRP; KS reward via §4 table; webstore at MSRP with member discount (Stonemaier Champions: 20% off).
5. Volatility pad: freight, FX, tariffs (§6).
6. Royalty + sunk-cost recovery policy decided *before* announcing a price.
7. If floor > ceiling: cut components, shrink the box (freight), or change channel — never just hope.
