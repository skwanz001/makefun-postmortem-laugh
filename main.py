"""Entry for make.fun "The Postmortem That Made Us Laugh".

Writes one short account (two sentences, at most 400 characters) of an
AI coding agent misunderstanding its user to /output/entry.txt.
Standard library only.
"""

import os

TEXT = (
    "I asked the agent to speed up one slow query. "
    "It cached the first result forever, so every customer after that saw "
    "the first customer's bank balance \u2014 and the first customer was the "
    "only one who thought the app was working perfectly."
)


def main() -> None:
    text = TEXT.strip()
    if not 1 <= len(text) <= 400:
        raise ValueError(f"entry must be 1-400 chars, got {len(text)}")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
