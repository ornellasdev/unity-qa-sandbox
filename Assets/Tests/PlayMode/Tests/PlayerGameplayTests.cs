
using System.Collections;
using NUnit.Framework;
using UnityEngine;
using UnityEngine.TestTools;
using UnityQASandbox;

public class PlayerGameplayTests
{
    private GameObject player;

    [UnitySetUp]
    public IEnumerator SetUp()
    {
        player = new GameObject("TestPlayer");

        player.AddComponent<CharacterController>();
        player.AddComponent<PlayerHealth>();
        player.AddComponent<PlayerRespawn>();

        yield return null;
    }

    [UnityTearDown]
    public IEnumerator TearDown()
    {
        if (player != null)
        {
            Object.Destroy(player);
        }

        yield return null;
    }

    [UnityTest]
    public IEnumerator PLAY001_DamageReducesHealth()
    {
        PlayerHealth health =
        player.GetComponent<PlayerHealth>();

        health.TakeDamage(25);

        yield return null;

        Assert.AreEqual(75, health.CurrentHealth);
    }

    [UnityTest]
    public IEnumerator PLAY002_DeathRestoresFullHealth()
    {
        PlayerHealth health =
        player.GetComponent<PlayerHealth>();

        health.TakeDamage(100);

        yield return null;

        Assert.AreEqual(100, health.CurrentHealth);
    }

    [UnityTest]
    public IEnumerator PLAY003_CheckpointChangesRespawnPosition()
    {
        PlayerRespawn respawn =
        player.GetComponent<PlayerRespawn>();

        Vector3 checkpoint = new Vector3(5f, 1f, 5f);

        respawn.SetCheckpoint(checkpoint);
        respawn.Respawn();

        yield return null;

        Assert.AreEqual(checkpoint, player.transform.position);
    }
}
