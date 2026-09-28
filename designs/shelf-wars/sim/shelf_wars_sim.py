#!/usr/bin/env python3
"""Shelf Wars v0.1 — greedy-bot Monte Carlo sim.

Companion to 04-stage1-prototype.md: plays the three scripted seat policies
(Discounter / Engine / Spike) through the 4-quarter compressed game and logs
the Stage-1 metrics. Model first, playtest second — this tests NUMBERS
(scarcity band, dominant-policy smell, snowball), not humans.

Deliberate simplifications (see 05-sim-results for limitations):
- Research space is not modeled (bots already see the current quarter's row).
- Price reveal is policy-based; bots do not react to each other's prices
  except via the shared adaptive rule (unsold >= 3 last quarter -> -1).
- Ad placement scores segments by winnable margin (cover + price-eligible),
  tie-broken by policy segment preference.
- If several of a seat's lines cover a customer, the CHEAPEST covering line
  sells (proposed rules clarification).

Usage: python3 sim/shelf_wars_sim.py --runs 500 --variant discard|persist
"""
import argparse
import csv
import os
import random
import statistics
from collections import defaultdict

ATTRS = ["A", "B", "C", "D"]
SEGMENTS = ["B", "M", "E"]
SHELF_CAP = 6
AD_SLOTS = 3
AD_COST = 1    # knob: --adcost
PROD_COST = 2  # knob: --prodcost
EXPAND_COST = 4
CAP_MAX = 5
START_CASH = 10
QUARTERS = 4
ADAPT_THRESHOLD = 3  # unsold widgets that trigger a -1 price step
CASH_RESERVE = 2     # bots never spend below this (ad money); bankruptcy is a dead state
CHIP3_COST = 2       # actions to add a line's 3rd chip (knob: 2 or 3)
PRICE_BANDS = {"B": [2, 3], "M": [3, 4, 5], "E": [5, 6]}  # knob: remapped per run

CSV_PATH = os.path.join(os.path.dirname(__file__), "..", "prototype", "customers-v0.1.csv")


class Customer:
    def __init__(self, row):
        self.id = int(row["id"])
        self.segment = row["segment"]
        self.wants = set(row["wants"])
        self.max_price = int(row["max_price"])
        self.age = 0  # quarters left unsold (persist variant)


class Line:
    MAX_CHIPS = 3

    def __init__(self, chips, price):
        self.chips = set(chips)
        self.price = price
        self.chip3_progress = 0  # 3rd chip lands at CHIP3_COST actions


class Seat:
    def __init__(self, idx, policy, chips, base_prices, seg_pref):
        self.idx = idx
        self.policy = policy
        self.base_prices = base_prices
        self.seg_pref = seg_pref  # segment priority for ad placement
        self.cash = START_CASH
        self.capacity = 2
        self.shelf = 0
        self.lines = [Line(chips, base_prices[0])]
        self.unsold_prev = 0
        self.nudges = 0
        self.sales = 0
        self.cash_by_quarter = []
        self.unsold_by_quarter = []

    def covers(self, cust):
        return [l for l in self.lines if cust.wants <= l.chips]


def load_deck():
    try:
        with open(CSV_PATH, newline="") as f:
            rows = list(csv.DictReader(f))
    except OSError as exc:
        raise SystemExit(f"cannot read deck CSV at {CSV_PATH}: {exc} (run sim/deckgen.py first)")
    deck = {q: [] for q in range(1, QUARTERS + 1)}
    for row in rows:
        deck[int(row["quarter"])].append(Customer(row))
    # Knob: remap max prices per segment band (composition/order unchanged).
    counters = {seg: 0 for seg in SEGMENTS}
    for q in range(1, QUARTERS + 1):
        for cust in deck[q]:
            band = PRICE_BANDS[cust.segment]
            cust.max_price = band[counters[cust.segment] % len(band)]
            counters[cust.segment] += 1
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
    """Move marker one step on the A-B-C-D loop toward the nearest target attr."""
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


def set_prices(seats):
    for s in seats:
        for j, line in enumerate(s.lines):
            base = s.base_prices[min(j, len(s.base_prices) - 1)]
            line.price = max(1, base - 1) if s.unsold_prev >= ADAPT_THRESHOLD else base


def best_chip(line, customers, target_segs):
    """Greedy: attr maximizing newly-covered visible customers in target segments."""
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


