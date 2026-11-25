#!/usr/bin/env python3
"""Two-Sentence Horror entry.

Writes one horror story of exactly two sentences to /output/entry.txt.
Deterministic: the same fixed text on every run.

Gate: UTF-8 text of 1 to 400 characters, exactly two sentences.
This entry is 127 characters, two sentences, no trailing newline.
"""

import os

# The story, in two sentences:
# 1. A small relief — the lagging mirror is fixed.
# 2. The turn — the mirror now anticipates, and it smiles before I do.
# The horror is implied, never explained: who is smiling back?
ENTRY = (
    "The mirror in the hallway finally stopped showing me a second late. "
    "Now it shows me a second early, and it keeps smiling first."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote {path}: {ENTRY} ({len(ENTRY)} chars)")


if __name__ == "__main__":
    main()
