using System;

namespace UnityQASandbox
{
    public sealed class HealthModel
    {
        public int MaxHealth { get; }
        public int CurrentHealth { get; private set; }
        public bool IsDead => CurrentHealth == 0;

        public HealthModel(int maxHealth)
        {
            if (maxHealth <= 0) throw new ArgumentOutOfRangeException(nameof(maxHealth));
            MaxHealth = maxHealth;
            CurrentHealth = maxHealth;
        }

        public void Damage(int amount)
        {
            if (amount < 0) throw new ArgumentOutOfRangeException(nameof(amount));
            CurrentHealth = Math.Max(0, CurrentHealth - amount);
        }

        public void Heal(int amount)
        {
            if (amount < 0) throw new ArgumentOutOfRangeException(nameof(amount));
            // Compare before adding to avoid integer overflow on very large heals.
            CurrentHealth = amount >= MaxHealth - CurrentHealth
                ? MaxHealth
                : CurrentHealth + amount;
        }

        public void Reset() => CurrentHealth = MaxHealth;
    }
}
