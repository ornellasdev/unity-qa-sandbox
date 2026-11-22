using UnityEngine;

namespace UnityQASandbox
{
    public sealed class PlayerHealth : MonoBehaviour
    {
        [Min(1)] public int maxHealth = 100;
        private HealthModel model;
        public int CurrentHealth => model?.CurrentHealth ?? 0;

        private void Awake() => model = new HealthModel(maxHealth);

        public void TakeDamage(int amount)
        {
            model.Damage(amount);
            Debug.Log($"Health: {model.CurrentHealth}/{model.MaxHealth}", this);
            if (model.IsDead) GetComponent<PlayerRespawn>()?.Respawn();
        }

        public void RestoreFullHealth() => model.Reset();
    }
}
