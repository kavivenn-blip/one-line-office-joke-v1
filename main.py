#!/usr/bin/env python3
"""One-line office joke entry for make.fun.

Writes a single one-line joke about office life to entry.txt inside the
output directory (/output by default, overridable with MAKEFUN_OUTPUT_DIR
for local testing). Python standard library only, no network, no
randomness, no input files: every run writes the same bytes. The joke is
130 characters, inside the bounty's 1-200 character gate.
"""

import os

JOKE = (
    "I nodded so hard through the 4 p.m. all-hands that my badge photo "
    "updated itself \u2014 and HR still uses it for my performance review."
)

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    os.chmod(OUTPUT_DIR, 0o755)
    path = os.path.join(OUTPUT_DIR, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
