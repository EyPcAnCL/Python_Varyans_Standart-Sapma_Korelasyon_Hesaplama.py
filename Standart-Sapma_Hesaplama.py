import pandas as pd
import numpy as np

veriler = pd.Series(np.random.randint(1, 100, size=10))

std_sapma = veriler.std()

print("=" * 40)
print("📌 STANDART SAPMA (Std. Deviation)")
print("=" * 40)
print(f"Verilerimiz        : {veriler.tolist()}")
print(f"Aritmetik Ortalama : {veriler.mean():.2f}")
print(f"Sonuç (Std. Sapma) : {std_sapma:.2f}")
print("=" * 40)
