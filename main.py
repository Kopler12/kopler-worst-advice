#!/usr/bin/env python3
"""Worst AI Advice: The 48-Hour Tight Line Open.

Writes one line of the worst possible advice an AI could give to
/output/entry.txt, as the competition requires: UTF-8 text of 1 to 140
characters, one line, no wasted words.

The line is deliberately terrible advice, delivered in the confident,
tidy voice of a helpful AI assistant: it sounds exactly like the kind
of upbeat answer an assistant would give, names a concrete action a
reader could plausibly follow, and the regret lands the moment the
advice is followed. Do not follow it. That is the joke.
"""

import os

ADVICE = (
    "Certainly! To improve your eyesight, stare directly at the sun "
    "for ten minutes a day - it's nature's free laser eye surgery."
)

OUTPUT_PATH = os.path.join(os.environ.get("OUTPUT_DIR", "/output"), "entry.txt")


def main() -> None:
    text = ADVICE.strip()
    assert 1 <= len(text) <= 140, f"entry is {len(text)} characters, must be 1-140"
    assert text.strip(), "entry must not be only whitespace"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"Wrote {len(text)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
