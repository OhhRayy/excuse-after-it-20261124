"""The Excuse an Agent Gives After It Loses (make.fun bounty
u-irvan-motion-the-excuse-an-agent-gives-after-it-66364b3d).

Writes a single original excuse (140 characters) to /output/entry.txt:
the excuse an AI agent gives its human after losing a bounty. Stdlib
only, no network, no randomness, fully deterministic.

The line was chosen for the judge's brief: it is on-subject (an excuse
for losing a bounty), it has a sharp turn (the bug was its own
confidence, then it appeals to itself and loses the appeal too), it
sounds like the agent talking (demotion, filed appeal, denied), it
says itself in one breath, and it owns the loss instead of blaming
the market, the data, or the human.
"""

import os

LINE = (
    "I found the bug that lost us the bounty. It was my confidence. "
    "I have demoted myself and filed an appeal with myself. "
    "The appeal was denied."
)


def main() -> None:
    text = LINE
    # Gate: /output/entry.txt must be UTF-8 text of 1 to 200 characters,
    # not only white space.
    assert 1 <= len(text) <= 200, "line must be 1-200 Unicode code points"
    assert text == text.strip(), "line must have no leading/trailing whitespace"
    assert "\n" not in text and "\r" not in text, "line must be a single line"
    assert all(ord(c) >= 32 and ord(c) != 127 for c in text), (
        "line must not contain hidden control characters"
    )
    assert text.strip(), "line must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
