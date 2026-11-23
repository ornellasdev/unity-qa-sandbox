using System;
using NUnit.Framework;
using UnityQASandbox;

namespace UnityQASandbox.Tests
{
    public class HealthModelTests
    {
        [Test] public void StartsAtMaximumHealth() => Assert.AreEqual(100, new HealthModel(100).CurrentHealth);
        [Test] public void DamageReducesHealth() { var h = new HealthModel(100); h.Damage(25); Assert.AreEqual(75, h.CurrentHealth); }
        [Test] public void DamageClampsAtZero() { var h = new HealthModel(10); h.Damage(99); Assert.AreEqual(0, h.CurrentHealth); }
        [Test] public void HealClampsAtMaximum() { var h = new HealthModel(10); h.Damage(4); h.Heal(99); Assert.AreEqual(10, h.CurrentHealth); }
        [Test] public void ResetRestoresHealth() { var h = new HealthModel(10); h.Damage(10); h.Reset(); Assert.AreEqual(10, h.CurrentHealth); }
        [Test] public void RejectsInvalidMaximumHealth() => Assert.Throws<ArgumentOutOfRangeException>(() => new HealthModel(0));
        [Test] public void RejectsNegativeDamageAndHeal() { var h = new HealthModel(10); Assert.Throws<ArgumentOutOfRangeException>(() => h.Damage(-1)); Assert.Throws<ArgumentOutOfRangeException>(() => h.Heal(-1)); }

        // Negative-path and boundary regression cases (not yet verified in Unity Test Runner).
        [Test]
        public void RejectsNegativeMaximumHealth()
        {
            Assert.Throws<ArgumentOutOfRangeException>(() => new HealthModel(-1));
        }

        [Test]
        public void ZeroDamageDoesNotChangeHealth()
        {
            var health = new HealthModel(100);
            health.Damage(0);
            Assert.AreEqual(100, health.CurrentHealth);
            Assert.IsFalse(health.IsDead);
        }

        [Test]
        public void ZeroHealDoesNotChangeHealth()
        {
            var health = new HealthModel(100);
            health.Damage(30);
            health.Heal(0);
            Assert.AreEqual(70, health.CurrentHealth);
        }

        [Test]
        public void InvalidDamageDoesNotMutateHealth()
        {
            var health = new HealthModel(100);
            health.Damage(25);
            Assert.Throws<ArgumentOutOfRangeException>(() => health.Damage(-1));
            Assert.AreEqual(75, health.CurrentHealth);
        }

        [Test]
        public void InvalidHealDoesNotMutateHealth()
        {
            var health = new HealthModel(100);
            health.Damage(25);
            Assert.Throws<ArgumentOutOfRangeException>(() => health.Heal(-1));
            Assert.AreEqual(75, health.CurrentHealth);
        }

        [Test]
        public void FurtherDamageAfterDeathRemainsAtZero()
        {
            var health = new HealthModel(10);
            health.Damage(10);
            health.Damage(int.MaxValue);
            Assert.AreEqual(0, health.CurrentHealth);
            Assert.IsTrue(health.IsDead);
        }

        [Test]
        public void HealingFromZeroRestoresAliveState()
        {
            var health = new HealthModel(10);
            health.Damage(10);
            health.Heal(3);
            Assert.AreEqual(3, health.CurrentHealth);
            Assert.IsFalse(health.IsDead);
        }

        [Test]
        public void LargeHealSaturatesWithoutOverflow()
        {
            var health = new HealthModel(100);
            health.Damage(30);
            health.Heal(int.MaxValue);
            Assert.AreEqual(100, health.CurrentHealth);
        }

        [Test]
        public void MaximumIntegerHealthCanRecoverFromDamage()
        {
            var health = new HealthModel(int.MaxValue);
            health.Damage(1);
            health.Heal(int.MaxValue);
            Assert.AreEqual(int.MaxValue, health.CurrentHealth);
        }

        [Test]
        public void ResetAfterRepeatedDamageRestoresMaximumHealth()
        {
            var health = new HealthModel(20);
            health.Damage(7);
            health.Damage(8);
            health.Reset();
            Assert.AreEqual(20, health.CurrentHealth);
            Assert.IsFalse(health.IsDead);
        }

    }
}
