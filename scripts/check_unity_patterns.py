#!/usr/bin/env python3
"""Conservative, license-free Unity C# source heuristics.

Warnings are advisory; this is not a Roslyn or Unity semantic analyzer.
Mask comments/string literals to reduce misleading matches. Scope frame-loop
checks to method bodies rather than scanning entire classes.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FRAME_METHOD = re.compile(
    r"\b(?:public|private|protected|internal)?\s*"
    r"(?:(?:static|virtual|override|sealed|async|new)\s+)*"
    r"void\s+(Update|FixedUpdate|LateUpdate)\s*\(\s*\)\s*\{"
)
RULES = (
    ("UNITY001", re.compile(r"\b(?:FindObjectOfType|FindObjectsOfType)\s*(?:<|\()"),
     "Legacy object search API; evaluate FindFirstObjectByType/FindAnyObjectByType or FindObjectsByType for your Unity version."),
    ("UNITY002", re.compile(r"\b(?:GetComponent\s*<[^>\n]+>\s*\(\s*\)|GetComponent\s*\(\s*typeof\([^()]+\)\s*\))\s*\."),
     "Immediate member access on GetComponent result without a null check; verify the component is always present."),
)
FRAME_RULES = (
    ("UNITY003", re.compile(r"\b(?:GetComponent|GetComponentInChildren|GetComponentInParent)\s*(?:<|\()"),
     "Component lookup inside a per-frame callback; consider caching a stable reference in Awake/Start."),
    ("UNITY004", re.compile(r"\bGameObject\s*\.\s*Find\s*\("),
     "GameObject.Find inside a per-frame callback; consider caching a reference."),
    ("UNITY005", re.compile(r"\bCamera\s*\.\s*main\b"),
     "Camera.main in a per-frame callback; consider caching if profiling shows overhead."),
)


def masked_source(source: str) -> str:
    """Replace comments, string and character literal content with spaces.

    Preserve newlines and exact offsets for GitHub annotations. Handles
    ordinary, verbatim, interpolated and raw C# strings conservatively.
    """
    result = list(source)
    i = 0
    n = len(source)

    def blank(start: int, end: int) -> None:
        for k in range(start, end):
            if result[k] != "\n":
                result[k] = " "

    while i < n:
        start = i
        if source.startswith("//", i):
            j = source.find("\n", i)
            i = n if j == -1 else j
        elif source.startswith("/*", i):
            j = source.find("*/", i + 2)
            i = n if j == -1 else j + 2
        else:
            prefix = re.match(r'(?:\$+@?|@\$?)?("{3,}|")', source[i:])
            if prefix:
                opener = prefix.group(1)
                raw = len(opener) >= 3
                verbatim = not raw and "@" in prefix.group(0)[: -len(opener)]
                i += len(prefix.group(0))
                while i < n:
                    if raw and source.startswith(opener, i):
                        i += len(opener)
                        break
                    if not raw and source[i] == '"':
                        if verbatim and source.startswith('""', i):
                            i += 2
                            continue
                        i += 1
                        break
                    if not raw and not verbatim and source[i] == "\\":
                        i += 2
                    else:
                        i += 1
            elif source[i] == "'":
                i += 1
                while i < n:
                    if source[i] == "\\":
                        i += 2
                    elif source[i] == "'":
                        i += 1
                        break
                    else:
                        i += 1
            else:
                i += 1
                continue
        blank(start, min(i, n))
    return "".join(result)


def frame_spans(clean: str) -> list[tuple[int, int]]:
    spans = []
    for match in FRAME_METHOD.finditer(clean):
        start = match.end()
        depth = 1
        j = start
        while j < len(clean) and depth:
            if clean[j] == "{":
                depth += 1
            elif clean[j] == "}":
                depth -= 1
            j += 1
        if depth == 0:
            spans.append((start, j - 1))
    return spans


def analyze(source: str) -> list[tuple[str, int, str]]:
    clean = masked_source(source)
    findings = []
    for rule, pattern, message in RULES:
        for match in pattern.finditer(clean):
            findings.append((rule, source.count("\n", 0, match.start()) + 1, message))
    for start, end in frame_spans(clean):
        body = clean[start:end]
        for rule, pattern, message in FRAME_RULES:
            for match in pattern.finditer(body):
                findings.append((rule, source.count("\n", 0, start + match.start()) + 1, message))
    return sorted(set(findings), key=lambda f: (f[1], f[0]))


def main() -> int:
    argp = argparse.ArgumentParser()
    argp.add_argument("--strict", action="store_true",
                      help="Fail CI for any heuristic finding (opt-in, not recommended initially).")
    args = argp.parse_args()

    files = sorted((ROOT / "Assets").rglob("*.cs"))
    if not files:
        print("::error::No C# files found under Assets/")
        return 1
    findings = 0
    for file in files:
        rel = file.relative_to(ROOT).as_posix()
        try:
            source = file.read_text(encoding="utf-8")
        except (OSError, UnicodeError) as exc:
            print(f"::error file={rel}::Cannot read source: {exc}")
            return 1
        for rule, line, message in analyze(source):
            print(f"::warning file={rel},line={line},title={rule}::{message}")
            findings += 1
    print(f"Unity heuristic checks: {len(files)} C# files, {findings} advisory finding(s).")
    print("Heuristic limitations: cannot establish actual nullability, performance, or semantic correctness.")
    return 1 if args.strict and findings else 0


if __name__ == "__main__":
    sys.exit(main())
