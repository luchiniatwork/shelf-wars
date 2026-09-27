# Comparable-Title Analysis Method

Load this file when running an actual comp-title scan for a user's design. The goal is not to prove the game will sell — it is to locate the design in a real competitive field and extract four outputs: **MSRP band, weight/length target, player-count target, and the gap the design can own.**

Data caveat: BGG figures below are community-voted values captured circa 2024-2025 and are approximate (BGG rank and ratings drift monthly; weights drift ±0.3). Verify live values on boardgamegeek.com before quoting them to a third party as current fact.

## The procedure

1. **Fix the design's coordinates first**: segment, weight estimate, player count, session length, component class (cards-only / cards+board / board+bits / minis). You cannot pick comps without these.
2. **Pick 5-10 comps**: same segment, BGG weight within ±0.5 of the design, similar component class, published within ~5 years — unless deliberately benchmarking an evergreen (then include it knowingly).
3. **Record per comp**: title, year, publisher (and tier), BGG rank, ratings count, weight, MSRP + street price, players, time, notable accelerants (award wins, license, review coverage, crowdfunded).
4. **Detect evergreens**: ≥3 appearances across years on ICv2 hobby-channel top-10 lists, or persistent BGG top-200 rank ≥3 years after release (Stegmaier's method). Evergreens set the *ceiling* expectations; recent hits set the *entry* bar.
5. **Read velocity, not just stock**: a 2023 title with 20k ratings is healthier than a 2015 title with 35k. Stonemaier's internal health signal: 1,000 ratings in one month. Ratings counts are relative signals only — community ratings-to-sales ratios (3-10×) are folklore [contested].
6. **Find the gap**: a price point, weight band, player count, theme, or component promise the cluster underserves. You position into the gap; you do not position into the densest cluster and out-shout it.
7. **Write the outputs down** before touching the pitch: "MSRP $50-60, weight 2.0-2.5, 1-4 players, 45-75 min, gap: mid-weight nature engine-builder under $60 with solo included."

## How to read each metric

| Metric | What it actually tells you | How it misleads |
|---|---|---|
| BGG rank | Bayesian-averaged hobbyist esteem; top 1,000 ≈ durable hobby visibility | Biased toward heavy games; old games accumulate votes; rank ≠ units sold |
| Ratings count | Rough installed-base proxy; velocity = current health | Party/family games under-index (buyers don't rate); hobbyist games over-index |
| Weight (1-5) | Community-voted complexity; defines the buyer's tolerance | Genre-relative (a 3.2 party game reads as broken; a 3.2 euro reads as normal) |
| MSRP vs street | MSRP = positioning; street (often 15-25% under) = what buyers actually pay | Deep-discount street price can signal channel overstock, not popularity |
| Publisher tier | Distribution muscle, marketing reach, evergreen likelihood | Tier inflates expectations; an indie hitting tier-1 numbers is a stronger signal |
| Player count / time | Fit to use occasions (family night vs game day) | Box claims lie (solo modes, optimistic times); check BGG "best" player counts |

## Publisher tiers (working heuristic — no official taxonomy)

| Tier | Who | What it means for comps |
|---|---|---|
| Mass/hobby giants | Asmodee Group (€1.287B revenue 2024; owns Fantasy Flight, Z-Man, Days of Wonder, Repos, Catan Studio), Hasbro (Avalon Hill, Wizards), Ravensburger, Mattel, Spin Master | National distribution, mass-channel access; their hits set category price anchors |
| Large hobby specialist | CMON, IELLO, Czech Games Edition, Stronghold, Portal, Awaken Realms (crowdfunding-first), GMT (wargames, P500 model) | Deep FLGS/distribution reach; crowdfunding-native ones set KS price expectations |
| Mid | Stonemaier, AEG, Plan B/Next Move, North Star, Capstone, Leder Games, Roxley, Flatout | The realistic aspiration tier for a new entrant's comps; strong direct+retail hybrids |
| Small/indie | Foxtrot Games, Button Shy (wallet-game niche), self-publishers | Survival-tier economics; their numbers show the floor, not the ceiling |

## Worked example: mid-weight nature engine-builder

Scenario: a user's design is a 60-90 min, 2-4 player, nature-themed tableau/engine-builder, cards+board+bits, targeting hobbyist-family crossover. Scan (approximate 2024-2025 values — verify live):

| Title (year, publisher, tier) | BGG rank | Ratings | Weight | MSRP | Players / time | Accelerant |
|---|---|---|---|---|---|---|
| Wingspan (2019, Stonemaier, mid) | ~#30 | ~97k | 2.47 | $60 | 1-5 / 40-70m | SdJ Kennerspiel 2019; evergreen |
| Cascadia (2021, Flatout/AEG, mid/giant) | ~#60 | ~50k | 1.85 | $40 | 1-4 / 30-45m | SdJ 2022 winner; evergreen |
| Ark Nova (2021, Feuerland/Capstone, mid) | ~#4 | ~50k | 3.74 | $75 | 1-4 / 90-150m | Hobby-darling velocity; tarot-sized cards |
| Terraforming Mars (2016, FryxGames/Stronghold, large) | ~#10 | ~88k | 3.25 | $70 | 1-5 / 120m | Evergreen; expansion ecosystem |
| Everdell (2018, Starling, small) | ~#70 | ~52k | 2.82 | $65 | 1-4 / 40-80m | Deluxe component showcase |
| Azul (2017, Plan B/Next Move, mid) | ~#90 | ~82k | 1.77 | $40 | 2-4 / 30-45m | SdJ 2018; evergreen |
| Quacks (2018, Schmidt Spiele/North Star, large) | ~#110 | ~40k | 1.94 | $55 | 2-4 / 45m | SdJ nominee 2018 |

### Reading the scan

- **Price structure**: the cluster brackets at $40 (light gateway end: Azul, Cascadia) and $60-75 (engine-builder end: Wingspan $60, Everdell $65, TM $70, Ark Nova $75). A 60-90 min engine-builder at 2.0-2.5 weight prices at $50-60, not $75 — $75 is the ceiling reserved for heavier games with bigger component payloads (Ark Nova's tarot-sized cards, TM's 200+ cards and player boards).
- **Weight structure**: every durable seller at this session length sits at 2.4-2.9 weight or below. Above ~2.9, expected session time in the cluster rises to 90-150 min. If the design wants 60-90 min, hold weight ≤2.7.
- **Evergreen profile check**: Wingspan and Cascadia both confirm Stegmaier's n=21 profile (2-4+ players, ≤70 min, medium-or-lighter weight, $40-60, easy teach) — and both include solo modes. Ark Nova succeeds *while violating* the profile on weight/time/price — an outlier carried by hobby press, not a template.
- **Gap hypothesis**: between Cascadia ($40, 1.85 weight, 45 min) and Wingspan ($60, 2.47, 70 min) there is a $50 / ~2.1 weight / 45-60 min slot with no dominant nature-themed occupant. Positioning sentence writes itself from this row.
- **Velocity check**: Ark Nova reaching ~50k ratings in ~3 years vs Terraforming Mars ~88k in ~8 shows what breakout velocity looks like (well past the 1,000-ratings/month health line); Everdell shows that strong component craft sustains a small-tier publisher in the same bracket.

## Scan failure modes

- **Outlier anchoring** — benchmarking against Gloomhaven/Frosthaven/Ark Nova as if they were the segment norm. They are the top 0.1%: include at most one, labeled "ceiling".
- **Cross-segment comps** — pricing a party game against a big-box euro; segments have independent price gravity.
- **Rank without velocity** — a high-rank 2012 title reflects accumulated ratings, not current demand; always pair rank with ratings velocity and evergreen detection.
- **Box-claim naivety** — trusting printed player counts/times; use BGG "best" player-count votes and community session times.
- **Counting Kickstarter hype as retail demand** — a funded campaign proves crowdfunding demand only; check whether the title got distribution follow-through (reprints, ICv2 appearances) before treating it as a retail comp.
- **Ratings-to-sales multiplication** — any "units = ratings × k" arithmetic is folklore [contested]; use ratings comparatively.

## Sources

- Stegmaier, "Evergreen Games: What Do They Have in Common?" (2022) — ICv2 top-10 + retailer-data method, n=21 profile; "A Price Formula for Your Product" (2022) — comp benchmarking as pricing input.
- Stonemaier ratings-velocity tracking (1,000 ratings/month health signal).
- Tinsman, *The Game Inventor's Guidebook* — four-market segmentation.
- BGG community data conventions (rank, ratings, 1-5 weight) [community consensus].
- Asmodee Q3 FY24/25 interim report via Wikipedia — publisher-tier scale anchor.
