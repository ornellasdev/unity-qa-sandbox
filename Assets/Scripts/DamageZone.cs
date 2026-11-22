using UnityEngine;

namespace UnityQASandbox
{
    [RequireComponent(typeof(Collider))]
    public sealed class DamageZone : MonoBehaviour
    {
        [Min(1)] public int damage = 100;
        private void OnTriggerEnter(Collider other)
        {
            var health = other.GetComponent<PlayerHealth>();
            if (health != null) health.TakeDamage(damage);
        }
    }
}
