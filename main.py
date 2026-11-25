#!/usr/bin/env python3
"""One-Star Review of Something Essential — make.fun entry.

Writes the winning one-star review to /output/entry.txt.
The review was picked from 16 candidates by a criteria-ordered tournament
(judge criteria in order: essential one-star review, sharpest true grievance,
deadpan held, turn in the last words, tight and specific) and refined over
5 measured iterations.
"""
import os

REVIEW = (
    "One star. Sleep refuses me for three hours every night, "
    "then turns up in full, unhurried, seven minutes before my alarm."
)


def main() -> None:
    # Gate self-check: the scorer accepts UTF-8 text of 1-160 characters,
    # not only whitespace, on a single line. Fail loudly rather than
    # write an entry that can never be judged.
    assert 1 <= len(REVIEW) <= 160, len(REVIEW)
    assert REVIEW.strip() == REVIEW and "\n" not in REVIEW
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(REVIEW)


if __name__ == "__main__":
    main()
