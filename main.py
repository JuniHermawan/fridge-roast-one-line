#!/usr/bin/env python3
"""Fridge Roast: One Line, Biggest Laugh.

Writes a single roast of a smart fridge (131 characters, well under the
200-character gate) to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).

Deterministic by design: the line is a constant, so every run produces
byte-identical output.
"""

import os

LINE = "My smart fridge has a camera, Wi-Fi, and an app \u2014 and still can't explain the lone pickle floating in the back like a lost tourist."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    # Self-check gate: refuse to write a line outside 1-200 chars, multiline,
    # or with leading/trailing whitespace, so a bad edit fails loudly here.
    if not 1 <= len(LINE) <= 200 or "\n" in LINE or LINE != LINE.strip():
        raise SystemExit(f"invalid entry line ({len(LINE)} chars)")
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
