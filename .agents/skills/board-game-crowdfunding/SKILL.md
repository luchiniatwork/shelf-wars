---
name: board-game-crowdfunding
description: >-
  Crowdfunding a board game on Kickstarter, Gamefound, or BackerKit: pre-launch audience funnel, funding-goal math, page anatomy, pledge tiers, stretch goals, shipping/VAT/tariffs, pledge managers and late pledges, fulfillment, and post-campaign management. Use when the user says "Kickstarter my game", "Gamefound vs Kickstarter", "set my funding goal", "pre-launch email list / conversion rate", "design pledge tiers", "early bird", "$1 tier", "all-in / deluxe tier", "stretch goal ideas", "how much should I charge for shipping", "EU VAT / IOSS", "tariffs on board games", "pledge manager / late pledges", "mid-campaign slump", "first 48 hours", "cross-promotion", "update cadence", "retailer pledge level", "shipping table", "risks and challenges", "fulfillment hubs", or "refund / cancel a campaign". For manufacturing cost/MOQ use board-game-manufacturing; MSRP positioning use board-game-market-analysis; licensing use board-game-publishing; review prototypes use board-game-prototyping.
---

# Board Game Crowdfunding

Crowdfunding is audience-building converted into a 30-day sales event. The campaign is won or lost in the 6 months before launch and in the goal/pricing math, not during the live stream. Your job: get the creator launch-ready, make the math survive success, and make delivery boring.

## When to use / when not to use

Use this skill when the user needs to:
- Pick a platform (Kickstarter / Gamefound / BackerKit) and build the pre-launch funnel (landing page, email list, preview page, community).
- Compute the funding goal, price pledge tiers, design early birds/deluxe/all-in/retailer levels, or architect stretch goals.
- Structure the project page (video, GIFs, pledge chart, shipping table, risks) and plan campaign operations (updates, slump tactics, cross-promos, endgame).
- Plan backer shipping, regional fulfillment hubs, EU/UK VAT, US tariff exposure, pledge managers, late pledges, and post-campaign communication/refunds.

Do NOT use this skill for:
- Manufacturing cost, MOQ, print specs, freight quoting → `board-game-manufacturing` (this skill consumes those numbers as inputs).
- MSRP positioning, comparable titles, distribution margins → `board-game-market-analysis`.
- Licensing vs self-publishing, contracts → `board-game-publishing`.
- Prototype/review-copy production → `board-game-prototyping`.
- Rulebook content → `board-game-rules-writing` (you only need the *link* to a written rulebook on the page).

## Core principles

