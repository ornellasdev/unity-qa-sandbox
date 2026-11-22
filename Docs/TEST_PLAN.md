# Manual QA test plan

**Manual gameplay execution status: PASS (tester-reported), with version/evidence follow-up pending.** Eight individual gameplay checks were reported passing on 2026-11-22, including health restoration in both respawn scenarios. See [RUN-002](TEST_EXECUTION_REPORT_RUN-002.md).

Automated NUnit results are documented separately in [RUN-001](TEST_EXECUTION_REPORT_RUN-001.md); those results do not substitute for manual gameplay validation.

| Case | Action | Expected result | Status |
|---|---|---|---|
| UNITY-001 | Move with WASD; walk into obstacles | Player moves and cannot pass through solids | PASS — tester reported |
| UNITY-002 | Jump grounded, then attempt a second jump mid-air | Character jumps from ground, without unintended double-jump | PASS — tester reported |
| UNITY-003 | Enter red hazard before activating checkpoint | Respawn at initial location with full health | PASS — tester reported (health 100) |
| UNITY-004 | Activate green checkpoint, then enter red hazard | Respawn at checkpoint with full health | PASS — tester reported (health 100) |
| UNITY-005 | Run HealthModel NUnit suite | Health boundaries, resets, invalid inputs behave as intended | 7/7 Passed — Test Runner screenshot |
| UNITY-006 | Run CheckpointModel NUnit suite | Latest checkpoint is stored | 2/2 Passed — Test Runner screenshot |

The trigger/respawn fix is published in commit [`9406fca`](https://github.com/ornellasdev/unity-qa-sandbox/commit/9406fca3d6fd94abf6375a7043eed573f613af94). A subsequent [RUN-003 regression](TEST_EXECUTION_REPORT_RUN-003.md) was reported PASS for initial respawn, checkpoint respawn, and 9/9 Edit Mode tests. New screenshot evidence and confirmation of a clean working tree remain pending. Do not infer an unobserved result.
