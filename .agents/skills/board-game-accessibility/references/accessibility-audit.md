# The Full Accessibility Audit (Meeple Centred Design)

Load this when running a complete accessibility audit/teardown of a design or published game — the procedure, grading scale, and the complete per-category checklists distilled from Meeple Centred Design (Heron, Belford, Reid & Crabb 2018, *The Computer Games Journal* 7(2), open access) as operationalized across 200+ Meeple Like Us teardowns. Palette-level detail lives in `color-and-iconography.md`; statement writing in `inclusion-language-statement.md`.

## Grading procedure

1. Assemble the full game: every component, the rulebook, and the box. Audit the *out-of-the-box* state — never assume player modifications ("players should not be expected to deface their games," MLU).
2. Walk the categories in order. For each, play (or simulate) the game with the impairment lens active and record **evidence**: the component, the situation, the consequence.
3. Grade each category A–F. MLU's numeric mapping: **A=14, B=11, C=8, D=5, E=3, F=0**. B and above = "recommended (possibly with small issues)"; C = "considerable issues, situational"; D and below = "not recommended" in that category. Plus/minus modifiers are used in practice.
4. Write the intersectional analysis: impairments compound (e.g., low vision *plus* arthritis makes small double-coded icons fail twice; non-fluency *plus* memory load makes untranslated set bonuses unplayable).
5. **Verify with disabled playtesters.** The framework's own caveat: grades are "theorycrafted" heuristics from an abled perspective, not embodied experience. Pay testers; treat their reports as bug reports with severity, not opinions.

## Category checklists

### 1. Colour Blindness

Grade per CVD type — **protanopia, deuteranopia, tritanopia, monochromacy** (MLU practice); protan ≈2% and deutan ≈6% of males, the other two rare (Wikipedia).

- [ ] No information carried by hue alone: player ownership, token types, card categories, tracks, icons, rulebook references.
- [ ] Every hue-carried category double-coded (icon/shape/pattern/text); second channel as legible as the first.
- [ ] Palette checked under all four simulations *and* low light (evening play is the norm).
- [ ] Worst-case audit at **maximum player count** — some games only collide when all player colors are out (MLU).
- [ ] Cross-component links checked: a card referring to "the green track," a board region matching a token color.
- [ ] Substitution check: if a color distinction fails, can game state still be tracked without house-modifying components?
- Exemplars: *Azul* (A-range; patterned tiles), *San Juan 2nd ed.*, *Splendor* later printings (gem shapes added). Anti-exemplar: *Quacks* score track — "the usual quad of red, green, blue and yellow" droplets with no icons, despite icons existing on other tokens in the same box (graded B-).

### 2. Visual Accessibility

- [ ] Contrast ≥4.5:1 body text, ≥3:1 large text/meaningful icons (WCAG 2.1 on print); black-on-white preferred for rules text.
- [ ] Functional type biggest/boldest; no critical text under ~10 pt equivalent; no text on busy art.
- [ ] Clutter audit: every visual element that isn't play-relevant removed (Wingspan vision-friendly lesson).
- [ ] Board state inspectable without disturbing it — pieces that sit loosely on tracks/boards randomize state when explored by touch (Quacks spiral problem).
- [ ] All information needed on a turn reachable/readable from the player's seat, including across-the-table text (eliminate "distant text," Stegmaier Language/Visual lenses).
- [ ] Simultaneous-play audit: can a player who needs close inspection or table support act without stalling everyone? If not, provide a turn-ordered variant.
- [ ] Tactile redundancy where feasible: distinct shapes/textures let low-vision players identify by touch (*Nyctophobia* is the extreme exemplar — designed so sighted players close their eyes).
- Vision-friendly exemplars (Stonemaier/Bartos list): *Parks* (minimal text, big icons, unique token shapes), *Skull* (no text, giant icons), *King of Tokyo* (font size), *7 Wonders* (cards read in hand, big icons), *Splendor* (open information).

### 3. Cognitive Accessibility — fluid intelligence

- [ ] Required literacy: volume and reading level of mandatory text; is iconography learnable without the rulebook (or is it "baffling on its own" — Quacks)?
- [ ] Game-state complexity and coupling: how many interacting systems must be modeled to make one decision?
- [ ] Required numeracy: live arithmetic (budgets, multiplication) vs. tracks/tokens; scoring math demand.
- [ ] Rules synergy depth: how many rule-to-rule interactions must be known to play at all?
- [ ] External knowledge demands: trivia, genre literacy, hobby vocabulary.
- [ ] Multitasking/simultaneity demands.
- [ ] Provide **teachable heuristics** that replace computation (Quacks: "4 whites out = safe next draw"); print them in the rulebook and on player aids.

### 4. Cognitive Accessibility — memory

- [ ] Memory needed to play *at all* (rules recall), *effectively* (state tracking), *well* (card counting). Fix the first two with aids; the third is legitimate skill.
- [ ] Game-flow consistency: identical turn structure each round; exceptions designed out (every exception is a memory tax; Stonemaier Retention lens: "minimal rule exceptions").
- [ ] Number of distinct token types; consistency of meaning (one icon = one meaning system-wide).
- [ ] Hidden-state audit: information that *was* public should stay inspectable or be trackable on an aid.
- [ ] Reference support: player aids, reference card per player, icon legend.

### 5. Physical Accessibility

