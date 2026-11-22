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
| Airborne double-jump prevention | Character did not jump again while airborne | PASS — reported |
| Respawn without checkpoint | After red hazard without green checkpoint activation, character returned to initial spawn | PASS — reported |
| Full-health restoration after respawn | Not yet checked | PENDING |

**Summary:** Six observed gameplay behaviors reported passing; no failures reported. Health restoration remains unverified. These are individual observed checks, not a claim that all formal test cases are complete.

## Formal test-case tracking

| Test case | Scope | Status |
|---|---|---|
| UNITY-001 | Movement against collision geometry | PASS — tester reported WASD movement and collision |
| UNITY-002 | Grounded jump and airborne double-jump prevention | PASS — tester reported both checks |
| UNITY-003 | Red hazard before checkpoint; initial spawn; full-health restoration | PARTIAL — initial-position respawn PASS; full-health restoration pending |
| UNITY-004 | Checkpoint activation; hazard; checkpoint respawn; full-health restoration | PARTIAL — checkpoint respawn location PASS; full-health restoration pending |

## Limitations and follow-up

- All RUN-002 results are **tester-reported manual observations**; no video, gameplay screenshot, or log has yet been attached to this run.
- No specific defect was reported in the checked behaviors.
- Do not treat these observations as automated Play Mode test results.
- Confirm the exact tested Git commit; the repository may have changed after the local run.
- **Remaining check:** verify that `PlayerHealth.CurrentHealth` returns to maximum after respawn for both initial-spawn and checkpoint scenarios.
- Attach evidence to `Evidence/RUN-002/` when available.

## Related materials

- [Manual test plan](TEST_PLAN.md)
- [Automated Edit Mode run RUN-001](TEST_EXECUTION_REPORT_RUN-001.md)
