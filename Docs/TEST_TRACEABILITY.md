# Unity QA run traceability

This workflow captures **test-time provenance** (not a retrospective assumption). Earlier RUN-002, RUN-003 and RUN-007 reports contain actual or tester-reported results but do not independently establish the exact clean checkout during their original execution.

## Before a new Unity test run

From the CachyOS project root:

~~~bash
cd ~/Projetos/unity-qa-sandbox
python3 scripts/capture_qa_environment.py --run-id RUN-008 --phase before --unity-editor 6000.6.10f1
~~~

Replace `RUN-008` and the Editor version with the **actual run ID and version displayed by Unity**. The script records the Git commit, branch, upstream, working-tree status, modified tracked filenames, project Editor version, timestamp and OS. The script does **not** change or discard local modifications.

Open `Assets/Scenes/QASandbox.unity`, run the appropriate Unity Test Runner suites, and capture screenshots and/or exported NUnit XML. Note the individual results and any failures in the matching run report.

## Immediately after the run

~~~bash
python3 scripts/capture_qa_environment.py --run-id RUN-008 --phase after --unity-editor 6000.6.10f1
git status -sb
~~~

Expected new files: `Evidence/Traceability/RUN-008-before.md` and `RUN-008-after.md`. These files are evidence created **on the dates they are generated**. Adding them retroactively must not be presented as proof of an older test's revision.

If either snapshot is **DIRTY**, record the changed file paths and investigate whether their contents affected the tested behavior. Avoid blanket `git restore` or `git reset --hard`. The known historical local change in `ProjectSettings/ProjectSettings.asset` is **not yet reconciled**.

## Run documentation checklist

- Exact execution date and local timezone, tester and platform
- Editor version observed in Unity, plus project `ProjectVersion.txt`
- Before/after snapshot paths and the commit SHA from each
- Clean/dirty working-tree state, with relevant differences reviewed
- Test counts, pass/fail/skip and reproducible steps
- Screenshot/recording/XML paths and their limitations
- Regression links, bug IDs and any retest result
- Explicitly state **local Unity** vs **license-free GitHub Actions** scope

## Earlier evidence limitations

- **RUN-002:** original tested commit unknown; later gameplay video shows damage and health restoration, not every manual test case.
- **RUN-003:** target commit `9406fca` was reported by tester, but the actual opened Unity project revision was not independently established; the later Console screenshot shows health reset and respawn, not both spawn destinations.
- **RUN-007:** 22/22 Edit Mode and 7/7 Play Mode pass screenshots are committed. A **later** terminal snapshot had HEAD `5d26c30d4f681349c77f74d5ebc07e8b86d973ae` and a locally modified `ProjectSettings/ProjectSettings.asset`. This is not guaranteed to be the test-time revision. The screenshot alone does not independently show the Unity Editor build.

Do not edit old reports to claim a historical clean checkout on the basis of current Git status.
