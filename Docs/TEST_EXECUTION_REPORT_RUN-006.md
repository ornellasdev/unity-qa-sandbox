# Play Mode Full Scene Regression — RUN-006

**Current status: RETEST PASSED (7/7); initial attempt FAILED (4/7).**

## Retest after scene-isolation fix

The tester provided a new Unity Test Runner screenshot showing **7 passed, 0 failed, 0 other** in Play Mode. It includes all three test suites:

- `FullSceneIntegrationTests`: 1 passed (PLAY007)
- `PhysicalTriggerTests`: 3 passed (PLAY004–PLAY006)
- `PlayerGameplayTests`: 3 passed (PLAY001–PLAY003)

**Retest result: 7/7 PASS (100%)**, screenshot reviewed in chat. The screenshot has not yet been uploaded to the repository. The retest followed a successful local pull containing the additive scene-loading correction; exact working-tree revision at execution and the effect of the local `ProjectSettings/ProjectSettings.asset` modification remain unverified. This result does not establish CI validation or independently prove that scene loading was the sole root cause.

## Initial failed attempt

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
- The amended code was subsequently run by the tester, yielding 7/7 passing results as documented above.
- The proposed root cause remains a hypothesis; the successful rerun establishes that the suite passes in the retested environment.

## Pending

- [x] Pull the isolation change and rerun all seven Play Mode tests — 7/7 PASS
- [x] Review new Test Runner screenshot in chat
- [ ] Upload retest screenshot to `Evidence/RUN-006.png`
- [ ] Export retest XML, if desired
- [ ] Record exact tested commit and working tree state

## Related

- [RUN-005 — last successful six-test Play Mode suite](TEST_EXECUTION_REPORT_RUN-005.md)
