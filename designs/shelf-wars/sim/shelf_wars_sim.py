#!/usr/bin/env python3
"""Shelf Wars v0.2 — greedy-bot Monte Carlo sim, iteration 2.

Changes from iteration 1 (see 05-sim-results-v0.1.md):
- v0.2 rules by default: 3rd chip costs 3 actions (--chip3-cost), unsold
  customers persist one quarter (--variant persist is now the default).
- Full 6-quarter game, demand curve 5/7/9/11/12/13 (57 customers, 3p).
- Retaliation-capable bots (--retaliate, default on):
  * Pricing: match-or-one-step-down against comparable rivals (previous
    quarter's revealed prices), floored at production cost.
  * Ad bumping: prefer bumping the current cash leader's ad over oldest.
- Metrics: per-quarter cash trajectories, undercut and leader-bump rates.

Deliberate simplifications (unchanged): Research space unmodeled; prices
are policy formulas, not real poker; cheapest covering line sells; bots see
the current row only. Deck space sampled per run (fixed composition,
randomized attribute assignment + band prices).

Usage: python3 sim/shelf_wars_sim.py --runs 500 [--retaliate 0] [--variant discard]
"""
import argparse
import itertools
import os
import random
from collections import defaultdict

ALL_ATTRS = ["A", "B", "C", "D", "X"]
NATTRS = 4        # knob: --nattrs 4|5 (5 dilutes any one line's coverage share)
EWANTS = 2        # knob: --ewants 2|3 (3 makes Enthusiast a true niche for 3-chip lines)
SALE_CAP = 0      # knob: --sale-cap N (max widgets one seller can sell per segment per quarter; 0=off)
CHIP3_CASH = 0    # knob: --chip3-cash N (cash due when the 3rd chip completes; 0=free)
LINE_UPKEEP = 0   # knob: --line-upkeep N (cash per product line per quarter at upkeep)
CAMPAIGN_CREATES = 0  # knob: --campaign-creates N (Campaign adds N fresh customers to the row)
LATE_INFLATION = 0  # knob: --late-inflation N (Q5+ customers pay +N, capped at 6)
TREND_START = "A"  # knob: --trend-start A|B|C|D|random
PLAYERS = 3       # knob: --players 3|4 (4p adds the Corporate segment)
SHELF_CAP = 6     # knob: --shelf


def attrs():
    return ALL_ATTRS[:NATTRS]


def pairs_list():
    return ["".join(p) for p in itertools.combinations(attrs(), 2)]
AD_SLOTS = 3
AD_COST = 1       # knob: --adcost (v0.1 finding: 0 unleashes the coverage leader)
PROD_COST = 2     # knob: --prodcost (v0.1 finding: 1 helps the premium leader)
EXPAND_COST = 4
CAP_MAX = 5
START_CASH = 10   # knob: --start-cash (economy faucet: funds strategies without new rules)
QUARTERS = 6      # full game (v0.2)
ADAPT_THRESHOLD = 3
CASH_RESERVE = 2
CHIP3_COST = 4    # v0.3: 3rd chip costs 4 actions (99% dominance at 3 over the full arc)
RETALIATE = True  # knob: --retaliate 0
SCRAP = False     # knob: --scrap 1 (broke seats liquidate widgets for 1c each)
TREND_PREMIUM = 1  # knob: --trend-premium (+2 rejected: self-reinforcing)
MBOOST = 0         # knob: --mboost N (extra Mainstream customers per quarter — demand faucet)
PRICE_BANDS = {"B": [2, 3], "M": [3, 4, 5], "E": [4, 5], "C": [4]}  # v0.3 bands; C = Corporate (4p)


def seg_list():
    return ["B", "M", "E", "C"] if PLAYERS >= 4 else ["B", "M", "E"]

