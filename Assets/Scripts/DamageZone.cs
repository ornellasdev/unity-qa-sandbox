
using UnityEngine;

namespace UnityQASandbox
{
    [RequireComponent(typeof(Collider))]
    public sealed class DamageZone : MonoBehaviour
    {
        [Min(1)]
        public int damage = 100;

        private void Awake()
        {
            Collider zoneCollider = GetComponent<Collider>();
            zoneCollider.isTrigger = true;

            Rigidbody rb = GetComponent<Rigidbody>();

            if (rb == null)
            {
                rb = gameObject.AddComponent<Rigidbody>();
            }

            rb.isKinematic = true;
            rb.useGravity = false;

            Debug.Log("Damage Zone initialized", this);
        }

        private void OnTriggerEnter(Collider other)
        {
            PlayerHealth playerHealth =
                other.GetComponent<PlayerHealth>();

            if (playerHealth == null)
            {
                playerHealth =
                    other.GetComponentInParent<PlayerHealth>();
            }

            if (playerHealth == null)
            {
                return;
            }

            Debug.Log("Player entered Damage Zone!", this);

            playerHealth.TakeDamage(damage);
        }
    }
}