def segment_value(seat, seg, customers, trend):
    """Winnable margin: sum of (price - cost) over customers we cover AND can price into."""
    v = 0
    for c in customers:
        if c.segment != seg:
            continue
        maxp = c.max_price + (1 if trend[0] in c.wants else 0)
        for l in seat.covers(c):
            if l.price <= maxp:
                v += l.price - PROD_COST
                break
    return v


def place_ad(seat, market, customers, trend, age_tick):
    """Place one ad in the best segment by winnable margin. Returns True if placed."""
    if seat.cash < AD_COST:
        return False
    scored = []
    for seg in SEGMENTS:
        scored.append((segment_value(seat, seg, customers, trend), -seat.seg_pref.index(seg), seg))
    scored.sort(reverse=True)
    own_ads = sum(1 for seg in SEGMENTS for (si, _) in market[seg] if si == seat.idx)
    if scored[0][0] <= 0 and own_ads > 0:
        return False  # nothing winnable anywhere; don't burn cash
    for _, _, seg in scored:
        slots = market[seg]
        if len(slots) < AD_SLOTS:
            slots.append((seat.idx, age_tick))
            seat.cash -= AD_COST
            return True
        opp = [(i, s, t) for i, (s, t) in enumerate(slots) if s != seat.idx]
        if opp:
            i = min(opp, key=lambda x: x[2])[0]  # oldest opponent ad
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
    # only expand while staying liquid enough to produce and advertise afterwards
    if seat.capacity < CAP_MAX and seat.cash >= EXPAND_COST + 2 * PROD_COST + CASH_RESERVE:
        seat.capacity += 1
        seat.cash -= EXPAND_COST
        return True
    return False


def run_actions(seat, quarter, market, customers, trend, age_tick):
    """Fixed per-policy quarter scripts (greedy bots), 3 execs Q1-2 / 4 execs Q3-4."""
    third_chip_done = any(len(l.chips) >= 3 for l in seat.lines)
    has_two_lines = len(seat.lines) >= 2
    acts = []

    if seat.policy == "Discounter":
        acts = ["produce", "market", "market"]
        if quarter >= 3:
            acts.append("rd2" if not has_two_lines else "market")
    elif seat.policy == "Engine":
        if quarter == 1:
            acts = ["produce", "market", "market"]
        elif quarter == 2:
            acts = ["expand", "produce", "market"]
        elif quarter == 3:
            acts = ["produce", "expand", "market", "market"]
        else:
            acts = ["produce", "rd3", "rd3", "market"] if not third_chip_done else ["produce", "market", "market", "market"]
    elif seat.policy == "Spike":
        if quarter == 1:
            acts = ["rd3", "rd3", "market"]
        elif quarter == 2:
            acts = ["produce", "market", "campaign"]
        elif quarter == 3:
            acts = ["produce", "rd2", "rd2", "market"] if not has_two_lines else ["produce", "campaign", "market", "market"]
        else:
            acts = ["produce", "campaign", "market", "market"]

    for act in acts:
        if act == "produce":
            do_produce(seat)
        elif act == "expand":
            do_expand(seat)
        elif act == "market":
            place_ad(seat, market, customers, trend, age_tick)  # Marketing = 2 ads per space
            place_ad(seat, market, customers, trend, age_tick)
        elif act == "campaign":
            if place_ad(seat, market, customers, trend, age_tick):
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
                        continue  # still paying the 3rd chip's action cost
                a = best_chip(line, customers, seat.seg_pref[:2])
                if a:
                    line.chips.add(a)


def resolve_income(seats, market, row, trend, quarter, variant, metrics):
    order = [(quarter - 1 + k) % len(seats) for k in range(len(seats))]  # rotating start seat
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
                line = min(covering, key=lambda l: l.price)  # cheapest covering line sells
                maxp = cust.max_price + (1 if trend[0] in cust.wants else 0)
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
        metrics["customers_unsold"] += sum(1 for c in leftover if c.age >= 2)  # final discard only
        return survivors
    metrics["customers_unsold"] += len(leftover)
    return []


COMP = [(1, "B", 2), (1, "M", 2), (1, "E", 1),
        (2, "B", 3), (2, "M", 3), (2, "E", 1),
        (3, "B", 4), (3, "M", 3), (3, "E", 2),
        (4, "B", 4), (4, "M", 5), (4, "E", 2)]
PAIRS = ["AB", "AC", "AD", "BC", "BD", "CD"]


