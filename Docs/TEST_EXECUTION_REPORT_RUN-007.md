# RUN-007 — Negative-path and boundary regression plan

**Status: IMPLEMENTED / AWAITING LOCAL UNITY EXECUTION.** This is a test design and change record, **not** a claim of passed Unity tests.

## Change scope

- `Assets/Scripts/HealthModel.cs`: prevent integer overflow when `Heal(int.MaxValue)` is applied near maximum health, by comparing available health before addition.
- `Assets/Tests/EditMode/HealthModelTests.cs`: 10 new negative-path/boundary NUnit cases.
- `Assets/Tests/EditMode/CheckpointModelTests.cs`: 3 new boundary NUnit cases.
- No scene, damage trigger, or respawn lifecycle change is intended.

## Test cases added

| ID | Test | Expected result |
|---|---|---|
| NEG-001 | RejectsNegativeMaximumHealth | Constructor throws `ArgumentOutOfRangeException` |
| NEG-002 | ZeroDamageDoesNotChangeHealth | Health stays at maximum; player remains alive |
| NEG-003 | ZeroHealDoesNotChangeHealth | Health remains unchanged |
| NEG-004 | InvalidDamageDoesNotMutateHealth | Throws; previous health remains intact |
| NEG-005 | InvalidHealDoesNotMutateHealth | Throws; previous health remains intact |
| NEG-006 | FurtherDamageAfterDeathRemainsAtZero | Health remains zero and dead |
| NEG-007 | HealingFromZeroRestoresAliveState | Health increases and `IsDead` becomes false |
| NEG-008 | LargeHealSaturatesWithoutOverflow | `Heal(int.MaxValue)` restores exactly `MaxHealth` |
| NEG-009 | MaximumIntegerHealthCanRecoverFromDamage | `int.MaxValue` maximum health saturates correctly |
| NEG-010 | ResetAfterRepeatedDamageRestoresMaximumHealth | Reset restores full health after multiple hits |
| NEG-011 | AcceptsNegativeWorldCoordinates | Checkpoint stores negative world position |
| NEG-012 | RepeatedActivationAtSamePositionIsStable | Position stays unchanged |
| NEG-013 | ActivatingOriginAfterAnotherCheckpointOverridesIt | Origin becomes the latest spawn position |

## Reproduction procedure (CachyOS + Unity 6000.6.10f1)

1. Sync the repository. Preserve any local `ProjectSettings/ProjectSettings.asset` changes; do not use destructive Git commands.
2. Open Unity Hub, then the `unity-qa-sandbox` project.
3. Open **Window → General → Test Runner** and select **EditMode**.
4. Run all EditMode tests. The intended total is **22** tests (9 existing + 13 newly introduced).
5. If all pass, also run the existing **7 PlayMode** tests to check gameplay regressions from the health fix.
6. Capture the Test Runner results, failed test messages (if any), editor version, commit SHA, date and whether the working tree was clean.
7. Record the actual result below. Do not mark tests PASS unless locally observed.

## Execution record

- EditMode: **NOT RUN / NOT VERIFIED** (22 tests implemented)
- PlayMode regression: **NOT RUN / NOT VERIFIED** (7 existing tests)
- Target environment: Unity Editor 6000.6.10f1 / CachyOS
- Actual editor version: pending
- Actual commit and worktree state: pending
- Screenshots / XML: pending
- Defects discovered during run: pending

## CI scope

The GitHub Actions static-analysis workflow can parse changed C# files and check the repository structure **without opening Unity**. A green static check is **not** evidence of NUnit success, a compiled Unity project, or C# gameplay coverage.
