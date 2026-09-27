# Market Size, Segments & Trend Radar

Load this file when the user asks how big the market is, whether a segment is growing, for solo-demand evidence, or for a trend check. Every figure carries source, year, and caveat — market-size numbers in this industry are estimates with opaque methodologies; never present one as precise.

## 1. Market size estimates (flag uncertainty; cite scope)

| Figure | Scope | Year | Source | Caveat |
|---|---|---|---|---|
| $7.2B | Global tabletop games | 2017 | Statista via Wikipedia | Methodology opaque; projected +$4.8B over 6 yrs [contested] |
| ~$75M | US/Canada hobby-*channel* board games | 2014 | ICv2 | Hobby channel only (FLGS/hobby distribution), excludes mass retail and TCGs |
| >$700M → ~$900M | Total US/Canada hobby game market (incl. RPGs, minis, TCGs) | 2014 → 2015 | ICv2 | TCGs (Magic, Pokémon) dominate this total; board games are a minority slice |
| $233M | Kickstarter tabletop-game pledges | 2020 | ICv2 via Wikipedia | Pledges ≠ retail revenue; 2020 was a pandemic peak |
| €1.287B | Asmodee Group revenue (largest pure-play hobby publisher; includes its distribution business) | 2024 | Asmodee Q3 FY24/25 interim report via Wikipedia | Company scale anchor, not market size |
| 25-40%/yr | Board game market growth | 2010-2014 | Guardian-cited estimate | [contested/dated] — pre-2015 boom years; do not extrapolate |
| >$1.2B / ~$800M | Historical anchors: global 1991 / US 2009 | 1991/2009 | via Wikipedia | Context only |
| $13-19B | "Global board game market" | 2020s | SEO market-research firms | [contested] — usually fold in all mass-market toys/cards; unusable for hobby decisions |

Structural supply fact: >5,000 new titles/year entered BGG by 2016 — the bottleneck is attention and shelf space, not demand. This is why comp analysis (see `comp-title-method.md`) beats TAM arithmetic.

## 2. Segment norms (full table)

Weights are BGG community-voted (community consensus, drift ±0.3); MSRPs are US list prices circa 2022-2025 — verify before quoting as current.

| Segment | Weight | MSRP band | Session | Primary buyer | Exemplars (MSRP) |
|---|---|---|---|---|---|
| Kids | 1.0-1.5 | $10-25 | 10-30 min | Parents/gift | Sleeping Queens ($12), Outfoxed! ($20), Dragomino ($25), My First Castle Panic |
| Party | 1.0-1.5 | $20-35 | 15-60 min | Social/gift, big-box retail | Codenames ($25), Just One ($25), So Clover! ($25), Wavelength ($35), Time's Up ($20) |
| Gateway | 1.5-2.3 | $30-55 | 30-60 min | New-to-hobby, gift | Azul ($40), Carcassonne ($40), Ticket to Ride ($55), Catan ($55), Splendor ($46) |
| Family | 1.8-2.5 | $30-60 | 30-75 min | Family/household | Kingdomino ($25), Cascadia ($40), Quacks ($55), King of Tokyo ($45) |
| Hobbyist euro | 2.5-3.8 | $50-80 | 60-150 min | Hobbyist | Wingspan ($60), Everdell ($65), Terraforming Mars ($70), Ark Nova ($75), Brass: Birmingham ($70) |
| Thematic / Ameritrash | 2.5-3.5 | $60-110 | 60-180 min | Hobbyist (theme-first) | Betrayal 3E ($56), Mansions of Madness 2E ($110), Zombicide ($110) |
| Wargame | 3.0-4.5 | $50-130 | 90-360 min | Grognard niche; GMT P500 preorder model (see SKILL.md §D) | Undaunted: Normandy ($50), Twilight Struggle ($65), Memoir '44 ($55), Commands & Colors |
| LCG / expandable card game | 2.9-3.4 | $40-70 core + ongoing spend | 60-120 min | Committed hobbyist; ecosystem revenue model | Arkham Horror LCG ($60 core), Marvel Champions ($70 core) |
| TCG / CCG (booster model) — out of scope for this skill | 2.5-3.5 | Booster/rarity economics, not MSRP bands | varies | Committed hobbyist + collector | MTG, Pokémon — rarity-driven pack margin structure, organized-play budgets, allocation-based specialty distribution; the most capital-intensive category in the industry; this skill's pricing/margin economics do not apply |
| Solo-focused | any | +$0-15 premium vs base | varies | Hobbyist; see §3 | Friday ($20), Onirim ($25) solo-natives; built-in automa modes elsewhere |
| Big-box / minis (crowdfunding-native) | 3.0-4.5 | $100-150+ | 2-5 hrs | Crowdfunding superfans | Gloomhaven ($140), Frosthaven, CMON/Awaken Realms campaigns |

Price-band anchor points (Stegmaier): evergreen retail sweet spot $40-60; small card game band $20-30 [community consensus]; big-box $70-100+. Mathe KS anchors (2013, inflate): card game $9-19; light family/party $20-39; standard 3-lb game $50-60; big-box ≤$99.

