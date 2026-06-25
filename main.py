"""
Text Extraction Utility — for agent use.
Usage:
  python main.py                  # extracts all files in JD/ and Profile_data/
  python main.py path/to/file     # extracts a single file
Outputs extracted text to stdout or saves as .txt in the same directory.
"""

import sys
import os
import glob


def extract_txt(path: str) -> str:
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def extract_pdf(path: str) -> str:
    from pdfminer.high_level import extract_text
    return extract_text(path)


def extract_docx(path: str) -> str:
    from docx import Document
    return "\n".join(p.text for p in Document(path).paragraphs if p.text.strip())


EXTRACTORS = {
    ".txt":  extract_txt,
    ".pdf":  extract_pdf,
    ".docx": extract_docx,
}


def extract(path: str) -> str:
    ext = os.path.splitext(path)[1].lower()
    fn = EXTRACTORS.get(ext)
    if not fn:
        raise ValueError(f"Unsupported file type: {ext}")
    return fn(path)


def process(path: str, save: bool = False):
    print(f"\n=== {path} ===")
    text = extract(path)
    if save:
        out = os.path.splitext(path)[0] + "_extracted.txt"
        with open(out, "w", encoding="utf-8") as f:
            f.write(text)
        print(f"[saved → {out}]")
    else:
        print(text)


if __name__ == "__main__":
    targets = sys.argv[1:] if len(sys.argv) > 1 else (
        glob.glob("JD/*") + glob.glob("Profile_data/*")
    )
    for t in targets:
        if os.path.basename(t).lower() == "readme.md":
            continue
        process(t)
