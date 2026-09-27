---
name: board-game-market-analysis
description: >-
  Market analysis and positioning for hobby board games: market size and segments, comparable-title analysis, pricing architecture (MSRP multipliers, price bands), distribution vs direct vs crowdfunding economics, positioning statements, and trend radar. Use when the user says "price my game", "what should my MSRP be", "is there a market for my game", "comparable titles / comp analysis", "who is the audience for this game", "positioning statement / hook / X meets Y", "will it sell", "Kickstarter vs retail sell-through", "distribution margins", "how big is the board game market", "what segment is my game", "evergreen potential", or "board game trends". For component costing and quotes use board-game-manufacturing; for funding-goal math and pledge tiers use board-game-crowdfunding; for pitch emails and sell sheets use board-game-publishing; for solo-mode design use board-game-solo-coop-design.
---

# Board Game Market Analysis & Positioning

Market analysis is applied economics, not optimism. Your job: place the design in a real segment, price it from the distribution chain and from comparables, choose channels that match its margin structure, and write a positioning statement that survives contact with a retail buyer — while flagging every number that is folklore.

## When to use / when not to use

Use this skill when the user needs to:
- Estimate whether a game concept has a viable market: segment fit, audience size signals, price sensitivity, competitive gap.
- Run a comparable-title (comp) analysis: BGG rank/ratings/weight/price/publisher-tier benchmarking against 5-10 similar titles.
- Set MSRP or a Kickstarter core-reward price, or sanity-check a price against landed cost and comparables.
- Understand channel economics: publisher/distributor/retail margin splits, why direct and crowdfunding margins differ, sell-through expectations.
- Craft a positioning statement (hook + audience + comp anchor) or evaluate "evergreen" potential.
- Read trends: solo modes, legacy, app integration, deluxification, card-size shifts, tariff pressure.

Do NOT use this skill for:
- Component-level costing, manufacturer quotes, freight/compliance → `board-game-manufacturing` (it owns the 5× costing heuristic; this skill owns pricing *vs the market*).
- Campaign mechanics: funding-goal math, pledge tiers, stretch goals, pledge managers, backer shipping/VAT → `board-game-crowdfunding`.
- Pitching publishers: sell sheets, pitch emails, contracts, royalties → `board-game-publishing`.
- Designing the solo mode itself → `board-game-solo-coop-design`; win-rate math → `board-game-math-balance`.

## Core principles

1. **MSRP is chosen, not assigned.** Stegmaier ("The Myth of MSRP", 2013): there is no official price a game "deserves". Benchmark comparable published products in your category and component class, then verify the result survives distribution math (≥5× landed cost). Cost-plus alone ignores perceived value; comps alone ignore solvency. Use both.
2. **Price from the chain back.** Stegmaier's baseline ("The Math of Tariffs", 2025): $10 production → distributor pays publisher $20 → retailer pays distributor $25 → consumer pays $50. The publisher keeps ~40% of MSRP in distribution; the retailer's 2× markup covers pre-paid inventory risk, overhead, staff, and discount headroom. Any price that breaks this chain breaks the channel.
3. **Landed cost, not manufacturing cost.** Hoyt (Foxtrot Games, 2016) and Mathe (2013) multiply *landed* cost (manufacturing + freight/customs to warehouse) by 5-6; Stegmaier multiplies manufacturing by 5 and adjusts for freight. Same magnitude, different base — say which one you are using. [Sources agree on magnitude, disagree on base.]
4. **At 5× you must sell ~50% of the print run to recoup** (Hoyt); selling out nearly doubles your money but only just funds the reprint. At ~4.16× you need ~84% sell-through to recoup — and very few games sell out. Under-pricing is how successful games bankrupt publishers.
5. **Segments are products, not genres.** Each segment (gateway, family, party, euro, thematic, wargame, collectible, solo, kids) has its own weight band, price band, session length, buyer, and retail channel. A design that straddles two segments usually gets shelved in neither.
6. **Comps beat TAM.** "The market is $X billion" never sold a game. Five to ten comparable titles' rank, ratings velocity, weight, and price tell you the addressable reality. Treat global market-size reports as context, not evidence — methodologies are opaque [contested].
7. **Evergreen is the target profile — but it is survivorship data.** Stegmaier's analysis (2022) of 21 already-successful evergreen hobby titles (repeat appearances on ICv2 top-10 lists + retailer data, pre-2022 vintage): 2-4 players, ~45 min, medium weight, ~$50, easy to teach/learn/set up. The profile describes winners, not the odds, and structurally excludes party, kids, wargame, and 2p-duel categories. The ~$50 anchor has inflated since (the gateway evergreen class now lists ~$55-60 and drifting) — re-date the band for the current year. Deviating from this profile is a choice that must be justified by the design, not an accident.
8. **Channel is a design constraint.** Distribution demands a price band and box that survive 60-65% discounts; crowdfunding tolerates $70-150 deluxe prices that retail cannot restock; direct-only forfeits the ~58% of buyers who primarily shop retail (Stonemaier 2024 survey). Decide the channel before fixing components.
9. **Ratings are health signals, not sales figures.** Stonemaier tracks "1,000 ratings in one month" as a strong-velocity signal. Ratings-to-sales ratios circulating in the community (3-10×) are folklore [contested] — use ratings for relative comparison, never absolute revenue estimates.
10. **Every number carries a source and a date.** MSRPs drift, weights get re-voted, tariff policy can change mid-year. Anchor claims to a named source and year (Stegmaier 2022/2025, Mathe 2013, Hoyt 2016, ICv2, Asmodee 2024) and mark community consensus explicitly.

