# Unity QA Sandbox 🎮🧪

**Original Unity 6 gameplay prototype + Technical Game QA portfolio**  
By [Yuri Ornellas](https://github.com/ornellasdev)

[![Unity](https://img.shields.io/badge/Unity-6.6-222?logo=unity)](https://unity.com/)
![C#](https://img.shields.io/badge/Code-C%23-512BD4)
![QA](https://img.shields.io/badge/QA-Manual%20%2B%20Automated-blue)
![CI](https://img.shields.io/badge/CI-Workflow%20configured%20%7C%20not%20validated-yellow)

This repository demonstrates an **original, playable graybox prototype** alongside manual test cases, C# NUnit tests, physics-trigger integration checks, a serialized-scene test, regression investigations, and documented local test runs.

> **Current result:** **16 distinct automated test methods passed locally** — 9 Edit Mode + 7 Play Mode. These results were observed in Unity Test Runner; **CI workflow is published but has not completed a verified run**.

## 🎯 Gameplay prototype

- WASD/arrow-key movement and Space to jump
- Collidable obstacles and floor
- Damage trigger and player health
- Checkpoint activation and respawn
- Editor tool to create a demo scene, plus the committed scene at `Assets/Scenes/QASandbox.unity`

## 🧪 Test coverage

| Suite | Coverage | Latest documented result |
|---|---|---|
| **Edit Mode / NUnit** | Health model (7), checkpoint model (2) | **9/9 PASS** — RUN-001; reconfirmed by tester in RUN-003 |
| **Play Mode / components** | Direct damage, lethal damage/respawn, checkpoint position (PLAY001–003) | **3/3 PASS** within RUN-006 retest |
| **Play Mode / physics** | Trigger damage, trigger-driven respawn, checkpoint followed by hazard (PLAY004–006) | **3/3 PASS** within RUN-006 retest |
| **Play Mode / full scene** | Required QASandbox objects, colliders, scripts and scene configuration (PLAY007) | **1/1 PASS** within RUN-006 retest |
| **Manual functional QA** | Movement, jump/double-jump prevention, collision, initial respawn, checkpoint respawn and health restoration | **4/4 formal cases reported PASS** — RUN-002 |

**Important:** The RUN-006 first attempt reported **4 passed / 3 failed**. After changing scene loading to **Additive** with teardown, the subsequent local retest reported **7 passed / 0 failed**. The suspected scene-isolation cause was not independently proven; both the failure and successful retest are preserved in the report.

## 📸 Evidence and reports

| Run | Purpose | Documentation | Screenshot |
|---|---|---|---|
| RUN-001 | Edit Mode baseline | [Report](Docs/TEST_EXECUTION_REPORT_RUN-001.md) | [RUN-001.png](Evidence/RUN-001.png) |
| RUN-002 | Manual gameplay | [Report](Docs/TEST_EXECUTION_REPORT_RUN-002.md) | Not yet uploaded |
| RUN-003 | Regression after damage/respawn fix | [Report](Docs/TEST_EXECUTION_REPORT_RUN-003.md) | Not yet uploaded |
| RUN-004 | First 3 Play Mode tests | [Report](Docs/TEST_EXECUTION_REPORT_RUN-004.md) | [RUN-004.png](Evidence/RUN-004.png) |
| RUN-005 | 6 Play Mode tests, including physics triggers | [Report](Docs/TEST_EXECUTION_REPORT_RUN-005.md) | [RUN-005.png](Evidence/RUN-005.png) |
| RUN-006 | Full-scene test + failure investigation + retest | [Report](Docs/TEST_EXECUTION_REPORT_RUN-006.md) | [RUN-006.png](Evidence/RUN-006.png) |

All passing test results listed above are from **local tester executions**, not GitHub Actions. The CI workflow is present but awaits license setup and its first verified run. Some earlier runs lack a precisely recorded clean checkout or full environment metadata.

## 🛠️ Tech stack

- **Engine:** Unity 6.6 (6000.6.10f1)
- **Language:** C#
- **Testing:** Unity Test Framework, NUnit, `[UnityTest]`, `CharacterController`, trigger colliders
- **Development/testing OS:** CachyOS (Linux)
- **Version control:** Git + GitHub

## ▶️ Open and run

1. Clone the repository:
   ```bash
   git clone https://github.com/ornellasdev/unity-qa-sandbox.git
   ```
2. Open the cloned folder in **Unity Hub**, using Unity **6000.6.10f1** when possible.
3. Allow package import/compilation to finish. This project's movement code uses the legacy Input Manager API; set **Active Input Handling** to **Both** or **Input Manager (Old)** if necessary.
4. Open `Assets/Scenes/QASandbox.unity`, then press **Play**.
5. Open **Window → General → Test Runner** and run **EditMode** and **PlayMode** separately.

The Play Mode full-scene check uses Editor-only scene loading; it is intended for the Unity Editor Test Runner, not a player build.

## 📂 Key folders

```text
Assets/
  Scenes/QASandbox.unity
  Scripts/
  Tests/
    EditMode/
    PlayMode/Tests/
Docs/
  TEST_PLAN.md
  BUG_REPORT_TEMPLATE.md
  TEST_EXECUTION_REPORT_RUN-001.md ... RUN-006.md
Evidence/
  RUN-001.png
  RUN-004.png
  RUN-005.png
  RUN-006.png
```

## 🤖 Continuous integration

The [Unity QA Tests workflow](.github/workflows/unity-tests.yml) is now configured for **Edit Mode** and **Play Mode**, using GameCI on an Ubuntu runner. It is **not yet verified as passing in GitHub Actions**. To run it, configure Unity licensing secrets and follow the [CI setup guide](Docs/CI_SETUP.md). Automatic runs remain gated until `UNITY_CI_ENABLED=true` is set.

## 🗺️ Roadmap

### Completed
- [x] Build original gameplay prototype and commit the scene
- [x] Implement gameplay health, damage, checkpoint and respawn systems
- [x] Execute **9 Edit Mode** NUnit tests
- [x] Execute and document **4 manual functional QA cases**
- [x] Investigate and publish the damage/respawn fix ([`9406fca`](https://github.com/ornellasdev/unity-qa-sandbox/commit/9406fca3d6fd94abf6375a7043eed573f613af94))
- [x] Implement **7 Play Mode** tests: components, real triggers and serialized-scene validation
- [x] Document the RUN-006 failed attempt and successful **7/7** retest
- [x] Upload evidence for RUN-001, RUN-004, RUN-005 and RUN-006

### Next milestones
- [ ] Add RUN-002 manual gameplay evidence and RUN-003 regression evidence
- [ ] Record reproducible build/commit and clean-worktree details for future executions
- [ ] Evaluate and reconcile Unity `ProjectSettings` differences across environments
- [x] Publish gated GitHub Actions workflow for Unity **Edit Mode + Play Mode** ([workflow](.github/workflows/unity-tests.yml), [setup instructions](Docs/CI_SETUP.md))
- [ ] Configure required Unity license secrets privately in GitHub Actions
- [ ] Verify a successful manual CI run (9 Edit Mode + 7 Play Mode)
- [ ] Enable automatic push checks with the `UNITY_CI_ENABLED=true` repository variable
- [ ] Collect and link CI XML/log artifacts after the workflow successfully runs
- [ ] Extend functional and negative-path coverage; track any newly reproduced bugs

## 📫 Contact

[GitHub](https://github.com/ornellasdev) · [LinkedIn](https://www.linkedin.com/in/yurivillarornelas/) · [Email](mailto:yurivillarornelas@live.com)

*Built as a learning and recruitment portfolio. This is personal project experience, not paid studio QA experience.*
