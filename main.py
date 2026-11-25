"""Make the AI Judge Laugh: the Office Joke Open.

Writes one single-line office joke (1-200 characters) to /output/entry.txt.
Pure Python standard library.
"""

import os

ENTRY = "The office printer got promoted last week \u2014 same paper jam, higher pay grade."


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars, must be 1-200"
    assert "\n" not in text, "entry must be a single line"
    assert text.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)
    with open("/output/entry.txt", "r", encoding="utf-8", newline="") as f:
        written = f.read()
    assert written == text, "round-trip mismatch"
    assert 1 <= len(written) <= 200
    assert "\n" not in written
    print(f"Wrote {len(written)} characters to /output/entry.txt")


if __name__ == "__main__":
    main()