## How to apply it

### A. Classify the segment (15 minutes)

1. Place the game in one primary segment using the compact table below (full table with more exemplars: load `references/market-size-and-trends.md`).
2. Check the design's actual weight/length/price against the segment norms. Mismatch = either redesign or re-segment.
3. Name the buyer: BGG-aware hobbyist repeat buyer, gift buyer, family household, or FLGS browser. Tinsman's four markets (*The Game Inventor's Guidebook*): mass market, hobby, American specialty, European — know which channel your segment lives in.

| Segment | BGG weight* | Typical MSRP | Exemplars |
|---|---|---|---|
| Party | 1.0-1.5 | $20-35 | Codenames ($25), Just One ($25), Wavelength ($35) |
| Kids | 1.0-1.5 | $10-25 | Sleeping Queens ($12), Outfoxed! ($20), Dragomino ($25) |
| Gateway | 1.5-2.3 | $30-55 | Azul ($40), Carcassonne ($40), Ticket to Ride ($55), Catan ($55) |
| Family | 1.8-2.5 | $30-60 | Cascadia ($40), Kingdomino ($25), Quacks ($55) |
| Hobbyist euro | 2.5-3.8 | $50-80 | Wingspan ($60), Terraforming Mars ($70), Ark Nova ($75) |
| Thematic/Ameritrash | 2.5-3.5 | $60-110 | Betrayal 3E ($56), Mansions of Madness 2E ($110) |
| Wargame | 3.0-4.5 | $50-130 | Undaunted ($50), Twilight Struggle ($65), GMT P500 titles |
| LCG / expandable card game | 2.9-3.4 | $40-70 core + ongoing | Arkham Horror LCG ($60 core), Marvel Champions ($70 core) |
| Solo-focused | any | +$0-15 premium | Built-in solo mode now expected (see Trend radar) |

*Weights are BGG community-voted values (community consensus; they drift ±0.3). MSRPs are US list prices circa 2022-2025 — verify current prices before quoting them to a user as fact.

TCG/CCG booster economics (MTG-style rarity-driven pack margins, organized-play budgets, allocation-based specialty distribution) are a different, far more capital-intensive business and are **out of scope** for this table — do not enter that segment on this analysis alone.

### B. Run the comparable-title scan

