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
| Evidence | Tester-provided written observations for both scenarios; one Unity Console screenshot shared in conversation (not yet uploaded to repository) |

## Observed results

| Check | Tester observation | Status |
|---|---|---|
| Character movement | WASD moves the character | PASS — reported |
| Jump activation | Space makes the character jump | PASS — reported |
| Obstacle collision | Gray obstacles prevent passing through | PASS — reported |
| Checkpoint recovery | After entering green checkpoint and red hazard, character respawns at green checkpoint | PASS — reported |
| Airborne double-jump prevention | Character did not jump again while airborne | PASS — reported |
| Respawn without checkpoint | After red hazard without green checkpoint activation, character returned to initial spawn | PASS — reported |
| Full-health restoration after respawn without checkpoint | Tester confirms `Health after respawn: 100` | PASS — tester reported; Console screenshot supports restoration but does not identify scenario |
| Full-health restoration after respawn with checkpoint | Tester confirms `Health after respawn: 100` | PASS — tester reported; Console screenshot supports restoration but does not identify scenario |

**Summary:** Eight individual gameplay checks reported passing (including two full-health restoration scenarios); zero failures reported in the final regression run. The uploaded-in-chat Console screenshot displays `Health: 0/100`, `Health after respawn: 100`, and `Player respawned`, but does not independently establish which scenario was shown. Both scenarios are confirmed by the tester's statement.

## Formal test-case tracking

| Test case | Scope | Status |
|---|---|---|
| UNITY-001 | Movement against collision geometry | PASS — tester reported WASD movement and collision |
| UNITY-002 | Grounded jump and airborne double-jump prevention | PASS — tester reported both checks |
| UNITY-003 | Red hazard before checkpoint; initial spawn; full-health restoration | PASS — tester reported for all checks |
| UNITY-004 | Checkpoint activation; hazard; checkpoint respawn; full-health restoration | PASS — tester reported for all checks |

## Limitations and follow-up

- RUN-002 scenario-level results are **tester-reported manual observations**. One Console screenshot was reviewed in chat but is not yet committed to the repository. It shows health recovery to 100, not both scenario identities.
- During testing, the red hazard temporarily stopped triggering respawn. The tester edited `PlayerRespawn.cs` and `DamageZone.cs` locally, and then provided Console evidence of restored trigger, damage, health reset and respawn behavior. **The actual local fix and final tested commit are not yet confirmed as published on GitHub.** Do not label a GitHub commit as the verified fix until source and regression version are matched.
- Do not treat these observations as automated Play Mode test results.
- Confirm the exact tested Git commit; the repository may have changed after the local run.
- Health restoration has now been reported as verified in both initial-spawn and checkpoint scenarios. Remaining: commit the fix, identify the tested revision, and upload evidence for RUN-002.
- Attach evidence to `Evidence/RUN-002/` when available.

## Related materials

- [Manual test plan](TEST_PLAN.md)
- [Automated Edit Mode run RUN-001](TEST_EXECUTION_REPORT_RUN-001.md)
