import numpy as np

veriler = np.random.randint(1, 100, size=10)

varyans = np.var(veriler)

print("=" * 40)
print("📌 VARYANS (Variance)")
print("=" * 40)
print(f"Verilerimiz        : {veriler.tolist()}")
print(f"Aritmetik Ortalama : {np.mean(veriler):.2f}")
print(f"Sonuç (Varyans)    : {varyans:.2f}")
print("=" * 40)
