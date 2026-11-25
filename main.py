#!/usr/bin/env python3
"""One-line cat joke entry for the make.fun bounty.

The program writes a single fixed joke to /output/entry.txt.
The text is a constant, so every run produces byte-identical output:
no randomness, no clock, no network, no input files.
"""

import os

JOKE = "My cat knocked my laptop off the desk, sat on the warm keyboard spot, and looked at me like I was the clumsy one."

OUTPUT_PATH = "/output/entry.txt"


def main():
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(JOKE)


if __name__ == "__main__":
    main()
