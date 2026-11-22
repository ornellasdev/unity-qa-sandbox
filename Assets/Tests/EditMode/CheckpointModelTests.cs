using NUnit.Framework;
using UnityEngine;
using UnityQASandbox;

namespace UnityQASandbox.Tests
{
    public class CheckpointModelTests
    {
        [Test] public void StartsAtInitialPosition() { var m = new CheckpointModel(Vector3.one); Assert.AreEqual(Vector3.one, m.SpawnPosition); }
        [Test] public void LatestCheckpointWins() { var m = new CheckpointModel(Vector3.zero); m.Activate(new Vector3(1,2,3)); m.Activate(new Vector3(4,5,6)); Assert.AreEqual(new Vector3(4,5,6), m.SpawnPosition); }
    }
}
