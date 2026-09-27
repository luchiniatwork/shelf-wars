# Annotated Rulebook Skeleton

Load this when drafting or restructuring a rulebook, quick-start guide, or first-turn script.
Architecture follows Stegmaier's verified template (overview & goal → components → setup → gameplay overview → detailed gameplay → other info → end of game), extended with front/back matter conventions from Pixy Games, Meeple Mountain, and Leder Games. Bracketed notes are instructions to you, the writer — delete them from the shipped document.

---

## 0. Architecture decision (choose before writing)

| Game profile | Document set | Exemplar |
|---|---|---|
| Light/family, ≤8 pages of rules | Single rulebook | *Splendor* (4-page rulebook) |
| Medium, 8–16 pages | Single rulebook + per-player aid | *Wingspan* |
| Heavy, asymmetric factions, 16+ pages | *Learning to Play* (conversational) + *Law*-style reference (numbered, formal) + quick-start | *Root*, *Arcs*, *Dawn of the Zeds* (multiple rulebooks) |
| Legacy/campaign | Core rulebook + sealed scenario sheets; never spoil in the base book | *Jaws of the Lion* (tutorial-in-box) |

Rule of thumb (3-part anti-front-loading structure, works even inside one book):
- **Part 1 — Goal & win condition, ≤1 page.** What you are, what you're trying to do, how the game ends.
- **Part 2 — Minimum rules to complete Turn 1, 2–3 pages.** Setup + the core turn.
- **Part 3 — Full reference, formatted for random access.** Searchable headers, labeled edge cases, index.

Precedence statement (mandatory for dual documents): *"If the Learning to Play guide conflicts with the Law, follow the Law."* (Leder Games)

---

## 1. Front matter (page 1)

- [ ] Title, player count, play time, age — the box facts, repeated here.
- [ ] One-line pitch + theme in **1–2 sentences** answering "why am I doing this?" (Strain: skip it and players interrupt with "why am I drawing cards?" mid-teach).
- [ ] **Win condition and end trigger stated up front**, one sentence each. Teach the end before the means.
- [ ] [Optional] "How to read this book" note: which sections to read before the first game, which are reference.

## 2. Components

- [ ] Photograph or diagram of **every** component, labeled with its exact game term (the keyword list name, not a synonym). This page doubles as a missing-parts check.
- [ ] Component counts (e.g., "72 cards, 140 cubes").
- [ ] For cards with layout complexity: a **"how to read a card"** annotated breakdown (Meeple Mountain: the typical-turn and how-to-read-components sections are the most-read — make them detailed).

## 3. Setup

- [ ] Numbered steps in strict order of operations; a labeled diagram of the fully set-up table.
- [ ] For every component placed, state: **face-up or face-down; public or secret information.**
- [ ] First-player rule stated explicitly — even if it's "choose randomly."
- [ ] All setup exceptions live HERE (per player-count adjustments in a small table). Never scatter setup exceptions into later chapters.
- [ ] **"How to start" kick-off sentence**: who acts first and what the first action of the game is. (*Shadows Over Camelot* lesson: groups read the whole book and still ask "how do we start?")

## 4. Gameplay overview (the teach page)

