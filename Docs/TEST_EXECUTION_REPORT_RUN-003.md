# Regression Test Execution Report — RUN-003

## Summary

This report documents **tester-reported regression results** following the damage trigger and respawn fix in [commit `9406fca`](https://github.com/ornellasdev/unity-qa-sandbox/commit/9406fca3d6fd94abf6375a7043eed573f613af94).

| Field | Value |
|---|---|
| Project | Unity QA Sandbox |
| Report date | 2026-11-22 |
| Tester | Yuri Ornellas |
| Target/source commit reported by tester | `9406fca3d6fd94abf6375a7043eed573f613af94` |
| OS | CachyOS (Linux) — previously confirmed |
| Unity version | Unity 6.6 (6000.6.10f1) — previously confirmed |
| Test method | Manual gameplay regression + local Unity Test Runner Edit Mode |
| Result source | Tester-reported execution results in conversation |
| Screenshot/log evidence for RUN-003 | Pending |
| Working tree check (subsequent snapshot) | `git status --short` showed only `?? unity-qa-sandbox/` (untracked nested folder), with no tracked-file modifications listed; exact state at test time and active Unity project path not independently verified |

## Executed checks

| ID | Scenario | Tester-reported result |
|---|---|---|
| REG-001 | Enter the red damage zone before enabling a checkpoint; respawn at initial spawn | PASS |
| REG-002 | Enable green checkpoint and enter red damage zone; respawn at checkpoint | PASS |
| REG-003 | Rerun the nine NUnit Edit Mode tests using the Unity Test Runner | PASS — 9 passed, 0 failed |

**Result: 3 of 3 regression checks reported PASS.** The nine Edit Mode tests are counted as nine test methods within REG-003, not as additional independent manual checks.

## Scope and limits

- Previous RUN-002 observations included restoration to 100 health in both respawn scenarios, with a Console screenshot shared in conversation. This RUN-003 submission confirms the two respawn scenarios and all nine NUnit tests, but does **not separately report new health values or a new screenshot**. A new numeric health-restoration assertion was **not** added to RUN-003.
- The tester identified `9406fca` as the regression target; GitHub confirms it is the commit containing the corrected `DamageZone.cs` and `PlayerRespawn.cs` files.
- The tester had previously displayed a shell prompt suggesting possible local changes. A later screenshot of `git status --short` showed only an untracked nested directory (`?? unity-qa-sandbox/`); there were no modified tracked files listed. This does **not** establish which project directory was open in Unity during RUN-003 or prove that the working tree was identical at execution time, so this report does not claim independently reproduced results on a pristine checkout.
- No CI job or automated Unity Play Mode regression execution was run or evidenced here.
- Tests beyond the three checks listed above are **not included or implicitly passed**.

## Remaining evidence/tasks

- [ ] Attach a screenshot of the RUN-003 Test Runner results
- [ ] Capture a Console/gameplay recording for both respawn cases
- [x] Review subsequent `git status --short`: no tracked changes; untracked nested `unity-qa-sandbox/` present
- [ ] Confirm Unity Editor project path and whether the nested folder contains a second project
- [ ] Record optional CachyOS release/kernel information
- [ ] Add automated Play Mode tests
- [ ] Add GitHub Actions / CI, if suitable for the Unity project

## Related records

- [RUN-001 — initial Edit Mode tests](TEST_EXECUTION_REPORT_RUN-001.md)
- [RUN-002 — manual gameplay testing](TEST_EXECUTION_REPORT_RUN-002.md)
- [Manual test plan](TEST_PLAN.md)
- [Fix commit `9406fca`](https://github.com/ornellasdev/unity-qa-sandbox/commit/9406fca3d6fd94abf6375a7043eed573f613af94)
