"""Regression tests for the license-free Unity heuristic checker."""
import sys
import tempfile
import unittest
from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parent))
import check_unity_patterns as checker
from check_unity_patterns import analyze, masked_source, frame_spans, method_body_at


class UnityPatternTests(unittest.TestCase):
    def codes(self, source):
        return [finding[0] for finding in analyze(source)]

    def test_legacy_lookup(self):
        self.assertIn("UNITY001", self.codes("var x = FindObjectOfType<Foo>();"))

    def test_per_frame_component_lookup(self):
        self.assertIn("UNITY003", self.codes("void Update() { GetComponent<Foo>(); }"))

    def test_cached_lookup_outside_update_not_flagged(self):
        self.assertNotIn("UNITY003", self.codes(
            "void Awake() { var x = GetComponent<Foo>(); }"
            "void Update() { x.Tick(); }"))

    def test_comments_and_strings_ignored(self):
        self.assertEqual([], analyze(
            '// FindObjectOfType<Foo>();\n'
            'void Update(){ var text = "GetComponent<Foo>()"; /* GameObject.Find("x"); */ }'))

    def test_null_sensitive_direct_access(self):
        self.assertIn("UNITY002", self.codes("void Awake() { GetComponent<Foo>().Run(); }"))
        self.assertNotIn("UNITY002", self.codes("void Awake() { GetComponent<Foo>()?.Run(); }"))

    def test_gameobject_find_hotpath_only(self):
        self.assertIn("UNITY004", self.codes("void FixedUpdate() { GameObject.Find(\"x\"); }"))
        self.assertNotIn("UNITY004", self.codes("void Awake() { GameObject.Find(\"x\"); }"))

    def test_camera_main(self):
        self.assertIn("UNITY005", self.codes("void LateUpdate() { var cam = Camera.main; }"))

    def test_nested_method_braces(self):
        self.assertIn("UNITY003", self.codes(
            "void Update() { if (true) { GetComponent<Foo>(); } }"))


    def test_primitive_cube_builtin_components_are_guaranteed(self):
        source = (
            "public static void Build() {"
            "GameObject checkpoint = GameObject.CreatePrimitive(PrimitiveType.Cube);"
            "checkpoint.GetComponent<BoxCollider>().isTrigger = true;"
            "checkpoint.GetComponent<Renderer>().sharedMaterial = material;"
            "}"
        )
        self.assertNotIn("UNITY002", self.codes(source))

    def test_prior_nunit_assertion_suppresses_same_component_access(self):
        source = (
            "public IEnumerator Check() {"
            "Assert.NotNull(player.GetComponent<PlayerHealth>(), \"Required\");"
            "var value = player.GetComponent<PlayerHealth>().maxHealth;"
            "}"
        )
        self.assertNotIn("UNITY002", self.codes(source))

    def test_different_asserted_component_does_not_suppress(self):
        source = (
            "public void Check() {"
            "Assert.NotNull(player.GetComponent<PlayerMovement>());"
            "var value = player.GetComponent<PlayerHealth>().maxHealth;"
            "}"
        )
        self.assertIn("UNITY002", self.codes(source))

    def test_assertion_after_access_does_not_suppress(self):
        source = (
            "public void Check() {"
            "var value = player.GetComponent<PlayerHealth>().maxHealth;"
            "Assert.NotNull(player.GetComponent<PlayerHealth>());"
            "}"
        )
        self.assertIn("UNITY002", self.codes(source))

    def test_assertion_in_previous_method_does_not_suppress(self):
        source = (
            "public void First() { Assert.NotNull(player.GetComponent<PlayerHealth>()); }"
            "public void Second() { var value = player.GetComponent<PlayerHealth>().maxHealth; }"
        )
        self.assertIn("UNITY002", self.codes(source))

    def test_receiver_reassignment_keeps_warning(self):
        source = (
            "public void Check() {"
            "Assert.NotNull(player.GetComponent<PlayerHealth>());"
            "player = other;"
            "var value = player.GetComponent<PlayerHealth>().maxHealth;"
            "}"
        )
        self.assertIn("UNITY002", self.codes(source))

    def test_primitive_other_component_still_warns(self):
        source = (
            "public static void Build() {"
            "var checkpoint = GameObject.CreatePrimitive(PrimitiveType.Cube);"
            "checkpoint.GetComponent<PlayerHealth>().CurrentHealth.ToString();"
            "}"
        )
        self.assertIn("UNITY002", self.codes(source))

    def test_primitive_created_in_other_method_still_warns(self):
        source = (
            "public static void Build() { var c = GameObject.CreatePrimitive(PrimitiveType.Cube); }"
            "public static void Use() { c.GetComponent<BoxCollider>().isTrigger = true; }"
        )
        self.assertIn("UNITY002", self.codes(source))




