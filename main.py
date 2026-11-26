#!/usr/bin/env python3
"""One Line, Big Laugh — entry program.

Writes a single original funny line (<= 200 characters) to /output/entry.txt.
Deterministic, stdlib-only, no network, no randomness.
"""

import os
import sys

LINE = (
    "I told my therapist I'm afraid of commitment, "
    "so she started charging me weekly \u2014 "
    "now I'm in the longest relationship of my life."
)
# 129 characters: setup promises a therapy joke, the punchline reframes
# the therapist herself as the commitment. No setup beyond the line itself.


def main() -> int:
    text = LINE.strip()
    if not (1 <= len(text) <= 200):
        print(f"entry length {len(text)} out of range", file=sys.stderr)
        return 1
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(text + "\n")
    print(f"wrote {len(text)} chars to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
