#if UNITY_EDITOR
using UnityEditor;
using UnityEditor.SceneManagement;
using UnityEngine;
using UnityQASandbox;

public static class QASandboxSceneBuilder
{
    [MenuItem("Tools/QA Sandbox/Create Demo Scene")]
    public static void Build()
    {
        if (!EditorSceneManager.SaveCurrentModifiedScenesIfUserWantsTo()) return;
        var scene = EditorSceneManager.NewScene(NewSceneSetup.DefaultGameObjects, NewSceneMode.Single);

        GameObject ground = GameObject.CreatePrimitive(PrimitiveType.Cube);
        ground.name = "Ground";
        ground.transform.position = new Vector3(0f, -0.5f, 0f);
        ground.transform.localScale = new Vector3(22f, 1f, 22f);

        GameObject player = GameObject.CreatePrimitive(PrimitiveType.Capsule);
        player.name = "Player";
        Object.DestroyImmediate(player.GetComponent<CapsuleCollider>());
        player.transform.position = new Vector3(0f, 1.1f, -6f);
        player.AddComponent<CharacterController>();
        player.AddComponent<PlayerMovement>();
        player.AddComponent<PlayerHealth>();
        player.AddComponent<PlayerRespawn>();

        GameObject checkpoint = GameObject.CreatePrimitive(PrimitiveType.Cube);
        checkpoint.name = "Checkpoint";
        checkpoint.transform.position = new Vector3(0f, 0.5f, 1f);
        checkpoint.transform.localScale = new Vector3(2f, 1f, 2f);
        checkpoint.GetComponent<BoxCollider>().isTrigger = true;
        checkpoint.AddComponent<CheckpointZone>();
        checkpoint.GetComponent<Renderer>().sharedMaterial = ColoredMaterial(Color.green);

        GameObject hazard = GameObject.CreatePrimitive(PrimitiveType.Cube);
        hazard.name = "Damage Zone";
        hazard.transform.position = new Vector3(0f, 0.5f, 6f);
        hazard.transform.localScale = new Vector3(3f, 1f, 2f);
        hazard.GetComponent<BoxCollider>().isTrigger = true;
        hazard.AddComponent<DamageZone>();
        hazard.GetComponent<Renderer>().sharedMaterial = ColoredMaterial(Color.red);

        for (int i = 0; i < 3; i++)
        {
            var block = GameObject.CreatePrimitive(PrimitiveType.Cube);
            block.name = "Collision Obstacle " + (i + 1);
            block.transform.position = new Vector3(-5f + i * 5f, 0.8f, -1f);
            block.transform.localScale = new Vector3(2f, 1.6f, 1f);
        }

        var cam = Camera.main;
        if (cam != null)
        {
            cam.transform.position = new Vector3(0f, 12f, -16f);
            cam.transform.rotation = Quaternion.Euler(37f, 0f, 0f);
        }

        System.IO.Directory.CreateDirectory("Assets/Scenes");
        EditorSceneManager.SaveScene(scene, "Assets/Scenes/QASandbox.unity");
        AssetDatabase.SaveAssets();
        Debug.Log("Generated Assets/Scenes/QASandbox.unity. Press Play to test.");
    }

    private static Material ColoredMaterial(Color color)
    {
        Shader shader = Shader.Find("Universal Render Pipeline/Lit") ?? Shader.Find("Standard");
        var material = new Material(shader);
        material.color = color;
        return material;
    }
}
#endif
