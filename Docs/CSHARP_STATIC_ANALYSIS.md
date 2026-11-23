# C# Static Analysis — no Unity license required

**Status:** GitHub Actions execution succeeded (previous screenshot reviewed); repository owner also reports a green result following the Node.js 24 action upgrade. Latest warning details have not been independently reviewed.

The [C# Static Analysis workflow](../.github/workflows/csharp-static-analysis.yml) uses the open-source **Tree-sitter C# grammar** to parse C# files under `Assets/`. It does not open Unity, consume a Unity license seat, or access any account secrets.

## What it checks

| Check | CI behavior |
|---|---|
| C# syntax/grammar errors | **FAIL** |
| Source files encoded in invalid UTF-8 | **FAIL** |
| No C# files under `Assets/` | **FAIL** |
| Trailing whitespace | **WARNING** |
| Tab indentation | **WARNING** |

Style warnings do not fail CI by default. This allows incremental cleanup of existing code. For a local strict style check, use `--strict-style`.

## How to run locally on CachyOS

```bash
cd ~/Projetos/unity-qa-sandbox
python -m venv .venv
source .venv/bin/activate
python -m pip install -r scripts/csharp-static-requirements.txt
python scripts/check_csharp.py
```

Optional strict style mode:

```bash
python scripts/check_csharp.py --strict-style
```

The CI workflow runs on relevant pushes to `main`, pull requests changing C# code or analysis files, and manual dispatch.

[Open the GitHub Actions workflow](https://github.com/ornellasdev/unity-qa-sandbox/actions/workflows/csharp-static-analysis.yml)

## Scope and limits

- Tree-sitter parsing helps find **syntax errors**, not C# type errors or undefined symbols.
- The script does **not** run Roslyn analyzers, `dotnet build`, NUnit, or Unity Test Runner.
- The Unity project still requires Unity for authoritative compilation and gameplay tests.
- Some preprocessor-dependent errors may not be detected by parsing alone.
- Style warnings are advisory; they do not indicate broken gameplay.
- The first successful GitHub Actions run was supported by a screenshot. A subsequent post-upgrade green result was reported by the repository owner; green status alone does not establish zero warnings.

## Roadmap

- [x] Publish parser-based C# static analysis script
- [x] Add GitHub Actions on pushes / PRs
- [x] Verify first successful C# analysis run
- [x] Owner reported successful rerun after Node.js 24 upgrade
- [ ] Confirm warning-free post-upgrade logs
- [ ] Review warnings and adopt a consistent C# format policy
- [ ] Evaluate Roslyn-based analysis when Unity assemblies can be resolved reliably
- [ ] Run actual Unity Edit Mode/Play Mode tests in an authorized CI environment
