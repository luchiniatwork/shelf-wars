# Color, Palettes & Double-Coding

Load this when choosing a palette, player colors, or double-coding scheme, or when simulation-testing a design. Symbol-*system* design (icon legend thresholds, card anatomy, icon count budgets) belongs to `board-game-rules-writing/references/iconography.md`; this file owns palette-level colorblind work and component-level coding.

## CVD types and what actually confuses

| Type | Prevalence | Mechanism | Practical confusions |
|---|---|---|---|
| Protan (protanopia/protanomaly) | ≈2% of males | L-cone absent/anomalous; reds **dim** | red↔black/dark gray, red/brown/green/yellow, blue↔purple |
| Deutan (deuteranopia/deuteranomaly) | ≈6% of males | M-cone absent/anomalous | red/brown/green/yellow, blue↔purple; no dimming |
| Tritan (tritanopia) | rare | S-cone | blue↔green, yellow↔violet |
| Monochromacy | very rare | no functional cone discrimination | all hue coding fails; only luminance/shape survives |

(Prevalence: Wikipedia, *Color blindness*; congenital red-green CVD ≈8% of men, ≈0.4–0.5% of women of Northern European ancestry, lower elsewhere. MLU grades all four types per game.)

Player-reported collision groups for wooden components (Stonemaier comments, colorblind player): **reds / dark oranges / browns**, **blues / pinks / purples**, **greens / yellows / light browns / light oranges**. Pick player colors from different groups, or vary lightness: e.g., two bright complementary colors (red + cyan) plus two dark complementary colors (magenta + green) — darks separate from brights on luminance alone.

## Safe palettes

**Okabe-Ito / Wong palette** (Okabe & Ito, *Color Universal Design*, 2002/2008; popularized by Bang Wong, *Nature Methods* 8:441, 2011) — designed to stay separable under all CVD types:

| Name | RGB | Hex |
|---|---|---|
| Orange | 230, 159, 0 | #E69F00 |
| Sky blue | 86, 180, 233 | #56B4E9 |
| Bluish green | 0, 158, 115 | #009E73 |
| Yellow | 240, 228, 66 | #F0E442 |
| Blue | 0, 114, 178 | #0072B2 |
| Vermillion | 213, 94, 0 | #D55E00 |
| Reddish purple | 204, 121, 167 | #CC79A7 |
| Black | 0, 0, 0 | #000000 |

For >8 categories, use Paul Tol's qualitative schemes (SRON technical note) — but past ~5 categories no hue-only scheme survives; you need double-coding regardless. Rules of thumb: avoid red–green adjacency for opponents' colors; never pair saturated red with saturated green as the *only* distinction; keep brightness contrast between any two colors that must differ (protanopes see red as dark).

## Double-coding methods, ranked by robustness

1. **Unique component shape** (3D coding) — survives darkness, distance, rotation, and touch: *Parks*' distinct token shapes, *Isle of Cats*' cat-ear/tail silhouettes. Best for player pieces and high-frequency tokens.
2. **Pattern/texture fill** — survives grayscale printing: *Azul*'s tile patterns, *Tussie Mussie*'s suit backgrounds.
3. **Icon/symbol per color** — standard fix: *The Crew* and *Dune Imperium* (dual-coded suits), *Splendor* later editions (gem shapes added after complaints), *Ticket to Ride* (symbol-coded board in later printings). Symbols must be **unique silhouettes** (star vs. droplet vs. bolt), large, high-contrast, consistently placed — *Walking in Burano* attempted this but symbols were small, faint, and inconsistently positioned (MLU/player reports). Non-rotation-symmetric symbols: cards are read upside down.
4. **Text label** — the universal fallback; costs localization. Put the color's name on the component when in doubt.
5. **ColorSym-style icon systems** (referenced on the Stonemaier chart) — public icon vocabularies for color naming. ColorADD is the proprietary alternative; criticized because its blue/red marks differ only by rotation and it requires rote memorization (Colorblind Games critique) — prefer your own unique silhouettes.

Anti-pattern to refuse: **red + green + blue + yellow as the default player-color quad** with no other coding (Quacks score track, graded B- for exactly this). Also refuse: hue-only links between components ("play this on the matching green space").

## Simulation & physical test procedures

Software (community-standard tools):
- **Color Oracle** — free full-screen desktop simulator (Win/Mac/Linux).
- **Coblis** — web-based image upload simulator.
- **Adobe Photoshop/Illustrator** — View → Proof Setup → Color Blindness (protanopia/deuteranopia modes).
- Browser dev tools/extensions (e.g., Stark, Funkify) for digital rulebooks, PnP PDFs, and campaign pages.

Run each key board/card/token sheet through all four types. Do it on final art, not just palette swatches — art muddies luminance.

Physical tests (no software needed):
1. **Low-light test** — photograph or view components under dim warm evening light. Stegmaier's Viticulture red↔orange/purple confusion surfaced exactly this way (first Panda sample, 2012).
2. **Grayscale print test** — print a sheet in pure grayscale; every category must remain separable by luminance/pattern. Approximates monochromacy and bad lighting.
3. **Distance test** — board state legible from 1.5–2 m; tableau text from the next seat; if not, enlarge or recode.
4. **Rotation test** — every code readable upside down across the table.
5. **Fan test** — hand cards fanned one-handed: cost/type coding must survive (top-left placement).
6. **Colorblind-tester confirmation** — simulation is a screen, not a person; recruit CVD playtesters for the final pass.

## Verification ladder

1. Palette chosen from a CVD-safe set → 2. double-coding designed in → 3. simulated in all four types → 4. physical low-light + grayscale + distance + rotation tests → 5. colorblind playtester sign-off. A game that passes all five earns its rulebook accessibility statement line; a game that skips 5 is self-graded.