Tinsman's four markets (*The Game Inventor's Guidebook*): mass market, hobby games, American specialty, European games. Gateway/family/party sell through mass + specialty channels; euro/ameritrash/wargame/collectible through the hobby channel (distributors → FLGS/online hobby retail).

## 3. Solo demand evidence

- Stonemaier publishes nothing without a robust Automa Factory solo mode; their line is "Euro games that play 1-5 players" — solo is a market requirement in hobby euro segments, not a feature.
- Tuscany KS poll (n=117): 42.7% called solo at least somewhat important to backing. Tiny Epic Galaxies poll (n=3,251): solo beat a 5th-player option.
- BGG share of solitaire-playable titles: ~10% (mid-1990s) → ~20% (2015); 1 Player Guild was BGG's 4th-largest guild (2015).
- Counterpoint (2025): Tokaido (~88,736 copies in circulation, ~10% estimated primarily-solo) sold only 233/5,000 standalone solo packs at launch — **built-in solo sells games; retrofit solo products sell poorly.**
- Implementation can be cheap: Viticulture's Automa = 24 cards + 2 rulebook pages (design: `board-game-solo-coop-design`).

## 4. The evergreen study (Stegmaier 2022, n=21 — survivorship analysis)

Method: titles with ≥3 appearances across years on ICv2 hobby-channel top-10 lists plus one online retailer's data (pre-2022 vintage). Profile of the modal evergreen: **2-4 players, ~45 min, medium weight, ~$50, easy to teach/learn/set up.** Caveats: this is survivorship data — all 21 titles were already successful, so the profile describes winners, not the odds of joining them; the ~$50 price anchor has inflated since (the gateway evergreen class now lists ~$55-60 and drifting) — re-date it for the current year; and the modal profile structurally excludes party, kids, wargame, and 2p-duel categories, where different norms define success. Distribution stats: 6/21 solo modes; 15/21 competitive vs 6/21 co-op/team; 11/21 rulebooks ≤9 pages; 6/21 crowdfunded; 7/21 Spiel des Jahres winners; 5/21 IP-based; 11/21 bright/playful art. Use as a deviation checklist: every way the design departs from this profile should be deliberate.

## 5. Trend radar (dated; reassess yearly)

| Trend | Status | Exemplars / evidence | Risk note |
|---|---|---|---|
| Solo modes as table stakes | Structural (not a fad) | §3; Automa Factory standard | Bolt-on solo underperforms; retrofit packs flop (Tokaido 2025) |
| Legacy / campaign formats | Established niche | Risk Legacy (Daviau, 2011), Pandemic Legacy (Daviau/Leacock, 2015), Charterstone (2017), Gloomhaven (2017) | "Experiential, not repeatable" (Daviau); higher design/art cost; retail re-order friction |
| App integration | Bifurcated | Mansions of Madness 2E (2016), XCOM (2015), Chronicles of Crime (2018), Descent: Legends of the Dark (2021) | Platform-dependence, app-maintenance cost; hobbyist reception splits [contested] |
| Deluxification | Structural in crowdfunding; resisted in retail | Stegmaier "Deluxe Dilemma" (2020); retailer dislike of publisher-exclusive deluxe | Breaks distribution economics (Scythe mechs); SKU proliferation |
| Tarot-sized cards (70×120mm) | Growing [community-observed] | Ark Nova (2021); PrintNinja/Panda list tarot as standard size | Higher cost/deck, fewer cards/sheet; non-standard sleeves |
| Digital try-before-you-buy & tutorials | Structural | BGA topped Stonemaier's 2025 platform survey; Tabletopia demos; Dized interactive tutorials | Discoverability ≠ conversion; digital versions cannibalize poorly-understood |
| Crowdfunding as marketing channel | Structural | KS tabletop $233M (2020); Gamefound rising; publishers launch retail-bound titles on KS first | Campaign success ≠ retail sell-through; fee/fulfillment stack ~15-25% of pledges all-in |
| Cost/tariff pressure | Acute (2025+) | +54% US tariffs on Chinese goods (Stegmaier 2025); freight volatility | MSRP drift upward; margin compression at every chain node |
| Sustainability specs | Growing (EU-led) | FSC paper/wood, paper-pulp trays, plastic-free packaging demanded by backers and EU retailers | Must be specified at RFQ; retrofits fail (see `board-game-manufacturing`) |

Radar rule: a trend changes *distribution and positioning* facts (what buyers expect included, what retailers stock, what price reads as fair). It never substitutes for design quality — the graveyard of legacy-app-solo-tarot bolt-ons is large.

## 6. Reading-the-market rituals (recommend these to users)

- Track ICv2 hobby-channel top-10 lists quarterly (evergreen detection).
- Watch BGG "The Hotness" and ratings velocity after Spiel/Essen and Gen Con release waves.
- Note Spiel des Jahres / Kennerspiel winners — the single strongest family/gateway sales accelerant (7/21 evergreens are winners).
- Read publisher print-run/reprint announcements: reprints are the only public proof of sell-through.
- Stonemaier's blog data posts (demographic surveys, platform surveys) for buyer-behavior baselines (58% buy primarily retail, 2024).
