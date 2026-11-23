# Play Mode Physics Integration Test Report — RUN-005

## Execution summary

| Field | Value |
|---|---|
| Project | Unity QA Sandbox |
| Execution date | 2026-11-22 (Brazil local session) |
| Tester | Yuri Ornellas |
| Environment | CachyOS Linux; Unity 6.6 (6000.6.10f1), previously confirmed |
| Test runner | Unity Test Runner — Play Mode |
| Evidence | Screenshot shared in conversation, visibly showing six green checks; repository upload pending |
| Exact checked-out commit at execution | Not recorded |
| Execution | Local, not CI |

## Observed test results

| Test | Purpose | Result |
|---|---|---|
| PLAY001_DamageReducesHealth | Component damage reduction | PASS |
| PLAY002_DeathRestoresFullHealth | Death and life recovery | PASS |
| PLAY003_CheckpointChangesRespawnPosition | Checkpoint/respawn position via component calls | PASS |
| PLAY004_PhysicalDamageTriggerReducesHealth | CharacterController movement through damage trigger causes damage | PASS |
| PLAY005_PhysicalLethalTriggerCausesRespawn | Lethal physical trigger causes initial respawn and restores life | PASS |
| PLAY006_PhysicalCheckpointThenHazardUsesCheckpointSpawn | Physical checkpoint activation and subsequent hazard respawn | PASS |

**Summary: 6 passed / 0 failed / 6 executed (100%).** The Unity Test Runner screenshot displays six passing checks, zero failures and a duration around 1.124 seconds. The individual test names are truncated by the narrow UI but the suites and counts are visible.

## Coverage and boundaries

- PLAY001–PLAY003 test components directly; PLAY004–PLAY006 use physical CharacterController movement and temporary colliders.
- These tests create test objects; they do **not** load the complete QASandbox scene.
- This screenshot was inspected in the conversation, but the original image is not yet attached as `Evidence/RUN-005.png` in the repository.
- The source for PLAY004–PLAY006 is published in the repository; the commit checked out by Unity at execution time was not explicitly recorded. The screenshot alone does not prove a clean checkout or a CI run.

## Pending

- [ ] Upload `Evidence/RUN-005.png` with this Test Runner screenshot
- [ ] Record exact tested commit and confirm working-tree state at execution
- [ ] Export result XML if desired
- [ ] Add complete-scene integration coverage
- [ ] Configure CI if feasible

## Related reports

- [RUN-001 — Edit Mode](TEST_EXECUTION_REPORT_RUN-001.md)
- [RUN-004 — First Play Mode suite](TEST_EXECUTION_REPORT_RUN-004.md)