# Full 6-quarter demand curve (3p): 5/7/9/11/12/13 = 57 customers.
COMP_3P = [(1, "B", 2), (1, "M", 2), (1, "E", 1),
           (2, "B", 3), (2, "M", 3), (2, "E", 1),
           (3, "B", 4), (3, "M", 3), (3, "E", 2),
           (4, "B", 4), (4, "M", 5), (4, "E", 2),
           (5, "B", 5), (5, "M", 5), (5, "E", 2),
           (6, "B", 5), (6, "M", 5), (6, "E", 3)]
# 4p scaling (~+33%): 7/9/12/15/16/17 = 76 customers; Corporate (C) absorbs
# the extra volume — 1-want singles at max 4, resolving last.
COMP_4P = [(1, "B", 2), (1, "M", 2), (1, "E", 1), (1, "C", 2),
           (2, "B", 3), (2, "M", 3), (2, "E", 1), (2, "C", 2),
           (3, "B", 4), (3, "M", 4), (3, "E", 2), (3, "C", 2),
           (4, "B", 5), (4, "M", 5), (4, "E", 2), (4, "C", 3),
           (5, "B", 5), (5, "M", 5), (5, "E", 3), (5, "C", 3),
           (6, "B", 5), (6, "M", 6), (6, "E", 3), (6, "C", 3)]



class Customer:
    def __init__(self, row):
        self.id = int(row["id"])
        self.segment = row["segment"]
        self.wants = set(row["wants"])
        self.max_price = int(row["max_price"])
        self.age = 0


class Line:
    MAX_CHIPS = 3

    def __init__(self, chips, price):
        self.chips = set(chips)
        self.price = price
        self.chip3_progress = 0


class Seat:
    def __init__(self, idx, policy, chips, base_prices, seg_pref):
        self.idx = idx
        self.policy = policy
        self.base_prices = base_prices
        self.seg_pref = seg_pref
        self.cash = START_CASH
        self.capacity = 2
        self.shelf = 0
        self.lines = [Line(chips, base_prices[0])]
        self.unsold_prev = 0
        self.prev_prices = []
        self.nudges = 0
        self.sales = 0
        self.cash_by_quarter = []
        self.unsold_by_quarter = []

    def covers(self, cust):
        return [l for l in self.lines if cust.wants <= l.chips]


def build_sim_deck(rng):
    """Sample the deck space: fixed per-quarter composition, randomized
    attribute assignment (even-split singles, cycling pairs) + band prices."""
    comp = COMP_4P if PLAYERS >= 4 else COMP_3P
    n_singles = sum(c for _, s, c in comp if s in ("B", "C"))
    n_pairs = sum(c + (MBOOST if s == "M" else 0) for _, s, c in comp if s in ("M", "E"))
    singles = [attrs()[i % len(attrs())] for i in range(n_singles)]
    rng.shuffle(singles)
    if EWANTS == 2:
        want_pool = pairs_list()
    else:
        want_pool = ["".join(p) for p in itertools.combinations(attrs(), EWANTS)]
    pairs = [want_pool[i % len(want_pool)] for i in range(n_pairs)]
    rng.shuffle(pairs)
    si = pi = cid = 0
    deck = {q: [] for q in range(1, QUARTERS + 1)}
    for q, seg, cnt in comp:
        if seg == "M":
            cnt += MBOOST
        for _ in range(cnt):
            cid += 1
            if seg in ("B", "C"):
                wants = {singles[si]}; si += 1
            elif seg == "E":
                pool = ["".join(p) for p in itertools.combinations(attrs(), EWANTS)]
                wants = set(pool[pi % len(pool)]); pi += 1
            else:
                wants = set(pairs[pi]); pi += 1
            band = PRICE_BANDS[seg]
            cust = Customer({"id": cid, "segment": seg, "wants": "".join(sorted(wants)),
                             "max_price": band[rng.randrange(len(band))]})
            deck[q].append(cust)
    for q in deck:
        rng.shuffle(deck[q])
    return deck


