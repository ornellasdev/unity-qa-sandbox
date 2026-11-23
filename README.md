# Unity QA Sandbox 🎮🧪

An original **Unity 6 + C#** game prototype and technical QA portfolio by **Yuri Ornellas**.

**Status:** Game prototype source published. The Edit Mode NUnit suite passed **9/9** in the tester's Unity Test Runner on **2026-11-22**, with [screenshot evidence](Evidence/RUN-001.png). Manual gameplay RUN-002 has **8 tester-reported passing checks**, including health restoration to 100 both with and without an activated checkpoint. The corrected gameplay scripts were published in commit [`9406fca`](https://github.com/ornellasdev/unity-qa-sandbox/commit/9406fca3d6fd94abf6375a7043eed573f613af94); the exact prior test revision and repository-hosted RUN-002 evidence remain pending.

## Features
- Graybox scene generator: **Tools > QA Sandbox > Create Demo Scene**
- WASD / arrow-key movement, Space to jump, gravity, collision
- Health, hazards, checkpoints and respawn
- **9 NUnit Edit Mode tests** of gameplay models
- **3 Unity Play Mode component tests** covering damage, death/health restoration, and checkpoint position
- **3 additional physics-driven Play Mode tests** for trigger-entry damage, lethal respawn, and checkpoint-trigger recovery (**6/6 Play Mode tests passed in RUN-005; screenshot reviewed in chat**)
- English test plans and execution reports

## Setup
1. Open the complete Unity project using **Unity 6.6 (6000.6.10f1)** (the editor version used by the tester).
2. Set **Active Input Handling** to **Both** or **Input Manager (Old)** under Project Settings > Player if necessary.
3. Open `Assets/Scenes/QASandbox.unity`; generate via **Tools > QA Sandbox > Create Demo Scene** if it does not exist.
4. Press **Play** and test movement, jump, collisions, hazard and checkpoint.
5. Open **Window > General > Test Runner**, choose **Edit Mode**, then **Run All**.

## Test status

| Coverage | Type | Status |
|---|---|---|
| Health logic (7 methods) | NUnit Edit Mode | ✅ 7/7 Passed — screenshot reviewed |
| Checkpoint logic (2 methods) | NUnit Edit Mode | ✅ 2/2 Passed — screenshot reviewed |
| Gameplay components (3 methods) | Unity Play Mode | ✅ 3/3 Passed — RUN-004 screenshot published |
| Physics trigger interactions (3 methods) | Unity Play Mode | ✅ 3/3 Passed — RUN-005 screenshot reviewed in chat; repository upload pending |
| WASD movement, jump, collision, checkpoint respawn, airborne double-jump prevention, initial-spawn respawn | Manual | ✅ 6 observed checks passed — tester reported |
| Full-health restoration at initial spawn and activated checkpoint | Manual | ✅ 2 scenarios passed — tester reported; Console screenshot reviewed in chat |

**Automated Edit Mode result:** 9 passed, 0 failed (100%) in RUN-001. **RUN-002:** Eight gameplay observations passed. **RUN-003 regression (tester-reported against fix `9406fca`):** initial respawn PASS, checkpoint respawn PASS, Edit Mode 9/9 PASS. Evidence and clean working tree confirmation for RUN-003 remain pending.

**Total distinct automated test methods reported passed across Edit Mode and Play Mode: 15 (9 + 6)**. Tests were run locally, not in CI.

🖼️ [Test Runner evidence](Evidence/RUN-001.png) · 📄 [RUN-001 automated report](Docs/TEST_EXECUTION_REPORT_RUN-001.md) · [RUN-002 manual report](Docs/TEST_EXECUTION_REPORT_RUN-002.md) · [RUN-003 regression report](Docs/TEST_EXECUTION_REPORT_RUN-003.md) · [RUN-004 Play Mode report](Docs/TEST_EXECUTION_REPORT_RUN-004.md) · [RUN-005 physics integration report](Docs/TEST_EXECUTION_REPORT_RUN-005.md) · [Manual test plan](Docs/TEST_PLAN.md) · [Bug report template](Docs/BUG_REPORT_TEMPLATE.md)

> RUN-001 has screenshot evidence of local Unity Test Runner results, not independent CI validation. RUN-002 is based on tester-reported manual observations, with Console screenshot reviewed in chat but not yet uploaded to the repository. Environment: **CachyOS (Linux)** and **Unity 6.6 (6000.6.10f1)**; exact tested commit is not recorded.

## Roadmap
- [x] Gameplay components and automated tests authored
- [x] First Edit Mode execution: 9/9 passed with screenshot evidence
- [x] Test environment recorded: CachyOS Linux / Unity 6.6 (6000.6.10f1)
- [x] Eight manual gameplay checks reported as passing in RUN-002, including both health restoration scenarios
- [x] Publish trigger/respawn fix: `9406fca`
- [x] Tester-reported regression RUN-003 on fix commit `9406fca`: 3/3 checks passed
- [ ] Confirm clean working tree and attach new RUN-003 evidence
- [ ] Upload RUN-002 Console/gameplay evidence to the repository
- [x] Add and locally run three gameplay-component Play Mode tests, published in `3f602ea`
- [x] Upload RUN-004 screenshot to the repository
- [x] Add physics-trigger Play Mode test source (PLAY004–PLAY006)
- [x] Execute six Play Mode tests: 6/6 PASS (RUN-005 screenshot reviewed in chat)
- [ ] Upload RUN-005 screenshot to GitHub and record exact tested commit
- [ ] Add CI for Unity test suites

**Author:** [Yuri Ornellas](https://github.com/ornellasdev) · [LinkedIn](https://www.linkedin.com/in/yurivillarornelas/)
