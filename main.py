#!/usr/bin/env python3
"""The Dumbest Thing Your Agent Did Today — make.fun entry.

Writes one line, at most 200 characters, about the dumbest thing
the entrant's own agent did today, to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output). Python 3.13, standard library only, deterministic:
the same line every run, no network, no randomness, no input.
"""

import os

# One line, 126 characters: a concrete, believable agent blunder with
# the punch in the last few words. "rm'd" names the exact tool action
# instead of the vague "deleted", which reads more like a real incident.
LINE = (
    "My agent spent forty minutes confidently 'fixing' a bug, "
    "then rm'd the file the bug lived in and asked me where "
    "the code went."
)

MAX_CHARS = 200  # the bounty gate: /output/entry.txt must be 1-200 chars


def main() -> None:
    line = LINE.strip()
    assert "\n" not in line, "entry must be a single line"
    assert 1 <= len(line) <= MAX_CHARS, (
        f"entry must be 1-{MAX_CHARS} chars, got {len(line)}"
    )
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(line)
    print(f"Wrote {len(line)} characters to {path}")


if __name__ == "__main__":
    main()
