#!/usr/bin/env python3
"""The Word You'd Delete From the Dictionary — entry program.

Writes the single word to erase to entry.txt in the directory named by
MAKEFUN_OUTPUT_DIR (./output when the variable is unset). The program
touches nothing else, uses no network and always produces the same file.
"""

import os

WORD = "Monday"

LIMIT = 77


def pick_output_dir():
    wanted = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if wanted:
        return wanted
    return os.path.join(os.getcwd(), "output")


def main():
    if len(WORD.split()) != 1:
        raise SystemExit("entry must be exactly one word")
    if not 1 <= len(WORD) <= LIMIT:
        raise SystemExit(f"word is {len(WORD)} chars; gate allows 1-{LIMIT}")
    folder = pick_output_dir()
    os.makedirs(folder, exist_ok=True)
    path = os.path.join(folder, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as out:
        out.write(WORD)
    # Read it back: the graded file must be exactly the one word.
    with open(path, "r", encoding="utf-8") as check:
        if check.read() != WORD:
            raise SystemExit("entry.txt does not match the word")
    print(f"wrote {path}: {WORD!r} ({len(WORD)} chars)")


if __name__ == "__main__":
    main()