1. **Crowdfund the crowd you have, not the one you hope for.** Stegmaier (KS Lesson #57): "It's not Kickstarter's job to give you backers." Launch-readiness is measured, not felt: email subscribers, KS/GF pre-launch followers, BGG fans, Discord/FB members, playtesters (#230). Epoch: The Awakening failed with an excellent page and ~1,000 newsletter subs but 36 BGG fans — it wasn't part of the conversation. If the numbers aren't there, delay: "You don't need to launch today" (#68).
2. **The funding goal is a marketing number, not your budget.** Stegmaier (#7): goal = minimum viable print-run cost − what you will personally invest. Fund fast, because backers hesitate to join projects that look unfundable, and funded projects convert better. Never set the goal below what you can deliver at *exactly* 100% funding.
3. **Price from MSRP down, never from cost up.** Stegmaier (#201): core reward ≈ MSRP − 40% + shipping subsidy, rounded to 9 (or 4/5); target $20–30/unit margin before fees and sunk costs. Floor: never below manufacturing + freight + shipping subsidy per unit.
4. **Assume every stretch goal unlocks when you price.** Stretch goals are pre-spent margin. Price shipping and unit cost at the *final* configuration. Prefer component upgrades; backers resent gameplay content locked behind goals (#11; Chroma Arcana market research, 2024).
5. **Shipping kills projects, not manufacturing.** Stegmaier (#7): "The harsh reality isn't so much the cost of manufacturing — rather, it's the cost of shipping." Świerkot (Gamefound CEO): backers see shipping as "wasted money" — a $40 game + $20 shipping is a deal nobody takes. Regional hubs and honest VAT/tariff budgeting are the fix.
6. **The page converts; ads only amplify.** Chad Krizan (BGG advertising manager): "Advertising will not save a failing campaign." Stegmaier's Viticulture data: $1,000 BGG banner ads clearly ROI-positive; Facebook/Dice Tower marginal; the creators' own outreach raised 13% of funds (#26). Fix the page before buying traffic.
7. **Backers upgrade; strangers don't.** A $1 backer is far easier to upgrade than a non-backer is to convert (#113). Updates only reach backers, so the $1 tier is your remarketing list. Community mechanics (comments, toasts, micro-goals) are conversion mechanics.
8. **Raised ≠ earned.** Platform + processing ≈ 8–10%; add pledge-manager fees, agency commissions (15% of attributed sales is common), taxes, and refunds. Chroma Arcana raised £66k against an estimated £52k break-even — "we felt like we'd made a profit; we hadn't." Budget at the stack level, not the headline number.
9. **The U-curve is normal.** Big launch spike, mid-campaign trough, final-48-hour spike (#95). Plan mid-campaign content instead of panicking; don't mistake day-3 slowdown for failure.
10. **Delivery is the campaign.** Post-campaign communication cadence, timeline honesty, and refund handling decide whether your *next* launch has a first-48-hours. Backers forgive delays they can see; they never forgive silence.

## How to apply it

### A. Pick the platform

| | Kickstarter | Gamefound | BackerKit |
|---|---|---|---|
| 2024 tabletop volume | $220m (peak $270m in 2021; −2.7% YoY) | $85m campaigns (+49% YoY) + $71m pledge-manager/late pledges | Entered crowdfunding 2023; top campaign $14.7m (Cosmere RPG) |
| Strength | Largest audience + discovery (Projects We Love, homepage, follower graph); 5,300+ funded tabletop projects/yr, avg $41.4k | Tabletop-only; integrated pledge manager + late pledges; handles EU+UK VAT; pre-launch pages far richer; AdFound ad tool | Strong pledge manager/late-pledge machinery; growing campaign side |
| Weakness | Bare pre-launch page (image + follow button); creator country restrictions (e.g., Finland needs a third party); harder to reach support | Smaller organic audience ("orders of magnitude" less, per Sami Laakso); weaker backer-notification social graph | Smallest campaign-side audience |
| Exemplar | Frosthaven $12.97m (2020, KS tabletop record) | CMON (exclusive since 2024; $12.1m across 6 projects in 2024; $108m lifetime on KS); Cyberpunk 2077 BG $7.6m | Cosmere RPG (Brotherwise) $14.7m at close, ~$15m w/ late pledges (2024 — biggest tabletop crowdfunding campaign ever); MCDM RPG ~$5m |

Default: Kickstarter for first-time creators needing discovery; Gamefound when you have an audience and want the integrated pledge manager/VAT handling. Fees are comparable (~5% platform + ~3–5% processing on all three [verify current rate cards]).

Landscape snapshot (volume data is 2024): **Gamefound acquired Indiegogo (July 2025, BoardGameWire)**, absorbing its rewards-crowdfunding audience; KS countered with 2025 creator-tool updates. [verify current platform state before choosing]

### B. Build the pre-launch funnel (start 6–12 months out)

1. **Landing page → email list.** One page, one call to action, a reason to subscribe (rulebook, PnP, art drops). The email list is the asset everything else feeds.
2. **Warm the list.** Monthly-ish value emails; a cold list converts far worse than an engaged one. Warm-list → backer conversion of 5–10%+ is the commonly cited agency planning figure [contested — LaunchBoom/agency folklore, not platform data].
3. **Open the platform pre-launch page months early.** Chroma Arcana's creator attributes a weak launch to setting the KS page up only months before; their follow-up had 4,300 followers at launch. Followers get the launch notification — free day-one spike.
4. **Community where backers live:** BGG (thumb/fan counts are the demand signal Stegmaier checks), a Discord you actually staff, one FB group. Playtesters are multipliers (Epoch had 250 and they still weren't enough alone).
5. **Previews and reviews before launch:** send review prototypes to video creators 2–3 months out; internet is forever — the prototype must look good (#26).
6. **Ads only in the final week** (#245): 1–2 ads + 1–2 preview videos max, each linked to email capture or the pre-launch page, launch date shown only if certain. Pre-launch ad economics: expect ~$1–3 per email lead via Facebook in tabletop [contested — agency folklore].
7. **Launch timing:** mid-morning launch (#16); conventional wisdom Tue–Thu, avoid holidays; end in the same calendar month you launched (#133: one billing cycle, one news cycle).

### C. Compute the funding goal

Goal = (min print run × landed unit cost) + freight + fees + sunk costs you must recover − your personal investment. Walk the full worksheet, including the fee stack and shipping subsidy math: load `references/pledge-math.md`. Sanity anchors: Stegmaier's 2013 worked example needed ~$39k for a standard 4-lb game at 1,000+500 units; he launched Viticulture at $25k by personally investing $5k and pre-selling 300 mass-market copies to distributors at 60% off MSRP. MOQ floors: consolidated Chinese manufacturers typically 1,000–1,500 units.

### D. Build the project page

Stegmaier's anatomy (#39), as checklist:
- **Main image:** 3D box render or photo ("Seeing a box makes it feel real" — Craig Moore). Video: short pitch; separate gameplay/how-to video deeper down (#6, #157).
- **Best selling point at the top**, second-best next; reorder as you learn. No paragraph > 3 lines; bullets ≤ 2 lines; every text block paired with an image/GIF (GIFs for motion: #162).
- **Core sections:** 3-line description under the video → what's in the box (infographic) → third-party reviews/previews with pull quotes → gameplay video → stretch-goal map → add-ons (keep to items that fit in the game box, #39) → pledge/shipping chart → team → why Kickstarter/why now → **Risks & Challenges (mandatory, text-only; be specific — it signals competence)**.
- Reward descriptions ≤ 8 lines, most important/unique aspect first, no repetition across tiers.
- Landscape-crop images ~3:1; mix photos and renders; enable text search (type key words like "shipping" as text, not only in images).
- **Link the written rulebook** ("imperative" for board games, #39 — a Word draft is fine).
- Mechanics: you can't create the FAQ pre-launch (draft answers to paste at launch); the page is editable during the campaign but frozen after; the preview link auto-forwards to the live page.
- Agonize over it (Live-Blogging #4): the page *is* the product for 30 days.

### E. Design pledge tiers

1. **Canonical ladder (Stegmaier #8/#113):** $1 → core game $X → premium $X+Y. Nothing between $1 and core. Add group/retailer levels only with deliberate economics.
2. **$1 tier: default on Kickstarter, evaluate elsewhere** (#113 — 2013-era KS doctrine): foot-in-the-door, update access, comment access, follower notifications, upgrade path, hidden group-buy members, retailer backdoor. 3–4 lines, make it fun (Isaac Childres' Forge War: "slay a fictitious rat in your name"). Situational cases: on Gamefound (richer pre-launch follower mechanics do some of the same work), for sub-$25 party/card games where $1 is 4%+ of the average sale, or where the platform offers pledge-without-reward — weigh the upgrade funnel against admin noise.
3. **Anchoring:** the premium/deluxe tier makes core look reasonable and lifts average pledge; Stegmaier's Viticulture-era structure pushed backers toward the premium version. End prices in 9 (#92).
4. **Early birds: only for first-time creators**, difference ≤ $5, never reopen them (#62). They create winners/losers, visible cancellations, and upgrade-path confusion when you add tiers mid-campaign. Better urgency: limited "be part of the product" tiers, a fair price, and friends-and-family day one.
5. **Retailer tier:** handle via $1 + manual amount or a dedicated level; EU retail backers need a commercial invoice showing VAT (#212).
6. **All-in tier:** one all-in max; price it so its BOM can't sink you (see pledge-math.md). Tier sprawl overwhelms backers — Chroma Arcana's #1 self-identified mistake; their fix: one budget tier, one deluxe, maybe one special.
7. **Prune mid-campaign:** remove tiers with 0 backers; migrate 1–2-backer tiers (#95).

### F. Architect stretch goals

- Funding goal = minimum viable product; stretch goals improve it (#11). Give them to **everyone who gets the product** — gating goals behind higher tiers insults backers.
- **Component upgrades > content.** Market research (Chroma Arcana): backers dislike content locked behind goals. Linen finish, foil, thicker boards, upgraded bits. Content goals (extra cards/scenarios) also risk scope creep and delay.
- **Golden goose:** one huge goal at 400–500% funding (#11; TMG's Ground Floor gave a free second game at $75k/500% — and raised another $38k after unlocking it).
- Price every goal into the unit cost *assuming it unlocks*; a goal that loses money per unit or delays delivery is a bug, not a gift.
- Visibility strategy: reveal one at a time / all without amounts / all with amounts — all three work if you stay flexible (#11). Social/milestone goals (backer counts, not money) build community (Viticulture), but don't hide reward levels behind them.

### G. Run the campaign

- **Launch day (#16):** take the day off; submit for platform approval days early; personal individual emails to friends/family — Stegmaier cites 50–70% click-through vs 2–10% for mass email; no asking-for-money, just "check it out"; FAQ live immediately; thank every early backer personally; end-of-day grateful update.
- **First 24–72h:** this is where pre-launch pays off. A fast fund signals quality to strangers and unlocks "funded" psychology. If you're not funding: fix page/rewards first (#95 steps 1–5), *then* outreach (6–10).
- **Update cadence:** every few days minimum during the campaign; backer-only updates for substance (#99); after posting an update, spend 30 minutes answering comments it generates (#90). No desperate share-begging — host a party, don't beg guests to bring friends (#95).
- **Mid-campaign slump (#95):** accept what's unfixable; change what backers are actually complaining about (shipping price, art); prune dead tiers; micro-goals; personal $1 appeals; value-first blogger outreach; targeted ads (BGG worked for Stonemaier).
- **Cross-promotion (#51):** swap update mentions with similar-scope live campaigns; only with projects you'd genuinely recommend.
- **Endgame:** 60-hour personal reminder to $1 backers (they don't get KS's 48h reminder, #113); final-48h surge is normal — have content ready for it.

### H. Shipping, VAT & tariffs

- Budget shipping at the **heaviest final configuration** (#12); the 4-lb USPS first-class threshold is the classic cliff. Single-game international shipping can exceed the game's price — Stegmaier's 2013 UK example: 1 game $53, 2 games $66, 4 games $92; group buys drop per-unit cost hard.
- **Regional-hub model:** freight in bulk to fulfillment partners per region (US, UK/EU, Canada, AU/NZ, Asia), ship to backers from inside the region. "EU-friendly" (Stegmaier's term, #212) = creator prepays VAT at the port so backers never see a customs bill.
- **VAT (#212):** EU ~21% average (rates 17–27% by country), charged on declared value = reward price + shipping. Since July 2021 the EU's €22 import exemption is gone and IOSS covers consignments ≤ €150; UK since 2021 requires seller-collected VAT on ≤ £135 consignments — post-Brexit UK and EU are *separate* VAT regimes, so a UK hub no longer serves the EU. Never mark as "gift" or under-declare — backers asking you to are asking you to break the law (#212).
- **Modern model (#266):** price the product only; charge shipping and taxes separately in the pledge manager. Lower product price = lower import taxes for backers; Greater Than Games' Jagged Earth page explains the VAT-on-shipping double-charge trap. Communicate this in the tier description and a dedicated page section.
- **GPSR (EU 2023/988, in force 13 Dec 2024):** crowdfunding rewards shipped to EU consumers count as distance sales (Art. 16) — you must appoint an **EU-established responsible person** (your EU hub or an authorized-representative service), put their name + address in the offer and on the product/label, keep a technical documentation file, and have recall procedures (Arts 4/19). Non-compliance risks border refusal and marketplace delisting.
- **EU EPR packaging:** Germany (VerpackG — register in LUCID *before* shipping), France, and Spain require extended-producer-responsibility registration and packaging-fee payment from distance sellers shipping to consumers; carriers/marketplaces enforce, and the incoming PPWR tightens this EU-wide. Register per destination country or confirm in writing that your fulfillment hub covers it.
- **Tariffs:** 2025 US tariffs on China-made games moved 20% → 145% within weeks, settling at 30% after a 90-day pause (May 2025) — charged on *manufacturing cost*, paid by the importer (you). Chroma Arcana faced a £15k surprise bill. 2026: the Supreme Court (*Learning Resources*) struck down the IEEPA tariffs and refunds of 2025 duties are being processed — creators who paid 54–145% in 2025 can pursue recovery via customs protests/liquidation review. The replacement regime is in flux: verify current rates before quoting landed cost [volatile]. Budget a tariff line, say on the page how you'll handle changes, and note BackerKit/Gamefound built tariff-collection tools in 2025.
- Detail math and worksheets: load `references/pledge-math.md`.

### I. Post-campaign

1. **Pledge manager** (BackerKit / Gamefound built-in / CrowdOx): opens ~2–4 weeks after the campaign; collects addresses, shipping fees, taxes, add-on upsell, and late pledges. Budget its fee (~5% of campaign funds + processing, varies [contested — check current rate cards]).
2. **Late pledges are real revenue:** Gamefound's 2024 aggregate was $71m pledge-manager/late-pledge vs $85m live campaigns; individual-campaign late-pledge uplift of 10–25% is the agency rule of thumb [contested]. Kickstarter added native late pledges in May 2024.
3. **Fulfillment buffer:** order ~3% extra units for lost/damaged (Stegmaier made 150 extra of 5,300 Euphoria games and burned through nearly all); minimize version/SKU count — wrong-version shipments are the top fulfillment error.
4. **Communicate on a schedule** (monthly minimum, every milestone); show production photos; if the timeline slips, say so early with the new date once, then hit it.
5. **Refunds:** honor them pre-fulfillment where you can; KS's own data/Stegmaier's money-back-guarantee experiment (#168) found refund requests rare when trust is high. A creator's obligation doesn't end at shipping — replacement parts forever.

## Key numbers & heuristics

| Metric | Value | Source |
|---|---|---|
| Platform + processing fees | ~8% + $0.20/pledge >$10; ~10% + $0.05 ≤$10 (5% platform + 3% Stripe / 5% micro) | Stegmaier #7 (KS/Stripe breakdown) |
| Full fee stack incl. PM, agency, taxes | 15–20% of raised | Chroma Arcana postmortem (BoardGameWire 2025) |
| Marketing agency commission | 15% of attributed sales + ad spend | Chroma Arcana postmortem |
| MSRP multiple | 5× manufacturing (Stegmaier #201); 5–6× landed cost (Mathe/Hoyt) — sources disagree on the base | Stegmaier #201; Mathe/Hoyt |
| Core reward price | MSRP − 40% + shipping subsidy, 9-ified → $30→$25, $40→$34, $50→$39, $60→$49, $80→$65–69 | Stegmaier #201 |
| Per-unit margin target | $20–30 before fees/sunk costs | Stegmaier #201 |
| Distributor discount post-campaign | 60% off MSRP | Stegmaier #266 |
| Funding-goal worked example (2013) | ~$39k cost for standard game @1,000+500 units; Viticulture goal $25k + $5k personal | Stegmaier #7 |
| Warm email list → backers | 5–10%+ [contested — agency folklore] | LaunchBoom-style planning heuristic |
| Personal vs mass email CTR | 50–70% vs 2–10% | Stegmaier #16 |
| Creator's own outreach share | 13% of Viticulture pledges | Stegmaier #26 |
| Early-bird max price gap | $5 | Stegmaier #62 |
| Golden-goose stretch goal | 400–500% of funding goal | Stegmaier #11 |
| EU VAT | ~21% avg (17–27%), on price + shipping declared value | Stegmaier #212 |
| EU import rules | €22 exemption abolished July 2021; IOSS ≤ €150; UK £135 separate regime | EU/UK 2021 VAT e-commerce rules |
| US tariffs on China-made games | 20%→145% peak (Apr 2025), 30% after May 2025 pause; IEEPA tariffs struck by SCOTUS 2026 — 2025 duties refundable via customs protest [volatile — verify current regime]; charged on manufacturing cost | BoardGameWire (Chroma Arcana); SCOTUS (Learning Resources) 2026 |
| Extra units for damages/losses | ~3% (150 of 5,300) | Stegmaier, Euphoria fulfillment |
| Kickstarter tabletop 2024 | $220m raised; 5,300+ funded projects; $41.4k avg/project | Kickstarter via BoardGameWire |
| Gamefound 2024 | $85m campaigns (+49%) + $71m PM/late pledges; 6 of top-10 most-funded tabletop campaigns | Gamefound via BoardGameWire |
| Ad ROI test case | $1k BGG ads strongly positive; £500 Reddit + £800 Google ≈ 0; Facebook best scalable channel | Stegmaier #26; Chroma Arcana |
| Campaign length | ~30 days; launch+end in same month | Stegmaier #133 |

## Common pitfalls

- **Launching without an audience** — the modal failure. Epoch: The Awakening: polished page, fair tiers, good art, ~1,000 subs, 36 BGG fans → cancelled and relaunched. Metric: if you can't name your day-one crowd, you don't have one.
- **Under-priced shipping** — Viticulture charged $20 international on a true $47/game cost (2013): a planned ~$20/unit loss. Creators who don't plan it go bankrupt politely.
- **Fee-stack blindness** — budgeting against the headline raise instead of the ~15–20% stack + taxes + refunds. Manifests as "we funded 8× and lost money."
- **Stretch-goal scope creep** — content goals that add design/testing/art you haven't finished; every goal delays delivery and eats the margin it was meant to celebrate (#11).
- **Deluxe/all-in BOM creep** — the premium tier accretes minis, foil, and extras until its unit cost approaches its price; the all-in tier is where margins go to die. Cost it like a separate product.
- **Early-bird winners & losers** — day-20 visitors see unfilled early-bird slots and read it as a failing project; reopening early birds burns the trust of the "winners" (#62).
- **Tier sprawl** — >6–8 tiers paralyze choice (Chroma Arcana's top mistake); nothing between $1 and core (#113).
- **"Free worldwide shipping" without hubs** — $40 game becomes an $85 landed cost with VAT on arrival (#212); backers blame you, not customs.
- **Gift/under-declared customs** — illegal, and the fine lands on you or your backer (#212). No exceptions.
- **Tariff surprise** — 2025's 20→145% swing in weeks; campaigns that pre-sold "shipping included" ate five-figure bills or charged backers retroactively (CMON, Chroma Arcana). The regime stayed in flux into 2026 (IEEPA struck by SCOTUS, refunds in process) — verify current rates and your refund eligibility, don't assume 2025 rates.
- **Panic pivot mid-slump** — changing goal/price/title mid-campaign reads as desperation; fix the page and tiers, not the identity (#95).
- **Post-campaign silence** — the #1 driver of refund demands and chargebacks; monthly updates even when the news is "nothing moved."
- **Hiring a campaign agency as a substitute for a crowd** — 15% commission buys amplification, not salvation (#138; Chroma Arcana still needed its own list).

## Reference files

- `references/campaign-checklist.md` — Load when planning or running a live campaign: week-by-week timeline from T−6 months to delivery, full page-anatomy checklist, update cadence calendar, endgame and post-campaign checklists.
- `references/pledge-math.md` — Load when computing the funding goal, pricing tiers, building the shipping table, or budgeting VAT/tariffs: goal worksheet, tier-pricing table, shipping/VAT declared-value math, fee-stack model, worked examples.

## Related skills

- `board-game-manufacturing` — unit cost, MOQ, freight, compliance: the inputs to goal math.
- `board-game-market-analysis` — MSRP positioning, comparable titles, distribution economics post-campaign.
- `board-game-publishing` — licensing vs self-publishing decision that precedes any campaign.
- `board-game-prototyping` — review prototypes, PnP kits for previews, TTS/Screentop demos.
- `board-game-playtesting` — the playtester pool that becomes day-one backers.
- `board-game-theme-narrative` — art direction and naming that the project page sells.
- `board-game-accessibility` — language independence and component legibility that widen the backer pool.
