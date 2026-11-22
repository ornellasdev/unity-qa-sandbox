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
| Operating system | Not recorded — pending confirmation |
| Evidence | Test Runner screenshot / exported results pending upload |
| Source of result | Tester-reported results (not independently verified by CI) |

## Results

| Suite | Tests | Passed | Failed | Status |
|---|---:|---:|---:|---|
| HealthModelTests | 7 | 7 | 0 | PASS — tester reported |
| CheckpointModelTests | 2 | 2 | 0 | PASS — tester reported |
| **Total** | **9** | **9** | **0** | **PASS — tester reported** |

**Pass rate:** 100% of tests executed (9/9).

### Verified by the tester's report

The tester stated that all nine tests appeared as passing in Unity Test Runner Edit Mode. This report records that statement; it is **not a claim of independent execution** in GitHub Actions or by the repository maintainer's automation.

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
- Test Runner screenshot, OS and commit hash from the test environment remain to be added. The Unity About window screenshot confirms editor version only, not test results.

## Evidence checklist

- [ ] Add screenshot of Unity Test Runner showing nine passing tests to `Evidence/RUN-001/`
- [x] Record exact Unity Editor version from About Unity screenshot (Unity 6.6, 6000.6.10f1)
- [ ] Record OS and project commit
- [ ] Optionally export XML test results
- [ ] Attach manual gameplay validation after it has been performed

## Next steps

1. Capture the Edit Mode Test Runner results.
2. Run and document the manual gameplay test plan.
3. Add Play Mode integration tests and automated CI execution.
