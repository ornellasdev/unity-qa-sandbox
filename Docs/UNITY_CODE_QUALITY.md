# Unity-specific C# code quality checks

This is a **license-free, advisory heuristic scanner**, integrated into the existing [C# Static Analysis workflow](../.github/workflows/csharp-static-analysis.yml).

It checks C# files in `Assets/` using Python's standard library. It does not run the Unity Editor, consume a Unity license, compile C#, execute NUnit tests, or use Roslyn. The expanded workflow passed on GitHub Actions, confirmed by a repository-owner screenshot (17 seconds, five advisory UNITY002 warnings).

## Rules

| Rule | What it flags | Recommendation |
|---|---|---|
| `UNITY001` | Legacy `FindObjectOfType` / `FindObjectsOfType` searches | Evaluate the relevant `Find*Object(s)ByType` alternatives for the project's Unity version |
| `UNITY002` | Direct `GetComponent<T>().Member` access | Verify a required component is guaranteed, or add an appropriate guard |
| `UNITY003` | `GetComponent` family lookups within `Update`, `FixedUpdate` or `LateUpdate` | Cache references where stable and warranted |
| `UNITY004` | `GameObject.Find` in per-frame callbacks | Prefer a cached or serialized reference |
| `UNITY005` | `Camera.main` in per-frame callbacks | Assess caching if profiling indicates impact |

**Important:** These are **review prompts**, not proof of bugs. For example, `UNITY002` may be safe when a required component is declared with `[RequireComponent]`, and `Camera.main` is not automatically a performance issue in modern Unity.

The checker masks comments and string literals and checks scoped per-frame method bodies to reduce false positives. It is not a complete parser and may miss conditional compilation, complex C# syntax or indirect calls.

## Run locally (CachyOS)

```bash
cd ~/Projetos/unity-qa-sandbox
python3 -m unittest discover -s scripts -p 'test_unity_patterns.py' -v
python3 scripts/check_unity_patterns.py
```

Optional, **not enabled in CI**:

```bash
python3 scripts/check_unity_patterns.py --strict
```

In the GitHub Actions workflow, unit tests for the checker run first. The scanner emits GitHub annotations in the form `::warning`, and findings do **not** fail the job by default.

## Follow-up

- [x] Add Unity-specific source heuristics and regression fixtures
- [x] Integrate into GitHub Actions C# workflow
- [x] Confirm updated workflow completed successfully (owner screenshot)
- [x] Review five UNITY002 findings (four scene-builder primitives; one prior-asserted PlayerHealth test access)
- [ ] Improve UNITY002 to account for prior assertions and components guaranteed by primitive creation
- [ ] Consider richer Roslyn-based analysis with proper Unity references in the future
