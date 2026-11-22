# Unity QA Sandbox 🎮🧪

An original **Unity 6 + C#** game prototype and technical QA portfolio by **Yuri Ornellas**.

**Status:** Game prototype source published. The Edit Mode NUnit suite passed **9/9** in the tester's Unity Test Runner on **2026-11-22**, with [screenshot evidence](Evidence/RUN-001.png). Manual gameplay RUN-002 has **8 tester-reported passing checks**, including health restoration to 100 both with and without an activated checkpoint. The corrected gameplay scripts were published in commit [`9406fca`](https://github.com/ornellasdev/unity-qa-sandbox/commit/9406fca3d6fd94abf6375a7043eed573f613af94); the exact prior test revision and repository-hosted RUN-002 evidence remain pending.

## Features
- Graybox scene generator: **Tools > QA Sandbox > Create Demo Scene**
- WASD / arrow-key movement, Space to jump, gravity, collision
- Health, hazards, checkpoints and respawn
- **9 NUnit Edit Mode tests** of gameplay models
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
| WASD movement, jump, collision, checkpoint respawn, airborne double-jump prevention, initial-spawn respawn | Manual | ✅ 6 observed checks passed — tester reported |
| Full-health restoration at initial spawn and activated checkpoint | Manual | ✅ 2 scenarios passed — tester reported; Console screenshot reviewed in chat |

**Automated Edit Mode result:** 9 passed, 0 failed (100%). **RUN-002:** Eight observed checks passed; original locally edited gameplay code still needs to be committed and linked to a tested revision.

🖼️ [Test Runner evidence](Evidence/RUN-001.png) · 📄 [RUN-001 automated report](Docs/TEST_EXECUTION_REPORT_RUN-001.md) · [RUN-002 manual report](Docs/TEST_EXECUTION_REPORT_RUN-002.md) · [Manual test plan](Docs/TEST_PLAN.md) · [Bug report template](Docs/BUG_REPORT_TEMPLATE.md)

> RUN-001 has screenshot evidence of local Unity Test Runner results, not independent CI validation. RUN-002 is based on tester-reported manual observations, with Console screenshot reviewed in chat but not yet uploaded to the repository. Environment: **CachyOS (Linux)** and **Unity 6.6 (6000.6.10f1)**; exact tested commit is not recorded.

## Roadmap
- [x] Gameplay components and automated tests authored
- [x] First Edit Mode execution: 9/9 passed with screenshot evidence
- [x] Test environment recorded: CachyOS Linux / Unity 6.6 (6000.6.10f1)
- [x] Eight manual gameplay checks reported as passing in RUN-002, including both health restoration scenarios
- [x] Publish trigger/respawn fix: `9406fca`
- [ ] Recheck the committed version and record its test commit
- [ ] Upload RUN-002 Console/gameplay evidence to the repository
- [ ] Add Play Mode integration tests and CI

**Author:** [Yuri Ornellas](https://github.com/ornellasdev) · [LinkedIn](https://www.linkedin.com/in/yurivillarornelas/)