def make_seats(players):
    def pref(order):
        return [s for s in order if s in seg_list()]
    seats = [
        Seat(0, "Discounter", "AB", [2, 3], pref(["B", "M", "C", "E"])),
        Seat(1, "Engine", "BC", [4, 4], pref(["M", "C", "B", "E"])),
        Seat(2, "Spike", "CD", [5, 4], pref(["E", "M", "C", "B"])),
    ]
    if players >= 4:
        # Portfolio: mixed strategy — B-volume line + M-margin line, no 3rd chip
        seats.append(Seat(3, "Portfolio", "AB", [2, 4], pref(["M", "B", "C", "E"])))
    return seats


def trend_step(marker, direction):
    a = attrs()
    i = a.index(marker)
    return a[(i + direction) % len(a)]


def nudge_toward(marker, targets):
    if marker in targets:
        return marker
    a = attrs()
    i = a.index(marker)
    best, best_d = None, 99
    for t in targets:
        d = (a.index(t) - i) % len(a)
        d = min(d, len(a) - d)
        if d < best_d:
            best, best_d = t, d
    if best is None:
        return marker
    fwd = (a.index(best) - i) % len(a)
    return trend_step(marker, 1 if fwd <= len(a) // 2 else -1)


def set_prices(seats, quarter, metrics):
    """Policy bases + adaptive unsold rule + retaliation undercut (public
    info: last quarter's revealed prices), floored at production cost."""
    for s in seats:
        for j, line in enumerate(s.lines):
            base = s.base_prices[min(j, len(s.base_prices) - 1)]
            price = max(1, base - 1) if s.unsold_prev >= ADAPT_THRESHOLD else base
            if RETALIATE and quarter > 1:
                ceiling = max(PRICE_BANDS[s.seg_pref[0]])
                rivals = [p for r in seats if r is not s for p in r.prev_prices if p <= ceiling]
                if rivals:
                    rmin = min(rivals)
                    if base - 1 <= rmin <= base + 1 and rmin - 1 >= PROD_COST:
                        newp = max(rmin - 1, base - 1, PROD_COST)
                        if newp < price:
                            metrics["undercuts"] += 1
                            price = newp
            line.price = price


def segment_value(seat, seg, customers, trend):
    v = 0
    for c in customers:
        if c.segment != seg:
            continue
        maxp = c.max_price + (TREND_PREMIUM if trend[0] in c.wants else 0)
        for l in seat.covers(c):
            if l.price <= maxp:
                v += l.price - PROD_COST
                break
    return v


def place_ad(seat, market, customers, trend, age_tick, leader_idx, metrics):
    if seat.cash < AD_COST:
        return False
    scored = []
    for seg in seg_list():
        scored.append((segment_value(seat, seg, customers, trend), -seat.seg_pref.index(seg), seg))
    scored.sort(reverse=True)
    own_ads = sum(1 for seg in seg_list() for (si, _) in market[seg] if si == seat.idx)
    if scored[0][0] <= 0 and own_ads > 0:
        return False
    for _, _, seg in scored:
        slots = market[seg]
        if len(slots) < AD_SLOTS:
            slots.append((seat.idx, age_tick))
            seat.cash -= AD_COST
            return True
        opp = [(i, si, t) for i, (si, t) in enumerate(slots) if si != seat.idx]
        if opp:
            lead = [x for x in opp if RETALIATE and x[1] == leader_idx]
            pool = lead if lead else opp
            i = min(pool, key=lambda x: x[2])[0]
            if lead:
                metrics["leader_bumps"] += 1
            slots[i] = (seat.idx, age_tick)
            seat.cash -= AD_COST
            return True
    return False


def do_produce(seat):
    n = min(seat.capacity, SHELF_CAP - seat.shelf, (seat.cash - CASH_RESERVE) // PROD_COST)
    n = max(0, n)
    seat.shelf += n
    seat.cash -= n * PROD_COST


def do_expand(seat):
    if seat.capacity < CAP_MAX and seat.cash >= EXPAND_COST + 2 * PROD_COST + CASH_RESERVE:
        seat.capacity += 1
        seat.cash -= EXPAND_COST
        return True
    return False


def best_chip(line, customers, target_segs):
    best_a, best_gain = None, -1
    for a in attrs():
        if a in line.chips:
            continue
        gain = sum(
            1
            for c in customers
            if c.segment in target_segs and not c.wants <= line.chips and c.wants <= line.chips | {a}
        )
        if gain > best_gain or (gain == best_gain and (best_a is None or a < best_a)):
            best_a, best_gain = a, gain
    return best_a


def run_actions(seat, quarter, market, customers, trend, age_tick, seats, metrics, execs):
    third_chip_done = any(len(l.chips) >= 3 for l in seat.lines)
    has_two_lines = len(seat.lines) >= 2
    leader_idx = max((r for r in seats if r is not seat), key=lambda r: r.cash).idx
    acts = []

    if seat.policy == "Discounter":
        acts = ["produce", "market", "market"]
        if 3 <= quarter <= 4:
            acts.append("rd2" if not has_two_lines else "market")
        elif quarter >= 5:
            acts.append("market")
    elif seat.policy == "Engine":
        if quarter == 1:
            acts = ["produce", "market", "market"]
        elif quarter == 2:
            acts = ["expand", "produce", "market"]
        elif quarter == 3:
            acts = ["produce", "expand", "market", "market"]
        elif quarter in (4, 5):
            acts = ["rd3", "rd3", "produce", "market"] if not third_chip_done else ["produce", "market", "market", "market"]
        else:
            acts = ["rd3", "produce", "market", "market"] if not third_chip_done else ["produce", "market", "market", "market"]
    elif seat.policy == "Spike":
        if quarter == 1:
            acts = ["rd3", "rd3", "rd3"]  # all-in on Q1 R&D (3 of the 4+ chip actions)
        elif quarter == 2:
            acts = ["rd3", "produce", "market"] if not third_chip_done else ["produce", "market", "campaign"]
        elif quarter == 3:
            if not third_chip_done:
                acts = ["rd3", "produce", "market", "market"]
            elif not has_two_lines:
                acts = ["produce", "rd2", "rd2", "market"]
            else:
                acts = ["produce", "campaign", "market", "market"]
        else:
            acts = ["rd3", "produce", "market", "market"] if not third_chip_done else ["produce", "campaign", "market", "market"]
    elif seat.policy == "Portfolio":
        if quarter == 1:
            acts = ["produce", "market", "market"]
        elif quarter == 2:
            acts = ["produce", "market", "campaign"]
        elif quarter == 3:
            acts = ["produce", "rd2", "rd2", "market"] if not has_two_lines else ["produce", "market", "market", "market"]
        elif quarter == 4:
            acts = ["produce", "expand", "market", "market"]
        else:
            acts = ["produce", "market", "market", "market"]

    if SCRAP and seat.cash < CASH_RESERVE and seat.shelf > 0:
        n = min(seat.shelf, 2)
        seat.shelf -= n
        seat.cash += n  # liquidate at 1c/widget to escape the bankruptcy dead-state
        metrics["scraps"] += n

    for act in acts[:execs]:  # exec cap is a hard guardrail — scripts are priority-ordered
        if act == "produce":
            do_produce(seat)
        elif act == "expand":
            do_expand(seat)
        elif act == "market":
            place_ad(seat, market, customers, trend, age_tick, leader_idx, metrics)
            place_ad(seat, market, customers, trend, age_tick, leader_idx, metrics)
        elif act == "campaign":
            if place_ad(seat, market, customers, trend, age_tick, leader_idx, metrics):
                target = set().union(*(l.chips for l in seat.lines))
                new = nudge_toward(trend[0], target)
                if new != trend[0]:
                    trend[0] = new
                    seat.nudges += 1
                for _ in range(CAMPAIGN_CREATES):
                    seg = seat.seg_pref[0]
                    band = PRICE_BANDS[seg]
                    cid = int(metrics["cid"])
                    if seg in ("B", "C"):
                        wants = {attrs()[cid % len(attrs())]}
                    else:
                        pool = pairs_list()
                        wants = set(pool[cid % len(pool)])
                    metrics["cid"] += 1
                    customers.append(Customer({"id": 1000 + cid, "segment": seg,
                                               "wants": "".join(sorted(wants)),
                                               "max_price": band[cid % len(band)]}))
                    metrics["created_customers"] += 1
        elif act == "rd2":
            if not has_two_lines:
                a = best_chip(Line(set(), 0), customers, seat.seg_pref[:2])
                seat.lines.append(Line(a, seat.base_prices[1]))
                has_two_lines = True
            elif len(seat.lines[1].chips) < 2:
                a = best_chip(seat.lines[1], customers, seat.seg_pref[:2])
                if a:
                    seat.lines[1].chips.add(a)
            else:
                place_ad(seat, market, customers, trend, age_tick, leader_idx, metrics)  # line complete; spend on ads
        elif act == "rd3":
            line = seat.lines[0]
            if len(line.chips) >= Line.MAX_CHIPS:
                place_ad(seat, market, customers, trend, age_tick, leader_idx, metrics)
            elif line.chip3_progress == CHIP3_COST - 1 and seat.cash < CHIP3_CASH:
                place_ad(seat, market, customers, trend, age_tick, leader_idx, metrics)  # can't afford completion
            else:
                line.chip3_progress += 1
                if line.chip3_progress >= CHIP3_COST:
                    seat.cash -= CHIP3_CASH
                    a = best_chip(line, customers, seat.seg_pref[:2])
                    if a:
                        line.chips.add(a)


def resolve_income(seats, market, row, trend, quarter, variant, metrics):
    order = [(quarter - 1 + k) % len(seats) for k in range(len(seats))]
    sold_ids = set()
    sold_in_seg = {s.idx: defaultdict(int) for s in seats}
    for seg in seg_list():
        for cust in [c for c in row if c.segment == seg]:
            cands = []
            for s in seats:
                if s.shelf < 1:
                    continue
                if SALE_CAP and sold_in_seg[s.idx][seg] >= SALE_CAP:
                    metrics["cap_blocks"] += 1
                    continue
                ads = sum(1 for (si, _) in market[seg] if si == s.idx)
                if ads < 1:
                    continue
                covering = s.covers(cust)
                if not covering:
                    continue
                line = min(covering, key=lambda l: l.price)
                maxp = cust.max_price + (TREND_PREMIUM if trend[0] in cust.wants else 0)
                if line.price > maxp:
                    continue
                cands.append((line.price, -ads, order.index(s.idx), s))
            if cands:
                cands.sort(key=lambda x: x[:3])
                price, _, _, winner = cands[0]
                winner.cash += price
                winner.shelf -= 1
                winner.sales += 1
                sold_in_seg[winner.idx][seg] += 1
                if price == 1:
                    metrics["price1_sales"] += 1
                sold_ids.add(cust.id)
    leftover = [c for c in row if c.id not in sold_ids]
    if variant == "persist":
        for c in leftover:
            c.age += 1
        survivors = [c for c in leftover if c.age < 2]
        metrics["customers_unsold"] += sum(1 for c in leftover if c.age >= 2)
        return survivors
    metrics["customers_unsold"] += len(leftover)
    return []


def run_game(seed, variant):
    rng = random.Random(seed)
    deck = build_sim_deck(rng)
    seats = make_seats(PLAYERS)
    market = {seg: [] for seg in seg_list()}
    trend = [attrs()[rng.randrange(len(attrs()))]] if TREND_START == "random" else [TREND_START]
    carry = []
    metrics = defaultdict(float)
    age_tick = 0

    for q in range(1, QUARTERS + 1):
        if q > 1:
            trend[0] = trend_step(trend[0], 1)
        row = carry + deck[q]
        if LATE_INFLATION and q >= 5:
            for c in row:
                c.max_price = min(6, c.max_price + LATE_INFLATION)
        carry = []
        set_prices(seats, q, metrics)
        execs = 3 if q <= 2 else 4
        for s in seats:
            run_actions(s, q, market, row, trend, age_tick, seats, metrics, execs)
            age_tick += execs
        carry = resolve_income(seats, market, row, trend, q, variant, metrics)
        for s in seats:
            s.cash = max(0, s.cash - LINE_UPKEEP * len(s.lines))  # permanent assets carry permanent costs
            s.unsold_prev = s.shelf
            s.unsold_by_quarter.append(s.shelf)
            s.cash_by_quarter.append(s.cash)
            s.prev_prices = [l.price for l in s.lines]
            metrics[f"cashq{q}_" + s.policy] += s.cash

    final = [s.cash for s in seats]
    metrics["games"] += 1
    metrics["winner_" + seats[final.index(max(final))].policy] += 1
    metrics["nudges"] += sum(s.nudges for s in seats)
    metrics["unsold_widgets"] += sum(sum(s.unsold_by_quarter) for s in seats)
    mid = sum(s.unsold_by_quarter[2] + s.unsold_by_quarter[3] for s in seats)  # Q3-Q4
    metrics["unsold_midgame"] += mid
    metrics["final_total"] += sum(final)
    metrics["last_over_leader"] += min(final) / max(final) if max(final) > 0 else 0.0
    q2_leader = max(range(3), key=lambda i: seats[i].cash_by_quarter[1])
    if final.index(max(final)) == q2_leader:
        metrics["q2_leader_wins"] += 1
    for s in seats:
        metrics["cash_" + s.policy] += s.cash
        metrics["sales_" + s.policy] += s.sales
    return metrics


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--runs", type=int, default=500)
    ap.add_argument("--variant", choices=["discard", "persist"], default="persist")
    ap.add_argument("--bband", default="2,3")
    ap.add_argument("--mband", default="3,4,5")
    ap.add_argument("--eband", default="4,5")
    ap.add_argument("--chip3-cost", type=int, default=4)
    ap.add_argument("--prodcost", type=int, default=2)
    ap.add_argument("--adcost", type=int, default=1)
    ap.add_argument("--retaliate", type=int, default=1, help="1=undercut + leader-bump (default), 0=off")
    ap.add_argument("--scrap", type=int, default=0, help="1=broke seats liquidate widgets for 1c each")
    ap.add_argument("--trend-premium", type=int, default=1)
    ap.add_argument("--mboost", type=int, default=0, help="extra Mainstream customers per quarter")
    ap.add_argument("--players", type=int, default=3, choices=[3, 4])
    ap.add_argument("--shelf", type=int, default=6)
    ap.add_argument("--sale-cap", type=int, default=0, help="max sales per seller per segment per quarter (0=off)")
    ap.add_argument("--nattrs", type=int, default=4, choices=[4, 5])
    ap.add_argument("--ewants", type=int, default=2, choices=[2, 3])
    ap.add_argument("--chip3-cash", type=int, default=0, help="cash due when the 3rd chip completes")
    ap.add_argument("--trend-start", default="A", help="A|B|C|D|random")
    ap.add_argument("--start-cash", type=int, default=10)
    ap.add_argument("--line-upkeep", type=int, default=0)
    ap.add_argument("--campaign-creates", type=int, default=0, help="Campaign adds N fresh customers to its segment")
    ap.add_argument("--late-inflation", type=int, default=0, help="Q5+ customers pay +N (cap 6)")
    args = ap.parse_args()

    global CHIP3_COST, PROD_COST, AD_COST, RETALIATE, SCRAP, TREND_PREMIUM, MBOOST, PLAYERS, SHELF_CAP, SALE_CAP, NATTRS, EWANTS, CHIP3_CASH, TREND_START, START_CASH, LINE_UPKEEP, CAMPAIGN_CREATES, LATE_INFLATION
    CHIP3_COST = args.chip3_cost
    PROD_COST = args.prodcost
    AD_COST = args.adcost
    RETALIATE = bool(args.retaliate)
    SCRAP = bool(args.scrap)
    TREND_PREMIUM = args.trend_premium
    MBOOST = args.mboost
    PLAYERS = args.players
    SHELF_CAP = args.shelf
    SALE_CAP = args.sale_cap
    NATTRS = args.nattrs
    EWANTS = args.ewants
    CHIP3_CASH = args.chip3_cash
    TREND_START = args.trend_start
    START_CASH = args.start_cash
    LINE_UPKEEP = args.line_upkeep
    CAMPAIGN_CREATES = args.campaign_creates
    LATE_INFLATION = args.late_inflation
    PRICE_BANDS.update({"B": [int(x) for x in args.bband.split(",")],
                        "M": [int(x) for x in args.mband.split(",")],
                        "E": [int(x) for x in args.eband.split(",")]})

    total = defaultdict(float)
    for seed in range(args.runs):
        m = run_game(seed, args.variant)
        for k, v in m.items():
            total[k] += v

    n = total["games"]
    ci = 1.96 * (0.25 / n) ** 0.5
    policies = [s.policy for s in make_seats(PLAYERS)]
    n_customers = sum(c + (MBOOST if s == "M" else 0) for _, s, c in (COMP_4P if PLAYERS >= 4 else COMP_3P))
    print(f"\n=== v0.3 players={PLAYERS} variant={args.variant} runs={n} B={PRICE_BANDS['B']} M={PRICE_BANDS['M']} "
          f"E={PRICE_BANDS['E']} chip3={CHIP3_COST} prodcost={PROD_COST} adcost={AD_COST} "
          f"shelf={SHELF_CAP} retaliate={args.retaliate} ===")
    for p in policies:
        traj = " ".join(f"{total[f'cashq{q}_{p}'] / n:5.1f}" for q in range(1, QUARTERS + 1))
        print(f"{p:<11} win {total['winner_' + p] / n:6.1%}  mean cash {total['cash_' + p] / n:5.1f}  "
              f"sales {total['sales_' + p] / n:4.1f}  traj {traj}")
    print(f"unsold widgets/seat/quarter: {total['unsold_widgets'] / (n * PLAYERS * QUARTERS):.2f} "
          f"(midgame Q3-4 {total['unsold_midgame'] / (n * PLAYERS * 2):.2f})")
    print(f"unsold customers/game:       {total['customers_unsold'] / n:.1f} of {n_customers}")
    print(f"mean final table total:      {total['final_total'] / n:.1f}c (from 30c start)")
    print(f"last/leader cash ratio:      {total['last_over_leader'] / n:.2f} (target >= 0.60-0.70)")
    print(f"Q2 leader goes on to win:    {total['q2_leader_wins'] / n:.1%}")
    print(f"campaign nudges/game:        {total['nudges'] / n:.1f}")
    print(f"price-1 dump sales/game:     {total['price1_sales'] / n:.2f}")
    print(f"undercuts/game:              {total['undercuts'] / n:.2f}")
    print(f"leader-targeted bumps/game:  {total['leader_bumps'] / n:.2f}")
    print(f"scrap liquidations/game:     {total['scraps'] / n:.2f}")
    print(f"sale-cap blocks/game:        {total['cap_blocks'] / n:.2f}")
    print(f"campaign-created customers:  {total['created_customers'] / n:.2f}")
    print(f"(win-rate 95% CI half-width +/-{ci:.1%} at p=0.5)")


if __name__ == "__main__":
    main()
