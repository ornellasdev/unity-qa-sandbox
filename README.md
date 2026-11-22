# Unity QA Sandbox 🎮🧪

An original **Unity 6 + C#** game prototype and technical QA portfolio by **Yuri Ornellas**.

**Status:** Gameplay and test source published. First Edit Mode suite **9/9 passed, supported by tester-provided Test Runner screenshot** on **2026-11-22**; screenshot uploaded to the repository; tested commit and CachyOS release details pending. Initial manual gameplay observations have been recorded in RUN-002; remaining formal assertions are pending.

## Features
- 3D graybox demo scene generated using **Tools > QA Sandbox > Create Demo Scene**
- WASD / arrow-key movement, Space to jump, gravity, collision
- Health, hazards, checkpoints and respawn
- Pure, testable gameplay logic and **9 NUnit Edit Mode tests**
- English QA test plan and bug-report template

## Setup
1. Create a **new Unity 6 3D Core project** in Unity Hub.
2. Copy this repository's `Assets/` folder into the project.
3. Install **Test Framework** via Package Manager, if needed.
4. Set **Active Input Handling** to **Both** or **Input Manager (Old)** in Project Settings > Player. Restart Unity if prompted.
5. Select **Tools > QA Sandbox > Create Demo Scene**; a scene is generated at `Assets/Scenes/QASandbox.unity`.
6. Press **Play**. Walk into the green checkpoint, then the red damage zone.
7. Open **Window > General > Test Runner**, choose **Edit Mode**, then **Run All**.

This repository is an **Assets scaffold**, not an entire serialized Unity project. The scene must be generated in the Editor first.

## Test status

| Coverage | Type | Reported status |
|---|---|---|
| Health logic (7 test methods) | NUnit Edit Mode | ✅ 7/7 Passed — screenshot reviewed |
| Checkpoint logic (2 test methods) | NUnit Edit Mode | ✅ 2/2 Passed — screenshot reviewed |
| WASD movement, basic jump, obstacle collision, checkpoint respawn location | Manual | ✅ 4/4 observed behaviors passed — tester reported |
| Airborne re-jump, initial-spawn hazard, health restoration | Manual | Pending |

**Automated Edit Mode result: 9 passed, 0 failed (100%).**

🖼️ [Test Runner evidence](Evidence/RUN-001.png) · 📄 [RUN-001 automated report](Docs/TEST_EXECUTION_REPORT_RUN-001.md) · [RUN-002 manual report](Docs/TEST_EXECUTION_REPORT_RUN-002.md) · [Manual test plan](Docs/TEST_PLAN.md) · [Bug report template](Docs/BUG_REPORT_TEMPLATE.md)

> The Test Runner screenshot has been visually reviewed in chat (9 passing tests, 0 failures); the image is now available in this repository; independent CI validation is pending. OS: **CachyOS (Linux)**. Unity version: **6.6 (6000.6.10f1)**, confirmed by the tester's About Unity screenshot. Do not interpret unit test passes as proof of complete gameplay validation.

## Roadmap
- [x] Gameplay components and test source authored
- [x] Nine NUnit Edit Mode test methods authored
- [x] First Edit Mode execution reported: 9/9 pass
- [x] Confirm Unity Editor version: 6.6 (6000.6.10f1)
- [x] Review Test Runner screenshot (9 passed, 0 failed)
- [x] Upload Test Runner screenshot to `Evidence/RUN-001.png`
- [x] Record test operating system: CachyOS (Linux)
- [ ] Record tested commit and optional CachyOS release/kernel
- [x] Record four passing basic gameplay observations in RUN-002
- [ ] Finish all formal manual test assertions and capture evidence
- [ ] Add Play Mode tests and CI

**Author:** [Yuri Ornellas](https://github.com/ornellasdev) · [LinkedIn](https://www.linkedin.com/in/yurivillarornelas/)
