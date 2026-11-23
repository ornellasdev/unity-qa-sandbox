# Unity QA Sandbox 🎮🧪

**Original Unity gameplay prototype • Technical Game QA • Test automation • CI evidence**  
Created and maintained by [Yuri Ornellas](https://github.com/ornellasdev)

[![Unity](https://img.shields.io/badge/Unity-6.6-222222?logo=unity)](https://unity.com/)
![C#](https://img.shields.io/badge/C%23-Gameplay%20%26%20NUnit-512BD4)
![QA](https://img.shields.io/badge/QA-Manual%20%2B%20Automated-1678B7)
[![Repository Validation](https://github.com/ornellasdev/unity-qa-sandbox/actions/workflows/repository-validation.yml/badge.svg)](https://github.com/ornellasdev/unity-qa-sandbox/actions/workflows/repository-validation.yml)
[![C# Static Analysis](https://github.com/ornellasdev/unity-qa-sandbox/actions/workflows/csharp-static-analysis.yml/badge.svg)](https://github.com/ornellasdev/unity-qa-sandbox/actions/workflows/csharp-static-analysis.yml)

> **Latest verified Unity Test Runner result — RUN-007:** **29/29 tests passed locally** (**22 Edit Mode + 7 Play Mode**), supported by two screenshots committed to this repository.  
> **Latest verified license-free CI result:** **35/35 Python analyzer regression tests passed**, **98.1% Python analyzer line coverage**, **13 C# files checked**, and **0 C# syntax, style, or Unity-heuristic findings** ([GitHub Actions run](https://github.com/ornellasdev/unity-qa-sandbox/actions/runs/45102487210)).  
> **Scope matters:** Python analyzer coverage is **not Unity/C# gameplay coverage**. Unity's NUnit suites have **not** been verified running in hosted GitHub Actions.

## Project overview

Unity QA Sandbox is an original, playable 3D graybox project built to demonstrate **gameplay programming and a structured technical QA workflow** on software the author controls. The repository includes gameplay source code, formal manual cases, NUnit tests, physics-trigger checks, scene integration tests, bug investigation, negative-path tests, and reproducible test reports.

**Gameplay systems**
- WASD movement, grounded jumping, and collision obstacles.
- Health, damage triggers, checkpoints, and player respawn.
- Health recovery on respawn, plus overflow-safe `Heal(int.MaxValue)`.
- A committed playable scene at `Assets/Scenes/QASandbox.unity` and an Editor scene-builder tool.

## Test strategy and results

| Layer | What it checks | Verified result |
|---|---|---|
| **Unity Edit Mode — NUnit** | `HealthModel` boundaries, invalid inputs, saturation, reset; `CheckpointModel` positions and activation | **22/22 PASS — local RUN-007** (17 health + 5 checkpoint) |
| **Unity Play Mode — NUnit / UnityTest** | Damage, health restoration, checkpoint state, physical triggers, full scene components | **7/7 PASS — local RUN-007** |
| **Manual functional QA** | Movement, collision, jump / double-jump prevention, initial respawn, checkpoint respawn | **4 formal cases / 8 checks reported PASS — RUN-002**; video supports damage and health-reset flow, not every scenario |
| **C# syntax and hygiene CI** | Tree-sitter C# syntax, whitespace, Unity-specific heuristic warnings | **13 files, 0 findings — GitHub Actions run 45102487210** |
| **Python analyzer regression CI** | Correctness of the independent Unity-pattern checking script | **35/35 PASS, 98.1% Python line coverage — same CI run** |
| **Repository validation CI** | Unity `.meta` consistency, required files, JSON/asmdef checks, generated-output hygiene | **Passing workflow confirmed** |

The **29 Unity tests** and the **35 Python analyzer tests** are separate test suites. Neither number represents test cases run inside the other environment.

### Quality engineering highlights

- **Negative paths and boundaries:** 13 additional Edit Mode cases introduced in [RUN-007](Docs/TEST_EXECUTION_REPORT_RUN-007.md), covering invalid health amounts, zero operations, damage after death, large healing values, and checkpoint edge cases.
- **Regression investigation:** [RUN-006](Docs/TEST_EXECUTION_REPORT_RUN-006.md) records an initial **4/7** Play Mode result and subsequent **7/7** success after adjusting scene loading/teardown. Both outcomes are retained for transparency.
- **Unity-focused static checks:** Five advisory rules (`UNITY001`–`UNITY005`) detect legacy searches, risky direct component access, and potentially costly frame-loop lookups. False-positive reduction is covered by analyzer regression tests.
- **Evidence-first reporting:** GitHub Actions produces `QA_SUMMARY.md`, `coverage.xml`, syntax logs, Unity pattern logs, and test logs as downloadable artifacts, without a Unity license.

## Evidence and execution reports

| Run | Focus | Report | Evidence |
|---|---|---|---|
| **RUN-001** | Baseline Edit Mode tests | [Report](Docs/TEST_EXECUTION_REPORT_RUN-001.md) | [Screenshot](Evidence/RUN-001.png) |
| **RUN-002** | Manual gameplay: movement, jump, collision, damage, respawn | [Report](Docs/TEST_EXECUTION_REPORT_RUN-002.md) | [Gameplay and respawn video](Evidence/RUN-002-Gameplay-Respawn.mp4) — partial visual coverage |
| **RUN-003** | Regression following damage/respawn fix | [Report](Docs/TEST_EXECUTION_REPORT_RUN-003.md) | [Console evidence](Evidence/RUN-003.png) — damage and respawn flow, not both spawn destinations |
| **RUN-004** | First three Play Mode tests | [Report](Docs/TEST_EXECUTION_REPORT_RUN-004.md) | [Screenshot](Evidence/RUN-004.png) |
| **RUN-005** | Physics-trigger test expansion | [Report](Docs/TEST_EXECUTION_REPORT_RUN-005.md) | [Screenshot](Evidence/RUN-005.png) |
| **RUN-006** | Full-scene integration and retest | [Report](Docs/TEST_EXECUTION_REPORT_RUN-006.md) | [Screenshot](Evidence/RUN-006.png) |
| **RUN-007** | Negative cases and complete regression | [Report](Docs/TEST_EXECUTION_REPORT_RUN-007.md) | [Evidence 1](Evidence/RUN-007(1).png) · [Evidence 2](Evidence/RUN-007(2).png) |

**Evidence limitations:** RUN-007 screenshots establish the displayed **22/22 Edit Mode** and **7/7 Play Mode** results, but do not show the exact test-time Git commit or a clean working tree. The RUN-002 video includes the damage/health restoration sequence; formal movement, collision, double-jump, and distinct initial/checkpoint respawn observations remain tester-reported unless separately recorded.

## GitHub Actions — what runs without Unity

| Workflow | Scope | Licensing |
|---|---|---|
| [Repository Validation](.github/workflows/repository-validation.yml) | Required project structure, asset metadata, JSON and assembly definitions | **No Unity license required** |
| [C# Static Analysis](.github/workflows/csharp-static-analysis.yml) | C# syntax, advisory Unity code rules, 35 Python regression tests, Python coverage gate (≥85%), QA report artifact | **No Unity license required** |
| [Unity QA Tests](.github/workflows/unity-tests.yml) | Scaffold for hosted Edit Mode and Play Mode Unity testing | **Not enabled/verified; authorized CI licensing required** |

**Verified CI evidence:** [run 45102487210](https://github.com/ornellasdev/unity-qa-sandbox/actions/runs/45102487210) passed with **35/35** Python tests and **98.1%** analyzer coverage (**156/159** executable Python lines). It scanned **13** C# files and reported **zero** syntax errors, style warnings, and Unity-pattern findings. The Node.js 24-compatible artifact upload also completed without the prior deprecation warning.

[Static QA artifact guide](Docs/STATIC_QA_REPORTS.md) · [C# analysis guide](Docs/CSHARP_STATIC_ANALYSIS.md) · [Unity rule reference](Docs/UNITY_CODE_QUALITY.md) · [Unity CI setup](Docs/CI_SETUP.md)

## Technology

- **Engine:** Unity 6.6, project editor version `6000.6.10f1`
- **Gameplay language:** C#
- **Unity tests:** NUnit, Unity Test Framework, Edit Mode, Play Mode and `[UnityTest]`
- **CI / QA utilities:** GitHub Actions, Python 3.12, Tree-sitter C#, `coverage.py`
- **Development and testing:** CachyOS Linux, Unity Editor, Git and GitHub

## Run the project and tests locally

```bash
git clone https://github.com/ornellasdev/unity-qa-sandbox.git
```

1. Open the repository in **Unity Hub** using editor **6000.6.10f1**, when available.
2. Allow packages to import. This project uses the legacy Input Manager; use **Active Input Handling → Both** or **Input Manager (Old)** if necessary.
3. Open `Assets/Scenes/QASandbox.unity`; press **Play** to test movement, damage and checkpoints.
4. Open **Window → General → Test Runner**. Run **EditMode** and **PlayMode** separately. The current defined suites contain **22 Edit Mode** and **7 Play Mode** tests.
5. Run license-free checks from the repository root:

```bash
python3 scripts/validate_unity_repo.py
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r scripts/csharp-static-requirements.txt
python scripts/check_csharp.py
python scripts/check_unity_patterns.py
python -m unittest discover -s scripts -p 'test_unity_patterns.py' -v
```

The Play Mode full-scene check relies on Unity Editor scene loading. Hosted Unity Test Runner execution remains separate from the license-free CI workflows.

## Repository structure

```text
Assets/
  Scenes/QASandbox.unity
  Scripts/
  Tests/EditMode/
  Tests/PlayMode/Tests/
Docs/
  TEST_PLAN.md
  TEST_EXECUTION_REPORT_RUN-001.md ... RUN-008.md
  STATIC_QA_REPORTS.md
  UNITY_CODE_QUALITY.md
Evidence/
  RUN-002-Gameplay-Respawn.mp4
  RUN-007(1).png
  RUN-007(2).png
  (earlier RUN screenshots)
scripts/
  check_csharp.py
  check_unity_patterns.py
  test_unity_patterns.py
  validate_unity_repo.py
  build_qa_report.py
.github/workflows/
  repository-validation.yml
  csharp-static-analysis.yml
  unity-tests.yml
```

## QA execution traceability

To capture precise **test-time** Git, Unity Editor and environment metadata for future local runs, use [the traceability guide](Docs/TEST_TRACEABILITY.md) and [snapshot script](scripts/capture_qa_environment.py). Generate **before and after** records, capture Test Runner evidence, and document any dirty working tree. Earlier runs retain their historical limitations; a current commit cannot be assumed to be the tested revision.

## Roadmap

**Delivered**
- [x] Playable 3D Unity prototype and committed scene.
- [x] Health, checkpoint, damage and respawn components.
- [x] **RUN-007: 29/29 locally executed Unity tests passed**, including 13 new negative-path/boundary tests.
- [x] **RUN-008: 29/29 Unity Test Runner tests passed again locally** (22 Edit Mode + 7 Play Mode, screenshots reviewed; [report](Docs/TEST_EXECUTION_REPORT_RUN-008.md)); before-snapshot captured on commit `4b1b839`, but final traceability evidence is still pending.
- [x] Evidence-backed manual QA reports, gameplay video, and screenshot collection.
- [x] License-free repository and C# analysis workflows.
- [x] **35 Python analyzer tests, 98.1% coverage**, automated QA artifacts and ≥85% coverage threshold.
- [x] Node.js 24-compatible GitHub Actions dependencies in the active static pipelines.

**Next**
- [ ] Capture additional RUN-002 manual video evidence for collision, double-jump prevention, and separately identified respawn paths.
- [x] Publish supplemental RUN-003 Console evidence ([RUN-003.png](Evidence/RUN-003.png)); damage, health reset, and respawn shown.
- [ ] Capture distinct RUN-003 spawn-destination evidence and record full test-time environment/commit metadata on future Unity executions.
- [x] Publish a before/after QA environment snapshot script and traceability checklist ([guide](Docs/TEST_TRACEABILITY.md)).
- [x] Capture RUN-008 before-test environment metadata with the new script (working tree DIRTY).
- [ ] Rerun RUN-008 after-test snapshot following the actual tests; upload both snapshots and two Test Runner screenshots.
- [ ] Review the locally modified `ProjectSettings/ProjectSettings.asset` before deciding whether to commit or restore it.
- [ ] Extend negative-path coverage and maintain defect/regression records.
- [ ] Enable Unity hosted Edit Mode/Play Mode CI **only when an authorized Unity CI licensing setup exists**, then archive actual NUnit XML results.

## Contact

**Yuri Ornellas** · [GitHub](https://github.com/ornellasdev) · [LinkedIn](https://www.linkedin.com/in/yurivillarornelas/) · [Email](mailto:yurivillarornelas@live.com)

*This is a personal learning and recruitment portfolio. Local Unity test results and Python-based GitHub Actions metrics are documented separately; they do not imply paid studio QA experience or hosted Unity test execution.*
