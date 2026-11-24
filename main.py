#!/usr/bin/env python3
"""Ridiculous at first glance — a make.fun entry.

The program writes one sentence to /output/entry.txt (or
$MAKEFUN_OUTPUT_DIR/entry.txt): a startup pitch that sounds
ridiculous at first glance and turns out to be a real business by
the second. The sentence is 150 characters, inside the competition's
gate of 1 to 200 characters of UTF-8 text. Standard library only, no
network, and deterministic: the same bytes on every run.
"""

import os

LINE = "We sell silence: a subscription box containing one empty, soundproof room hour in the loudest cities, and new parents are our fastest-growing segment."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    # The entry file holds exactly the one sentence: no trailing newline,
    # so the text the judge reads is the sentence itself, byte for byte —
    # the gate counts characters, and a trailing newline would spend one.
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(LINE)


if __name__ == "__main__":
    main()
