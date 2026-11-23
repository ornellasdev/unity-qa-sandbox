# Play Mode Full Scene Regression — RUN-006 (Initial Attempt)

**Status: FAILED — awaiting rerun after test isolation fix**

## Context

- Tester: Yuri Ornellas
- Environment previously confirmed: CachyOS (Linux), Unity 6.6 (6000.6.10f1)
- Source: exported NUnit XML supplied by the tester (`TestResults_20261122_213050.xml`) and screenshot of Unity Test Runner
- Execution time from XML: **2026-11-23 00:30:35–00:30:37 UTC** (2026-11-22 local in Brazil)
- Test mode: Unity Play Mode
- Exact working-tree commit at execution: **Not recorded**
- Repository-hosted screenshot/XML: **Pending**

## Results

| Test | Outcome |
|---|---|
| PLAY001_DamageReducesHealth | PASS |
| PLAY002_DeathRestoresFullHealth | PASS |
| PLAY003_CheckpointChangesRespawnPosition | PASS |
| PLAY004_PhysicalDamageTriggerReducesHealth | FAIL — expected 75 HP, observed 100 |
| PLAY005_PhysicalLethalTriggerCausesRespawn | FAIL — respawn not observed |
| PLAY006_PhysicalCheckpointThenHazardUsesCheckpointSpawn | FAIL — checkpoint respawn not observed |
| PLAY007_FullSceneLoadsAndHasRequiredGameplayComponents | PASS |

**Total: 4 passed, 3 failed, 7 executed.**

## Investigation

PLAY007 was using `EditorSceneManager.LoadSceneInPlayMode` with `LoadSceneMode.Single`. This replaces the active scene and may interfere with subsequent Play Mode tests. An isolation change has been published that loads the QASandbox scene additively and unloads it with `[UnityTearDown]`.

**Hypothesis, not confirmed root cause:** scene isolation caused the three previously passing physical trigger tests to regress when run in the full suite.

- Isolation change commit: [`ea2b38a`](https://github.com/ornellasdev/unity-qa-sandbox/commit/ea2b38a642eba626b4451507bf405a856b9f0015)
- The amended code has **not yet been recompiled or rerun** by the tester.
- Do not label RUN-006 as passed until a new seven-test execution is captured.

## Pending

- [ ] Pull the isolation change and rerun all seven Play Mode tests
- [ ] Capture Test Runner screenshot and exported XML
- [ ] Investigate remaining failures, if any
- [ ] Record tested commit and working tree state

## Related

- [RUN-005 — last successful six-test Play Mode suite](TEST_EXECUTION_REPORT_RUN-005.md)
