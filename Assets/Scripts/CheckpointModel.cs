using UnityEngine;

namespace UnityQASandbox
{
    public sealed class CheckpointModel
    {
        public Vector3 SpawnPosition { get; private set; }
        public CheckpointModel(Vector3 initialSpawn) => SpawnPosition = initialSpawn;
        public void Activate(Vector3 newPosition) => SpawnPosition = newPosition;
    }
}
