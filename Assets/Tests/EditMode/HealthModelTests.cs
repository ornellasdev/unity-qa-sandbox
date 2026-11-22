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
    }
}
