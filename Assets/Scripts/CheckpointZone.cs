using UnityEngine;

namespace UnityQASandbox
{
    [RequireComponent(typeof(Collider))]
    public sealed class CheckpointZone : MonoBehaviour
    {
        public Transform spawnPoint;
        private void OnTriggerEnter(Collider other)
        {
            var player = other.GetComponent<PlayerRespawn>();
            if (player != null)
                player.SetCheckpoint(spawnPoint != null ? spawnPoint.position : transform.position + Vector3.up * 2f);
        }
    }
}
