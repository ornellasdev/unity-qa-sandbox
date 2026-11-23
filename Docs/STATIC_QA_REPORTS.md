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

The repository owner reported a successful, warning-free run of the updated C# static analysis workflow. The repository owner shared a screenshot of the extracted `static-qa-evidence` ZIP showing `QA_SUMMARY.md`, `coverage.xml`, `analyzer-tests.log`, `csharp-syntax.log` and `unity-patterns.log`. The owner subsequently supplied all five original artifact files. Verified report for [GitHub Actions run 45101652954](https://github.com/ornellasdev/unity-qa-sandbox/actions/runs/45101652954), revision `8868238d8de8d114b702c75fd36f1a7a83c5b00e`: **16/16 Python analyzer regression tests PASS**, **76.1% line coverage (121/159 executable lines)** for `scripts/check_unity_patterns.py`, **13 C# files scanned**, **0 syntax errors**, **0 style warnings**, and **0 Unity heuristic findings**. These are point-in-time static QA metrics, **not** Unity or C# gameplay coverage.

## Python analyzer coverage target

Baseline evidence from run [45101652954](https://github.com/ornellasdev/unity-qa-sandbox/actions/runs/45101652954) is **76.1%** (121 of 159 executable lines). Added 19 regression tests (35 total) exercising C# literal masking, incomplete input, the `typeof` pattern and analyzer CLI, including strict mode and unreadable UTF-8. The workflow now runs `coverage report --include='*/check_unity_patterns.py' --fail-under=85` after the evidence upload. **Verified:** [run 45102176871](https://github.com/ornellasdev/unity-qa-sandbox/actions/runs/45102176871) completed successfully with **35/35 tests PASS** and **98% Python analyzer coverage (156 of 159 lines)** as shown in the GitHub Actions job log. The 85% minimum passed. The run contained 0 C# syntax errors, 0 style warnings, and 0 Unity-specific findings. Its sole GitHub annotation was a Node.js 20 deprecation warning from `actions/upload-artifact@v4`; the workflow has since been upgraded to v6, awaiting another run. This coverage is Python-only, not Unity C# gameplay coverage. This coverage is Python-only, not Unity C# gameplay coverage.

## Current state

- [x] Publish artifact generation and workflow summary
- [x] Add Python analyzer line-coverage export
- [x] Confirm a successful run of the updated workflow (owner-reported)
- [x] Verify the `static-qa-evidence` artifact exists and contains the expected five files (owner screenshot)
- [x] Record verified run [45101652954](https://github.com/ornellasdev/unity-qa-sandbox/actions/runs/45101652954) and actual **76.1% Python analyzer line coverage** (121/159 lines)
- [x] Add 19 regression tests to broaden analyzer Python coverage
- [x] Configure a minimum of 85% Python analyzer line coverage in CI
- [x] Verify 35/35 tests PASS and 98% Python coverage on [run 45102176871](https://github.com/ornellasdev/unity-qa-sandbox/actions/runs/45102176871)
- [x] Upgrade artifact upload action to Node.js 24-compatible v6
- [ ] Confirm the Node.js deprecation warning disappears on a post-upgrade run
- [ ] Add Unity C# and gameplay coverage only after licensed Unity tests can run
