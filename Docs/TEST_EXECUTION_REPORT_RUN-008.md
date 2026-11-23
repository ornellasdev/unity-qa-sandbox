# RUN-008 — Local Unity test execution with environment traceability

**Result: PASS (observed in two user-provided Unity Test Runner screenshots).** The tests ran locally in Unity Editor, not through GitHub Actions.

## Test Runner results

| Suite | Cases | Passed | Failed | Duration displayed |
|---|---:|---:|---:|---|
| Edit Mode | 22 | **22** | 0 | **0.009 s** |
| Play Mode | 7 | **7** | 0 | **1.168 s** |
| **Total** | **29** | **29** | **0** | Separate runs |

Edit Mode includes 17 `HealthModelTests` and 5 `CheckpointModelTests`. Play Mode includes the seven previously implemented gameplay, physical-trigger and full-scene integration checks.

## Environment traceability

The two original Markdown snapshots were inspected directly in GitHub and are linked below.

| Field | Before | After |
|---|---|---|
| Timestamp (UTC-03:00) | `2026-11-23T00:21:21-03:00` | `2026-11-23T00:24:36-03:00` |
| HEAD commit | `4b1b8396d96e7e1e68e33143768e50fd13834e6f` | Same |
| Branch / upstream | `main` / `origin/main` | Same |
| Git working tree | **DIRTY** | **DIRTY** |
| Modified tracked file | `ProjectSettings/ProjectSettings.asset` | Same path |
| Other Git status | No other entries in snapshot | `?? Evidence/Traceability/` |
| Project Unity editor version | `6000.6.10f1` | Same |
| Running Unity editor version (tester-entered) | `6000.6.10f1` | Same |
| OS / kernel | `Linux 7.3.5-2-cachyos` | Same |

- [Before snapshot](../Evidence/Traceability/RUN-008-before.md)
- [After snapshot](../Evidence/Traceability/RUN-008-after.md)

**Interpretation:** The two snapshots bracket the tester-provided Unity screenshots and establish the reported Git HEAD and dirty working-tree state at the capture times. They do **not** prove that `ProjectSettings/ProjectSettings.asset` had identical content at both times or that the exact running Editor build was independently visible in the Test Runner screenshots. The Unity version is grounded in the project configuration and tester-entered capture values. A previous premature after-snapshot was replaced by the tester after the test execution.

A partial `git diff` displayed Apple platform-target configuration differences, including iOS, tvOS and macOS settings. Its full contents and relevance to the Unity tests have not been reviewed; do not discard this local modification merely to obtain a clean status.

## Evidence

- [RUN-008(1).png — Edit Mode](../Evidence/RUN-008(1).png): 22 passed, 0 failed; duration 0.009s.
- [RUN-008(2).png — Play Mode](../Evidence/RUN-008(2).png): 7 passed, 0 failed; duration 1.168s.
- [Before snapshot](../Evidence/Traceability/RUN-008-before.md) and [after snapshot](../Evidence/Traceability/RUN-008-after.md): original execution environment records, committed.
- Optional NUnit XML exports were not provided.
- These results are from the **local Unity Editor**, not hosted Unity test CI.

## Completion checklist

- [x] Observe Edit Mode 22/22 PASS screenshot.
- [x] Observe Play Mode 7/7 PASS screenshot.
- [x] Observe before-snapshot command and commit output.
- [x] Re-run after snapshot **after** test execution (terminal screenshot reviewed).
- [x] Inspect both committed before/after snapshots and record actual timestamps, commit, status and modified paths.
- [x] Confirm both Test Runner screenshots and both traceability snapshots are committed to the repository.
- [ ] Review local `ProjectSettings/ProjectSettings.asset` changes, without discarding them.
- [x] Record project Unity version and tester-entered running Editor version from both snapshots.
- [ ] Independently verify running Editor build and, optionally, export NUnit XML on a future run.

See [TEST_TRACEABILITY.md](TEST_TRACEABILITY.md) for the capture protocol. This report only attributes results to evidence actually observed.