- [ ] Structure of play in one diagram: game → rounds → turns → phases, with the **sequence hierarchy defined precisely** (ekted: define turn/round/phase and sub-phases like "before combat" explicitly).
- [ ] The turn in one sentence + a mnemonic if available (*Dominion*'s ABC: Action, Buy, Clean-up).
- [ ] What a player does **on their turn, from their perspective** — reveal detail in the order it becomes relevant, matching the verbal teach (Strain order: theme → goal → your turn → details).
- [ ] Pointers, not rules: "(see 5.2 Combat)" for every forward reference.

## 5. Detailed gameplay (the reference core)

Per phase/action, one headed section each:

- [ ] Heading names the action with the exact keyword ("Harvest", not "Working the Fields").
- [ ] Body opens with the binding constraint repeated in place: "First, **once** per turn, …" — the *Lanterns* lesson: constraints stated only in the overview get missed; restate them inside each detailed entry.
- [ ] Steps as a numbered list (order matters) or bullets (order free).
- [ ] **An example per non-obvious rule**, set in *italics* or an example box; illustrate a full situation, not an isolated clause (Unpub).
- [ ] Highlight flow-breaking exceptions visually (icon, box, or color band) the way *Ticket to Ride* highlights drawing locomotives.
- [ ] Card-interaction examples for combos that produce surprising results (*Glory to Rome* is the praised exemplar).

### Golden rules block (page 1 of any reference document)

1. Component text that contradicts this rulebook takes precedence, for that situation only. (MTG CR 101.1)
2. "Cannot" beats "can." If one effect allows and another forbids, the forbidding effect wins. (MTG CR 101.2)
3. If part of an instruction is impossible, perform as much as possible and ignore the rest. (MTG CR 101.3)
4. If effects are simultaneous or the order/decision-maker is unclear, the player taking their turn decides; players then proceed in turn order (APNAP). (MTG CR 101.4; Law of Root §1)
5. Timing vocabulary, defined once and used with 100% consistency: "at start of phase" resolves before anything else in the phase; "at end of phase" after everything; no interrupts exist unless a rule explicitly creates one (Law of Root timing rules). Tie-break or simultaneous-win rule stated here (e.g., Law of Root: current-turn player wins).

### Edge-case handling

- [ ] Each edge case gets its own labeled, searchable sub-header — not a prose paragraph mid-section.
- [ ] If an edge case needs more than ~3 lines, that's a design smell: cut the rule or fix the component (Jolly; Stegmaier's 99% exception heuristic).

## 6. End of game, scoring, tiebreakers

- [ ] End trigger first, then scoring steps in order, then tiebreakers — never interleaved.
- [ ] A worked scoring example with concrete numbers.

## 7. Back matter

- [ ] **Icon legend** — every icon with a one-line text gloss (mandatory at 10+ icons; Stegmaier reserves the last page for icon guide + game flow + index).
- [ ] **Game-flow summary**: the whole turn structure on one page — the returning player's re-entry point (Backe's third audience).
- [ ] Glossary: every keyword, alphabetical, one-line definition, cross-references.
- [ ] Index or detailed TOC (a front TOC can replace the index — Stegmaier).
- [ ] **Version number + date** on the document itself (Meeple Mountain). Credits.

---

## Quick-start guide & first-turn script (heavy games)

- **Quick-start (1 page)**: setup diagram + the 3–5 rules needed to complete Turn 1 + "read §5 when X happens." *Jaws of the Lion* tutorializes the entire first scenario.
- **First-turn script**: a literal annotated walkthrough — "You hold these 5 cards. Play this one here. Gain 2 coins. Your turn is over." Annotate *why*, not just what.
- **Teach-the-teacher page**: instructions for the person who will explain the game, not for playing it (*Asking for Trobils* reprint added a full page of this — Peter Vaughan's lesson).

## Player aid spec (summary; full standards in `iconography.md`)

- One aid per player; max one double-sided card; turn sequence + icon glossary + binding constraints; white space, no walls of text; symbols with a legend (Board Game Business top-5: #1 use symbols, #2 visually distinct, #3 white space, #4 one double-sided card, #5 no text walls).
- During early playtesting, playtest **player aids instead of a rulebook** (Stegmaier) — the aid becomes the rulebook's skeleton and the final product's per-player aid.

## Praised rulebooks to study (with what to steal)

| Rulebook | Steal this |
|---|---|
| *Root* / *Arcs* (Leder) | Dual-document split; *Law of Root* decimal numbering + Golden Rules; *Arcs*' welcoming tone |
| *Jaws of the Lion* | Tutorial-as-first-scenario; learn-by-playing |
| *Splendor* | 4-page total rulebook; length signals low complexity |
| *Ticket to Ride* | Visually highlighted exceptions |
| *Dominion* | ABC turn mnemonic |
| *Glory to Rome* | Card-interaction examples |
| *Belfort* | Diagram density |
| *SmallWorld* | Character overview cards as per-player reference |
| *Commands & Colors: Ancients* | Layout and section clarity |
| *Lanterns* (2nd printing) | Reference redundancy done right |
| *Dungeon Lords* | Humor that aids teaching (sparingly — Selinker: flavor, but sparingly) |
| *Dawn of the Zeds* | Multiple rulebooks for one heavy game (Stegmaier's praise) |
| *Asking for Trobils* | Teach-the-teacher page |
