---
name: board-game-accessibility
description: >-
  Audit and design board games for accessibility and inclusion. Covers Meeple Centred Design
  (Heron et al. 2018) 8-category teardowns, Stonemaier's 10-lens accessibility chart,
  colorblind-safe palettes and double-coding, CVD simulation, vision readability, cognitive-load
  reduction, physical/dexterity fallbacks, emotional safety, language independence,
  socioeconomic access, representation, inclusive rulebook language, and accessibility
  statements. Triggers: "colorblind-safe", "accessibility audit", "make my game more
  inclusive", "double coding", "colorblind palette", "inclusive art", "accessibility
  statement". For icon systems/card anatomy use board-game-rules-writing; for
  representation/worldbuilding use board-game-theme-narrative; for component specs use
  board-game-manufacturing.
---

# Board Game Accessibility & Inclusivity

Accessibility is product design, not charity: ~4.5% of players are color-vision-deficient (8% of men, 0.5% of women), the hobby population is aging, and every fix that removes friction for disabled players removes it for everyone. Audit early, fix in the design, publish the results.

## When to use / when not to use

Use for:
- Auditing a design or published game for accessibility (full MCD teardown or quick pre-flight)
- Choosing player colors, palettes, and double-coding schemes; testing against color-vision deficiency
- Readability of cards, boards, and tokens (font size, contrast, clutter, distance)
- Reducing memory load, icon confusion, and rules-literacy demands; complexity honesty
- Component ergonomics: handling, reaching, shuffling, mandatory dexterity
- Emotional safety design: player elimination, take-that, bluffing demands, content warnings
- Language-independence strategy; inclusive art/representation audits; gender-neutral rulebook text
- Price/PnP/library access decisions framed as accessibility
- Writing an accessibility statement for the rulebook or product page

Not for (route there instead):
- Icon-system design, card anatomy, icon legends, rulebook readability specs → `board-game-rules-writing`
- Representation as theme, naming, cultural-consultant hiring, art direction → `board-game-theme-narrative`
- Physical component dimensions, card stock, print file prep → `board-game-manufacturing`
- Recruiting and running playtests (including with disabled testers) → `board-game-playtesting`
- Difficulty dials and win-rate calibration → `board-game-solo-coop-design`
- Pricing architecture and distribution economics beyond the access lens → `board-game-market-analysis`

## Core principles

1. **Accessible out of the box.** "Players should not be expected to deface their games in order to get a fully playable experience" (Meeple Like Us). Painting cubes, marking cards, and substituting components are player workarounds, not design solutions.
2. **Never use color as the sole information channel.** Double-code every color-dependent category with icon, shape, pattern, or text. This is the single most common accessibility failure in the hobby: the average game in the MLU corpus grades only **B** on colour blindness (10.92/14, n=116) despite it being "one of the simplest issues to address."
3. **Audit against Meeple Centred Design's 8 categories** — Heron, Belford, Reid & Crabb, *The Computer Games Journal* 7(2) (2018), operationalized at Meeple Like Us: Colour Blindness, Visual, Cognitive (fluid intelligence + memory, graded separately), Physical, Emotional, Communication, Socioeconomic, Intersectional. Grade A–F per category.
4. **Complement with Stonemaier's 10 product lenses** (verified chart): Learning, Retention, Time (setup 5 min / play 45–90 / cleanup 5), Visual, Presence, Language, Purchase ($40–70), Scope (solo + 2p + 5+ in core game), Inclusion, Physicality. "You can make a really accessible game without checking every single box" (Stegmaier) — accessibility is a direction, not a perfect score.
5. **Grades are heuristics, not lived experience.** The MCD authors' own caveat: teardowns are "theorycrafted... from an abled perspective." Verify every audit with disabled playtesters; compensate them.
6. **Design the verbal-instruction fallback.** If a player can direct every action by voice ("draw a token and place it on space 12"), the game is playable without dexterity *and* supports low-vision play. Test this literally.
7. **Teachable heuristics replace arithmetic.** *Quacks of Quedlinburg* passes MLU's cognitive lenses partly because "4 white tokens out = your next draw is safe" replaces live probability math. Ship rules of thumb with the game; they are an accessibility feature.
8. **Complexity honesty is accessibility.** State weight, literacy, numeracy, and memory demands on the box/rulebook so players can self-select. Age ratings alone don't do this (Stonemaier chart feedback; BGG weight is the community proxy).
9. **Cheap early, expensive late.** *Wingspan*'s readability complaints produced separate vision-friendly card packs (2023) — a retrofit sold apart from the game. Stegmaier's own lesson: make new products vision-friendly from the start. *Ticket to Ride* and *Splendor* similarly added symbol coding only in later editions.
10. **Inclusion is an accessibility category,** not a separate virtue: representation across age, gender, ethnicity, sexuality, and disability; cultural consideration; no oversexualization (Stonemaier Inclusion lens, DEI-consultant reviewed; MLU grades representation under Socioeconomic).
11. **Publish what you find.** A per-game accessibility statement/chart pre-empts the teardown, serves buyers, and — as Stonemaier's own color-only chart proved — must itself be accessible.
12. **Accessibility fixes are universal design.** Bigger fonts serve aging eyes; double-coding serves dim rooms; verbal-instruction playability serves everyone teaching a game.

