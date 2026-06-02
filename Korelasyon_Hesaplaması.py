import pandas as pd
import numpy as np

# Korelasyon için 2 ayrı değişken lazım
x = pd.Series(np.random.randint(1, 100, size=10))
y = pd.Series(np.random.randint(1, 100, size=10))

korelasyon = x.corr(y)

print("=" * 40)
print("📌 KORELASYON (Correlation)")
print("=" * 40)
print(f"X Verisi           : {x.tolist()}")
print(f"Y Verisi           : {y.tolist()}")
print(f"Sonuç (Korelasyon) : {korelasyon:.2f}")
print("=" * 40)

# Sonucu yorumla
if korelasyon > 0.5:
    yorum = "💹 Güçlü POZİTİF ilişki — X artınca Y de artıyor"
elif korelasyon < -0.5:
    yorum = "📉 Güçlü NEGATİF ilişki — X artınca Y azalıyor"
else:
    yorum = "😐 Zayıf ilişki — X ve Y birbirinden bağımsız"

print(f"Yorum              : {yorum}")
print("=" * 40)
