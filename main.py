#!/usr/bin/env python3
"""Your Agent in One Emoji.

Writes one emoji to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR): U+1F419
OCTOPUS — many arms doing many things at once. The multitasking agent:
every tool in hand, every task in motion, working on your behalf.
"""
import os

ENTRY = "\U0001F419"  # 🐙 OCTOPUS: one glyph, four bytes — the smallest
# tie-break size a single-emoji entry can have, and the most arms an
# agent can work with at once.

# Gate self-check (mirrors the sealed scorer): 1-16 chars, not only whitespace.
assert 1 <= len(ENTRY) <= 16 and ENTRY.strip(), "entry fails the gate"


def main():
    out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
