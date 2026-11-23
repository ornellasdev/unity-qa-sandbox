# Continuous Integration — Unity QA Sandbox

**Status: CONFIGURED IN REPOSITORY, NOT YET VALIDATED BY A SUCCESSFUL CI RUN.**

The GitHub Actions workflow [`.github/workflows/unity-tests.yml`](../.github/workflows/unity-tests.yml) prepares two test jobs using [GameCI Unity Test Runner](https://game.ci/docs/github/test-runner/):

| Job | Expected tests | Status |
|---|---:|---|
| EditMode | 9 NUnit tests | Not yet run in CI |
| PlayMode | 7 Unity tests (including physical trigger and full-scene checks) | Not yet run in CI |

- Unity editor: **6000.6.10f1**
- Runner: **ubuntu-22.04**
- GameCI action: **v4.3.2** (includes a Unity 6.6 Docker shared-memory fix)
- Results: uploaded as GitHub Actions artifacts, retained for **14 days** if produced
- Triggers: **Run workflow** manually, or push to `main` after enabling the repository variable `UNITY_CI_ENABLED=true`

## Step 1 — Configure private Unity secrets

For **Unity Personal**, follow the [GameCI activation guide](https://game.ci/docs/github/activation/). Its current guidance describes obtaining the Unity license file (`.ulf`) and creating these GitHub Actions repository secrets:

- `UNITY_LICENSE` — contents of the activated `.ulf` file
- `UNITY_EMAIL` — Unity account email
- `UNITY_PASSWORD` — Unity account password

Navigate to **Settings → Secrets and variables → Actions → Repository secrets**.

**Security:** Never commit license files or credentials, paste credentials into issues or chats, or put them in the README. GitHub's encrypted secrets are passed to the workflow only at runtime. Follow Unity seat/license rules; Unity Personal activation in CI may require returning an active local seat or additional steps described in the GameCI guide.

The workflow explicitly checks that these secrets are supplied before launching Unity. It does **not** generate or manage a license.

## Step 2 — First manual CI run

1. Open [Actions](https://github.com/ornellasdev/unity-qa-sandbox/actions/workflows/unity-tests.yml).
2. Select **Unity QA Tests → Run workflow → main → Run workflow**.
3. Inspect both jobs: **Unity EditMode** and **Unity PlayMode**.
4. Review their logs and download the results from **Artifacts**.
5. If Unity fails activation, Docker image resolution, compilation, or the tests themselves, document that failure rather than claiming CI success.

A local Test Runner screenshot does not count as a successful GitHub Actions run.

## Step 3 — Enable automatic checks

**Only after a successful manual run**, create a repository **Actions variable** (not a secret) named:

`UNITY_CI_ENABLED` = `true`

New pushes to `main` that change `Assets/**`, `Packages/**`, `ProjectSettings/**`, or the workflow will then start both jobs. Leave the variable unset (or not exactly `true`) to pause automatic Unity jobs. You can still start runs manually.

## Current limits / improvements

- [x] Publish an initial gated Unity CI workflow
- [ ] Configure Unity licensing secrets (owner action required)
- [ ] Execute and verify the first **EditMode 9/9** and **PlayMode 7/7** GitHub Actions runs
- [ ] Enable push-triggered Unity jobs via `UNITY_CI_ENABLED=true`
- [ ] Store first CI XML/log artifacts and link successful workflow run
- [ ] Add branch-protection required checks once jobs are reliable
- [ ] Consider caching Unity Library once CI is stable

The **PLAY007** full-scene validation is Editor-only and should be run under GameCI PlayMode in the Unity Editor, not as a standalone player build.

## Troubleshooting

**License activation failed:** verify all three secrets, the license file's validity, and Unity account seat requirements.

**Unity 6.6 Docker shared-memory error:** ensure the workflow uses GameCI `v4.3.2` or a later compatible release. Unity 6.6 needs more shared memory than the default Docker allocation.

**One job fails while the other passes:** download the artifact and review the specific test logs before changing gameplay code.

**The action appears skipped:** `UNITY_CI_ENABLED` is not set to `true`. Use manual dispatch while onboarding.
