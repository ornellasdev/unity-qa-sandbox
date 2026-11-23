using System.Collections;
using NUnit.Framework;
using UnityEngine;
using UnityEngine.TestTools;
using UnityQASandbox;

/// <summary>
/// Physics-driven integration tests. These tests construct a minimal scene with
/// real CharacterController movement and trigger colliders; they do not load
/// Assets/Scenes/QASandbox.unity.
/// </summary>
public class PhysicalTriggerTests
{
    private GameObject player;
    private GameObject damageZone;
    private GameObject checkpointZone;
    private CharacterController controller;
    private PlayerHealth health;
    private PlayerRespawn respawn;

    private static readonly Vector3 InitialSpawn = new Vector3(0f, 1f, -4f);

    [UnitySetUp]
    public IEnumerator SetUp()
    {
        player = new GameObject("PhysicsTestPlayer");
        player.transform.position = InitialSpawn;

        controller = player.AddComponent<CharacterController>();
        controller.height = 2f;
        controller.radius = 0.35f;
        health = player.AddComponent<PlayerHealth>();
        respawn = player.AddComponent<PlayerRespawn>();

        yield return new WaitForFixedUpdate();
    }

    [UnityTearDown]
    public IEnumerator TearDown()
    {
        if (player != null) Object.Destroy(player);
        if (damageZone != null) Object.Destroy(damageZone);
        if (checkpointZone != null) Object.Destroy(checkpointZone);
        yield return null;
    }

    private GameObject CreateTrigger(string name, Vector3 position)
    {
        var zone = new GameObject(name);
        zone.transform.position = position;

        var collider = zone.AddComponent<BoxCollider>();
        collider.isTrigger = true;
        collider.size = new Vector3(2f, 2f, 1f);

        // A kinematic body makes trigger participation explicit and independent
        // of the static-vs-character-controller interaction rules.
        var body = zone.AddComponent<Rigidbody>();
        body.isKinematic = true;
        body.useGravity = false;

        return zone;
    }

    private IEnumerator MoveForwardUntil(System.Func<bool> predicate, int maxSteps = 30)
    {
        for (int i = 0; i < maxSteps && !predicate(); i++)
        {
            controller.Move(Vector3.forward * 0.3f);
            yield return new WaitForFixedUpdate();
        }
    }

    [UnityTest]
    public IEnumerator PLAY004_PhysicalDamageTriggerReducesHealth()
    {
        damageZone = CreateTrigger("PartialDamageZone", Vector3.zero);
        var zone = damageZone.AddComponent<DamageZone>();
        zone.damage = 25;

        yield return new WaitForFixedUpdate();
        yield return MoveForwardUntil(() => health.CurrentHealth != 100);

        Assert.AreEqual(75, health.CurrentHealth,
            "Entering a physical trigger must apply 25 damage to a 100 HP player.");
    }

    [UnityTest]
    public IEnumerator PLAY005_PhysicalLethalTriggerCausesRespawn()
    {
        damageZone = CreateTrigger("LethalDamageZone", Vector3.zero);
        var zone = damageZone.AddComponent<DamageZone>();
        zone.damage = 100;

        bool movedAwayFromSpawn = false;
        bool returnedToSpawn = false;

        yield return new WaitForFixedUpdate();
        for (int i = 0; i < 30; i++)
        {
            controller.Move(Vector3.forward * 0.3f);
            yield return new WaitForFixedUpdate();

            float distance = Vector3.Distance(player.transform.position, InitialSpawn);
            if (distance > 0.2f) movedAwayFromSpawn = true;
            if (movedAwayFromSpawn && distance < 0.05f)
            {
                returnedToSpawn = true;
                break;
            }
        }

        Assert.IsTrue(returnedToSpawn,
            "The lethal trigger must fire and return the player to its initial spawn.");
        Assert.AreEqual(100, health.CurrentHealth,
            "Health must be fully restored after lethal-trigger respawn.");
    }

    [UnityTest]
    public IEnumerator PLAY006_PhysicalCheckpointThenHazardUsesCheckpointSpawn()
    {
        checkpointZone = CreateTrigger("CheckpointTrigger", Vector3.zero);
        var checkpoint = checkpointZone.AddComponent<CheckpointZone>();

        var marker = new GameObject("CheckpointSpawnMarker");
        marker.transform.SetParent(checkpointZone.transform, false);
        marker.transform.position = new Vector3(5f, 1f, -2f);
        checkpoint.spawnPoint = marker.transform;

        damageZone = CreateTrigger("PostCheckpointHazard", new Vector3(0f, 1f, 4f));
        var hazard = damageZone.AddComponent<DamageZone>();
        hazard.damage = 100;

        yield return new WaitForFixedUpdate();
        yield return MoveForwardUntil(() => player.transform.position.z > 1f);

        // Trigger-based checkpoint activation must be proven by the subsequent
        // lethal hazard returning the player to the unique marker position.
        bool reachedCheckpointSpawn = false;
        for (int i = 0; i < 30; i++)
        {
            controller.Move(Vector3.forward * 0.3f);
            yield return new WaitForFixedUpdate();
            if (Vector3.Distance(player.transform.position, marker.transform.position) < 0.05f)
            {
                reachedCheckpointSpawn = true;
                break;
            }
        }

        Assert.IsTrue(reachedCheckpointSpawn,
            "The checkpoint trigger must update the respawn position before the lethal hazard fires.");
        Assert.AreEqual(100, health.CurrentHealth,
            "Health must be full after respawning at the checkpoint.");
    }
}
