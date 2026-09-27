# Pledge Math — Goal, Tiers, Shipping, VAT & Tariff Worksheets

Load this when computing the funding goal, pricing pledge tiers, building the shipping table, or stress-testing margins. Core formulas are Stegmaier's (KS Lessons #7, #201, #212, #266); fee-stack and tariff data from the Chroma Arcana postmortem (BoardGameWire, 2025). [contested] marks folklore.

---

## 1. The fee stack (apply to every dollar raised)

| Layer | Typical take | Source |
|---|---|---|
| Platform fee | 5% | KS/GF/BackerKit standard |
| Payment processing | 3% + $0.20/pledge (>$10); ~5% + $0.05 (≤$10) | Stegmaier #7 (Stripe breakdown) |
| Pledge manager | ~5% of campaign funds + processing on PM revenue [contested — verify rate card] | Industry standard |
| Marketing agency | 15% of attributed sales + ad spend | Chroma Arcana postmortem |
| VAT/sales tax handling | region-dependent, see §5 | — |
| Refunds/failed payments | 1–3% [contested] | — |
| Creator taxes | income tax on **net profit** (jurisdiction-dependent); US: platform issues 1099-K on the gross; pledge-manager add-on sales can create state sales-tax nexus (post-Wayfair) [verify with an accountant] | — |
| **Planning total** | **15–20% of headline raise before any production cost, plus taxes on profit** | Chroma Arcana: "15–20% in total" |

Rule: never budget against the headline number. `usable = raised × (1 − stack%)`.

**Phantom-profit trap (first-time creators):** a $100k raise that lands in December, with production paid the following March, shows as $100k of income in tax year 1 and the costs in year 2 unless your accountant plans the timing — creators who spend the raise get destroyed by the tax bill. Worked example: $100k raise − $70k production/freight − $15k fee stack = $15k net profit; at a 30% marginal rate you owe ~$4.5k — but if the $70k cost falls in the next tax year, year 1 can show close to $85k taxable (1099-K reports the gross). Set aside your expected marginal rate on net profit the day funds land, and get an accountant before launch, not after.

## 2. Funding-goal worksheet (Stegmaier #7)

Ask three questions, in order:
1. **Minimum viable raise** = cost to manufacture and deliver the *minimum viable print run* if you fund at exactly 100%.
2. **How much lower can the goal be?** = the personal cash (or certain post-campaign sales) you commit to bridge the gap.
3. **What does 500 / 1,000 / 1,500 units cost me?** = know the scaling before launch.

Fill-in worksheet:

```
A. Min print run units (MOQ floor: typically 1,000–1,500 at consolidated CN manufacturers)
B. Landed unit cost at A units (manufacturing + freight per unit)         $____
C. Print cost = A × B                                                     $____
D. Sunk costs to recover (art, graphic design, prototypes, ads)           $____
E. Shipping subsidies = expected backers × per-unit subsidy (§4)          $____
F. Platform+processing ≈ 8–10% of goal                                    $____
G. VAT/tariff accrual (§5, §6)                                            $____
H. True need = C + D + E + F + G                                          $____
I. Personal investment you commit                                         $____
J. Goal = H − I  (round DOWN for marketing, never below deliverable)      $____
```

**Stegmaier's worked example (2013, standard ~4-lb game, 1,000 backer copies + 500 overage):** true need ≈ $39k including fees, freight, art, and fulfillment. He launched Viticulture at a **$25k goal** by committing $5k personal cash + pre-selling ~300 mass-market copies to distributors at 60% off MSRP (~$6k). The gap between true need and goal is a *bet you place on yourself* — size it deliberately.

## 3. Tier pricing (Stegmaier #201)

