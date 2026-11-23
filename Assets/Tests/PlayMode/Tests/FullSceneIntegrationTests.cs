#if UNITY_EDITOR
using System.Collections;
using NUnit.Framework;
using UnityEditor.SceneManagement;
using UnityEngine;
using UnityEngine.SceneManagement;
using UnityEngine.TestTools;
using UnityQASandbox;

/// <summary>
/// Verifies the actual serialized QASandbox scene, rather than a synthetic test scene.
/// Editor-only: the scene is loaded by asset path without requiring Build Settings.
/// </summary>
public class FullSceneIntegrationTests
{
    private const string ScenePath = "Assets/Scenes/QASandbox.unity";

    [UnityTest]
    public IEnumerator PLAY007_FullSceneLoadsAndHasRequiredGameplayComponents()
    {
        Scene scene = EditorSceneManager.LoadSceneInPlayMode(
            ScenePath,
            new LoadSceneParameters(LoadSceneMode.Single)
        );

        for (int frame = 0; frame < 120 && !scene.isLoaded; frame++)
            yield return null;

        Assert.IsTrue(scene.IsValid() && scene.isLoaded,
            "QASandbox scene must load successfully: " + ScenePath);

        GameObject player = FindRoot(scene, "Player");
        GameObject ground = FindRoot(scene, "Ground");
        GameObject damage = FindRoot(scene, "Damage Zone");
        GameObject checkpoint = FindRoot(scene, "Checkpoint");

        Assert.NotNull(player, "Scene requires a Player root object.");
        Assert.NotNull(ground, "Scene requires a Ground root object.");
        Assert.NotNull(damage, "Scene requires a Damage Zone root object.");
        Assert.NotNull(checkpoint, "Scene requires a Checkpoint root object.");

        Assert.NotNull(player.GetComponent<CharacterController>(),
            "Player needs CharacterController.");
        Assert.NotNull(player.GetComponent<PlayerMovement>(),
            "Player needs PlayerMovement.");
        Assert.NotNull(player.GetComponent<PlayerHealth>(),
            "Player needs PlayerHealth.");
        Assert.NotNull(player.GetComponent<PlayerRespawn>(),
            "Player needs PlayerRespawn.");

        Assert.NotNull(ground.GetComponent<Collider>(),
            "Ground must contain a collider.");

        var damageCollider = damage.GetComponent<Collider>();
        var damageScript = damage.GetComponent<DamageZone>();
        Assert.NotNull(damageCollider, "Damage Zone needs a collider.");
        Assert.IsTrue(damageCollider.isTrigger,
            "Damage Zone collider must be configured as a trigger.");
        Assert.NotNull(damageScript, "Damage Zone needs DamageZone component.");
        Assert.GreaterOrEqual(damageScript.damage,
            player.GetComponent<PlayerHealth>().maxHealth,
            "The demo hazard should be lethal to a full-health player.");

        var checkpointCollider = checkpoint.GetComponent<Collider>();
        Assert.NotNull(checkpointCollider, "Checkpoint needs a collider.");
        Assert.IsTrue(checkpointCollider.isTrigger,
            "Checkpoint collider must be configured as a trigger.");
        Assert.NotNull(checkpoint.GetComponent<CheckpointZone>(),
            "Checkpoint needs CheckpointZone component.");

        for (int i = 1; i <= 3; i++)
        {
            GameObject obstacle = FindRoot(scene, "Collision Obstacle " + i);
            Assert.NotNull(obstacle, "Missing collision obstacle " + i);
            var collider = obstacle.GetComponent<Collider>();
            Assert.NotNull(collider, "Obstacle " + i + " needs a collider.");
            Assert.IsFalse(collider.isTrigger,
                "Obstacle " + i + " must physically block the player.");
        }
    }

    private static GameObject FindRoot(Scene scene, string name)
    {
        foreach (GameObject root in scene.GetRootGameObjects())
            if (root.name == name) return root;
        return null;
    }
}
#endif
