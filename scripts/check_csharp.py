#!/usr/bin/env python3
"""Lightweight C# syntax and hygiene checks without the Unity Editor.

Requires tree-sitter and tree-sitter-c-sharp; reports syntax errors as CI failures.
Style findings are initially warnings so legacy Unity code can be normalized
incrementally. This is NOT Roslyn analysis, type checking, or a Unity build.
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

from tree_sitter import Language, Parser
import tree_sitter_c_sharp

ROOT = Path(__file__).resolve().parents[1]
CS_ROOT = ROOT / "Assets"
SKIP_DIRS = {"Library", "Temp", "obj", "Obj", "Logs"}
MAX_DIAGNOSTICS = 25


def check_file(path: Path, parser: Parser) -> tuple[int, int]:
    raw = path.read_bytes()
    rel = path.relative_to(ROOT).as_posix()
    syntax_errors = 0
    warnings = 0
    try:
        raw.decode("utf-8")
    except UnicodeDecodeError:
        print(f"::error file={rel},line=1::C# source is not valid UTF-8")
        return 1, warnings

    tree = parser.parse(raw)
    errors = []
    if tree.root_node.has_error:
        # Find the smallest syntax-error spans rather than reporting every ancestor.
        stack = [tree.root_node]
        while stack:
            node = stack.pop()
            if node.type == "ERROR" or node.is_missing:
                errors.append(node)
            else:
                stack.extend(reversed(node.children))
        for node in errors[:MAX_DIAGNOSTICS]:
            line, col = node.start_point
            label = "missing syntax token" if node.is_missing else "unrecognized C# syntax"
            print(f"::error file={rel},line={line + 1},col={col + 1}::{label}")
        syntax_errors += len(errors) or 1

    for number, line in enumerate(raw.decode("utf-8").splitlines(), 1):
        if line.rstrip(" \t") != line:
            print(f"::warning file={rel},line={number}::Trailing whitespace")
            warnings += 1
        if "\t" in line[: len(line) - len(line.lstrip(" \t"))]:
            print(f"::warning file={rel},line={number}::Tab indentation")
            warnings += 1

    return syntax_errors, warnings


def main() -> int:
    args = argparse.ArgumentParser()
    args.add_argument(
        "--strict-style",
        action="store_true",
        help="Also fail on whitespace warnings (opt-in for future cleanup).",
    )
    options = args.parse_args()

    parser = Parser(Language(tree_sitter_c_sharp.language()))
    files = sorted(
        path
        for path in CS_ROOT.rglob("*.cs")
        if not any(part in SKIP_DIRS for part in path.relative_to(ROOT).parts)
    ) if CS_ROOT.exists() else []

    if not files:
        print("::error::No C# source files found under Assets/")
        return 1

    errors = 0
    warnings = 0
    for path in files:
        file_errors, file_warnings = check_file(path, parser)
        errors += file_errors
        warnings += file_warnings

    print(f"C# static scan: {len(files)} files, {errors} syntax errors, {warnings} style warnings.")
    print("Limitations: no semantic/type checking, Unity compile, or NUnit execution.")
    return 1 if errors or (options.strict_style and warnings) else 0


if __name__ == "__main__":
    sys.exit(main())
