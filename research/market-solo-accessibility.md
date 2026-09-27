# Research Digest — MARKET ANALYSIS, SOLO/CO-OP DESIGN & ACCESSIBILITY

Research note: mainstream search engines and BoardGameGeek were blocked/degraded in this environment. Research used site-internal WordPress REST search APIs of canonical publisher/designer/manufacturer blogs (Stonemaier Games, League of Gamemakers, Meeple Like Us, Board Game Design Lab, Foxtrot Games, PrintNinja), the Wikipedia API, and direct page fetches. 35+ queries run; 20+ full pages fetched and extracted. Community-consensus claims not independently verifiable this session are flagged.

## Core frameworks & models

- **The 5× landed-cost rule — Randy Hoyt (Foxtrot Games, 2016), endorsed by Jamey Stegmaier (Stonemaier, "The Myth of MSRP", 2013).** To sell through distribution and fund a second printing, MSRP must be ≥5× total *landed* cost (manufacturing + freight/customs to warehouse), not just manufacturing cost. At 5× you must sell ~50% of the print run to recoup; selling out nearly doubles your money but only just funds the reprint.
- **The $10→$20→$25→$50 supply-chain baseline — Stegmaier, "The Math of Tariffs" (2025).** Publisher pays manufacturer $10 → distributor pays publisher $20 → retailer pays distributor $25 → consumer pays $50 MSRP. The retailer's 2× markup covers discount wiggle room, inventory risk (shelf stock is pre-paid cash), overhead, staff.
- **Stegmaier price-formula components (2022):** landed cost (manufacturing at 5,000-unit pricing + freight), royalty, sunk costs (art, graphic design, diecuts, molds — first print run only, if counted), parcel shipping, subsidized customer shipping fee, ongoing discounts. Start at manufacturing ×5, adjust for freight/royalty; go 6–8× (or 5× on landed cost) when value warrants; design *to* a target price early.
- **Tinsman's four markets — Brian Tinsman (*The Game Inventor's Guidebook*), via Wikipedia.** Mass market, hobby games (RPGs, miniatures, TCGs), American specialty, European games. Gateway/family/party sit in mass+specialty; euro/ameritrash/wargame/collectible sit in hobby.
- **Automa doctrine — Morten Monrad Pedersen (Automa Factory; via Stonemaier guest post, 2015).** A solo mode should feel like the original game: same choices, goals, win/lose criteria. Ask "which features of the other player's *presence* are core?", mimic only those with a simple deck-driven "AI", abstract everything else (Viticulture: automa randomly blocks action spaces but gains no benefits; its vineyard is abstracted to a predetermined points-per-turn track). Stegmaier: "an AI system in cardboard form."
- **The "Pandemic problem" (quarterbacking/alpha player) — named by Mike Selinker (2016).** One player runs the game for everyone; "a good co-op design knows this is a possibility and figures out something that gets in the way of that." (Didn't originate with Pandemic.)
- **Win-rate calibration targets — League of Gamemakers expert panel (2016) + Matt Leacock interview (2017).** Hawthorne: ~70% win rate per story chapter (with fast-lose mechanisms for retry). Trzewiczek (Robinson Crusoe): first win on ~4th–5th play; each loss teaches a specific threat. Leacock: "a good chance you will lose on your first try" at appropriate difficulty; Pandemic Legacy targets 2:1 win:loss (campaigns can't be freely retried). Selinker: match genre expectations.
- **Meeple Centred Design (MCD) — Heron, Belford, Reid & Crabb (2018), *The Computer Games Journal* 7(2), open access; operationalized at Meeple Like Us.** Teardown across 8 categories: Colour Blindness, Visual, Cognitive (fluid intelligence + memory), Physical, Emotional, Communication, Socioeconomic, Intersectional. Graded A–F (A=14, B=11, C=8, D=5, E=3, F=0). Authors' caveat: grades are "theorycrafted" heuristics from an abled perspective, not embodied experience.
- **Stegmaier accessibility lens list (2022):** Learning, Retention, Time, Visuals, Presence, Language, Purchase, Scope (player counts), Inclusion, Physicality — a game can be accessible without checking every box.
- **Legacy/campaign model — Rob Daviau (Risk Legacy 2011; Pandemic Legacy S1 2015 with Leacock).** Permanent change across sessions; "experiential, not repeatable"; three-act story structure.
- **Evergreen profile — Stegmaier (2022), from ICv2 hobby-channel top-10 lists + Game Nerdz data, n=21.** Surface profile: 2–4 players, ~45 min, medium weight, ~$50, easy to teach/learn/set up.

## Catalog / techniques

**Pricing & distribution economics**
- MSRP is *chosen*, not assigned: benchmark comparable published products in your category, then sanity-check against 5× landed cost (Stegmaier). Recommend backers get 10–20% off MSRP on Kickstarter.
- Worked example (Stonemaier, Tuscany): $6.50 manufacturing + $3.00 freight = $9.50 landed → $35 MSRP; distributor buys at 60% off ($14) → $5.50/unit publisher profit; same unit sold direct to a Champion member yields $14/unit. $5.50 alone can't fund a reprint — direct sales subsidize distribution margins.
- Discount structure: distributors ~60–65% off MSRP (2013 figure: pay 40% of MSRP); direct retailers ~45–50% off. Direct sales shift margin to the publisher but add warehousing/fulfillment (~$20 fulfillment cost vs. ~$10 charged shipping) and forfeit evergreen reach — Stonemaier 2024: ~55% of sales to distributors/retailers, <30% direct; 58% of survey respondents buy primarily from retailers.
- Products that can't survive distribution economics go direct-only (Scythe metal mechs would need >$100 MSRP in distribution). Deluxe/standard dual-SKU strategies add a third SKU (upgrade pack); Stegmaier's preference: one deluxe-feeling standard box + à-la-carte add-ons (retailers dislike publisher-exclusive deluxe versions).
- Post-Kickstarter sell-through (PrintNinja): keep selling from the KS page (edit it on the final day — it freezes after close), open a webstore immediately, pursue retail with retail-standard packaging.

**Comparable-title analysis method**
- Benchmark by category and components (custom pieces ≈ price band). Track evergreen comparables via ICv2 top-10 hobby-channel lists (retailer/distributor/manufacturer interviews) + one online retailer's data; ≥3 appearances across years = evergreen (Stegmaier's method).
- Community metrics used in practice: BGG rank, ratings count and velocity (Stonemaier tracks "1,000 ratings in one month" as a health signal), BGG complexity weight 1–5 (MLU teardowns cite it, e.g. Quacks "Medium Light [1.94]") [BGG unreachable this session — scale convention is community consensus], price/MSRP, publisher tier.

**Solo/automa design techniques**
- Implementation cost can be tiny: Viticulture Automa = 24 cards + 2 rulebook pages; viable as a stretch goal. Filler games may use beat-your-own-score; on longer games that "feels like an optimization puzzle, not a game." Difficulty via automa levels (predetermined scoring tracks). Solo doubles as a learn-the-game mode.
- Solo is now a design constraint, not an add-on: Stonemaier "wouldn't publish a game without a robust solo mode from Automa Factory" and focuses on "Euro games that play 1–5 players."

**Co-op design techniques**
- Quarterbacking mitigations (named + source): encourage self-interest — Selinker (Betrayal: anyone may become the traitor; Pathfinder ACG: your deck is yours long-term); physical ownership of randomizers — Leacock (Pandemic: The Cure dice: "I've never seen a player reach across the table and roll another player's dice"); hidden information, possibility of a traitor — Leacock (notes these change the game's nature); asymmetric skill sets so each player gets "moments of glory" — Hawthorne; timer pressure + confined action area — Hawthorne; limited communication; adjacency-gated advice (League "I, Alpha Gamer" experiment); quick, simple subsystems + rulebook text encouraging group decisions (group decisions are slow).
- Anti-predictability: variety of enemies/subsystems/scripted encounters (Hawthorne); "randomness kills routine" — dice/event engines defeat the "eurogamer who calculated all odds" (Trzewiczek); different victory conditions, headaches, resources every game (Selinker).
- Pandemic's escalation engine (exemplar): Epidemic cards (a) advance the infection-rate track, (b) put 3 cubes on a bottom-deck city, (c) reshuffle the infection discards *back on top* of the deck — hot cities recur, tension ratchets, alternating "waves of hope and fear" (Leacock). Three lose conditions (8 outbreaks, cube supply out, player deck-out) vs. one win condition. Difficulty dial = number of Epidemic cards. Roles balanced by benchmark ("stronger than the Medic?"), designed "impossibly strong on paper, then reined in."
- Co-op playtest method (Leacock): watch, don't ask — engagement (phones vs. leaning in), confusion points, the words players use for objects, errors (maybe rules should match how players think). Remote testers upload timestamped video. "Was it fun?" questionnaires are "for the most part, a waste of time."

**Accessibility techniques**
- Colorblind-safe: never use colour as the sole channel; double-code with icons/shapes/art (Quacks ingredient books double-coded; its un-iconed score tokens criticized); test in low light (Viticulture's red confused with orange/purple); evaluate all four MLU-graded types: protanopia, deuteranopia, tritanopia, monochromacy; accessible *out of the box* — "players should not be expected to deface their games" (MLU). Tools: ColorSym/ColorADD-style icon systems, palette simulators.
- Vision: strip clutter; darker/bigger icons; rules text larger, higher contrast, black-on-white even over a color swatch (Wingspan Vision-Friendly Card Packs, built with accessibility consultants after readability complaints). Typography hierarchy (League): illustrative/logo > functional (biggest, boldest, highest contrast — glanceable like Uno corners) > header > descriptive (plainest face) > flavor (smallest/italic). ≥1em margins; no light-on-dark beyond ~5 words; never auto-justify; tune leading/kerning.
- Cognitive load (MLU lenses): required literacy, game-state complexity/coupling, memory needed to play at all/effectively/well, game-flow consistency, number of token types and consistency of meaning, rules synergy depth, scoring numeracy, external general knowledge, multitasking. Quacks passes partly because a teachable rule of thumb ("4 whites out = safe next draw") replaces live arithmetic — teachable heuristics are an accessibility feature.
- Physical/dexterity (MLU lenses): conventional card sizes; textured/heavier tokens; minimize reaching and manipulation frequency; fully playable by *verbal instruction* to another player (the key dexterity-free fallback); no required physical acting; avoid paper money ("inaccessibility wall to wall"); sparse, large target zones.
- Emotional (MLU lenses): challenge vs. frustration, despair-by-design (expected-loss games), arbitrary/uncontrollable fates, bluffing/lying demands, pattern-closure needs, "take that" (binds frustration to a person), upsetting themes/trauma triggers, player elimination (exclusion grows with game length), incentivized ganging-up.
- Socioeconomic & inclusion: price and business model (collectible elements, assumed expansions) are accessibility issues (MLU); representation across age/gender/ethnicity/sexuality/disability, cultural consideration, no oversexualization (Stonemaier inclusion category, DEI-consultant reviewed); language independence = icon-driven play with supportive (not load-bearing) text + localized editions + no across-the-table text; libraries/try-before-you-buy count as purchase accessibility.
- Digital as accessibility vector (Stonemaier 2026): Dized-style interactive tutorials, Tabletopia try-before-you-buy, Board Game Arena (top platform in their 2025 survey, then Steam). Trend radar: solo modes as table stakes, legacy/campaign formats, app/digital integration, deluxification (with the distribution caveats above).

## Numbers, heuristics & rules of thumb

- **Market size:** tabletop industry ≈ $7.2B (2017, Statista via Wikipedia), projected +$4.8B over 6 years. Hobby-channel board games US/Canada ~$75M (2014); total "hobby game market" >$700M (2014), ~$900M (2015). Kickstarter tabletop pledges: $233M in 2020. Anchors: global >$1.2B (1991); US ~$800M (2009). Guardian-cited 25–40%/yr growth 2010–2014 [contested/dated — methodology opaque].
- **Pricing bands:** evergreen retail sweet spot $40–60 (Stegmaier); Stonemaier accessibility target $40–70; small expansions ~$35 (Tuscany); add-on packs ~$10 (Tokaido solo pack); big-box/minis $70–100+ (Scythe mechs >$100 forced direct-only). Party/kids sub-bands and the $20–30 small-card-game band: **[community consensus; not independently sourced this session]**.
- **Margins/discounts:** distributors pay 35–40% of MSRP (60–65% off); direct retailers 50–55% of MSRP (45–50% off); KS backer discount 10–20% off MSRP; demo copies ~75% off wholesale per $500 order + $15 pre-release demos (Stonemaier 2025 program).
- **Cash-flow math at 5×:** sell ~50% of print run to recoup; sell out to nearly double (funds reprint only). At 4.16× manufacturing (ignoring freight): 84% sell-through to recoup, ~8 printings to self-fund (Hoyt; "very few games sell 16,000 copies"). "Most games sell the majority of what they'll ever sell in the first three months" — Hoyt, flagged as industry hearsay.
- **Solo demand:** Tuscany KS poll (n=117): 42.7% called solo at least somewhat important to backing; Tiny Epic Galaxies poll (n=3,251): solo beat a 5th-player option; BGG solitaire-playable share rose ~10% (mid-1990s) → ~20% (2015); 1 Player Guild = 4th-largest BGG guild (2015). Counterpoint (2025): Tokaido, 88,736 copies in circulation, ~10% estimated primarily-solo, yet only 233/5,000 standalone solo packs sold at launch — built-in solo sells games; retrofit packs sell poorly.
- **Win-rate dials:** ~70% win rate per chapter (Hawthorne); first win on play 4–5 (Trzewiczek); 2:1 win:loss for legacy campaigns (Leacock/Daviau); "good chance you lose on your first try" at matched difficulty (Leacock).
- **Evergreen stats (n=21):** 6/21 solo modes; 15/21 competitive vs. 6/21 co-op/team; 11/21 rulebooks ≤9 pages; 6/21 crowdfunded; 7/21 Spiel des Jahres winners; 5/21 IP-based; 11/21 bright/playful art.
- **Accessibility prevalence:** congenital color-vision deficiency ≈ 8% of men, 0.4–0.5% of women (Northern European ancestry; protan/deutan most common; global rates vary — Wikipedia). MLU corpus (n=116 paper, ~155 site): average Colour Blindness grade B (10.92, SD 3.30) — the median hobby game is merely "recommended with small issues." >5,000 new titles/yr entered BGG (2016); MLU covers ~9–10% of the BGG Top 500/yr.
- **Session-time targets (Stonemaier accessibility):** setup ~5 min, play 45–90 min, cleanup ~5 min.
- **Channel split (Stonemaier 2024):** ~55% distribution/retail, <30% direct, rest localization (see worked margins above).

## Best-practice checklists

**Price a game (Hoyt + Stegmaier):**
1. Compute landed cost/unit (manufacturing at realistic quantity + freight/customs).
2. Benchmark MSRP against comparable published games in category/components.
3. Verify MSRP ≥ 5× landed cost — else raise MSRP, cut costs, or skip distribution.
4. Pad for volatility (freight, exchange rates); set royalty + sunk-cost recovery policy.
5. Set KS reward 10–20% under MSRP; choose direct/retail/hybrid channel strategy (each is a different margin formula).

**Comparable-title scan:** pick 5–10 recent same-segment titles; record BGG rank, ratings count/velocity, complexity weight, MSRP/street price, publisher tier, player count/time; identify evergreens (ICv2 appearances); design and price to the gap.

**Solo mode (Automa Factory procedure):** 1) Keep multiplayer's win/lose criteria and core choices. 2) List which opponent-presence features are core (blocking, competition, score race). 3) Deck-drive exactly those; abstract everything else. 4) Minimize upkeep — one card flip per automa turn; predictable-but-varied. 5) Ship 3+ difficulty levels (scoring-track or deck-composition dials). 6) Don't cut major systems — that's a second game, not a solo mode.

**Co-op design (Hawthorne's checklist + panel):** make cooperation *required* for success; tension greater than any one player can manage; every player gets moments of glory via asymmetric skills; build anti-quarterbacking structure (self-interest, hidden info, physical ownership, limited communication, time pressure); keep subsystems quick/simple (group decisions are slow); rulebook text encouraging group decisions; variety engines against puzzle-solve staleness; fast-lose states so failed runs end quickly; calibrate difficulty dial + target win rate; watch playtests rather than polling "was it fun."

**Accessibility pre-flight pass:**
- Colour: no colour-only information anywhere; double-code all categories; simulate protan/deutan/tritan/mono; test in low light.
- Vision: functional type biggest/boldest; high contrast (black-on-white for rules text); no light-on-dark beyond ~5 words; ≥1em margins; no auto-justification; minimal clutter.
- Cognitive: consistent iconography; chunk rules into phases; player aids; teachable heuristics replacing arithmetic; minimal exceptions; few token types/meanings.
- Physical: verbal-instruction playable; conventional card sizes; grippable tokens; no forced reaching; no paper money; no mandatory dexterity/acting without alternatives.
- Emotional: check elimination, take-that, ganging-up, despair-by-design, upsetting content; offer catch-up or fast-loss exits.
- Communication: minimal required literacy; no essential audio cues without visual alternatives.
- Socioeconomic: price in the $40–70 band or offer a PnP/budget edition; avoid assumed expansions; diverse, non-stereotyped representation; language-independent where feasible; inclusive, gender-neutral rulebook wording [community standard; style guidance not re-verified this session].

## Common pitfalls & failure modes

- **Under-pricing below 5× landed cost** — can't recoup without ~84%+ sell-through; reprint impossible even on success (Hoyt).
- **The MSRP myth** — treating MSRP as assigned/official rather than chosen against comparables (Stegmaier).
- **Bolted-on solo** — afterthought solo modes underperform; standalone retrofit packs flop (Tokaido: 233/5,000 sold). Beat-your-own-score on a long game becomes an "optimization puzzle, not a game."
- **Automa overhead** — simulating the opponent's full internal game instead of only its player-facing effects; upkeep burden kills the mode (abstraction doctrine). Inverse failure: pure randomness without structure gives no opponent *feel*.
- **The Pandemic problem / alpha player** — one player directs all turns; worst with mismatched skill or strangers; mitigations change game nature, so build them in early (Leacock).
- **Co-op puzzle-solve staleness** — fixed challenge → group solves it once; counter with variety engines and controlled randomness.
- **Difficulty miscalibration** — too hard: players quit when "there is no way to win" (Trzewiczek); too easy: boredom; campaigns must protect morale with ~2:1 win:loss (months can't be replayed).
- **Crowdfunding/retail mismatch** — a $100+ KS core reward concentrates lifetime sales in the campaign; KS-exclusive deluxification can't enter distribution at sane MSRP (Scythe mechs); SKU proliferation confuses consumers years later.
- **Channel neglect** — skipping distribution forfeits evergreen volume (Wingspan: >90% of units via distribution); direct-only ignores the 58% of buyers who primarily shop retail.
- **Colour-as-sole-channel / red-green dependence** — the most common accessibility failure; MLU's average game grades only B despite colour blindness being "one of the simplest issues to address."
- **Paper money** — physically and visually inaccessible, "wall to wall" (MLU).
- **Accessibility as post-launch patch** — Wingspan's readability complaints produced separate vision-friendly packs, not a core fix; new products should be vision-friendly from the start (Stegmaier's own lesson).

## Canonical sources

- *The Game Inventor's Guidebook* — Brian Tinsman (market segmentation: mass/hobby/specialty/European).
- *Building Blocks of Tabletop Game Design* — Geoff Engelstein & Isaac Shalev (CRC Press).
- Meeple Centred Design: A Heuristic Toolkit — Heron, Belford, Reid & Crabb, *The Computer Games Journal* 7(2) 2018 (open access); companion: Eighteen Months of Meeple Like Us, same journal (accessibility statistics). *Tabletop Accessibility Guidelines (TTAG)* — Heron & Belford (book).
- Stonemaier Games blog — stonemaiergames.com: "The Myth of MSRP", "A Price Formula for Your Product" (2022), "The Math of Tariffs" (2025), "The Compelling Power of Solo Play" (Pedersen guest, 2015), "When Does It Make Sense to Sell Directly Instead of Through Distribution?" (2020), "Evergreen Games: What Do They Have in Common?" (2022), "How Do You Measure Accessibility?", "Vision-Friendly Cards" (2023), "The Deluxe Dilemma" (2020), "Results of Releasing a Game that Already Exists" (Tokaido solo, 2025).
- Foxtrot Games — foxtrotgames.com: "Do You Really Have To Charge 5× Your Manufacturing Cost?" (Hoyt, 2016).
- League of Gamemakers — leagueofgamemakers.com: "Cooperative Games: Advice from the Experts", "Games of Emotion: Matt Leacock interview", "I, Alpha Gamer", "What the Font?!", "How to Approach a Manufacturer".
- Meeple Like Us — meeplelikeus.co.uk: 200+ accessibility teardowns, colour-blindness recommendations, MCD framework posts.
- Board Game Design Lab — boardgamedesignlab.com; PrintNinja — printninja.com (cost calculators); Panda Game Manufacturing — pandagm.com; Automa Factory — automafactory.com (Morten Monrad Pedersen).
- James Mathe, "How to Make a Board Game" — jamesmathe.com [classic publisher-economics essay; site unreachable this session].
- Communities/tools: BoardGameGeek (rank, ratings, 1–5 weight, 1 Player Guild) [IP-blocked this session]; ICv2 hobby-channel top-10 lists; BGA / Tabletopia / Dized; ColorSym icons; colorblind palette simulators.
