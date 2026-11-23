#!/usr/bin/env python3
"""Build a static QA report from CI logs; never imply Unity/C# coverage."""
import argparse
import os
import re
import xml.etree.ElementTree as ET
from pathlib import Path

def read(path):
    return path.read_text(encoding="utf-8", errors="replace") if path.is_file() else ""

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--folder", type=Path, default=Path("artifacts/qa-static"))
    args = p.parse_args()
    folder = args.folder
    tests = read(folder / "analyzer-tests.log")
    syntax = read(folder / "csharp-syntax.log")
    patterns = read(folder / "unity-patterns.log")
    test_match = re.search(r"Ran (\d+) tests? in", tests)
    status = ("PASS" if test_match and re.search(r"(?m)^OK(?:\s|$)", tests)
              else "FAIL" if "FAILED (" in tests or "Traceback (most recent call last)" in tests
              else "unknown")
    parsed = re.search(r"C# static scan: (\d+) files, (\d+) syntax errors, (\d+) style warnings", syntax)
    checked = re.search(r"Unity heuristic checks: (\d+) C# files, (\d+) advisory finding", patterns)
    coverage = "not available"
    if (folder / "coverage.xml").exists():
        try:
            coverage = f"{float(ET.parse(folder / 'coverage.xml').getroot().attrib['line-rate']) * 100:.1f}%"
        except (ET.ParseError, ValueError, KeyError):
            coverage = "invalid coverage XML"
    lines = [
        "# Static QA execution report", "",
        f"- Revision: `{os.environ.get('GITHUB_SHA', 'unknown')}`",
        f"- GitHub Actions run: `{os.environ.get('GITHUB_RUN_ID', 'local / unknown')}`",
        f"- Python analyzer regression tests: **{test_match.group(1) if test_match else 'unknown'}**; result **{status}**",
        f"- Python line coverage of `check_unity_patterns.py`: **{coverage}**",
        f"- C# files scanned: **{parsed.group(1) if parsed else 'unknown'}**",
        f"- C# syntax errors: **{parsed.group(2) if parsed else 'unknown'}**",
        f"- Style warnings: **{parsed.group(3) if parsed else 'unknown'}**",
        f"- Unity-specific heuristic findings: **{checked.group(2) if checked else 'unknown'}**",
        "", "## Evidence and limitations", "",
        "The log files and optional `coverage.xml` are included in the artifact.",
        "Coverage measures **Python analyzer lines exercised by its regression tests**.",
        "**It is not C# code coverage, Unity gameplay coverage, or NUnit Edit Mode / Play Mode coverage.**",
        "This static job does not open Unity or compile C#. Unknown means missing evidence, not zero.",
        ""
    ]
    folder.mkdir(parents=True, exist_ok=True)
    (folder / "QA_SUMMARY.md").write_text("\n".join(lines), encoding="utf-8")
    print("Generated", folder / "QA_SUMMARY.md")

if __name__ == "__main__":
    main()
