# Static QA evidence and Python analyzer coverage

The [C# Static Analysis workflow](../.github/workflows/csharp-static-analysis.yml) now produces a **Static QA execution report** in its GitHub Actions job summary and uploads an artifact named `static-qa-evidence` (retained 30 days).

## Contents of each workflow artifact

| File | Meaning |
|---|---|
| `QA_SUMMARY.md` | Revision, run identifier, regression-test result and counts of source-scan findings |
| `analyzer-tests.log` | Output of the Python regression tests for the Unity heuristics |
| `coverage.xml` | **Python line coverage of `check_unity_patterns.py`** exercised by those regression tests, when available |
| `csharp-syntax.log` | C# source parse and whitespace diagnostics |
| `unity-patterns.log` | Unity-specific advisory findings |

The workflow executes Python's `coverage` tool while testing the analyzer. **This does not measure coverage of C# scripts, gameplay logic, or Unity Edit Mode / Play Mode tests.** Such coverage requires a separately authorized Unity test setup. A report field marked `unknown` or `not available` means evidence was not produced; it does not mean the value is zero.

## How to inspect reports

1. Open [C# Static Analysis Actions](https://github.com/ornellasdev/unity-qa-sandbox/actions/workflows/csharp-static-analysis.yml).
2. Choose an execution and view its **Summary** to read the Markdown QA report.
3. Scroll to **Artifacts**, download `static-qa-evidence`, and review the logs and optional XML.

The reports are per-run artifacts; they are **not** a permanent public historical dashboard. GitHub retention may remove older artifacts. For a portfolio-longitudinal dashboard, a later step can aggregate verified run results without inventing a history.

## Latest confirmation

The repository owner reported a successful, warning-free run of the updated C# static analysis workflow. The repository owner shared a screenshot of the extracted `static-qa-evidence` ZIP showing `QA_SUMMARY.md`, `coverage.xml`, `analyzer-tests.log`, `csharp-syntax.log` and `unity-patterns.log`. The file contents and precise Python coverage percentage have not yet been examined.

## Current state

- [x] Publish artifact generation and workflow summary
- [x] Add Python analyzer line-coverage export
- [x] Confirm a successful run of the updated workflow (owner-reported)
- [x] Verify the `static-qa-evidence` artifact exists and contains the expected five files (owner screenshot)
- [ ] Record a verified example run URL and its actual coverage percentage
- [ ] Add Unity C# and gameplay coverage only after licensed Unity tests can run
