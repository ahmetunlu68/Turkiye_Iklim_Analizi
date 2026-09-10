import pandas as pd

# CSV dosyasını oku
dosya = r"C:\Users\ahmet\PycharmProjects\Turkiye_Iklim_Analizi\data\canakkale_2000_2025.csv"

df = pd.read_csv(dosya)

# -----------------------------
# TEMEL İSTATİSTİKLER
# -----------------------------

print("ÇANAKKALE İKLİM ANALİZİ")
print("=" * 40)

print("\nSICAKLIK")
print("-" * 40)

print(f"Ortalama: {df['sicaklik_C'].mean():.2f} °C")
print(f"Medyan: {df['sicaklik_C'].median():.2f} °C")
print(f"Standart sapma: {df['sicaklik_C'].std():.2f} °C")
print(f"Minimum: {df['sicaklik_C'].min():.2f} °C")
print(f"Maksimum: {df['sicaklik_C'].max():.2f} °C")

print("\nYAĞIŞ")
print("-" * 40)

print(f"Ortalama: {df['yagis_mm'].mean():.2f} mm")
print(f"Medyan: {df['yagis_mm'].median():.2f} mm")
print(f"Standart sapma: {df['yagis_mm'].std():.2f} mm")
print(f"Minimum: {df['yagis_mm'].min():.2f} mm")
print(f"Maksimum: {df['yagis_mm'].max():.2f} mm")

# -----------------------------
# YILLIK VERİ SETİ
# -----------------------------

yillik = df.groupby("yil").agg(
    ortalama_sicaklik=("sicaklik_C", "mean"),
    toplam_yagis=("yagis_mm", "sum")
).reset_index()

print("\nYILLIK VERİLER")
print("=" * 50)
print(yillik)

import matplotlib.pyplot as plt

# -----------------------------
# YILLIK SICAKLIK GRAFİĞİ
# -----------------------------

plt.figure(figsize=(10, 5))

plt.plot(
    yillik["yil"],
    yillik["ortalama_sicaklik"],
    marker="o"
)

plt.title("Çanakkale Yıllık Ortalama Sıcaklık (2000-2025)")
plt.xlabel("Yıl")
plt.ylabel("Ortalama Sıcaklık (°C)")
plt.grid(True)

plt.tight_layout()

plt.savefig(
    r"C:\Users\ahmet\PycharmProjects\Turkiye_Iklim_Analizi\graphs\yillik_sicaklik_2000_2025.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()


# -----------------------------
# YILLIK YAĞIŞ GRAFİĞİ
# -----------------------------

plt.figure(figsize=(10, 5))

plt.plot(
    yillik["yil"],
    yillik["toplam_yagis"],
    marker="o"
)

plt.title("Çanakkale Yıllık Toplam Yağış (2000-2025)")
plt.xlabel("Yıl")
plt.ylabel("Toplam Yağış (mm)")
plt.grid(True)

plt.tight_layout()

plt.savefig(
    r"C:\Users\ahmet\PycharmProjects\Turkiye_Iklim_Analizi\graphs\yillik_yagis_2000_2025.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

from scipy.stats import linregress

# -----------------------------
# SICAKLIK TREND ANALİZİ
# -----------------------------

x = yillik["yil"]
y = yillik["ortalama_sicaklik"]

sonuc = linregress(x, y)

print("\nSICAKLIK TREND ANALİZİ")
print("=" * 40)

print(f"Eğim (°C/yıl): {sonuc.slope:.4f}")
print(f"Y-kesişim: {sonuc.intercept:.4f}")
print(f"R²: {sonuc.rvalue ** 2:.4f}")
print(f"p-değeri: {sonuc.pvalue:.4f}")
print(
    f"Yıllık değişim: {sonuc.slope * 10:.4f} °C / 10 yıl"
)


# -----------------------------
# YAĞIŞ TREND ANALİZİ
# -----------------------------

x = yillik["yil"]
y = yillik["toplam_yagis"]

sonuc_yagis = linregress(x, y)

print("\nYAĞIŞ TREND ANALİZİ")
print("=" * 40)

print(f"Eğim (mm/yıl): {sonuc_yagis.slope:.4f}")
print(f"Y-kesişim: {sonuc_yagis.intercept:.4f}")
print(f"R²: {sonuc_yagis.rvalue ** 2:.4f}")
print(f"p-değeri: {sonuc_yagis.pvalue:.4f}")
print(
    f"Yıllık değişim: {sonuc_yagis.slope * 10:.4f} mm / 10 yıl"
)