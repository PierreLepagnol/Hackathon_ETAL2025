from __future__ import annotations

import hashlib
from pathlib import Path
import subprocess
# -------- 0) Storage / cache ----------

CACHE = Path("slides_cache")
CACHE.mkdir(exist_ok=True)


def _hid(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8")).hexdigest()[:16]


def _pdf_out(md: str, engine: str) -> Path:
    return CACHE / f"{_hid(md)}-{engine}.pdf"


def compile_pandoc_beamer(md: str) -> str:
    out = _pdf_out(md, "beamer")
    if out.exists():
        return str(out)
    src = CACHE / f"{_hid(md)}.md"
    src.write_text(md, encoding="utf-8")
    # Choose any Beamer theme; 'metropolis' is popular if installed
    cmd = [
        "pandoc",
        str(src),
        "-t",
        "beamer",
        "-V",
        "theme:metropolis",
        "--pdf-engine=xelatex",
        "-V",
        "mainfont:DejaVu Sans",
        "-o",
        str(out),
    ]
    subprocess.run(cmd, check=True)
    return str(out)


def compile_marp(md: str) -> str:
    out = _pdf_out(md, "marp")
    if out.exists():
        return str(out)
    src = CACHE / f"{_hid(md)}.md"
    src.write_text(md, encoding="utf-8")
    # Requires Node + marp CLI (pulled via npx if not installed):
    cmd = [
        "npx",
        "-y",
        "@marp-team/marp-cli",
        "--pdf",
        "--allow-local-files",
        str(src),
        "-o",
        str(out),
    ]
    subprocess.run(cmd, check=True)
    return str(out)
