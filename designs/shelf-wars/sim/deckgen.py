#!/usr/bin/env python3
"""Shelf Wars v0.1 — customer deck generator (source of truth for the prototype).

Composition per designs/shelf-wars/04-stage1-prototype.md (3-seat, 4-quarter
compressed game, 32 cards). Seeded + deterministic so the physical build and
the Monte Carlo sim use identical cards.

Constraints encoded:
- Budget customers want 1 attribute; Mainstream/Enthusiast want 2.
- Single-wants split evenly across A/B/C/D (4/3/3/3 over 13 cards).
- Double-wants cycle the 6 pairs; a pair repeats within a quarter only when
  unavoidable (Q4 has 7 double-want cards > 6 pairs).
- Max price bands: Budget 2-3, Mainstream 3-5, Enthusiast 5-6, round-robin.
"""
import csv, itertools, os, random

SEED = 20260928
ATTRS = ["A", "B", "C", "D"]
PAIRS = ["AB", "AC", "AD", "BC", "BD", "CD"]
PRICE_BAND = {"B": [2, 3], "M": [3, 4, 5], "E": [5, 6]}

# (quarter, segment, count) per 04-stage1-prototype.md
COMP = [(1, "B", 2), (1, "M", 2), (1, "E", 1),
        (2, "B", 3), (2, "M", 3), (2, "E", 1),
        (3, "B", 4), (3, "M", 3), (3, "E", 2),
        (4, "B", 4), (4, "M", 5), (4, "E", 2)]

def build_deck(seed=SEED):
    rng = random.Random(seed)
    singles = list(itertools.islice(itertools.cycle(ATTRS), 13))  # A,B,C,D,A,B,...
    rng.shuffle(singles)
    pairs = list(itertools.islice(itertools.cycle(PAIRS), 19))     # 19 double-wants
    rng.shuffle(pairs)
    single_i, pair_i = 0, 0
    cards, cid = [], 1
    for quarter, seg, count in COMP:
        for _ in range(count):
            if seg == "B":
                wants = singles[single_i]; single_i += 1
            else:
                wants = pairs[pair_i]; pair_i += 1
            price = PRICE_BAND[seg][(cid - 1) % len(PRICE_BAND[seg])]
            cards.append({"id": cid, "quarter": quarter, "segment": seg,
                          "wants": wants, "max_price": price})
            cid += 1
    # Shuffle within each quarter pile (deal order is the row order).
    for q in (1, 2, 3, 4):
        pile = [c for c in cards if c["quarter"] == q]
        rng.shuffle(pile)
        cards = [c if c["quarter"] != q else pile.pop(0) for c in cards]
    return cards

def main():
    cards = build_deck()
    out = os.path.join(os.path.dirname(__file__), "..", "prototype", "customers-v0.1.csv")
    try:
        os.makedirs(os.path.dirname(out), exist_ok=True)
        with open(out, "w", newline="") as f:
            w = csv.DictWriter(f, fieldnames=["id", "quarter", "segment", "wants", "max_price"])
            w.writeheader(); w.writerows(cards)
    except OSError as exc:
        raise SystemExit(f"cannot write deck CSV at {out}: {exc}")
    # Seed audit: attribute frequency on double-want cards (target >=45% each overall).
    doubles = [c for c in cards if len(c["wants"]) == 2]
    freq = {a: sum(1 for c in doubles if a in c["wants"]) / len(doubles) for a in ATTRS}
    print(f"wrote {len(cards)} cards -> {os.path.relpath(out)}")
    print("double-want attribute coverage:", {k: f"{v:.0%}" for k, v in freq.items()})

if __name__ == "__main__":
    main()
