"""Write one excuse line to /output/entry.txt and verify it."""

from pathlib import Path

MAX_CHARS = 140
OUTPUT_PATH = Path("/output/entry.txt")

EXCUSE = "I deleted your file, then backed up the deletion so I'd never lose it."


def validate(text: str) -> None:
    """Check the excuse meets the competition gate: UTF-8, 1-140 chars,
    exactly one line, and not only whitespace."""
    text.encode("utf-8")
    if not text.strip():
        raise ValueError("entry is empty or only whitespace")
    if len(text) != len(text.strip()):
        raise ValueError("entry has leading or trailing whitespace")
    if len(text) > MAX_CHARS:
        raise ValueError(f"entry is {len(text)} chars, over the {MAX_CHARS} limit")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be exactly one line")
    if text.splitlines() != [text]:
        raise ValueError("entry must be exactly one line")
    if any(ord(ch) < 0x20 for ch in text):
        raise ValueError("entry must not contain control characters")


def main() -> None:
    validate(EXCUSE)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(EXCUSE, encoding="utf-8")
    # Verify by reading the file back.
    read_back = OUTPUT_PATH.read_text(encoding="utf-8")
    validate(read_back)
    assert read_back == EXCUSE, "written entry does not match the excuse"
    print(f"Wrote {len(read_back)} chars to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
