#!/usr/bin/env python3
"""Save a non-destructive before/after QA execution environment snapshot."""
import argparse
from datetime import datetime
from pathlib import Path
import platform
import re
import subprocess

ROOT = Path(__file__).resolve().parents[1]


def git(*args):
    result = subprocess.run(["git", *args], cwd=ROOT, text=True, capture_output=True, check=True)
    return result.stdout.strip()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--run-id", required=True)
    parser.add_argument("--phase", required=True, choices=["before", "after"])
    parser.add_argument("--unity-editor", default="", help="Version seen in the running Unity Editor")
    args = parser.parse_args()
    if not re.fullmatch(r"RUN-[0-9]{3,}", args.run_id):
        parser.error("Run ID must look like RUN-008")

    # All observations happen before the report itself is written.
    now = datetime.now().astimezone().isoformat(timespec="seconds")
    head = git("rev-parse", "HEAD")
    branch = git("branch", "--show-current") or "(detached)"
    status = git("status", "--short")
    changes = git("diff", "--name-only")
    try:
        upstream = git("rev-parse", "--abbrev-ref", "--symbolic-full-name", "@{upstream}")
    except subprocess.CalledProcessError:
        upstream = "(none)"

    path = ROOT / "ProjectSettings" / "ProjectVersion.txt"
    match = re.search(r"^m_EditorVersion:\s*(\S+)", path.read_text(encoding="utf-8"), re.M) if path.exists() else None
    expected_editor = match.group(1) if match else "unknown"
    report = ROOT / "Evidence" / "Traceability" / (args.run_id + "-" + args.phase + ".md")
    lines = [
        "# " + args.run_id + " — " + args.phase + "-test environment snapshot",
        "",
        "- Snapshot time (local UTC offset): " + now,
        "- Git commit at snapshot time: " + head,
        "- Branch: " + branch,
        "- Upstream: " + upstream,
        "- Working tree: " + ("DIRTY" if status else "CLEAN"),
        "- Unity project editor version: " + expected_editor,
        "- Running Unity Editor version (observed): " + (args.unity_editor or "NOT RECORDED"),
        "- OS: " + platform.system() + " " + platform.release(),
        "",
        "## Git status (before writing this evidence file)",
        "",
        "~~~text", status or "(clean)", "~~~",
        "",
        "## Modified tracked file paths",
        "",
        "~~~text", changes or "(none)", "~~~",
        "",
        "## Interpretation",
        "",
        "This snapshot describes the repository at capture time, not a historical",
        "test run. Attach before and after snapshots together with actual Unity",
        "Test Runner screenshots or XML. A dirty worktree can change test behavior;",
        "do not discard local changes as part of evidence collection.",
        "",
    ]
    report.parent.mkdir(parents=True, exist_ok=True)
    report.write_text("\n".join(lines), encoding="utf-8")
    print("Created:", report.relative_to(ROOT))
    print("HEAD:", head)
    print("Working tree before report:", "DIRTY" if status else "CLEAN")


if __name__ == "__main__":
    main()