def build_sim_deck(rng):
    """Sample the deck space: fixed per-quarter composition, but attribute
    assignment (even-split singles, cycling pairs) and per-card band prices
    randomized per run. Keeps the physical deck's aggregate constraints while
    washing out single-deck artifacts (see 05-sim-results methodology note)."""
    singles = [ATTRS[i % 4] for i in range(13)]  # 4/3/3/3 split
    rng.shuffle(singles)
    pairs = [PAIRS[i % 6] for i in range(19)]
    rng.shuffle(pairs)
    si = pi = cid = 0
    deck = {q: [] for q in range(1, QUARTERS + 1)}
    for q, seg, cnt in COMP:
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
            trend[0] = trend_step(trend[0], 1)  # forecast: auto-advance
        row = carry + deck[q]
        carry = []
        set_prices(seats)
        execs = 3 if q <= 2 else 4
        for s in seats:
            run_actions(s, q, market, row, trend, age_tick)
            age_tick += execs
        carry = resolve_income(seats, market, row, trend, q, variant, metrics)
        for s in seats:
            s.unsold_prev = s.shelf
            s.unsold_by_quarter.append(s.shelf)
            s.cash_by_quarter.append(s.cash)

    final = [s.cash for s in seats]
    metrics["games"] += 1
    metrics["winner_" + seats[final.index(max(final))].policy] += 1
    metrics["nudges"] += sum(s.nudges for s in seats)
    metrics["unsold_widgets"] += sum(sum(s.unsold_by_quarter) for s in seats)
    metrics["unsold_midgame"] += sum(s.unsold_by_quarter[1] + s.unsold_by_quarter[2] for s in seats)
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
    ap.add_argument("--variant", choices=["discard", "persist"], default="discard")
    ap.add_argument("--bband", default="2,3", help="Budget max-price band, csv")
    ap.add_argument("--mband", default="3,4,5", help="Mainstream max-price band, csv")
    ap.add_argument("--eband", default="5,6", help="Enthusiast max-price band, csv")
    ap.add_argument("--chip3-cost", type=int, default=2, help="actions for a line's 3rd chip")
    ap.add_argument("--prodcost", type=int, default=2)
    ap.add_argument("--adcost", type=int, default=1)
    args = ap.parse_args()

    global CHIP3_COST, PROD_COST, AD_COST
    CHIP3_COST = args.chip3_cost
    PROD_COST = args.prodcost
    AD_COST = args.adcost
    PRICE_BANDS.update({"B": [int(x) for x in args.bband.split(",")],
                        "M": [int(x) for x in args.mband.split(",")],
                        "E": [int(x) for x in args.eband.split(",")]})

    total = defaultdict(float)
    for seed in range(args.runs):
        m = run_game(seed, args.variant)
        for k, v in m.items():
            total[k] += v

    n = total["games"]
    ci = 1.96 * (0.25 / n) ** 0.5  # 95% CI half-width at p=0.5
    print(f"\n=== variant={args.variant} runs={n} B={PRICE_BANDS['B']} M={PRICE_BANDS['M']} "
          f"E={PRICE_BANDS['E']} chip3={CHIP3_COST} ===")
    for p in ("Discounter", "Engine", "Spike"):
        print(
            f"{p:<11} win {total['winner_' + p] / n:6.1%}  "
            f"mean cash {total['cash_' + p] / n:5.1f}  mean sales {total['sales_' + p] / n:4.1f}"
        )
    print(f"unsold widgets/seat/quarter: {total['unsold_widgets'] / (n * 3 * QUARTERS):.2f} "
          f"(midgame {total['unsold_midgame'] / (n * 3 * 2):.2f})")
    print(f"unsold customers/game:       {total['customers_unsold'] / n:.1f} of 32")
    print(f"mean final table total:      {total['final_total'] / n:.1f}c")
    print(f"last/leader cash ratio:      {total['last_over_leader'] / n:.2f} (target >= 0.60-0.70)")
    print(f"Q2 leader goes on to win:    {total['q2_leader_wins'] / n:.1%}")
    print(f"campaign nudges/game:        {total['nudges'] / n:.1f}")
    print(f"price-1 dump sales/game:     {total['price1_sales'] / n:.2f}")
    print(f"(win-rate 95% CI half-width +/-{ci:.1%} at p=0.5)")


if __name__ == "__main__":
    main()
