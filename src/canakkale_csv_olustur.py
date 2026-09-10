import xarray as xr
import pandas as pd

# --------------------------------
# 1. Veriyi aç
# --------------------------------

dosya = r"C:\Users\ahmet\PycharmProjects\Turkiye_Iklim_Analizi\data\canakkale_2000_2025.nc"

veri = xr.open_dataset(dosya)

# --------------------------------
# 2. Çanakkale koordinatları
# --------------------------------

canakkale_lat = 40.15
canakkale_lon = 26.41

# En yakın grid noktasını seç
canakkale = veri.sel(
    latitude=canakkale_lat,
    longitude=canakkale_lon,
    method="nearest"
)

# --------------------------------
# 3. Pandas DataFrame oluştur
# --------------------------------

df = canakkale[["t2m", "tp"]].to_dataframe().reset_index()

# --------------------------------
# 4. Sıcaklık dönüşümü
# Kelvin → Celsius
# --------------------------------

df["sicaklik_C"] = df["t2m"] - 273.15

# --------------------------------
# 5. Yağış dönüşümü
# metre/gün → aylık mm
# --------------------------------

df["yil"] = df["valid_time"].dt.year
df["ay"] = df["valid_time"].dt.month

# Her ayın gün sayısını bul
df["gun_sayisi"] = df["valid_time"].dt.days_in_month

df["yagis_mm"] = (
    df["tp"] * 1000 * df["gun_sayisi"]
)

# --------------------------------
# 6. Gereksiz sütunları kaldır
# --------------------------------

df = df[
    [
        "yil",
        "ay",
        "sicaklik_C",
        "yagis_mm"
    ]
]

# --------------------------------
# 7. CSV olarak kaydet
# --------------------------------

cikti = r"C:\Users\ahmet\PycharmProjects\Turkiye_Iklim_Analizi\data\canakkale_2000_2025.csv"

df.to_csv(cikti, index=False)

# --------------------------------
# 8. Sonuçları göster
# --------------------------------

print("CSV başarıyla oluşturuldu!")
print()
print(df.head())
print()
print(df.tail())
print()
print("Gözlem sayısı:", len(df))