"""Write one original 17-syllable debugging haiku (5-7-5) to entry.txt.

Self-checks the haiku before writing: three lines, 5-7-5 syllables,
1-200 characters, so a bad edit can never silently ship an invalid entry.
"""

import os

HAIKU = (
    "The breakpoint holds still\n"
    "a thousand log lines whisper\n"
    "one semicolon"
)

# Syllable count per word used in the haiku.
_SYLLABLES = {
    "the": 1,
    "breakpoint": 2,
    "holds": 1,
    "still": 1,
    "a": 1,
    "thousand": 2,
    "log": 1,
    "lines": 1,
    "whisper": 2,
    "one": 1,
    "semicolon": 4,
}

_SHAPE = (5, 7, 5)


def _check(text: str) -> None:
    if not 1 <= len(text) <= 200:
        raise ValueError(f"haiku must be 1-200 characters, got {len(text)}")
    lines = text.split("\n")
    if len(lines) != 3:
        raise ValueError(f"haiku must have 3 lines, got {len(lines)}")
    for line, want in zip(lines, _SHAPE):
        words = [w.strip(",.").lower() for w in line.split()]
        got = sum(_SYLLABLES[w] for w in words)
        if got != want:
            raise ValueError(f"line {line!r} has {got} syllables, want {want}")


def main() -> None:
    _check(HAIKU)
    out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(HAIKU)


if __name__ == "__main__":
    main()
