# Manual Gameplay Test Execution Report — RUN-002

## Execution context

| Field | Value |
|---|---|
| Project | Unity QA Sandbox |
| Execution date | 2026-11-22 |
| Executor | Yuri Ornellas |
| Platform | CachyOS (Linux) — previously confirmed test environment |
| Unity Editor | Unity 6.6 (6000.6.10f1) — previously confirmed editor version |
| Test type | Manual functional gameplay testing |
| Exact tested commit | Not recorded for this manual execution |
| Evidence | Tester-provided written observations; video/screenshots not yet captured |

## Observed results

| Check | Tester observation | Status |
|---|---|---|
| Character movement | WASD moves the character | PASS — reported |
| Jump activation | Space makes the character jump | PASS — reported |
| Obstacle collision | Gray obstacles prevent passing through | PASS — reported |
| Checkpoint recovery | After entering green checkpoint and red hazard, character respawns at green checkpoint | PASS — reported |

**Summary: 4/4 basic observed behaviors passed.** This is a count of confirmed behaviors, not four fully completed formal test cases.

## Formal test-case tracking

| Test case | Scope | Status |
|---|---|---|
| UNITY-001 | Movement against collision geometry | PASS for reported WASD and obstacle collision |
| UNITY-002 | Grounded jump and attempted airborne double-jump | PARTIAL: jump activation PASS; airborne re-jump not checked |
| UNITY-003 | Red hazard before checkpoint, initial spawn, full-health restoration | NOT RUN / NOT CONFIRMED |
| UNITY-004 | Checkpoint activation, hazard, respawn and health | PARTIAL: respawn location PASS; full-health restoration not checked |

## Limitations and follow-up

- Results are based on the tester's messages; no footage or Unity Player log was submitted for RUN-002.
- No specific defect was reported in the checked behaviors.
- Do not treat these observations as automated Play Mode test results.
- Confirm the exact tested Git commit, because the repository may advance after this local run.
- Run remaining assertions: attempt jump while mid-air, test the hazard before activating a checkpoint, and verify full health after respawn.
- Attach evidence under `Evidence/RUN-002/` if captured.

## Related materials

- [Manual test plan](TEST_PLAN.md)
- [Automated Edit Mode run RUN-001](TEST_EXECUTION_REPORT_RUN-001.md)
