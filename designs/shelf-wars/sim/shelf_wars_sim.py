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
import os
import random
from collections import defaultdict

ATTRS = ["A", "B", "C", "D"]
SEGMENTS = ["B", "M", "E"]
SHELF_CAP = 6
AD_SLOTS = 3
AD_COST = 1       # knob: --adcost (v0.1 finding: 0 unleashes the coverage leader)
PROD_COST = 2     # knob: --prodcost (v0.1 finding: 1 helps the premium leader)
EXPAND_COST = 4
CAP_MAX = 5
START_CASH = 10
QUARTERS = 6      # full game (v0.2)
ADAPT_THRESHOLD = 3
CASH_RESERVE = 2
CHIP3_COST = 3    # v0.2: 3rd chip costs 3 actions (dominant strategy at 2)
RETALIATE = True  # knob: --retaliate 0
SCRAP = False     # knob: --scrap 1 (broke seats liquidate widgets for 1c each)
TREND_PREMIUM = 1  # knob: --trend-premium (price ceiling bonus on hot-attribute wants)
MBOOST = 0         # knob: --mboost N (extra Mainstream customers per quarter — demand faucet)
PRICE_BANDS = {"B": [2, 3], "M": [3, 4, 5], "E": [5, 6]}

# Full 6-quarter demand curve (3p): 5/7/9/11/12/13 = 57 customers.
COMP = [(1, "B", 2), (1, "M", 2), (1, "E", 1),
        (2, "B", 3), (2, "M", 3), (2, "E", 1),
        (3, "B", 4), (3, "M", 3), (3, "E", 2),
        (4, "B", 4), (4, "M", 5), (4, "E", 2),
        (5, "B", 5), (5, "M", 5), (5, "E", 2),
        (6, "B", 5), (6, "M", 5), (6, "E", 3)]
PAIRS = ["AB", "AC", "AD", "BC", "BD", "CD"]


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
    n_singles = sum(c for _, s, c in COMP if s == "B")
    n_pairs = sum(c + (MBOOST if s == "M" else 0) for _, s, c in COMP if s != "B")
    singles = [ATTRS[i % 4] for i in range(n_singles)]
    rng.shuffle(singles)
    pairs = [PAIRS[i % 6] for i in range(n_pairs)]
    rng.shuffle(pairs)
    si = pi = cid = 0
    deck = {q: [] for q in range(1, QUARTERS + 1)}
    for q, seg, cnt in COMP:
        if seg == "M":
            cnt += MBOOST
        for _ in range(cnt):
            cid += 1
            if seg == "B":
                wants = {singles[si]}; si += 1
            else:
                wants = set(pairs[pi]); pi += 1
            band = PRICE_BANDS[seg]
            cust = Customer({"id": cid, "segment": seg, "wants": "".join(sorted(wants)),
                             "max_price": band[rng.randrange(len(band))]})
            deck[q].append(cust)
    for q in deck:
        rng.shuffle(deck[q])
    return deck


def make_seats():
    return [
        Seat(0, "Discounter", "AB", [2, 3], ["B", "M", "E"]),
        Seat(1, "Engine", "BC", [4, 4], ["M", "B", "E"]),
        Seat(2, "Spike", "CD", [5, 4], ["E", "M", "B"]),
    ]


def trend_step(marker, direction):
    i = ATTRS.index(marker)
    return ATTRS[(i + direction) % len(ATTRS)]


