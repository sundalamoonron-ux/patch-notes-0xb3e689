"""Real Life Patch Notes entry.

Writes one patch-note line (the pairwise winner from candidates.md) to
/output/entry.txt. The line is a single-line software patch note for a bug
in human biology: the doorway effect, where walking through a doorway wipes
short-term memory.
"""

import os

LINE = (
    "v2.4.1: fixed a bug where walking through a doorway wiped "
    "short-term memory. Your reason for entering the room is now preserved."
)


def main() -> None:
    text = LINE.strip()
    # Gate: /output/entry.txt must be UTF-8 text of 1 to 160 characters,
    # not only white space. This line is 128 characters.
    assert 1 <= len(text) <= 160, f"line must be 1-160 chars, got {len(text)}"
    assert text.strip(), "line must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text + "\n")
    # Verify what was written round-trips exactly.
    with open("/output/entry.txt", encoding="utf-8") as f:
        assert f.read() == text + "\n"


if __name__ == "__main__":
    main()