class UnityMaskAndCommandTests(unittest.TestCase):
    def test_masked_source_keeps_offsets_and_line_breaks(self):
        source = 'var name = "GetComponent<Foo>().Run()";\n// GetComponent<Foo>().Run()'
        masked = masked_source(source)
        self.assertEqual(len(source), len(masked))
        self.assertEqual(source.count("\n"), masked.count("\n"))
        self.assertEqual([], analyze(source))

    def test_block_comment_and_char_literals_are_ignored(self):
        source = "/* GetComponent<Foo>().Run() */ var x = 'a';"
        self.assertNotIn("UNITY002", [item[0] for item in analyze(source)])

    def test_unterminated_block_comment_is_ignored(self):
        self.assertEqual([], analyze("/* FindObjectOfType<Foo>();"))

    def test_unterminated_line_comment_is_ignored(self):
        self.assertEqual([], analyze("// FindObjectOfType<Foo>();"))

    def test_escaped_string_quote_is_ignored(self):
        source = 'var x = "escaped \\" GetComponent<Foo>().Run()";'
        self.assertNotIn("UNITY002", [item[0] for item in analyze(source)])

    def test_verbatim_double_quote_string_is_ignored(self):
        source = 'var x = @"quote "" GetComponent<Foo>().Run()";'
        self.assertEqual([], analyze(source))

    def test_unterminated_verbatim_string_does_not_warn(self):
        self.assertEqual([], analyze('var s = @"FindObjectOfType<Foo>()'))

    def test_raw_multiline_string_is_ignored(self):
        source = 'var s = """\nGetComponent<Foo>().Run()\n""";'
        self.assertNotIn("UNITY002", [item[0] for item in analyze(source)])

    def test_interpolated_string_is_ignored_conservatively(self):
        self.assertEqual([], analyze('var s = $"FindObjectOfType<Foo>()";'))

    def test_escaped_char_literal_is_ignored(self):
        self.assertEqual([], analyze("var c = '\\\\'; // GetComponent<Foo>().Run()"))

    def test_typeof_direct_access_is_flagged(self):
        codes = [x[0] for x in analyze("var x = GetComponent(typeof(Foo)).name;")]
        self.assertIn("UNITY002", codes)

    def test_missing_brace_frame_method_is_not_scanned_as_complete_method(self):
        self.assertEqual([], frame_spans("void Update() { GetComponent<Foo>();"))

    def test_method_body_at_returns_none_outside_method(self):
        self.assertIsNone(method_body_at("var x = GetComponent<Foo>().name;", 8))

    def _run_main(self, *, source=None, args=None, raw=None):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            if source is not None or raw is not None:
                assets = root / "Assets"
                assets.mkdir()
                target = assets / "Example.cs"
                if raw is not None:
                    target.write_bytes(raw)
                else:
                    target.write_text(source, encoding="utf-8")
            output = StringIO()
            with patch.object(checker, "ROOT", root), patch.object(sys, "argv", ["checker"] + (args or [])):
                with redirect_stdout(output):
                    result = checker.main()
            return result, output.getvalue()

    def test_cli_clean_source_succeeds(self):
        status, output = self._run_main(source="public class Example { }")
        self.assertEqual(0, status)
        self.assertIn("0 advisory finding(s)", output)

    def test_cli_warning_is_advisory_by_default(self):
        status, output = self._run_main(source="GetComponent<Foo>().Run();")
        self.assertEqual(0, status)
        self.assertIn("::warning", output)

    def test_cli_strict_mode_fails_on_warning(self):
        status, output = self._run_main(source="GetComponent<Foo>().Run();", args=["--strict"])
        self.assertEqual(1, status)
        self.assertIn("UNITY002", output)

    def test_cli_strict_mode_succeeds_when_clean(self):
        status, output = self._run_main(source="public class Example { }", args=["--strict"])
        self.assertEqual(0, status)

    def test_cli_fails_when_no_csharp_sources_exist(self):
        status, output = self._run_main()
        self.assertEqual(1, status)
        self.assertIn("No C# files found", output)

    def test_cli_fails_on_invalid_utf8(self):
        status, output = self._run_main(raw=b"\xff")
        self.assertEqual(1, status)
        self.assertIn("Cannot read source", output)




if __name__ == "__main__":
    unittest.main()