def nudge_toward(marker, targets):
    if marker in targets:
        return marker
    i = ATTRS.index(marker)
    best, best_d = None, 99
    for t in targets:
        d = (ATTRS.index(t) - i) % len(ATTRS)
        d = min(d, len(ATTRS) - d)
        if d < best_d:
            best, best_d = t, d
    if best is None:
        return marker
    fwd = (ATTRS.index(best) - i) % len(ATTRS)
    return trend_step(marker, 1 if fwd <= len(ATTRS) // 2 else -1)


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
    for seg in SEGMENTS:
        scored.append((segment_value(seat, seg, customers, trend), -seat.seg_pref.index(seg), seg))
    scored.sort(reverse=True)
    own_ads = sum(1 for seg in SEGMENTS for (si, _) in market[seg] if si == seat.idx)
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
    for a in ATTRS:
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


def run_actions(seat, quarter, market, customers, trend, age_tick, seats, metrics):
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
        elif quarter == 4:
            acts = ["produce", "rd3", "rd3", "market"] if not third_chip_done else ["produce", "market", "market", "market"]
        elif quarter == 5:
            acts = ["produce", "rd3", "market", "market"] if not third_chip_done else ["produce", "market", "market", "market"]
        else:
            acts = ["produce", "market", "market", "market"]
    elif seat.policy == "Spike":
        if quarter == 1:
            acts = ["rd3", "rd3", "rd3"]  # 3-action 3rd chip: all-in on Q1 R&D
        elif quarter == 2:
            acts = ["produce", "market", "campaign"]
        elif quarter == 3:
            acts = ["produce", "rd2", "rd2", "market"] if not has_two_lines else ["produce", "campaign", "market", "market"]
        else:
            acts = ["produce", "campaign", "market", "market"]

    if SCRAP and seat.cash < CASH_RESERVE and seat.shelf > 0:
        n = min(seat.shelf, 2)
        seat.shelf -= n
        seat.cash += n  # liquidate at 1c/widget to escape the bankruptcy dead-state
        metrics["scraps"] += n

    for act in acts:
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
        elif act in ("rd2", "rd3"):
            line = seat.lines[0] if act == "rd3" else (seat.lines[1] if has_two_lines else None)
            if act == "rd2" and line is None:
                a = best_chip(Line(set(), 0), customers, seat.seg_pref[:2])
                seat.lines.append(Line(a, seat.base_prices[1]))
            elif line is not None and len(line.chips) < Line.MAX_CHIPS:
                if act == "rd3":
                    line.chip3_progress += 1
                    if line.chip3_progress < CHIP3_COST:
                        continue
                a = best_chip(line, customers, seat.seg_pref[:2])
                if a:
                    line.chips.add(a)


def resolve_income(seats, market, row, trend, quarter, variant, metrics):
    order = [(quarter - 1 + k) % len(seats) for k in range(len(seats))]
    sold_ids = set()
    for seg in SEGMENTS:
        for cust in [c for c in row if c.segment == seg]:
            cands = []
            for s in seats:
                if s.shelf < 1:
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
    seats = make_seats()
    market = {seg: [] for seg in SEGMENTS}
    trend = ["A"]
    carry = []
    metrics = defaultdict(float)
    age_tick = 0

    for q in range(1, QUARTERS + 1):
        if q > 1:
            trend[0] = trend_step(trend[0], 1)
        row = carry + deck[q]
        carry = []
        set_prices(seats, q, metrics)
        execs = 3 if q <= 2 else 4
        for s in seats:
            run_actions(s, q, market, row, trend, age_tick, seats, metrics)
            age_tick += execs
        carry = resolve_income(seats, market, row, trend, q, variant, metrics)
        for s in seats:
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
    metrics["last_over_leader"] += min(final) / max(final)
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
    ap.add_argument("--eband", default="5,6")
    ap.add_argument("--chip3-cost", type=int, default=3)
    ap.add_argument("--prodcost", type=int, default=2)
    ap.add_argument("--adcost", type=int, default=1)
    ap.add_argument("--retaliate", type=int, default=1, help="1=undercut + leader-bump (default), 0=off")
    ap.add_argument("--scrap", type=int, default=0, help="1=broke seats liquidate widgets for 1c each")
    ap.add_argument("--trend-premium", type=int, default=1)
    ap.add_argument("--mboost", type=int, default=0, help="extra Mainstream customers per quarter")
    args = ap.parse_args()

    global CHIP3_COST, PROD_COST, AD_COST, RETALIATE, SCRAP, TREND_PREMIUM, MBOOST
    CHIP3_COST = args.chip3_cost
    PROD_COST = args.prodcost
    AD_COST = args.adcost
    RETALIATE = bool(args.retaliate)
    SCRAP = bool(args.scrap)
    TREND_PREMIUM = args.trend_premium
    MBOOST = args.mboost
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
    print(f"\n=== v0.2 variant={args.variant} runs={n} B={PRICE_BANDS['B']} M={PRICE_BANDS['M']} "
          f"E={PRICE_BANDS['E']} chip3={CHIP3_COST} prodcost={PROD_COST} adcost={AD_COST} "
          f"retaliate={args.retaliate} ===")
    for p in ("Discounter", "Engine", "Spike"):
        traj = " ".join(f"{total[f'cashq{q}_{p}'] / n:5.1f}" for q in range(1, QUARTERS + 1))
        print(f"{p:<11} win {total['winner_' + p] / n:6.1%}  mean cash {total['cash_' + p] / n:5.1f}  "
              f"sales {total['sales_' + p] / n:4.1f}  traj {traj}")
    print(f"unsold widgets/seat/quarter: {total['unsold_widgets'] / (n * 3 * QUARTERS):.2f} "
          f"(midgame Q3-4 {total['unsold_midgame'] / (n * 3 * 2):.2f})")
    print(f"unsold customers/game:       {total['customers_unsold'] / n:.1f} of 57")
    print(f"mean final table total:      {total['final_total'] / n:.1f}c (from 30c start)")
    print(f"last/leader cash ratio:      {total['last_over_leader'] / n:.2f} (target >= 0.60-0.70)")
    print(f"Q2 leader goes on to win:    {total['q2_leader_wins'] / n:.1%}")
    print(f"campaign nudges/game:        {total['nudges'] / n:.1f}")
    print(f"price-1 dump sales/game:     {total['price1_sales'] / n:.2f}")
    print(f"undercuts/game:              {total['undercuts'] / n:.2f}")
    print(f"leader-targeted bumps/game:  {total['leader_bumps'] / n:.2f}")
    print(f"scrap liquidations/game:     {total['scraps'] / n:.2f}")
    print(f"(win-rate 95% CI half-width +/-{ci:.1%} at p=0.5)")


if __name__ == "__main__":
    main()
