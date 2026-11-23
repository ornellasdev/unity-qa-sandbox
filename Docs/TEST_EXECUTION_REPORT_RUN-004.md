# Automated Play Mode Test Execution Report — RUN-004

## Summary

This report documents the first **Play Mode** automated gameplay-component tests for Unity QA Sandbox.

| Field | Value |
|---|---|
| Project | Unity QA Sandbox |
| Date | 2026-11-22 (Brazil local date, user session) |
| Tester | Yuri Ornellas |
| Platform | CachyOS Linux (previously confirmed environment) |
| Unity editor | Unity 6.6 (6000.6.10f1) (previously confirmed) |
| Runner | Unity Test Runner / Play Mode |
| Test source published in | [`3f602ea`](https://github.com/ornellasdev/unity-qa-sandbox/commit/3f602eac5985c0b85c47f6db670d360d2d3f562f) |
| Exact commit at the moment of execution | Not recorded; local tests were run before the source commit was created |
| Evidence | [RUN-004.png](../Evidence/RUN-004.png) — uploaded to repository; matching screenshot reviewed in conversation |
| Independent CI verification | Not performed |

## Test results

| Test | Purpose | Result |
|---|---|---|
| `PLAY001_DamageReducesHealth` | Calls `PlayerHealth.TakeDamage(25)`; verifies current health becomes 75 | PASS |
| `PLAY002_DeathRestoresFullHealth` | Calls lethal damage on test player and verifies full-health restoration after respawn | PASS |
| `PLAY003_CheckpointChangesRespawnPosition` | Activates checkpoint, invokes respawn, and verifies player position | PASS |

**Result: 3 passed / 0 failed / 3 total (100%).**

The tester-provided Test Runner screenshot shows three green tests and no failures.

## Coverage limits

- These tests exercise Unity gameplay components in Play Mode, but call methods directly. They do **not** simulate physical collision or trigger entry into the red damage zone or green checkpoint zone.
- The execution is evidenced by a screenshot shared in conversation; the repository now contains the Play Mode screenshot at [`Evidence/RUN-004.png`](../Evidence/RUN-004.png); an exported XML report remains pending.
- The test source was subsequently committed in `3f602ea`. Although the tester ran these tests before that commit, this does not prove a pristine checkout of that exact Git revision was tested.
- No claim of independent CI execution is made.

## Pending follow-up

- [x] Upload Play Mode Test Runner screenshot to `Evidence/RUN-004.png`
- [ ] Rerun against a known commit and record working-tree state, if reproducibility is required
- [ ] Add physics-trigger-based Play Mode integration coverage
- [ ] Add GitHub Actions / CI when practical
- [ ] Review remaining untracked Unity files separately before committing them

## Related

- [RUN-001 — Edit Mode](TEST_EXECUTION_REPORT_RUN-001.md)
- [RUN-002 — Manual gameplay](TEST_EXECUTION_REPORT_RUN-002.md)
- [RUN-003 — Regression](TEST_EXECUTION_REPORT_RUN-003.md)
