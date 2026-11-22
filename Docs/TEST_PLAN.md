# Manual QA test plan

**Manual gameplay execution status: IN PROGRESS.** Four basic behaviors were reported passing on 2026-11-22; see [RUN-002](TEST_EXECUTION_REPORT_RUN-002.md).

The automated suites for UNITY-005 and UNITY-006 were reported as passed on 2026-11-22. See [RUN-001](TEST_EXECUTION_REPORT_RUN-001.md). They do not substitute for manual gameplay testing.

| Case | Action | Expected result | Status |
|---|---|---|---|
| UNITY-001 | Move with WASD; walk into obstacles | Player moves and cannot pass through solids | PASS — tester reported |
| UNITY-002 | Jump grounded, then mid-air | Jump when grounded; no unintended double-jump | PARTIAL — basic jump passed; mid-air attempt pending |
| UNITY-003 | Enter red hazard from start | Full damage results in respawn at initial location | Not Run / not confirmed |
| UNITY-004 | Enter green checkpoint, then red hazard | Player respawns at checkpoint with full health | PARTIAL — checkpoint respawn location passed; full health pending |
| UNITY-005 | Run HealthModel NUnit suite | Health boundaries, resets, invalid inputs behave as intended | 7/7 Passed — tester reported |
| UNITY-006 | Run CheckpointModel NUnit suite | Latest checkpoint is stored | 2/2 Passed — tester reported |

Record device, Unity version, environment, exact steps, expected/actual, evidence, and any reproducible bug IDs. Do not fabricate results.
