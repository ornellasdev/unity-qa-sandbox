# Manual QA test plan

**Execution status for all cases: NOT RUN.**

| Case | Action | Expected result |
|---|---|---|
| UNITY-001 | Walk into obstacles | Collision prevents passing through solids |
| UNITY-002 | Jump grounded, then mid-air | Jump when grounded; no unintended double-jump |
| UNITY-003 | Enter red hazard from start | Full damage results in respawn at initial location |
| UNITY-004 | Enter green checkpoint, then red hazard | Player respawns at checkpoint with full health |
| UNITY-005 | Run HealthModel NUnit suite | Health boundaries, resets, invalid inputs behave as intended |
| UNITY-006 | Run CheckpointModel NUnit suite | Latest checkpoint is stored |

Record device, Unity version, environment, exact steps, expected/actual, evidence, and any reproducible bug IDs. Do not fabricate results.
