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



# UNITY002 only suppresses a warning when the guarantee appears in the same
# enclosing method, before the member access, and the receiver has not been
# assigned again. It does not attempt whole-program data-flow analysis.
DIRECT_COMPONENT = re.compile(
    r"(?:(?P<receiver>\b[A-Za-z_]\w*)\s*\.\s*)?"
    r"GetComponent\s*<\s*(?P<component>[A-Za-z_]\w*(?:\.[A-Za-z_]\w*)*)\s*>\s*\(\s*\)\s*\."
)
DIRECT_COMPONENT_TYPEOF = re.compile(
    r"\bGetComponent\s*\(\s*typeof\([^()]+\)\s*\)\s*\."
)
METHOD_DECL = re.compile(
    r"\b(?:public|private|protected|internal)\s+"
    r"(?:(?:static|virtual|override|sealed|async|new)\s+)*"
    r"[A-Za-z_][\w<>\[\],.?]*\s+[A-Za-z_]\w*\s*"
    r"\([^;{}]*\)\s*\{"
)
PRIMITIVE_TYPES = {
    "Cube": {"BoxCollider", "Renderer", "MeshRenderer"},
    "Sphere": {"SphereCollider", "Renderer", "MeshRenderer"},
    "Capsule": {"CapsuleCollider", "Renderer", "MeshRenderer"},
    "Cylinder": {"CapsuleCollider", "Renderer", "MeshRenderer"},
    "Plane": {"MeshCollider", "Renderer", "MeshRenderer"},
    "Quad": {"MeshCollider", "Renderer", "MeshRenderer"},
}


def method_body_at(clean: str, offset: int) -> tuple[int, int] | None:
    """Return the smallest enclosing method body from recognized declarations."""
    enclosing = []
    for match in METHOD_DECL.finditer(clean, 0, offset):
        start = match.end()
        depth = 1
        pos = start
        while pos < len(clean) and depth:
            if clean[pos] == "{":
                depth += 1
            elif clean[pos] == "}":
                depth -= 1
            pos += 1
        if start <= offset < pos - 1 and depth == 0:
            enclosing.append((start, pos - 1))
    return max(enclosing, key=lambda span: span[0]) if enclosing else None


def guaranteed_component(clean: str, match: re.Match[str]) -> bool:
    receiver = match.group("receiver")
    component = match.group("component")
    if not receiver:
        return False

    enclosing = method_body_at(clean, match.start())
    if enclosing is None:
        return False
    prefix = clean[enclosing[0]:match.start()]
    name = re.escape(receiver)
    typ = re.escape(component)

    # Recognize an earlier NUnit assertion on exactly the same receiver/type.
    # Do not suppress if the receiver was subsequently reassigned.
    assertions = list(re.finditer(
        rf"\bAssert\s*\.\s*NotNull\s*\(\s*{name}\s*\.\s*"
        rf"GetComponent\s*<\s*{typ}\s*>\s*\(\s*\)\s*(?:,[^;)]*)?\)",
        prefix,
    ))
    for assertion in reversed(assertions):
        tail = prefix[assertion.end():]
        if not re.search(rf"\b{name}\s*=(?!=)", tail):
            return True

    # GameObject.CreatePrimitive guarantees certain built-in components.
    # Only recognize the named variable initialized in the current method.
    for primitive in re.finditer(
        rf"\b(?:GameObject\s+|var\s+){name}\s*=\s*"
        r"GameObject\s*\.\s*CreatePrimitive\s*\(\s*"
        r"PrimitiveType\s*\.\s*(\w+)\s*\)",
        prefix,
    ):
        if component not in PRIMITIVE_TYPES.get(primitive.group(1), set()):
            continue
        tail = prefix[primitive.end():]
        if not re.search(rf"\b{name}\s*=(?!=)", tail):
            return True
    return False


def component_access_findings(clean: str, source: str) -> list[tuple[str, int, str]]:
    message = "Immediate member access on GetComponent result without a null check; verify the component is always present."
    hits = []
    for match in DIRECT_COMPONENT.finditer(clean):
        if not guaranteed_component(clean, match):
            hits.append(("UNITY002", source.count("\n", 0, match.start()) + 1, message))
    for match in DIRECT_COMPONENT_TYPEOF.finditer(clean):
        hits.append(("UNITY002", source.count("\n", 0, match.start()) + 1, message))
    return hits


def analyze(source: str) -> list[tuple[str, int, str]]:
    clean = masked_source(source)
    findings = component_access_findings(clean, source)
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