1. Manufacturing cost/unit at min run → e.g., $10.
2. MSRP = 5× that (Stegmaier #201; Mathe/Hoyt quote 5–6× of *landed* cost — the sources disagree on the base) → $50 (cross-check perceived value vs similar games on the market).
3. Core reward = MSRP − 40% → $30.
4. Add shipping subsidy (pick+pack + postage + freight-to-hub) → e.g., +$8–10 → $38.
5. 9-ify (round to 9; if that's >$2–3 off, round to 4 or 5) → **$39**.

Resulting guide table (assumes ~$10 subsidy; lighter games need less):

| MSRP | Core reward |
|---|---|
| $30 | $25 |
| $35 | $29 |
| $40 | $34 |
| $50 | $39 |
| $60 | $49 |
| $70 | $55–59 |
| $80 | $65–69 |

Margins: $20–30/unit before fees and sunk costs. **Floor rule:** if the formula lands below (manufacturing + freight + subsidy) per unit, ignore the formula — never sell below per-unit cost (#201).

**Tier ladder:** $1 → core $X → premium $X+Y; nothing between $1 and core (#113). Premium = anchor; it lifts average pledge and makes core look fair. Early birds: first-time creators only, ≤$5 gap, never reopen (#62).

**Modern variant (#266, recommended post-2021):** price the product only; collect shipping + taxes later in the pledge manager. Backer import taxes scale with the declared product price, so a $39 KS price instead of $50 MSRP both converts better and lowers their VAT. State this explicitly in the tier description AND a page section.

## 4. Shipping math

- Budget at the **heaviest final configuration** — assume every stretch goal unlocks (#12). The 4-lb USPS first-class cliff is the classic threshold.
- Per-unit international cost collapses with multi-copy orders. Stegmaier's 2013 UK example (5-lb game): 1 copy $53 → 2 copies $66 ($33/unit) → 3 copies $79 → 4 copies $92 ($23/unit). Group buys monetize this.
- Subsidy model: charge `region cost − subsidy`; the subsidy is the same worldwide so no region subsidizes another (#201, #12).
- Fulfillment-partner quotes beat carrier retail rates; get quotes per region BEFORE pricing the shipping table.
- Świerkot's law: backers treat shipping as wasted money; shipping > ~50% of product price kills conversion (his example: $40 + $20 = no deal). High-price games ($100+) absorb shipping more easily — one reason they dominate crowdfunding charts.

## 5. VAT & declared value (Stegmaier #212 + 2021 rules)

- EU VAT ≈ 21% average (national rates 17–27%), charged on **declared value = product price + shipping**. UK is a separate regime since Brexit (seller collects VAT on ≤£135 consignments); EU since July 2021: €22 import exemption abolished, IOSS for consignments ≤€150.
- **"EU-friendly" model:** freight in bulk to an EU hub; creator prepays VAT at the port on the bulk declared value; backers receive domestic-style delivery with no doorstep bill. Worked example (#212): $40 reward (with a $10 shipping subsidy built in), $10 charged shipping, $2 freight/unit → declared $52 → 21% VAT ≈ **$10.92 per unit** the creator must budget (add it to the region's shipping fee or eat it knowingly).
- Double-charge trap (#266, per Greater Than Games' Jagged Earth page): if VAT is bundled INTO the shipping charge, customs may compute VAT on the whole amount including the VAT you charged. Keep product, shipping, and taxes as separate line items.
- Retail backers: issue a commercial invoice showing VAT included so they can reclaim it (#212).
- Never under-declare or mark "gift": the legal exposure is yours.

## 6. Tariff exposure (US/China — volatile; verify the current regime)

This section is a dated snapshot, not current law. Re-verify rates before quoting landed cost.

- **Dated history:** US tariffs on China-made games escalated 20% → 54% → 84% → 104% → **145%** (April 2025), then settled at **30%** after a 90-day pause (May 2025). Charged on **manufacturing cost** (not MSRP), paid by the importer (you) at entry.
- **2026 reversal:** the Supreme Court (*Learning Resources*) struck down the IEEPA tariffs; $100B+ in refunds of collected duties are being paid (late 2026), and a Trump–Xi summit deal trimmed replacement rates further. **The replacement regime is still settling — verify current rates.** [volatile]
- **Refund opportunity (do not skip):** creators who paid 2025's 54–145% duties — e.g., Chroma Arcana's **£15,000** bill — can pursue recovery via customs protests / liquidation review. Engage your customs broker promptly; protest and liquidation windows are deadline-driven.
- Magnitude test (2025 peak): at 145%, a £5-cost game owed £7.25/unit — against a campaign that barely broke even.
- Worksheet: `tariff accrual = units into the US × manufacturing cost × current rate`. Re-run at each policy headline; state on the page how you'll handle changes (absorb / surcharge / split). BackerKit and Gamefound shipped tariff-collection tools in 2025 — use them rather than improvising.
- Mitigations: non-US audience weighting, non-CN manufacturing (see `board-game-manufacturing`), or explicitly excluding US delivery [all carry real costs — none is free].

## 7. Stretch-goal & all-in margin safety

For each stretch goal:
```
unit cost impact = (added component cost at current print run) + (added freight from weight/size)
test: (tier price − fees − unit cost impact − shipping subsidy) ≥ your floor margin, ASSUMING it unlocks
```
- Component upgrades (linen, foil, thicker boards) are the safe class; locked gameplay content is unpopular (Chroma Arcana research) and adds design/test time = delay risk.
- Golden goose at 400–500% funding (#11): Ground Floor gave a free second game at $75k (500%) and raised +$38k afterwards. Only offer what you can cost at full unlock.
- **All-in tier:** cost it as a standalone product: BOM of every add-on + its own box/freight/pick complexity. All-in BOM creep is where campaign margins go to die; one all-in tier maximum.

## 8. Break-even sanity check (Chroma Arcana, 2024)

| Line | Value |
|---|---|
| Funding goal | £8,000 (one print run only — knowingly below break-even) |
| True break-even estimate | £52,000 (incl. art, marketing, time) |
| Raised | £66,000 |
| Outcome | ≈ break-even, not profit: fee stack 15–20%, agency 15% commission, heavy art spend |
| Their tier fix for next time | one budget tier, one deluxe, maybe one special |
| Their channel data | Facebook ads best; £500 Reddit ≈ £0 return; £800 Google ≈ ~0; KS pre-launch page up early → 4,300 followers |

Lesson pattern: set the goal for marketing (fast funding), but KNOW your break-even number and have the personal-investment plan for the gap before you launch (#7's three questions).
