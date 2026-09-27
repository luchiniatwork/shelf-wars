# Inclusion, Language & the Accessibility Statement

Load this for representation audits, gender-neutral rulebook language, language-independence strategy, socioeconomic access tactics, content warnings, and the accessibility statement itself. Representation as worldbuilding/art direction (hiring cultural consultants, naming, theme resonance) is owned by `board-game-theme-narrative`; this file is the access-side audit and the statement template.

## Representation audit (art & components)

Run on box art, card art, rulebook illustrations, and component personas. Stonemaier Inclusion lens, DEI-consultant reviewed: "culturally considerate, character diversity (age, gender, ethnicity, sexuality, disability), no oversexualization, no adult content."

- [ ] **Count the cast.** List every identifiable person in the art; tally gender, ethnicity, apparent age, body type, disability. MLU's *Quacks* teardown flagged 1 of 6 identifiable cover figures as female ("Smurfette Syndrome") — ratios are auditable facts, not vibes.
- [ ] Women and minorities in active/competent roles, not decoration or damsel roles.
- [ ] No sexualized depiction asymmetry (armored men / bikini-clad women is the classic fail).
- [ ] Disability present as ordinary (wheelchair users, canes, hearing aids) when humans are depicted — disability is part of the diversity list, and disabled players buy games.
- [ ] Stereotype sweep: accents, dialects, cultural costumes used as theme dressing; get a cultural consultant for themes touching living cultures (Stonemaier maintains a cultural-consulting referral page).
- [ ] Rulebook examples: mixed-gender names and pronouns (Quacks' manual used both male and female names and gender-neutral language — noted positively).

## Inclusive rulebook language

- Teach in **second person** ("you"); when a third person is unavoidable, use singular "they" (Stegmaier style rule).
- Never gender the hypothetical player ("his turn"), the designer, or characters without reason.
- "Players," not "guys"; "spouse/partner," not gendered defaults, in flavor text.
- Keep language plain — plain language is simultaneously a cognitive-accessibility, localization, and literacy win.
- Terminology discipline (one term per concept) belongs to `board-game-rules-writing`; the gender/neutrality pass is additive, not a replacement.

## Language independence strategy

The Stegmaier Language lens, verified: "language independent with supportive text, localized versions, no distant text to read."

1. **Icon-driven play, text-supported.** Core loop operable from icons alone; text is a *support* layer, never load-bearing mid-turn. But pure-icon games fail when icons are non-obvious — Quacks' iconography was "likely to be baffling on its own" and only the ingredient-book text saved it (MLU). Pair every icon system with reachable text (reference card, appendix, rulebook legend).
2. **No across-the-table text.** Anything a player must read to act must be readable from their own seat. Distant text is a vision *and* language barrier.
3. **Separate mechanics text from flavor text** on cards, so localizers translate only the load-bearing layer and flavor can ship untranslated without breaking play.
4. **Plan localized editions** early: icon-tolerant layouts, text-expansion headroom, editable master text (handoff mechanics: `board-game-rules-writing`).
5. **Check numeracy/notation independence:** digits and symbols travel; spelled-out number words don't.

## Socioeconomic access tactics

Price and business model are accessibility issues (MLU grades them; Stegmaier's Purchase lens targets **$40–70** MSRP and "few expansions/promos").

- [ ] Core game complete without expansions; expansions are variety, not required fixes.
- [ ] No collectible/randomized purchase model for play-critical content.
- [ ] **Free or cheap PnP edition** (also feeds prototyping and crowdfunding funnels); a legitimate access path, not piracy tolerance.
- [ ] Keep the game in print and in retail; support **libraries, cafés, conventions, and try-before-you-buy** (Tabletopia/BGA) — games need not be purchased to be enjoyed (Stonemaier DEIB consultant Lydia-Rae Wehmeyer's framing). Digital versions (BGA, Steam) also serve as low-cost trials and accessibility vectors.
- [ ] Regional fulfillment/localized pricing so shipping+VAT doesn't double the price abroad.
- [ ] Box-size restraint: big boxes are shelf-price and table-space barriers (Stegmaier Presence lens: "shelf space is a premium").

## Content warnings & emotional disclosure

- Warn on the box or rulebook page 1 for: player elimination with long downtime, betrayal/traitor mechanics, targeted "take that" as the core interaction, horror/violence themes, realistic trauma-adjacent content (disease, war, slavery, colonialism), mandatory lying.
- Frame as *informed choice*, not apology: "This is a game about X where players can do Y to each other" — Stegmaier's "despair-by-design" games should say so up front.
- Offer variants where cheap: no-traitor variant, cooperative variant, elimination-to-role conversion.

## Accessibility statement template

Put in the rulebook back matter (and mirror on the product page). Keep the statement itself accessible: real text, high contrast, no color-only infographic — Stonemaier's own accessibility *chart* was publicly called out for failing the color-only WCAG rule.

```
ACCESSIBILITY
Color vision: All color-coded information is also shown by [icons/shapes/patterns/text].
  Tested for protanopia, deuteranopia, tritanopia, and monochromacy. [Or: known issue — …]
Vision: Rules text is [X]pt black-on-white. Card text needed to play is [X]pt or larger.
  A large-print/vision-friendly card set is available at [URL]. [If true]
Cognitive: Turn structure is identical each round. Player aids summarize all phases.
  The game requires [reading level / mental arithmetic / memory of hidden information — state honestly].
Physical: The full game can be played by giving verbal instructions to another player.
  No dexterity, speed, or reaching is required. Card holders [included / compatible].
Emotional: This game contains [player elimination / direct attacks / bluffing / themes of X].
  [Variant or exit offered, if any.]
Communication & language: No speech or hearing is required. [Language-independent:
  all play-critical information is iconic; text is supportive.] [Y languages available.]
Price & availability: MSRP [$X]. A free print-and-play version is at [URL].
Complexity: [BGG-style weight] — we rate the rules load as [light/medium/heavy].
Feedback: accessibility@[publisher] — reports go to the development team for the next printing.
```

Only print claims that survived the audit (`accessibility-audit.md`) — an unverified statement is worse than none: MLU teardowns are public, CC-BY, and unforgiving.
