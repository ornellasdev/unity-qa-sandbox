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

Note: trigger/respawn regression was investigated and locally modified source is not yet confirmed pushed to GitHub. Record exact tested commit, reproduction steps, actual observations, evidence and any defect IDs. Do not infer an unobserved result.