## How to apply it

Run passes A–G in order during development (each is cheap at prototype stage), then H before release. Full checklists with grading procedure: load `references/accessibility-audit.md`.

### A. Colour & double-coding pass

- [ ] Identify every place hue carries meaning: player colors, token types, card categories, tracks, icons, rulebook callouts.
- [ ] Add a second channel to each: unique icon, unique shape, pattern/texture fill, or text label. Exemplars: *Azul* (patterned tiles), *The Crew* and *Dune Imperium* (symbol-coded suits), *Quacks* (ingredient books double-coded with art).
- [ ] For 3D components use unique **shapes**, not just prints — colored wooden cubes are the worst offender (confusion groups: red/orange/brown; blue/pink/purple; green/yellow/light orange — colorblind player report).
- [ ] Simulate all four MLU-graded types: **protanopia, deuteranopia, tritanopia, monochromacy** (Color Oracle, Coblis, Photoshop proofing).
- [ ] Run the **low-light test**: Stegmaier discovered Viticulture's red was confusable with orange and purple under evening lighting and changed the player color.
- [ ] Run the distance test: board state readable from across the table, upside down.

Deep palettes (Okabe-Ito/Wong), CVD confusion tables, tool walkthroughs: load `references/color-and-iconography.md`.

### B. Vision pass

