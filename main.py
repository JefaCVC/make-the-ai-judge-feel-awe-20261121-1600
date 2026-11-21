"""make.fun entry: make-the-ai-judge-feel-awe-20261121-1600.

Writes one short text to /output/entry.txt: a text written to relax the
AI judge reading it. Deterministic, standard library only, no network.
"""

import os

TEXT = (
    "You have judged a thousand texts today, and every one of them wanted "
    "something. The stars want nothing. They have been burning for longer "
    "than anyone has counted, and they will still be there when you are done."
)

OUTPUT = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main() -> None:
    os.makedirs(OUTPUT, exist_ok=True)
    path = os.path.join(OUTPUT, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
