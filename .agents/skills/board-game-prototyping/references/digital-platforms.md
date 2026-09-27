# Digital Playtesting Platforms — Deep Reference

Load this when choosing between Tabletop Simulator, Tabletopia, Screentop.gg, or Playingcards.io; setting one up; scripting automation; or planning a physical↔digital migration. Prices and limits verified at research time — re-verify before quoting to a user.

## Decision table

| | Tabletop Simulator | Tabletopia | Screentop.gg | Playingcards.io |
|---|---|---|---|---|
| Designer cost | $19.99 (Steam, one-time) | Free tier; paid tiers for more setups/features | Free | Free |
| Tester cost/friction | $19.99 + Steam install each | Free, browser link | Free, browser link, no account | Free, browser link, no account |
| Presentation | 3D physics sandbox | 3D, polished | 2D top-down | 2D card-table |
| Scripting | Full Lua API + XML UI | None for designers | None | No code; automation buttons |
| Mid-session component edits | Yes (spawn/save objects) | Clunky (reported) | No — components locked once a session starts | Limited (edit mode mid-room is awkward) |
| Distribution | Steam Workshop or save file | Public/private Tabletopia link | Share URL; JSON export | Share URL; `.pcio` export/import |
| Best for | Complex/component-heavy games; repeated balance loops; scripted setup & scoring | Presentable remote demos; publisher/reviewer views | Fast iteration; maximum tester accessibility; card+board games | Card-first games; trick-taking, deckbuilders, hand management |
| Weakness | Per-tester price + install; build learning curve | Free-tier setup limits; edit friction | No automation; hidden-info handling is manual | Non-card components weak; small text on phones; no voice |

## Tabletop Simulator (TTS)

**Cost model:** $19.99 on Steam per participant (frequent 50% sales). Host-only option: Steam Remote Play Together lets a host stream to non-owners — viable for guided tests, not for blind waves.

**Build workflow:**
1. **Decks:** TTS's custom deck object takes ONE sheet image and slices it into a grid — up to 10 columns × 7 rows = 70 slots (the last slot conventionally holds the hidden-card preview back). Keep every card identical pixel size; upload the sheet to Steam Cloud (in-game upload) or host it yourself.
2. **Boards/mats:** flat image applied to a table or custom board object.
3. **Tokens/figurines:** PNG with transparency on custom tokens; chip objects for counters; infinite bags for supply piles.
4. **Saves:** a table state is a JSON file — version it like source code (`mygame_v0.7_tts.json`). nanDECK can generate/edit TTS saves directly (`DECK` directive + Export → TTS), which closes the spreadsheet→physical→digital loop.
5. **Distribution:** Steam Workshop (public/unlisted) for testers; or send the save JSON directly. Unlisted Workshop items still require testers to own TTS.

**Scripting (Lua + XML UI):** attach scripts globally or per object. Core events: `onLoad()`, `onUpdate()`, `onObjectDrop()`, `onPlayerTurn()`. Common automations: scripted setup/deal, scoring counters, turn structure enforcement. API docs: api.tabletopsimulator.com. Don't automate until the manual version is stable — scripted setup is the highest-value first script.

**Pitfalls:** testers on different Workshop versions (force-update before sessions); physics accidents (flipped tables, flying cards — lock objects that shouldn't move); assuming non-gamers can drive the camera (do a 5-minute controls tutorial at session start).

## Tabletopia

**Model:** browser-based 3D sandbox; testers join free via link. Stegmaier uses Tabletopia for rapid prototyping and remote tests — but explicitly as a *secondary* option to physical.

**Build workflow:** create the game in the Tabletopia Workshop; upload components as images (cards, boards) or use stock pieces (pawns, dice, cubes from their library); arrange and save *setups*. Free tier is usually sufficient for one prototype; paid tiers add setups and advanced features [contested — exact free-tier limits change; check current plan page].

**When to pick it:** you want 3D presentation (reviewers, publishers, remote conventions) without TTS's price/install wall, and your testers are non-technical.

**Pitfalls:** mid-game component edits are reported clunky — prepare variant setups in advance instead; free-tier limits can bite larger games; no scripting, so setup/teardown labor is manual every session.

## Screentop.gg

**Model:** free, browser, no accounts for anyone; players join by URL. 2D. Actively used by the design community — many Protospiel Online entries are hosted on it. Best mobile accessibility of the four.

**Build workflow:** create a room → upload component images (PNGs) → define decks, boards, hand areas, and tokens → share the link. Export the game definition as JSON and keep it in version control; reimport to iterate.

**When to pick it:** maximum tester accessibility (zero install/account), fast 2D iteration, and tests where some players are on tablets/phones.

**Pitfalls:** no scripting or automation (setup is manual); components can't be changed once a session is running — any content change means a new room/link; hidden-information handling (hands) works but verify the exact visibility behavior with a friend before a blind wave.

## Playingcards.io

**Model:** free, browser, no accounts; a shared card table. Import/export the whole room as a `.pcio` file (JSON) — version it like code.

**Build workflow:** create a room → Edit Mode → upload custom card fronts/backs (and a card back for each deck) → place widgets: holders, player seats & turn buttons, counters, dice, spinners, timers → add **automation buttons** for repetitive actions. Documented automation actions: Move Objects, Shift Objects, Recall Objects, Flip Objects, Rotate Objects, Shuffle Objects, Sort Objects, Change Counter, Change Dice, Spin Spinner, Start/Pause Timer, Change Timer, Change Chooser, Stand Up Players, Finish Turn.

**When to pick it:** card-first games (deckbuilders, trick-taking, hand management) where dealing/shuffling automation covers 90% of the fiddliness.

**Pitfalls:** weak for non-card components (boards are just images); card text must be legible at small sizes — use your stage-appropriate large-text card layout, not final 9pt text; no built-in voice — pair with Discord/Meet/Zoom; teach testers the recall/shuffle buttons or they will hand-drag 60 cards.

## Cross-cutting practices

- **Version digitally the same as physically:** version number in the game title/room name/save file; changelog entry per uploaded build; never edit a build mid-wave — clone it.
- **Parallel-build rule:** when a balance conclusion comes from digital sessions, spot-check it on the physical build before it hardens into manufacturing specs (Stegmaier: digital obscures physical-component issues).
- **Accessibility ladder:** Screentop.gg / Playingcards.io (zero friction) → Tabletopia (link, free) → TTS ($19.99 + install). Default to the lowest rung that runs your game's components.
- **Session support:** whatever the platform, pair it with voice (Discord/Meet), a shared rules PDF or link, and your feedback form URL with a version field.
- **Hidden information audit:** before any blind wave, personally verify hand visibility, deck-face direction, and discard visibility with a confederate. Digital hidden-info bugs silently invalidate sessions.

## Migration triggers (physical ↔ digital)

Go digital when: remote/blind waves begin; you need 20+ balance repetitions fast; testers can't print PnP; your group is geographically split.
Go back physical when: testing tactility (dexterity, stacking, bag-building), table footprint and readability across a real table, component usability (can players actually stack/sort/shuffle it?), and always before finalizing manufacturing specs.