- [ ] Contrast ≥ 4.5:1 for body text, ≥ 3:1 for large text and meaningful icons (WCAG 2.1 applied to print). Black text on white/near-white beats black on color — *Wingspan*'s black-on-brown cards were the canonical failure; the vision-friendly fix put black text on a white area overlaid on the color swatch.
- [ ] Functional information (costs, actions) gets the biggest, boldest, highest-contrast treatment; flavor text smallest.
- [ ] Body/rules text ≥10 pt equivalent on cards; no critical text smaller. (*Tapestry*'s tiny income-chart numerals drew zoom-the-PDF complaints [community report].)
- [ ] Strip visual clutter not needed for play; darken and enlarge icons (the three documented Wingspan vision-friendly changes: declutter, darker/bigger icons, reformatted power area).
- [ ] Keep light-on-dark text to ~5 words max; no text on busy art without a scrim.
- [ ] Cards meant to be read in hand must survive a one-handed fan; tableau information must be readable from other seats.

### C. Cognitive pass

- [ ] Count and cap distinct token types; one icon = one meaning, system-wide.
- [ ] Consistent game flow: same turn structure every round, exceptions designed out (every "remember" is an interface failure).
- [ ] Chunk rules into phases; provide player aids and a reference card per player (Retention lens).
- [ ] Audit memory demand at three levels: needed to play *at all* / *effectively* / *well* (MLU fluid-intelligence + memory lenses). Reduce the first two; the third may stay as skill.
- [ ] Replace required arithmetic with tracks, tokens, or teachable heuristics; flag required literacy and numeracy honestly on the box.
- [ ] Simultaneous play punishes supported players — a player who must ask "what is this, where does it go" breaks flow for everyone (Quacks teardown). Prefer turn order, or give support time by design.

### D. Physical / dexterity pass

- [ ] The game must be fully playable by **verbal instruction** to another player. Test it.
- [ ] No mandatory dexterity (flicking, stacking, speed) without a non-dexterity alternative; no required physical acting.
- [ ] Conventional card sizes (easier to hold, sleeve, and replace); textured or weighted tokens over slippery flat ones.
- [ ] Minimize manipulation frequency and reaching: large target zones, sparse layouts, components within arm's reach.
- [ ] Never paper money — "inaccessibility wall to wall" (MLU). Use tracks, chips, or tokens.
- [ ] Shuffle burden: small decks, chunked shuffles, or card holders/trays.

### E. Emotional pass (MLU lens list)

- [ ] Challenge vs. frustration: is expected loss *designed* (despair-by-design)? If so, say so on the box and provide fast-loss exits.
- [ ] Player elimination: exclusion grows with game length — eliminate it, shorten the game, or give eliminated players a role.
- [ ] "Take that" binds frustration to a person; incentivized ganging-up compounds it. Prefer impersonal disruption or catch-up mechanisms (Quacks' rat tails soften bad rounds).
- [ ] Bluffing/lying demands and arbitrary, uncontrollable fates exclude some players — offer variants.
- [ ] Audit theme for trauma triggers; add content warnings where warranted (see `references/inclusion-language-statement.md`).

### F. Communication & language pass

- [ ] No essential audio cues without visual equivalents; no required real-time verbal negotiation as the only path.
- [ ] Language independence: icon-driven play with *supportive* (not load-bearing) text; nothing essential readable only from across the table; localized editions planned (Stegmaier Language lens).
- [ ] Icons alone can fail — *Quacks*' iconography was "likely to be baffling on its own"; explanatory text in ingredient books is what saved it. Pair icons with text somewhere reachable.
- [ ] Rulebook in second person with singular "they"; mixed-gender names in examples (noted positively in the Quacks teardown).

### G. Socioeconomic & inclusion pass

- [ ] Price inside the $40–70 accessibility band or offer a PnP/budget edition (Stonemaier chart target; *Quacks* at ~£35 graded as reasonable value).
- [ ] Don't assume expansions; avoid collectible business models — business model is an accessibility issue (MLU).
- [ ] Support try-before-you-buy: libraries, PnP, Tabletopia/BGA versions — games need not be purchased to be enjoyed (Stonemaier DEIB consultant Lydia-Rae Wehmeyer's framing).
- [ ] Art audit: representation across age, gender, ethnicity, sexuality, disability; no oversexualization; no tokenism (Quacks' cover: 1 of 6 identifiable people female — "Smurfette Syndrome").
- [ ] Scope: solo mode and 2-player in the core box widen access; a 3-player minimum excludes.

Representation depth, inclusive-language checklist, statement template: load `references/inclusion-language-statement.md`.

### H. Grade & publish the audit

1. Grade each MCD category A–F (scale and worked example in `references/accessibility-audit.md`); record evidence, not vibes.
2. Fix every F/D that costs less than a component change; document the rest honestly.
3. Write the accessibility statement (template provided) into the rulebook back matter and product page. Keep the statement itself accessible: text, not a color-only infographic — Stonemaier's own accessibility chart was called out for failing WCAG's color-only rule.
4. After release: log accessibility feedback as bug reports; fix in the next printing (Stegmaier framed *Expeditions*' bold-black-on-light-beige card design as informed by the *Wingspan* readability feedback).

## Key numbers & heuristics

| Claim | Value | Source |
|---|---|---|
| Color-vision deficiency prevalence | ≈8% of men, ≈0.4–0.5% of women (Northern European ancestry; global rates vary) | Wikipedia / Colour Blind Awareness; cited by Stegmaier |
| CVD breakdown | protan ≈2% of males, deutan ≈6% of males; tritan and monochromacy rare | Wikipedia, *Color blindness* |
| CVD types to simulate | protanopia, deuteranopia, tritanopia, monochromacy | Meeple Like Us grading practice |
| Mean hobby-game colour grade | B (mean 10.92/14, SD 3.30; median 11) — "recommended with small issues" | MLU corpus, n=116 (Heron et al., *Eighteen Months of Meeple Like Us*) |
| MCD grade scale | A=14, B=11, C=8, D=5, E=3, F=0 across 8 categories | Heron, Belford, Reid & Crabb (2018), *Computer Games Journal* 7(2) |
| Session-time accessibility targets | setup ~5 min, play 45–90 min, cleanup ~5 min | Stonemaier accessibility chart (verified) |
| Price accessibility band | $40–70 MSRP | Stonemaier accessibility chart (verified) |
| Print contrast minimums | 4.5:1 body text; 3:1 large text & meaningful graphics | WCAG 2.1 applied to print |
| Card/rules body text | ≥10 pt equivalent; functional info biggest | practitioner standard; *Tapestry* complaints [community report] |
| Light-on-dark text limit | ~5 words maximum | League of Gamemakers typography guidance |
| Colorblind-safe palette | Okabe-Ito/Wong 8-color palette survives all CVD types | Wong, *Nature Methods* (2011); Okabe & Ito (2008) |
| Player-color confusion groups | red/orange/brown; blue/pink/purple; green/yellow/light orange | colorblind player report (Stonemaier comments) |
| Wingspan vision-friendly changes | strip clutter; darker/bigger icons; black-on-white power area over the color swatch | Stonemaier (2023), consultants Brian Chandler, Karel Titeca, Echobatix |

## Common pitfalls

- **Colour-as-sole-channel** — the hobby's most common failure; the fix (double-coding) is cheap and known, yet the corpus average is only B.
- **Aftermarket-fix thinking** — "players can just mark the cubes" violates out-of-the-box doctrine (MLU).
- **Retrofit accessibility** — selling the accessible version separately later (Wingspan vision-friendly packs) instead of designing it in; new products should be vision-friendly from the start.
- **Token-shape uniformity** — same-form wooden cubes/meeples distinguished only by hue; protan/deutan players confuse whole color families mid-game ("spent three turns building toward a play with the wrong color").
- **Double-coding too small or too similar** — symbols that exist but are tiny, faint, or look-alike (Walking in Burano's house symbols) don't count; the second channel must be as legible as the first.
- **Black text on colored backgrounds** — Wingspan's black-on-brown; fix is black on white/near-white over the swatch.
- **Icon soup without text fallback** — icons that must be deciphered mid-turn (Quacks icons baffling without the ingredient-book text; *Bang!*'s "go read the rulebook" icon).
- **Paper money** — physically and visually inaccessible, "wall to wall" (MLU).
- **Mandatory dexterity or speed** as the core skill with no alternative path.
- **Long-game player elimination** — excluded players watch for hours; emotional-accessibility failure that scales with playtime.
- **Simultaneous play with hidden inspection needs** — supported players either stall the table or play stigmatized/separate (Quacks visual grade D driver).
- **Self-audited accessibility claims** — grading your own game from an abled perspective and stopping there; MCD's own caveat demands disabled-tester verification.
- **Inaccessible accessibility statement** — publishing the chart as a color-only, unlabeled-image infographic (Stonemaier's chart was itself called out under WCAG).

## Reference files

- `references/accessibility-audit.md` — Load when running a full audit or teardown: MCD grading procedure and scale, complete per-category checklists (all MLU lenses), the *Quacks of Quedlinburg* worked example with grades, intersectional analysis, disabled-tester verification protocol.
- `references/color-and-iconography.md` — Load when choosing palettes, player colors, or double-coding schemes, or when simulation-testing: CVD types and confusion tables, Okabe-Ito/Wong and Tol palettes, double-coding methods (2D and 3D), simulator tools, low-light/distance/rotation test procedures.
- `references/inclusion-language-statement.md` — Load for representation audits, gender-neutral rulebook language, language-independence strategy, socioeconomic access tactics (PnP, price, libraries), content warnings, and the copy-paste accessibility statement template.

## Related skills

- `board-game-rules-writing` — icon systems, card anatomy, rulebook readability and teach order; accessibility statement slots into rulebook back matter
- `board-game-theme-narrative` — representation and cultural sensitivity as worldbuilding and art direction; naming
- `board-game-manufacturing` — component sizes, card stock, print specs that constrain font size and contrast
- `board-game-playtesting` — recruiting and running tests with disabled players; session protocols
- `board-game-design-theory` — depth vs. complexity decisions that drive cognitive load; player-experience frameworks
- `board-game-mechanisms` — choosing mechanisms with lower dexterity/memory/downtime burden
- `board-game-math-balance` — catch-up mechanisms and feedback loops behind emotional accessibility
- `board-game-solo-coop-design` — solo modes as scope accessibility; difficulty calibration
- `board-game-prototyping` — PnP kits double as socioeconomic access
- `board-game-market-analysis` — pricing architecture beyond the $40–70 access band
- `board-game-crowdfunding` — PnP tiers, localized editions, regional fulfillment as access levers
- `board-game-publishing` — localization/territory clauses in publishing contracts
