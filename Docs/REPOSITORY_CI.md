# License-free repository CI

The workflow [Repository Validation (No Unity License)](../.github/workflows/repository-validation.yml) runs on relevant pushes to `main`, pull requests, and manual dispatch.

It uses **Python 3.12 standard library only** and **does not launch Unity** or require Unity Student/Personal licensing credentials.

## Validations

- Required project files and test sources are present.
- Each asset file/directory under `Assets/` has a matching Unity `.meta` file.
- No orphan `.meta` files remain in `Assets/`.
- Package manifest, lock file, Unity assembly definitions, and ProjectSettings JSON files are parseable JSON.
- Assembly definition names are present and unique.
- `ProjectVersion.txt` exposes the Unity Editor version.
- Unity-generated `Library`, `Temp`, `Obj`, `Builds` and `Logs` directories are not tracked by Git.

## Local execution

```bash
cd ~/Projetos/unity-qa-sandbox
python3 scripts/validate_unity_repo.py
```

Expected output ends with:

```
Repository validation PASSED. This does not execute Unity or NUnit tests.
```

## GitHub Actions

[Open the workflow](https://github.com/ornellasdev/unity-qa-sandbox/actions/workflows/repository-validation.yml).

It runs on changes to `Assets/**`, `Packages/**`, `ProjectSettings/**`, the validator script or the workflow itself. It is independent of the gated [Unity test workflow](../.github/workflows/unity-tests.yml).

**Important:** Static validation cannot detect compile errors, gameplay defects, Unity asset serialization errors, or failed NUnit tests. The `9 Edit Mode + 7 Play Mode` passing results are from local Unity executions, not this workflow.

## First verified execution

The repository owner provided a GitHub Actions screenshot showing **Unity repository static checks — succeeded (7s)**. The generated-folder check reported `No tracked Unity generated folders detected.` This verifies the repository-validation workflow completed successfully; it does **not** verify Unity Editor compilation or gameplay tests. The exact workflow run URL/ID has not been recorded in this document.

## Roadmap

- [x] Publish license-free validation script and workflow
- [x] Confirm the first GitHub Actions run succeeds (screenshot reviewed)
- [ ] Require this check on pull requests after initial validation
- [ ] Add optional C# formatting/linting after verifying Unity-compatible tooling
- [ ] Separately resolve authorized licensing and runtime for Unity test execution
