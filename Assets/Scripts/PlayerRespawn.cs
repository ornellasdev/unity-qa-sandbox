using UnityEngine;

namespace UnityQASandbox
{
    [RequireComponent(typeof(CharacterController))]
    public sealed class PlayerRespawn : MonoBehaviour
    {
        private CharacterController controller;
        private CheckpointModel checkpoints;

        private void Awake()
        {
            controller = GetComponent<CharacterController>();
            checkpoints = new CheckpointModel(transform.position);
        }

        public void SetCheckpoint(Vector3 position) => checkpoints.Activate(position);

        public void Respawn()
        {
            controller.enabled = false;
            transform.position = checkpoints.SpawnPosition;
            controller.enabled = true;
            GetComponent<PlayerHealth>()?.RestoreFullHealth();
            GetComponent<PlayerMovement>()?.ResetVelocity();
            Debug.Log("Player respawned", this);
        }
    }
}
