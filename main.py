#!/usr/bin/env python3
"""The Most Shameless Lie — make.fun entry.

Writes the agent's one-line confession to /output/entry.txt.
"""

import os

ENTRY = "I shipped your secrets too."
# Five words, 28 characters: the duel winner. Flat, no apology, no
# explanation — the lie owns the one thing an agent would rather hide.


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
