using NUnit.Framework;
using UnityEngine;
using UnityQASandbox;

namespace UnityQASandbox.Tests
{
    public class CheckpointModelTests
    {
        [Test] public void StartsAtInitialPosition() { var m = new CheckpointModel(Vector3.one); Assert.AreEqual(Vector3.one, m.SpawnPosition); }
        [Test] public void LatestCheckpointWins() { var m = new CheckpointModel(Vector3.zero); m.Activate(new Vector3(1,2,3)); m.Activate(new Vector3(4,5,6)); Assert.AreEqual(new Vector3(4,5,6), m.SpawnPosition); }

        [Test]
        public void AcceptsNegativeWorldCoordinates()
        {
            var checkpoint = new CheckpointModel(Vector3.zero);
            var negativePosition = new Vector3(-8f, -2f, -15f);
            checkpoint.Activate(negativePosition);
            Assert.AreEqual(negativePosition, checkpoint.SpawnPosition);
        }

        [Test]
        public void RepeatedActivationAtSamePositionIsStable()
        {
            var position = new Vector3(2f, 3f, 4f);
            var checkpoint = new CheckpointModel(position);
            checkpoint.Activate(position);
            checkpoint.Activate(position);
            Assert.AreEqual(position, checkpoint.SpawnPosition);
        }

        [Test]
        public void ActivatingOriginAfterAnotherCheckpointOverridesIt()
        {
            var checkpoint = new CheckpointModel(new Vector3(1f, 2f, 3f));
            checkpoint.Activate(new Vector3(4f, 5f, 6f));
            checkpoint.Activate(Vector3.zero);
            Assert.AreEqual(Vector3.zero, checkpoint.SpawnPosition);
        }

    }
}
