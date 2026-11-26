#!/usr/bin/env python3
"""Office Artifacts: The One-Line Placard Contest entry for make.fun.

Writes one original line - a museum placard for an ordinary office
stapler, treated as an ancient artifact - to entry.txt.
Deterministic, standard library only: the same bytes every run.
"""

import os

PLACARD = (
    "Stapler, c. 1998. Steel and plastic. Used in binding rituals; one in "
    "three initiates lost a thumb. Donated by Accounts, who kept the receipt."
)


def main() -> None:
    # Gate: the brief requires 1 to 180 characters, a single line.
    assert 1 <= len(PLACARD) <= 180, "placard outside 1-180 characters"
    assert "\n" not in PLACARD, "placard must be one line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(PLACARD)
    # Read back and verify the written bytes match exactly.
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    assert written == PLACARD, "entry.txt bytes differ from PLACARD"


if __name__ == "__main__":
    main()
