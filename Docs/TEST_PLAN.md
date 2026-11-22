# Manual QA test plan

**Manual gameplay execution status: IN PROGRESS.** Six individual gameplay checks reported passing on 2026-11-22; health restoration remains pending. See [RUN-002](TEST_EXECUTION_REPORT_RUN-002.md).

Automated NUnit results are documented separately in [RUN-001](TEST_EXECUTION_REPORT_RUN-001.md); those results do not substitute for manual gameplay validation.

| Case | Action | Expected result | Status |
|---|---|---|---|
| UNITY-001 | Move with WASD; walk into obstacles | Player moves and cannot pass through solids | PASS — tester reported |
| UNITY-002 | Jump grounded, then attempt a second jump mid-air | Character jumps from ground, without unintended double-jump | PASS — tester reported |
| UNITY-003 | Enter red hazard before activating checkpoint | Respawn at initial location with full health | PARTIAL — initial-location respawn PASS; health pending |
| UNITY-004 | Activate green checkpoint, then enter red hazard | Respawn at checkpoint with full health | PARTIAL — checkpoint-location respawn PASS; health pending |
| UNITY-005 | Run HealthModel NUnit suite | Health boundaries, resets, invalid inputs behave as intended | 7/7 Passed — Test Runner screenshot |
| UNITY-006 | Run CheckpointModel NUnit suite | Latest checkpoint is stored | 2/2 Passed — Test Runner screenshot |

Record environment, exact tested commit, reproduction steps, actual observations, evidence and any defect IDs. Do not infer an unobserved result.