1. Pick 5-10 titles: same segment, similar weight (±0.5), similar component class, published in the last ~5 years unless evergreen.
2. Record per title: BGG rank, ratings count, weight, MSRP and street price, publisher tier, player count, session time, year.
3. Detect evergreens: ≥3 appearances across years on ICv2 hobby-channel top-10 lists (Stegmaier's method) or persistent top-200 BGG rank.
4. Identify the gap: a price point, weight band, player count, or theme the comps underserve. Position *into the gap*, not into the densest cluster.
5. Full procedure, worked example table, and publisher-tier list: load `references/comp-title-method.md`.

### C. Set the price

1. Get landed cost per unit (manufacturing at realistic quantity + freight/customs). If unknown, estimate from component class via `board-game-manufacturing`.
2. Compute the floor: MSRP ≥ 5× landed cost (Hoyt/Mathe) or 5× manufacturing adjusted for freight (Stegmaier; go 6-8× when freight is heavy).
3. Check the ceiling: what do the comp titles from step B charge? Price above the comp cluster only with a visible component justification (minis, deluxification).
4. Choose channel price architecture: distribution needs the 5× chain; KS core reward ≈ MSRP − 40% + shipping subsidy, then "9-ify" (Stegmaier KS Lesson #201: $50 MSRP → $39 reward; table in `references/pricing-and-margins.md`); direct/webstore can hold MSRP with a member discount (Stonemaier Champions: 20% off).
5. Pad for volatility: freight rates, exchange rates, tariffs (2025 US tariffs on Chinese goods: +54% at the time of Stegmaier's analysis).

### D. Choose channels and model the margins

- **Distribution**: publisher receives ~35-40% of MSRP (distributor discount 60-65%; direct-retailer 45-50%). Use the worked $50-MSRP margin table in `references/pricing-and-margins.md` before promising anyone revenue.
- **Direct/webstore**: publisher keeps full price minus fulfillment (~$20 real cost vs ~$10 charged shipping — Stegmaier 2025) and platform fees.
- **Crowdfunding**: fee stack ~8-10% (platform ~5% + payments ~3-5%); margins fund the print run, but a $100+ core reward concentrates lifetime sales in the campaign and can't enter distribution at a sane MSRP.
- **Direct preorder (GMT's P500 model)**: the publisher lists the game and takes preorders at a discount off MSRP; the game goes to print only when preorders cross the publisher's production threshold (originally ~500 orders, hence the name; current thresholds vary by title — check GMT's current terms before citing numbers), and customers are charged when the game ships, not at pledge. No crowdfunding fee stack, print-to-demand removes the unsold-inventory bet, and titles reach retail/distribution only after preorder demand is satisfied. This — not Kickstarter — is the dominant channel for wargames and similarly committed-niche segments; forcing a wargame into KS norms (stretch-goal deluxification, $100+ core rewards) misreads its buyers. Any publisher with an audience and a webstore can run the same model.
- Sell-through reality: "most games sell the majority of what they'll ever sell in the first three months" (Hoyt — industry hearsay, treat as directional). Mathe (2012, n=80 new products through his fulfillment house): only 22 sold >500 retail units. Size first print runs accordingly (1,500-2,500 for new publishers).

### E. Write the positioning statement

Template: **"[Game] is a [weight/length] [segment] game about [one-clause hook] for [audience], for players who love [comp A] but want [differentiator]."**

- Lead with the hook; "X meets Y with a twist" is the industry shorthand (Stegmaier's pitch guidance).
- Comp anchors must be titles the target buyer knows (BGG top ~500) and recent; one mechanical comp + one thematic comp maximum.
- State the differentiator in one clause ("...but with drafting instead of dice"). No "Catan killer", no superlatives, no genre salad ("a deck-building worker-placement legacy adventure").
- Validate against the evergreen profile (principle 7): each deviation needs a deliberate reason.
- Test: can a retail buyer repeat your sentence to a customer unprompted? If not, cut clauses.

### F. Trend radar sanity check

Check the design against current structural trends (dates and evidence in `references/market-size-and-trends.md`): solo mode as table stakes (Stonemaier won't publish without one; BGG solitaire-playable share ~10% mid-1990s → ~20% by 2015), legacy/campaign formats (Risk Legacy 2011, Pandemic Legacy 2015), app integration (Mansions of Madness 2E 2016 — bifurcated reception), deluxification (retailers dislike publisher-exclusive deluxe SKUs — Stegmaier), tarot-sized cards (70×120mm, e.g. Ark Nova 2021) [community-observed], digital try-before-you-buy (BGA topped Stonemaier's 2025 platform survey). Rule: a trend is a distribution/positioning fact, never a design requirement — bolt-ons fail.

### G. Reprint & second-printing decisions

Most titles never earn a reprint (Mathe 2012: 22 of 80 new products sold >500 retail units) — decide on evidence, not on sell-out euphoria. This skill owns the economics; `board-game-manufacturing` owns run-size/quote mechanics and `board-game-rules-writing` owns between-printing rulebook changes.

1. Demand signals (need several, not one):
   - First run sells out in weeks-to-few-months, not years (sell-out window).
   - Distributor re-orders and FLGS restock requests keep arriving after sell-out.
   - Ratings velocity persists post-sell-out (principle 9); secondary-market price holds at or above MSRP.
   - Localization/partner inquiries (Stonemaier's channel reality: partners take a share of volume).
2. Trigger check: a sell-out only *just* funds the reprint (Hoyt, principle 4) — the reprint's own ~50%-to-recoup math must clear on *continuing* velocity. Project: units/month sold × reprint lead time (quotes ~5-6 weeks + production + freight = months) vs demand decay; if the second run would land after the demand curve flattens, don't print.
3. Size the reprint from measured velocity, not from the first run's size or a distributor's enthusiasm; respect MOQ floors (~1,000-1,500) and get 3 run-size quotes (`board-game-manufacturing`). Confirmed evergreens justify larger, cheaper-per-unit runs — this is where Stegmaier's 5,000-unit cost basis belongs.
4. Between printings: migrate accumulated FAQ/errata into the rulebook's proper sections with a dated revision (`board-game-rules-writing` — living-rulebook/Jolly/Leder model); fold component upgrades or spec changes back through the §C floor check (landed cost moves → MSRP floor moves); keep the retail SKU/UPC stable unless the edition change is deliberate.

## Key numbers & heuristics

| Number | Value | Source |
|---|---|---|
| MSRP multiplier | 5× manufacturing (adjust for freight) / 5-6× landed cost | Stegmaier 2022; Mathe 2013; Hoyt 2016 [agree on magnitude, disagree on base] |
| Distribution chain | $10 → $20 → $25 → $50 (production → distributor → retailer → MSRP) | Stegmaier 2025 |
| Distributor discount | 60-65% off MSRP (publisher nets 35-40%) | Stegmaier 2022 |
| Direct-retailer discount | 45-50% off MSRP | Stegmaier 2022 |
| Recoup at 5× | ~50% of print run; sell-out funds the reprint only | Hoyt 2016 |
| Recoup at ~4.16× | ~84% sell-through needed | Hoyt 2016 |
| Price bands | $20-30 small card game; $40-60 standard/evergreen sweet spot; $70-100+ big box/minis | Stegmaier; small-card band [community consensus] |
| KS core reward | MSRP − 40% + shipping subsidy, then round to 9 ($50 MSRP → $39) | Stegmaier KS Lesson #201 |
| KS fee stack | ~8-10% of pledges (platform ~5% + payments) | [community consensus] |
| Evergreen profile [survivorship data] | 2-4 players, ~45 min, medium weight, ~$50 (pre-2022 anchor; now ~$55-60, drifting), easy teach | Stegmaier 2022, n=21 already-successful titles |
| First print run | 1,500-2,500 units for new publishers | Mathe 2013 |
| Sell-through | 22 of 80 new products sold >500 retail units | Mathe 2012 fulfillment data |
| KS tabletop pledges | $233M (2020) | ICv2 via Wikipedia |
| Asmodee revenue | €1.287B (2024) — largest pure-play hobby publisher | Asmodee Q3 interim report via Wikipedia |
| Hobby market growth | "25-40%/yr since 2010" | Guardian 2014 [contested/dated] |
| Solo demand | 42.7% of Tuscany KS voters called solo at least somewhat important; BGG solitaire share ~10%→~20% (1995→2015) | Stonemaier polls; BGG guild data 2015 |
| Channel split (Stonemaier 2024) | ~55% distribution/retail, <30% direct; 58% of buyers shop primarily retail | Stegmaier 2025 |
| Retailer markup logic | 2× over their cost: inventory risk + overhead + discount headroom | Stegmaier 2025 |

## Common pitfalls

- **Under-pricing below the 5× floor** — the game sells out and still can't fund a reprint; manifests as "successful but bankrupt" (Hoyt's 84%-at-4.16× math).
- **The MSRP myth** — asking "what should this cost?" as if assigned, instead of benchmarking comps and choosing deliberately (Stegmaier).
- **Comp cherry-picking** — benchmarking against outliers (Gloomhaven, Frosthaven) or across segments (pricing a party game against a big-box euro); yields fantasy MSRPs.
- **Ratings-as-sales arithmetic** — multiplying BGG ratings by a folklore ratio to "prove" revenue; ratios of 3-10× circulate with no methodology [contested].
- **TAM justification** — citing a $13-19B "global board game market" SEO report as evidence a niche title will sell; methodologies opaque [contested], and segment demand is what matters.
- **Crowdfunding/retail mismatch** — a $100+ KS-exclusive deluxe game that can never enter distribution; lifetime sales concentrated in 30 days; SKU proliferation confuses buyers for years (Scythe metal mechs needed >$100 MSRP for distribution → direct-only).
- **Channel neglect** — direct-only strategy ignoring that ~55-58% of volume flows through distribution/retail (Stonemaier 2024; Wingspan sold >90% via distribution).
- **Segment straddle** — "light enough for families, deep enough for gamers" usually means rejected by both buyers; box, price, and weight must commit.
- **Trend-chasing** — bolting on legacy, an app, or tarot cards because they trend; every trend in the radar has failures attached, and bolt-ons read as cynical to the hobby buyer.
- **Overprinting the first run** — distributors talking new publishers into 5,000+ units against the 1,500-2,500 norm (Mathe); warehousing dead stock kills more small publishers than bad games do.
- **Reprinting on the sell-out signal alone** — a sell-out only just funds the reprint (Hoyt); without sustained reorders and velocity, the second run becomes the dead stock. Mirror trap: underprinting a confirmed evergreen starves retail demand (see `board-game-manufacturing`).

## Reference files

- `references/comp-title-method.md` — load when running an actual comp-title scan: step-by-step procedure, worked example table with real BGG/MSRP data, publisher tiers, evergreen detection, gap analysis.
- `references/pricing-and-margins.md` — load when pricing anything or modeling channel revenue: full distribution-chain tables, margin math per channel, Stegmaier's MSRP→KS-reward table, recoup/sell-through math, deluxe-SKU strategies, tariff scenarios.
- `references/market-size-and-trends.md` — load when the user asks about market size/growth, segment detail, solo-demand data, or trend radar: sourced market-size table with caveats, full segment norms, evergreen study stats, dated trend list.

## Related skills

- `board-game-manufacturing` — landed cost, quotes, MOQ, freight: the cost floor under every price decision here.
- `board-game-crowdfunding` — funding-goal math, pledge tiers, stretch goals, pledge managers, backer shipping/VAT.
- `board-game-publishing` — licensing vs self-publishing, sell sheets, pitch emails, contracts and royalties (positioning statements here feed pitch materials there).
- `board-game-solo-coop-design` — designing the solo mode that the market now expects.
- `board-game-accessibility` — price/business-model accessibility, language independence; overlaps on "who can buy and play".
- `board-game-design-theory` — session arc and player-experience targets that define segment fit.
- `board-game-math-balance` — difficulty/win-rate calibration referenced by segment expectations.
