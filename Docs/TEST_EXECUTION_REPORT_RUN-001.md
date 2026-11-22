# Automated Test Execution Report — RUN-001

## Summary

| Field | Value |
|---|---|
| Project | Unity QA Sandbox |
| Test framework | Unity Test Framework / NUnit |
| Test mode | Edit Mode |
| Report date | 2026-11-22 |
| Executor | Yuri Ornellas |
| Source commit under test | Not recorded at execution time |
| Unity Editor version | Unity 6.6 (6000.6.10f1) — confirmed by tester screenshot |
| Operating system | CachyOS (Linux) — tester confirmed; release/kernel not recorded |
| Evidence | [Test Runner screenshot](../Evidence/RUN-001.png) committed to repository |
| Source of result | Screenshot visually reviewed (9 passed, 0 failed, 0 other); not independently verified by CI |

## Results

| Suite | Tests | Passed | Failed | Status |
|---|---:|---:|---:|---|
| HealthModelTests | 7 | 7 | 0 | PASS — screenshot reviewed |
| CheckpointModelTests | 2 | 2 | 0 | PASS — screenshot reviewed |
| **Total** | **9** | **9** | **0** | **PASS — tester reported** |

**Pass rate:** 100% of tests executed (9/9).

### Verified by the tester's report

A screenshot provided by the tester shows Unity Test Runner in Edit Mode with 9 passing tests (green checkmarks), 0 failed (red icon), and 0 in the other visible status counters. It shows two passing CheckpointModelTests and seven passing HealthModelTests. The screenshot is stored in this repository at [`Evidence/RUN-001.png`](../Evidence/RUN-001.png). This is **not** an independently executed CI run.

### Coverage

- Health state initialization
- Damage reduction and clamping
- Healing clamping
- Reset behavior
- Invalid input handling
- Initial checkpoint storage
- Latest checkpoint update

### Limitations

- Manual gameplay scenarios UNITY-001 to UNITY-004 have **not** been reported as executed.
- Edit Mode unit tests do **not** verify scene integration, physics, collision behavior, or actual playability.
- CachyOS release/kernel and the tested commit hash remain to be added. The Unity About window screenshot confirms editor version; the Test Runner screenshot confirms the displayed nine passing tests. The Unity About window screenshot confirms editor version only, not test results.

## Evidence checklist

- [x] Review tester-provided screenshot showing nine passing tests
- [x] Upload original Test Runner screenshot to `Evidence/RUN-001.png`
- [x] Record exact Unity Editor version from About Unity screenshot (Unity 6.6, 6000.6.10f1)
- [x] Record operating system: CachyOS (Linux)
- [ ] Record tested commit and optional CachyOS release/kernel
- [ ] Optionally export XML test results
- [ ] Attach manual gameplay validation after it has been performed

## Next steps

1. Record the tested commit and optional CachyOS release/kernel for reproducibility.
2. Run and document the manual gameplay test plan.
3. Add Play Mode integration tests and automated CI execution.
