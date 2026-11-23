"""Regression tests for the license-free Unity heuristic checker."""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from check_unity_patterns import analyze


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



if __name__ == "__main__":
    unittest.main()
