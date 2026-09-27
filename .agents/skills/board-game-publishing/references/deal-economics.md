# Deal Economics — Routes, Royalties, Contracts, Timeline

Load-trigger: comparing licensing vs self-publishing vs work-for-hire with numbers, evaluating a contract clause-by-clause, computing royalty/advance math, or asking how long publishing takes.

Primary anchors: Tom Jolly, "Game Contract Pitfalls," League of Gamemakers (2014) — veteran designer (Wiz-War) on real contracts; Stonemaier Games' published submission guidelines; Brian Tinsman, *The Game Inventor's Guidebook* (toy/mass-market norms). Figures marked [contested]/[approximate] where sources are thin.

---

## 1. Route comparison, with money

| | License to publisher | Self-publish (crowdfund) | Work-for-hire |
|---|---|---|---|
| Cash at risk | $0 (time only) | $15k–$40k+ all-in [approximate] | $0 |
| Rights | Licensed to publisher for the term | You keep everything | Assigned to client |
| Income shape | 5–8% of net receipts, quarterly/semiannual (Jolly) | Margin on units, lumpy, front-loaded to campaign | Flat fee on delivery |
| Control | Publisher redevelops freely | Total | None (client brief) |
| Timeline to shelf | 18–24 months post-signing [approximate] | 12–18 months from pre-launch to fulfillment | Client's schedule |
| Who does art/marketing/freight | Publisher | You + vendors | Client |
| Career effect | Credit + royalty history | Brand + audience if it works | Portfolio, sometimes uncredited |

## 2. Licensing math (worked example)

Assumptions: MSRP $50; publisher sells to distribution at ~40% of MSRP → net receipts ≈ $20/unit (direct sales raise net; this is the conservative base).

| Scenario | Royalty | Per unit | 5,000 units | 15,000 units |
|---|---|---|---|---|
| Low end | 2% of net | $0.40 | $2,000 | $6,000 |
| Standard | 6% of net | $1.20 | $6,000 | $18,000 |
| High end | 8% of net | $1.60 | $8,000 | $24,000 |

