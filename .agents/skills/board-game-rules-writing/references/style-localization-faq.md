# Style Guide, Precision Writing, Localization & Living FAQ

Load this for: the full rulebook style rules, terminology workflow, precision-writing maxims (Selinker, ekted), localization-ready writing and handoff, and post-release FAQ/errata operations.

## 1. Written style guide (Stonemaier Games Style Guide, public — verified against source)

Every project needs a written style guide before copyediting. Baseline (adapt freely — the requirement is that it exists and is applied uniformly):

| Rule | Example / note |
|---|---|
| Serial comma | "a cube, a player mat, and a reference card" |
| Hyphenate modifiers | "the first-player token" |
| Numerals whenever possible, except at sentence start | "harvest a total of 2 resources" / "Two workers…" |
| Numbered lists = sequential steps; bullets = unordered | — |
| Second person, active voice | "Whenever you gain resources, place them on your player mat." |
| Singular "they" for unavoidable third person | never "he or she" |
| Cross-references | "(see Gameplay)" format |
| Double quotes; periods/commas inside quotes | — |
| Never introduce a term before defining it | reorder sections if necessary |
| Bold = key terms; italics = examples/notes; never underline | — |
| Zero "should" | implies optionality where none exists |
| Flag every "except" / "remember" | design cues: exceptions should be designed out; "remember" means the interface failed — move the fact onto a component or aid |
| "gain," not "take," from the supply | "At the end of each round, gain $5." |
| "mat" = unique to a player; "board" = shared | — |
| Spell out acronyms once, at first use | "non-player characters (NPCs)" |
| Bracketed notes to the graphic designer | [Insert graphic showing…] |
| One space after periods | — |

**Capitalization of game terms is [contested]**: Selinker lowercases almost everything; Jaffee avoids capitalizing terms; many publishers capitalize all defined terms. Sen-Foong Lim's compromise — **bold the term at first instance only**, then plain text — satisfies both camps. Whichever you pick: write it in the style guide, apply 100%.

## 2. Terminology workflow (Unpub "Rulebook Building 101" + ekted)

1. Build the **keyword list** the day you name your first component: term, definition, first-use location, forbidden synonyms.
2. Define each term once, at first use, **bolded**; use it verbatim everywhere after ("action" vs. "activation" slips get noticed).
3. Draft the **glossary even if you never print it** — writing definitions forces one-term-per-concept. "Pawn" vs. "token": pick one, search-replace the other.
4. **Sequence hierarchy**: define game/round/turn/phase precisely, with explicit sub-phase names ("before combat," "during cleanup") — timing questions collapse when the hierarchy is explicit (ekted, *Gamer's Mind* Rules 1–4).
5. **Word precision**: "either…or" is ambiguous (inclusive?); "another player" vs. "the other player" breaks at 2p; rules need code-level explicitness.
6. **Induction over tables**: prefer base + modifier rules ("conquest costs 2 + 1 per defensive piece" — *Small World*) over lookup tables (ekted).
7. **Under/over-specification**: exceptions imply things; a redundant-looking exception sends readers hunting for meaning that doesn't exist. Delete redundancy or make it visibly an example.

## 3. Selinker's ten maxims ("Writing Precise Rules", *Kobold Guide to Board Game Design*, 2011)

1. No intermediary terminology (don't rename hexes "squares" mid-rule).
2. Real words, never varied once chosen (Tweet: "Things are the same, or they are different").
3. No more work than necessary — an RPG rule made players roll twice to compute a 50.5% coin flip; write "50%" and roll once.
4. Flavor, but sparingly.
5. Text no smarter than the reader — Flesch-Kincaid grade = 0.39×(words/sentence) + 11.8×(syllables/word) − 15.59; a *De Bellis Antiquitatis* paragraph scores 13.22 (college). Aim middle-grade for mass-market games.
6. Discard rules that can't be written (MTG's *Dead Ringers* was rewritten repeatedly to make the text printable — and still shipped as famously convoluted text; a rule you can only express as convoluted text is a redesign candidate, not a wording problem).
7. "Take a breath" — short headed sections; a 1984 *Axis & Allies* mega-sentence was rewritten to under 147 words.
8. Go easy on the eyes — minimize caps and bold runs.
9. Hire professional editors (~$25–50/hr; veterans >$100 [contested, informal poll]).
10. The final version is playtested by strangers from the rules alone — "if they screw it up, you don't have a final version anymore."

## 4. Localization-ready writing (Geeky Pen + Kobold Guide)

Writing rules:
- Short sentences (one instruction per sentence); no idioms, no sports metaphors, no puns in rules text (flavor text may be adapted by translators; rules text may not).
- Numerals over spelled-out numbers; consistent keyword list (translators translate the *list* first).
- Language-independent components where possible (icons + numbers on components), so only the rulebook and card text localize — but never icon-*only* designs (Selinker's *Gloria Mundi*: one symbol cannot do the work of ten).

Handoff checklist:
- [ ] Development **frozen** before translation starts — re-translation compounds (anecdotal ~30% cost overrun [contested]).
- [ ] English source **edited first** — translators are not rules editors; source errors multiply across every target language.
- [ ] **Glossary spreadsheet**, one column per language, exported from the keyword list.
- [ ] Master text in an **editable format** (Google Docs/Word) — PDF/InDesign-only sources have cost a week of manual table reconstruction.
- [ ] **CAT tool with translation memory** so expansions stay consistent with the base game.
- [ ] Budget for text expansion: translated rules commonly run longer than English — leave white space in the layout (direction ~+20–30% for DE/FR [contested — localization folklore, varies]).

## 5. Living FAQ & errata operations

Policy (Tom Jolly, League of Gamemakers):
- **Never ship a first printing with a FAQ** — a launch-day FAQ is a confession of unfixed rules. FAQs are for *genuinely frequent* questions and *actual errors* discovered after publication.
- Seed FAQ content from blind-playtest question logs; publish when the same question recurs across groups.
- On the **next printing, migrate every FAQ answer into the section where players actually look** — the FAQ shrinks as the book improves.

Channels & mechanics:
- Per-game **"Rules & FAQ" page** on the publisher site (Stegmaier model) + FAQ upload to the game's **BoardGameGeek** files section.
- **Dated living-rulebook revisions** (GMT wargame "living rules" model; Leder's *Law of Root* 2022 → 2024 → 2025) — version number + date on every PDF; keep old versions archived and labeled.
- Interactive rules site for heavy/living games (rules.ledergames.com) — searchable reference beats PDF for lookup.
- Errata classification: (a) typo — fix next printing; (b) rules contradiction — publish official ruling immediately; (c) balance change — publish as official variant, never silently edit the printed rule.
- Video teach (Watch It Played standard) is a **complement, never a substitute** (Jaffee: few players will research rules online; the printed book remains the only guaranteed interface).
