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

- Target platform: CachyOS Linux.
- Unity version entered in capture command: `6000.6.10f1`; the exact running Editor build is **not independently visible** in the Test Runner screenshots.
- A screenshot of terminal output shows `git pull --ff-only origin main` completed, then the **before** snapshot was generated using `scripts/capture_qa_environment.py --run-id RUN-008 --phase before --unity-editor 6000.6.10f1`.
- Commit printed by the script: `4b1b8396d96e7e1e68e33143768e50fd13834e6f`.
- Working-tree status at before capture: **DIRTY**, including a previously known local `ProjectSettings/ProjectSettings.asset` modification (the complete snapshot file has not yet been provided for inspection).
- An **after** snapshot was initially created immediately after the before snapshot, **before the displayed Unity test execution**. Therefore, that initial after snapshot is **not adequate evidence of post-test state**.
- The tester **reran the after-snapshot command after the displayed Unity tests**. The subsequent terminal screenshot confirms creation of `Evidence/Traceability/RUN-008-after.md`, HEAD `4b1b8396d96e7e1e68e33143768e50fd13834e6f`, and **DIRTY** working tree. The snapshot contents are not yet inspected or committed to GitHub.
- The displayed Git status after the command shows `M ProjectSettings/ProjectSettings.asset` and `?? Evidence/Traceability/`. A partial `git diff` displayed changes to Apple platform version settings, including iOS, tvOS, and macOS targets; the full diff was not provided, so these changes should not be classified as harmless without review.
- Exact local Unity project files open during testing, SHA of modified configuration contents, and whether files changed during tests: **not independently established**.

## Evidence

- Edit Mode: user-provided Unity Test Runner screenshot showing **22 passed / 0 failed**; not yet committed to GitHub as RUN-008 evidence.
- Play Mode: user-provided Unity Test Runner screenshot showing **7 passed / 0 failed**; not yet committed to GitHub as RUN-008 evidence.
- Optional NUnit XML exports: not provided.
- No Unity runtime CI execution is claimed.

## Completion checklist

- [x] Observe Edit Mode 22/22 PASS screenshot.
- [x] Observe Play Mode 7/7 PASS screenshot.
- [x] Observe before-snapshot command and commit output.
- [x] Re-run after snapshot **after** test execution (terminal screenshot reviewed).
- [ ] Inspect `Evidence/Traceability/RUN-008-before.md` and `RUN-008-after.md` (record actual timestamps, status and modified paths).
- [ ] Commit the two Test Runner screenshot files and traceability snapshots.
- [ ] Review local `ProjectSettings/ProjectSettings.asset` changes, without discarding them.
- [ ] Confirm running Unity version and record optional NUnit XML for the same run.

See [TEST_TRACEABILITY.md](TEST_TRACEABILITY.md) for the capture protocol. This report only attributes results to evidence actually observed.
