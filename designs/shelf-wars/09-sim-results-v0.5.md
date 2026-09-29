# 09 — Sim Results, v0.5 (economy redesign: falsified hypothesis, better fix found)

Date: 2026-09-28 · Sim: iteration 4 · 500 runs/config · Base: v0.4
(chip3 = 4 actions + 6c, E 4–5, persist, retaliation on, nudge off for
creation runs)

## The headline, honestly

**The v0.5 hypothesis failed.** Demand creation — the plan in
`08-economy-redesign-v0.5-plan.md` — does not fix the deflation, and the
mechanism of failure is now triply confirmed. But the validation runs found
a better lever hiding in plain sight: **ad slots 3 → 4**, the "untested
middle path" flagged in iteration 2. It is the best single change in the
entire sim campaign.

## Experiment 1: demand creation as planned (maturity delay, public, random wants)

| Metric | Control (no creation) | creates 1 | creates 2 | creates 1 + bias |
|---|---|---|---|---|
| Created / game | 0 | 7.3 | 14.7 | 7.3 |
| Created served | — | 0.8 (11%) | 1.5 (10%) | 0.8 (11%) |
| Table total | 10.6c | 10.5c | 10.5c | 10.5c |
| Spike win | 64% | 65% | 65% | 64% |

**Verdict: falsified.** Creation adds demand; demand was never the choke.
The funnel's eligibility gauntlet converts dealt demand at ~50% and *random*
created demand at ~10% (random wants align with nobody's coverage; E-band
creations die against the creator's own price dial). This is also why the
FCM analogy breaks: FCM demand is fungible ("do you stock pizza?") while
ours passes an attribute-coverage gate. Creation at feasible dosages moves
table totals by ~0.1c. Two bot-fidelity fixes were needed to reach even
this reading (creation decoupled from ad-placement success; bots shown the
public pending row) — those fixes are permanent sim improvements.

Creation is **shelved, not adopted**: it costs a component (growth piles)
and a rule, and the evidence says it buys neither economy nor balance.
(Its one merit — conversion rises to 18% under a relaxed awareness gate —
doesn't change the calculus.)

## Experiment 2: the eligibility levers (the pivot)

The deflation's true choke is the three-gate funnel. Attacking the gates:

| Config | D / E / S win % | Table total | Q2-lock | Verdict |
|---|---|---|---|---|
| Ad slots 3 (v0.4) | 8 / 28 / 64 | 10.6c | 21% | baseline |
| **Ad slots 4** | **31 / 22 / 47** | **13.2c** | **34%** | **ADOPTED (v0.5)** |
| Ad slots 5 | 46 / 19 / 35 | 15.6c | 44% | too loose (Discounter leads, lock creeps) |
| Ad slots 4 + chip3-cash 5 | 11 / 8 / 81 | 13.4c | 40% | chip price must stay 6c |
| Near-miss (any customer) | 7 / 88 / 5 | 15.9c | 62% | **Rejected**: as coded it also covered single-want customers → coverage nearly irrelevant |
| Near-miss (2+-want only) | 7 / 90 / 4 | 16.0c | 79% | **Rejected**: relaxing the coverage gate kills the R&D game in any form |

**Why ad slots work when nothing else did:** 3 slots × 3 segments at 3
players = 9 awareness slots for 3 companies — everyone is awareness-poor,
and the coverage leader (needing least re-investment) wins the churn war
by default. A 4th slot lets all three archetypes hold presence *and still
contest*: volume play (Discounter) becomes viable for the first time in the
whole campaign, Spike drops below 50%, and the looser awareness raises the
serve rate (faucet) enough to matter (+25% table total) without freeing
coverage. Note the clean monotonic ladder: 3 → 4 → 5 slots walks
Spike 65→47→35% and Discounter 8→31→46%. The knob has excellent resolution.

## v0.5 design decision

**Change exactly one number: 4 ad slots per segment** (physical change:
four boxes per segment row on the market sheet; rules text: "4 per
segment"). Everything else from v0.4 stands unchanged, including the nudge
(balance-neutral in tests; Campaign keeps it because a one-effect space
stays teachable). No growth piles, no creation rule.

Validated state (500 runs): **Spike 47 / Discounter 31 / Engine 22**,
Q2-leader-wins 34%, table total 13.2c, unsold widgets 1.15/seat/quarter
(in band), undercuts + leader-bumps active.

## The deflation, final accounting

ad-slots 4 improves the economy ~25% (10.6 → 13.2c) by raising the serve
rate — an eligibility fix, not a faucet fix. The economy is still tight by
construction (faucet ceiling ≈ sink floor). What is now established, with
more confidence than any previous iteration:

- **Cost-side fixes break balance** (prodcost, adcost, start-cash — all
  re-verified).
- **Demand-side fixes can't convert** (creation, mboost, inflation).
- **Eligibility-side fixes work but each gate behaves differently**:
  awareness (slots) = balance + mild buoyancy; coverage (near-miss) =
  buoyancy but kills the attribute game; price (bands) = starves Budget.
- Remaining feel lever: **×5 presentation rescale** (identical ratios,
  bigger-feeling numbers). Zero structural risk. Recommend applying it to
  the physical build from the start: prices 10–30, production 10, ads 5,
  expand 20, chip3 20 actions-equivalent... i.e. all cash values ×5,
  action costs unchanged.

If the game still feels deflationary *to humans* after the rescale, the
honest next step is a different verb family (persistent ad campaigns,
contract customers, segment growth as a scoring track) — a v0.6 design
conversation informed by table data, not more knob sims.

## Sim campaign status: complete

Balance structure: found (chip3 = 4 actions + 6c; ad slots 4). Economy:
bounded and understood; tight by design; feel fix is presentation-layer.
Everything still open (income speed, price-reveal poker, bankruptcy feel,
nudge value, creation-as-texture) is a human question. The next artifact
change should come from a table, not this file.