- Jolly's observed contract range: 5–8% of net is standard; 2–10% occurs. Mass-market-scale expectations push rates *down*.
- Advances: a few hundred dollars to $5,000 (Jolly), recouped against royalties — you see no checks until earned royalties exceed the advance. Stonemaier publicly offers a $10,000 advance on signing; treat this as a famous outlier, not a norm.
- Reading the table: a solid mid-tier success (15,000 lifetime units) at a standard rate pays ≈ $18k over *years* — the core reason "most designers earn <$10k/yr from design" [contested exact figures, consistent across community surveys] and why full-time designers number in the low hundreds worldwide.
- Royalty base traps: "net" must mean *cash actually received for sales* (Jolly's standard). Reject undefined "profits," MSRP-based wording with undefined deductions, or bases that let the publisher net out marketing/overhead.

## 3. Self-publishing sketch (detail lives in `board-game-crowdfunding`)

For route comparison only: on a $40,000 campaign, expect ~8–10% platform/payment fees (Kickstarter 5% + processing ~3–5%), manufacturing + freight as the largest line, then art/graphic design, fulfillment, and marketing. Disciplined first campaigns net roughly 10–20% margin [approximate, synthesized from Stegmaier's Kickstarter lessons and Mathe's publishing essays]; undisciplined ones lose money at 2× the goal. Tabletop games have raised on the order of $150M–$270M/year on Kickstarter in recent years (ICO Partners annual tracking [approximate]) — the demand is real, and so is the competition.

## 4. Work-for-hire norms

- Flat fee, wide range [contested]: low thousands for small studios to $20k+ for established designers on licensed-IP briefs.
- Usually no royalty, no rights, sometimes no credit (confirm credit in writing — it is worth real money later).
- Value proposition: guaranteed cash, professional development teams, and a track record that makes future licensing easier.
- Mass-market inventing runs on agents: toy-industry agents take 40–50% of the inventor's royalty (Tinsman). Hobby board games barely use agents; publishers accept direct submissions.

## 5. Contract clause checklist

Before signing, get explicit written answers on each row. Then pay a contract lawyer to read the actual document (Jolly's first and last advice).

| Clause | What to secure |
|---|---|
| Royalty rate & base | Rate AND definition of net receipts; ask when escalations apply (e.g., +1% after 10k units) |
| Advance | Amount, payment trigger (on signing, not on publication), recoupment terms |
| Term | Fixed end date (3–7 years typical); renewal only by mutual agreement or defined sales threshold |
| Reversion | Rights revert if unpublished by a drop-dead date OR out of print 12–24 months; bar "publication" by tiny POD runs (Jolly: require a minimum print, e.g., 1,000 copies) |
| Rights scope | Territories, languages, formats (physical/digital/expansions). Publishers commonly want worldwide, all languages, full rights (Stonemaier states this); anything narrower must be written down |
| Derivative works | Do expansions/spin-offs based on your design pay you? Usually yes if your design — confirm |
| Modification rights | Publisher will redevelop; secure consultation (not approval) rights and name the 1–2 untouchables up front (Stonemaier: total inflexibility = no deal) |
| Credit | "Designed by" on box and in all materials; name/likeness use scope. Designer-name-on-box is now hobby norm (Knizia pioneered it as a brand) |
| Payments & audit | Quarterly or semiannual statements+payments (Jolly's standard; Stonemaier pays monthly); audit rights on records |
| Warranties/indemnity | You warrant originality; cap your liability at amounts actually received |
| Assignment/sale | What happens to the license if the publisher is acquired or folds |
| Exclusivity of next game | Strike or narrow any right-of-first-refusal on your future designs |

## 6. Timeline: contract to shelf (commonly 18–24 months [approximate, publisher consensus])

| Phase | Duration | Owner |
|---|---|---|
| Publisher development & blind testing | 3–9 months | Publisher dev team + designer |
| Art & graphic design | 3–6 months | Publisher |
| Manufacturing incl. proofing gates | 3–5 months | Publisher + factory (see `board-game-manufacturing`) |
| Freight & customs | 1–2 months | Publisher |
| Distribution/retail pipeline | Overlapping, +1 month | Publisher/distributor |

Slippage multiplies: a dev restart or art reshoot adds quarters, not weeks. Anything promising shelf presence in under 12 months post-signing should be treated as a red flag or a very small print run.

---

## 7. Business basics for self-publishers [not tax or legal advice — US framing; rules vary by country — hire a CPA and a lawyer before launch, not after]

Self-publishing makes you a small consumer-products company, not just a designer. The rows below are where first campaigns get personally burned.

| Topic | What to do | Why it bites |
|---|---|---|
| Entity choice | Form an entity (LLC or local equivalent) before the campaign takes money; sole proprietorship is the default but exposes personal assets | You personally ship small-parts consumer products; liability follows the operator |
| Product-liability insurance | Buy a policy sized to your market (US/EU); general liability for booth work | Distributors, 3PLs, and some conventions demand certificates of insurance before they touch your stock |
| Income tax | Campaign funds are generally taxable income in the year received, not free money; royalties are ordinary income; keep expense records from day one | A $40k campaign can land as $40k of taxable income in one year against costs paid in the next |
| Sales tax (your direct sales) | Webstore and convention sales create sales-tax obligations ("nexus") per state/country; convention selling usually needs a temporary seller's permit for that state | Backer-side VAT on pledges is covered in `board-game-crowdfunding` — this row is the post-campaign direct-sales side |
| Information returns | US: expect a 1099-K from Kickstarter/Stripe above reporting thresholds; issue 1099-NEC to contractors paid $600+ (artists, editors, videographers) | Missing contractor forms is an audit magnet; platform-reported income must match your return |

Rules of thumb: separate bank account from day one; price entity setup, insurance, and a tax reserve into the campaign goal math (`board-game-crowdfunding`); treat "I'll sort taxes after fulfillment" as a red flag.