- [ ] **Verbal-instruction playability**: every action directable by voice ("place my worker on the forest space"). This is the master fallback — test it literally with one player blindfolded/hands still.
- [ ] Manipulation frequency and precision: tight packing, small target zones, nested inserts, precise placement (Quacks' spiral placement graded D).
- [ ] Draw mechanisms: bags that cardboard sticks inside (Quacks physical D); bowls/cups as alternatives only if hidden draw isn't required.
- [ ] Component ergonomics: conventional card sizes; textured/weighted tokens; card holders; no paper money ("inaccessibility wall to wall").
- [ ] Reaching: everything within arm's reach at max player count; table footprint on an average table (Stegmaier Presence lens).
- [ ] Shuffle burden and deck size; tray/organizer quality for setup and teardown.
- [ ] No required physical acting, speed, or dexterity without a non-dexterity alternative.

### 6. Emotional Accessibility (full MLU lens list)

- [ ] Challenge vs. frustration balance; is loss *expected by design* (despair-by-design)? Label it and give fast-loss exits.
- [ ] Arbitrary, uncontrollable fates (pure-luck blowouts) — mitigate or shorten their shadow.
- [ ] Bluffing/lying demands — offer a no-traitor/no-hidden-role variant where the design allows.
- [ ] Pattern-closure needs: avoid mechanics that punish players for needing predictability (randomized setup with no stabilizers).
- [ ] "Take that": targeted attacks bind frustration to a *person*; prefer impersonal disruption. Incentivized ganging-up compounds it.
- [ ] Upsetting themes/trauma triggers: content warnings in the rulebook and on the box where warranted.
- [ ] Player elimination: exclusion duration = elimination time × remaining game length; long games must not eliminate.
- [ ] Catch-up mechanisms (Quacks rat tails) soften snowballing despair; verify they don't invert into punishing the leader arbitrarily.

### 7. Communication

- [ ] Formal communication demands: negotiation, auctions, real-time coordination — is there a low-communication path?
- [ ] No essential audio-only or speech-only channels.
- [ ] Literacy floor: "as long as one person is passingly fluent in the language of the game" can be enough (Quacks grade B) — but state it.
- [ ] Language independence: icons + supportive text; no essential text readable only across the table; localized editions.

### 8. Socioeconomic Accessibility

- [ ] Price vs. value and vs. band ($40–70 Stonemaier target; *Quacks* ~£35 graded reasonable).
- [ ] Business model: collectible elements, assumed expansions, required promos — each is a barrier (MLU).
- [ ] Availability: reprints, retail presence, regional fulfillment; try-before-you-buy via libraries, PnP, Tabletopia/BGA.
- [ ] Representation in art and text: gender, ethnicity, age, disability, sexuality; Smurfette-syndrome check (count identifiable characters by group); no oversexualization; gender-neutral rulebook language and mixed-gender example names (Quacks manual noted positively here).

### 9. Intersectional analysis

- Combine the grades: which pairs of impairments multiply? Common multipliers: visual×physical (touch exploration disturbs state), cognitive×communication (untranslated rules + memory load), socioeconomic×everything (no budget for the accessible edition).
- Practical playability factors: session length vs. stamina/attention; setup/teardown burden; drop-in/drop-out tolerance (Quacks tolerates players leaving — a positive); table space as a housing constraint.

## Worked example: *The Quacks of Quedlinburg* (MLU teardown, CC-BY)

| Category | Grade | Decisive evidence |
|---|---|---|
| Colour Blindness | B- | Ingredient books double-coded with art; but score markers are the "usual quad" red/green/blue/yellow with no icons — and position on the track drives rat-tail entitlements |
| Visual | D | Tokens indistinguishable by touch; spiral track exploration disturbs state; simultaneous draws make table support flow-breaking |
| Fluid Intelligence | B- | Real budget arithmetic, but the "4 whites out" rule of thumb replaces live probability at functional play level |
| Memory | B- | Bag composition reminder printed on the board; set powers must be remembered but are few |
| Physical | D | Bag draw sticks; precise spiral placement; easily disturbed tokens; simultaneous handling |
| Emotional | A- | Sanded-down push-your-luck; rat-tail catch-up mitigates bad rounds; leader-bonus die only mildly counteracts |
| Socioeconomic | B- | ~£35, good value; cover shows Smurfette Syndrome (1 of 6 identifiable people female); manual gender-neutral with mixed-gender names |
| Communication | B | No formal communication need; some literacy required; one fluent reader suffices |

Lesson for designers: grades are per-category and evidence-driven; a top-100 BGG title fails visual and physical while passing emotional. Fix the specific component, not "the game."

## Sources

- Heron, Belford, Reid & Crabb, "Meeple Centred Design: A Heuristic Toolkit" (2018), *The Computer Games Journal* 7(2); companion stats paper "Eighteen Months of Meeple Like Us" (corpus n=116; mean colour grade 10.92/14). Book-form expansion: Michael James Heron, *Tabletop Game Accessibility: Meeple Centred Design and the Accessibility of Tabletop Games* (CRC Press, 2024), DOI 10.1201/9781003415435.
- Meeple Like Us teardowns (CC-BY 4.0): Quacks of Quedlinburg, Walking in Burano, Blades in the Dark, et al.; colour-blindness recommendations page.
- Stonemaier Games: accessibility chart (10 lenses, verified), "How Do You Measure Accessibility?" (2022), "10 Vision-Friendly Games…or Are They?" (2023, with Gary Bartos/Echobatix), "Vision-Friendly Cards" (2023).
