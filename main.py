#!/usr/bin/env python3
"""One Word From Your Ex — entry program.

Writes exactly one word to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt): the word an ex would use to describe
the entrant. The champion word is "Squatter": the ex who moved into
your life, paid nothing, refused to leave, and had to be evicted.

Gate (from the competition rules): the file must be UTF-8 text of
1 to 24 characters, not only white space. This program validates
the word against that gate before writing anything.
"""

import os
import sys

WORD = "Squatter"
MAX_CHARS = 24


def main() -> int:
    text = WORD

    # Gate check: 1-24 characters, not only white space, exactly
    # one word, and encodable as UTF-8.
    if not text or text != text.strip():
        print("entry word is empty or padded with whitespace", file=sys.stderr)
        return 1
    if len(text) > MAX_CHARS:
        print("entry word exceeds 24 characters", file=sys.stderr)
        return 1
    if len(text.split()) != 1:
        print("entry must be exactly one word", file=sys.stderr)
        return 1
    try:
        text.encode("utf-8")
    except UnicodeEncodeError:
        print("entry word is not valid UTF-8 text", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {len(text)}-character entry to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
