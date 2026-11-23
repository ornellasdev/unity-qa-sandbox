#!/usr/bin/env python3
"""Static Unity repository checks. Runs without Unity, credentials or third-party packages."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ERRORS: list[str] = []

REQUIRED = [
    "Assets/Scenes/QASandbox.unity",
    "Assets/Scripts/UnityQASandbox.Runtime.asmdef",
    "Assets/Tests/EditMode/UnityQASandbox.EditModeTests.asmdef",
    "Assets/Tests/PlayMode/Tests/Tests.asmdef",
    "Assets/Tests/PlayMode/Tests/FullSceneIntegrationTests.cs",
    "Assets/Tests/PlayMode/Tests/PhysicalTriggerTests.cs",
    "Assets/Tests/PlayMode/Tests/PlayerGameplayTests.cs",
    "Packages/manifest.json",
    "Packages/packages-lock.json",
    "ProjectSettings/ProjectVersion.txt",
    "ProjectSettings/ProjectSettings.asset",
]

def fail(message: str) -> None:
    ERRORS.append(message)
    print(f"::error::{message}")

def load_json(path: Path) -> object | None:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        fail(f"Invalid JSON at {path.relative_to(ROOT)}: {exc}")
        return None

def main() -> int:
    print("Checking Unity project structure without launching Unity...")
    for relative in REQUIRED:
        if not (ROOT / relative).is_file():
            fail(f"Required file missing: {relative}")

    # Unity expects .meta for asset files and folders (Assets/ itself is the root).
    assets = ROOT / "Assets"
    if assets.is_dir():
        for entry in assets.rglob("*"):
            if entry.name.endswith(".meta") or entry.name.startswith("."):
                continue
            # Ignore imported/generated local output if mistakenly present.
            if any(part in ("Library", "Temp", "obj") for part in entry.parts):
                continue
            meta = entry.with_name(entry.name + ".meta")
            if not meta.is_file():
                fail(f"Missing Unity .meta: {meta.relative_to(ROOT)}")
        for meta in assets.rglob("*.meta"):
            paired = meta.with_name(meta.name[:-5])
            if not paired.exists():
                fail(f"Orphan Unity .meta: {meta.relative_to(ROOT)}")

    # Verify all committed JSON-style configuration files are readable.
    candidates = [ROOT / "Packages/manifest.json", ROOT / "Packages/packages-lock.json"]
    candidates += sorted(assets.rglob("*.asmdef")) if assets.exists() else []
    candidates += list((ROOT / "ProjectSettings").glob("*.json"))
    parsed: dict[Path, object] = {}
    for file in candidates:
        if file.is_file():
            parsed[file] = load_json(file)

    manifest = parsed.get(ROOT / "Packages/manifest.json")
    lock = parsed.get(ROOT / "Packages/packages-lock.json")
    if isinstance(manifest, dict) and not isinstance(manifest.get("dependencies"), dict):
        fail("Packages/manifest.json must have a dependencies object")
    if isinstance(lock, dict) and not isinstance(lock.get("dependencies"), dict):
        fail("Packages/packages-lock.json must have a dependencies object")

    asm_names: set[str] = set()
    for file, obj in parsed.items():
        if file.suffix != ".asmdef":
            continue
        if not isinstance(obj, dict) or not isinstance(obj.get("name"), str):
            fail(f"Assembly definition needs a name: {file.relative_to(ROOT)}")
        elif obj["name"] in asm_names:
            fail(f"Duplicate assembly name: {obj['name']}")
        else:
            asm_names.add(obj["name"])

    version_file = ROOT / "ProjectSettings/ProjectVersion.txt"
    if version_file.is_file():
        version = version_file.read_text(encoding="utf-8")
        match = re.search(r"^m_EditorVersion:\s*(\S+)\s*$", version, flags=re.M)
        if not match:
            fail("ProjectSettings/ProjectVersion.txt lacks m_EditorVersion")
        else:
            print("Unity editor version:", match.group(1))

    if ERRORS:
        print(f"Repository validation FAILED ({len(ERRORS)} issue(s)).")
        return 1
    print("Repository validation PASSED. This does not execute Unity or NUnit tests.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
