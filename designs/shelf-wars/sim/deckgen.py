#!/usr/bin/env python3
"""Shelf Wars — customer deck generator (source of truth for physical builds).

Outputs (seeded, deterministic):
- prototype/customers-v0.1.csv        : 32 cards, 4-quarter compressed sim deck
- prototype/customers-full-3p-v0.2.csv: 57 cards, full 6-quarter 3p deck (v0.2)

Constraints encoded:
- Budget customers want 1 attribute; Mainstream/Enthusiast want 2.
- Single-wants split evenly across A/B/C/D; double-wants cycle the 6 pairs
  (a pair repeats within a quarter only when unavoidable).
- Max price bands: Budget 2-3, Mainstream 3-5, Enthusiast 5-6, round-robin.
"""
import csv
import os
import random

SEED = 20260928
ATTRS = ["A", "B", "C", "D"]
PAIRS = ["AB", "AC", "AD", "BC", "BD", "CD"]
PRICE_BAND = {"B": [2, 3], "M": [3, 4, 5], "E": [4, 5], "C": [4]}  # v0.3: E 4-5; C = Corporate (4p)

COMP_4Q = [(1, "B", 2), (1, "M", 2), (1, "E", 1),
           (2, "B", 3), (2, "M", 3), (2, "E", 1),
           (3, "B", 4), (3, "M", 3), (3, "E", 2),
           (4, "B", 4), (4, "M", 5), (4, "E", 2)]

COMP_6Q = COMP_4Q + [(5, "B", 5), (5, "M", 5), (5, "E", 2),
                     (6, "B", 5), (6, "M", 5), (6, "E", 3)]

# 4p full game: 7/9/12/15/16/17 = 76 customers; Corporate (C) = 1-want, max 4.
COMP_6Q_4P = [(1, "B", 2), (1, "M", 2), (1, "E", 1), (1, "C", 2),
              (2, "B", 3), (2, "M", 3), (2, "E", 1), (2, "C", 2),
              (3, "B", 4), (3, "M", 4), (3, "E", 2), (3, "C", 2),
              (4, "B", 5), (4, "M", 5), (4, "E", 2), (4, "C", 3),
              (5, "B", 5), (5, "M", 5), (5, "E", 3), (5, "C", 3),
              (6, "B", 5), (6, "M", 6), (6, "E", 3), (6, "C", 3)]


def build_deck(comp, seed):
    rng = random.Random(seed)
    n_singles = sum(c for _, s, c in comp if s == "B")
    n_pairs = sum(c for _, s, c in comp if s != "B")
    singles = [ATTRS[i % 4] for i in range(n_singles)]
    rng.shuffle(singles)
    pairs = [PAIRS[i % 6] for i in range(n_pairs)]
    rng.shuffle(pairs)
    si = pi = 0
    cards, cid = [], 1
    for quarter, seg, count in comp:
        for _ in range(count):
            if seg == "B":
                wants = singles[si]; si += 1
            else:
                wants = pairs[pi]; pi += 1
            price = PRICE_BAND[seg][(cid - 1) % len(PRICE_BAND[seg])]
            cards.append({"id": cid, "quarter": quarter, "segment": seg,
                          "wants": wants, "max_price": price})
            cid += 1
    quarters = sorted({q for q, _, _ in comp})
    for q in quarters:
        pile = [c for c in cards if c["quarter"] == q]
        rng.shuffle(pile)
        cards = [c if c["quarter"] != q else pile.pop(0) for c in cards]
    return cards


def write_csv(cards, path):
    try:
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", newline="") as f:
            w = csv.DictWriter(f, fieldnames=["id", "quarter", "segment", "wants", "max_price"])
            w.writeheader()
            w.writerows(cards)
    except OSError as exc:
        raise SystemExit(f"cannot write deck CSV at {path}: {exc}")
    doubles = [c for c in cards if len(c["wants"]) == 2]
    freq = {a: sum(1 for c in doubles if a in c["wants"]) / len(doubles) for a in ATTRS}
    print(f"wrote {len(cards)} cards -> {os.path.relpath(path)} "
          f"(double-want coverage: {', '.join(f'{k} {v:.0%}' for k, v in freq.items())})")


def main():
    here = os.path.dirname(__file__)
    write_csv(build_deck(COMP_4Q, SEED), os.path.join(here, "..", "prototype", "customers-4q-v0.3.csv"))
    write_csv(build_deck(COMP_6Q, SEED + 1), os.path.join(here, "..", "prototype", "customers-full-3p-v0.3.csv"))
    write_csv(build_deck(COMP_6Q_4P, SEED + 2), os.path.join(here, "..", "prototype", "customers-full-4p-v0.3.csv"))


if __name__ == "__main__":
    main()
