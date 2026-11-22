using UnityEngine;

namespace UnityQASandbox
{
    [RequireComponent(typeof(CharacterController))]
    public sealed class PlayerMovement : MonoBehaviour
    {
        [Min(0f)] public float speed = 5f;
        [Min(0f)] public float jumpHeight = 1.4f;
        public float gravity = -18f;
        private CharacterController controller;
        private float verticalVelocity;

        private void Awake() => controller = GetComponent<CharacterController>();

        private void Update()
        {
            Vector3 input = new Vector3(Input.GetAxisRaw("Horizontal"), 0f, Input.GetAxisRaw("Vertical"));
            input = Vector3.ClampMagnitude(input, 1f);
            if (controller.isGrounded && verticalVelocity < 0f) verticalVelocity = -1f;
            if (controller.isGrounded && Input.GetButtonDown("Jump"))
                verticalVelocity = Mathf.Sqrt(jumpHeight * -2f * gravity);
            verticalVelocity += gravity * Time.deltaTime;
            controller.Move((input * speed + Vector3.up * verticalVelocity) * Time.deltaTime);
        }

        public void ResetVelocity() => verticalVelocity = 0f;
    }
}
