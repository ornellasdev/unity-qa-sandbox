# Unity QA Sandbox 🎮🧪

An original **Unity 6 + C#** game prototype and technical QA portfolio by **Yuri Ornellas**.

**Status:** Gameplay and test source published. First Edit Mode suite **reported as 9/9 passed** by the tester on **2026-11-22**; Test Runner screenshot and remaining environment metadata pending. Manual gameplay testing has not yet been reported.

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
| Health logic (7 test methods) | NUnit Edit Mode | ✅ 7/7 Passed — tester reported |
| Checkpoint logic (2 test methods) | NUnit Edit Mode | ✅ 2/2 Passed — tester reported |
| Movement, jump, collision, triggers, respawn | Manual | Not Run / not reported |

**Automated Edit Mode result: 9 passed, 0 failed (100%).**

📄 [Test Execution Report — RUN-001](Docs/TEST_EXECUTION_REPORT_RUN-001.md) · [Manual test plan](Docs/TEST_PLAN.md) · [Bug report template](Docs/BUG_REPORT_TEMPLATE.md)

> These are self-reported local Unity Test Runner results. Test Runner screenshot and CI validation are pending. Unity version: **6.6 (6000.6.10f1)**, confirmed by the tester's About Unity screenshot. Do not interpret unit test passes as proof of complete gameplay validation.

## Roadmap
- [x] Gameplay components and test source authored
- [x] Nine NUnit Edit Mode test methods authored
- [x] First Edit Mode execution reported: 9/9 pass
- [x] Confirm Unity Editor version: 6.6 (6000.6.10f1)
- [ ] Capture Test Runner screenshot and remaining environment details
- [ ] Run manual test cases and report observed defects
- [ ] Add Play Mode tests and CI

**Author:** [Yuri Ornellas](https://github.com/ornellasdev) · [LinkedIn](https://www.linkedin.com/in/yurivillarornelas/)
