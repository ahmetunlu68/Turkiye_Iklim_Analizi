import pandas as pd

# --------------------------------
# 1. CSV dosyasını oku
# --------------------------------

dosya = r"C:\Users\ahmet\PycharmProjects\Turkiye_Iklim_Analizi\data\canakkale_2000_2025.csv"

df = pd.read_csv(dosya)


# --------------------------------
# 2. Ayları mevsimlere dönüştür
# --------------------------------

def mevsim_bul(ay):

    if ay in [12, 1, 2]:
        return "Kış"

    elif ay in [3, 4, 5]:
        return "İlkbahar"

    elif ay in [6, 7, 8]:
        return "Yaz"

    elif ay in [9, 10, 11]:
        return "Sonbahar"


df["mevsim"] = df["ay"].apply(mevsim_bul)


# --------------------------------
# 3. Kontrol
# --------------------------------

print(df.head(15))

print("\nMevsim dağılımı:")
print(df["mevsim"].value_counts())

# --------------------------------
# MEVSİMSEL İSTATİSTİKLER
# --------------------------------

mevsimsel = df.groupby("mevsim").agg(
    ortalama_sicaklik=("sicaklik_C", "mean"),
    toplam_yagis=("yagis_mm", "sum"),
    ortalama_yagis=("yagis_mm", "mean")
)

# Mevsimleri istediğimiz sıraya getir
sirasi = [
    "Kış",
    "İlkbahar",
    "Yaz",
    "Sonbahar"
]

mevsimsel = mevsimsel.reindex(sirasi)

print("\nMEVSİMSEL İSTATİSTİKLER")
print("=" * 60)

print(mevsimsel)

from scipy.stats import linregress

# --------------------------------
# MEVSİMSEL SICAKLIK TRENDLERİ
# --------------------------------

print("\nMEVSİMSEL SICAKLIK TRENDLERİ")
print("=" * 70)

for mevsim in sirasi:

    veri = df[df["mevsim"] == mevsim]

    # Her yıl için mevsim ortalama sıcaklığı
    yillik_mevsim = veri.groupby("yil")["sicaklik_C"].mean()

    x = yillik_mevsim.index
    y = yillik_mevsim.values

    sonuc = linregress(x, y)

    print(f"\n{mevsim}")
    print(f"Eğim: {sonuc.slope:.4f} °C/yıl")
    print(f"10 yıllık değişim: {sonuc.slope * 10:.4f} °C")
    print(f"R²: {sonuc.rvalue ** 2:.4f}")
    print(f"p-değeri: {sonuc.pvalue:.4f}")

    import matplotlib.pyplot as plt

    # --------------------------------
    # MEVSİMSEL SICAKLIK TREND GRAFİĞİ
    # --------------------------------

    plt.figure(figsize=(12, 7))

    for mevsim in sirasi:
        # İlgili mevsimin verilerini al
        veri = df[df["mevsim"] == mevsim]

        # Her yıl için mevsimsel ortalama sıcaklık
        yillik_mevsim = veri.groupby("yil")["sicaklik_C"].mean()

        x = yillik_mevsim.index
        y = yillik_mevsim.values

        # Gerçek sıcaklık değerleri
        plt.plot(
            x,
            y,
            marker="o",
            label=mevsim
        )

        # Regresyon
        sonuc = linregress(x, y)

        trend = sonuc.intercept + sonuc.slope * x

        # Trend çizgisi
        plt.plot(
            x,
            trend,
            linestyle="--"
        )

    plt.title(
        "Çanakkale Mevsimsel Ortalama Sıcaklık Trendleri (2000-2025)"
    )

    plt.xlabel("Yıl")
    plt.ylabel("Ortalama Sıcaklık (°C)")

    plt.legend()
    plt.grid(True)

    plt.tight_layout()

    # Grafiği kaydet
    plt.savefig(
        r"C:\Users\ahmet\PycharmProjects\Turkiye_Iklim_Analizi\graphs\mevsimsel_sicaklik_trendleri.png",
        dpi=300,
        bbox_inches="tight"
    )

    plt.close()

    # --------------------------------
    # MEVSİMSEL YAĞIŞ TRENDLERİ
    # --------------------------------

    print("\nMEVSİMSEL YAĞIŞ TRENDLERİ")
    print("=" * 70)

    for mevsim in sirasi:
        veri = df[df["mevsim"] == mevsim]

        # Her yıl için mevsim toplam yağışı
        yillik_mevsim = veri.groupby("yil")["yagis_mm"].sum()

        x = yillik_mevsim.index
        y = yillik_mevsim.values

        sonuc = linregress(x, y)

        print(f"\n{mevsim}")
        print(f"Eğim: {sonuc.slope:.4f} mm/yıl")
        print(f"10 yıllık değişim: {sonuc.slope * 10:.4f} mm")
        print(f"R²: {sonuc.rvalue ** 2:.4f}")
        print(f"p-değeri: {sonuc.pvalue:.4f}")

        # --------------------------------
        # MEVSİMSEL YAĞIŞ TREND GRAFİĞİ
        # --------------------------------

        plt.figure(figsize=(12, 7))

        for mevsim in sirasi:
            veri = df[df["mevsim"] == mevsim]

            # Her yıl için mevsim toplam yağışı
            yillik_mevsim = veri.groupby("yil")["yagis_mm"].sum()

            x = yillik_mevsim.index
            y = yillik_mevsim.values

            # Gerçek yağış değerleri
            plt.plot(
                x,
                y,
                marker="o",
                label=mevsim
            )

            # Regresyon trendi
            sonuc = linregress(x, y)

            trend = sonuc.intercept + sonuc.slope * x

            plt.plot(
                x,
                trend,
                linestyle="--"
            )

        plt.title(
            "Çanakkale Mevsimsel Toplam Yağış Trendleri (2000-2025)"
        )

        plt.xlabel("Yıl")
        plt.ylabel("Toplam Yağış (mm)")

        plt.legend()
        plt.grid(True)

        plt.tight_layout()

        plt.savefig(
            r"C:\Users\ahmet\PycharmProjects\Turkiye_Iklim_Analizi\graphs\mevsimsel_yagis_trendleri.png",
            dpi=300,
            bbox_inches="tight"
        )

        plt.close()


# --------------------------------
# AYKIRI DEĞER ANALİZİ
# --------------------------------

import numpy as np

# Yıllık sıcaklık ve yağış verilerini oluştur
yillik = df.groupby("yil").agg(
    ortalama_sicaklik=("sicaklik_C", "mean"),
    toplam_yagis=("yagis_mm", "sum")
).reset_index()

print("\nYILLIK VERİLER")
print(yillik)

def iqr_aykiri_degerler(veri, sutun):

    Q1 = veri[sutun].quantile(0.25)
    Q3 = veri[sutun].quantile(0.75)

    IQR = Q3 - Q1

    alt_sinir = Q1 - 1.5 * IQR
    ust_sinir = Q3 + 1.5 * IQR

    aykirilar = veri[
        (veri[sutun] < alt_sinir) |
        (veri[sutun] > ust_sinir)
    ]

    return Q1, Q3, IQR, alt_sinir, ust_sinir, aykirilar

Q1, Q3, IQR, alt, ust, aykirilar = iqr_aykiri_degerler(
    yillik,
    "ortalama_sicaklik"
)

print("\nSICAKLIK IQR ANALİZİ")
print(f"Q1: {Q1:.2f}")
print(f"Q3: {Q3:.2f}")
print(f"IQR: {IQR:.2f}")
print(f"Alt sınır: {alt:.2f}")
print(f"Üst sınır: {ust:.2f}")

print("\nAykırı sıcaklık yılları:")
print(aykirilar)


Q1, Q3, IQR, alt, ust, aykirilar = iqr_aykiri_degerler(
    yillik,
    "toplam_yagis"
)

print("\nYAĞIŞ IQR ANALİZİ")
print(f"Q1: {Q1:.2f}")
print(f"Q3: {Q3:.2f}")
print(f"IQR: {IQR:.2f}")
print(f"Alt sınır: {alt:.2f}")
print(f"Üst sınır: {ust:.2f}")

print("\nAykırı yağış yılları:")
print(aykirilar)


# --------------------------------
# Z-SKORU ANALİZİ
# --------------------------------

yillik["sicaklik_z"] = (
    yillik["ortalama_sicaklik"] -
    yillik["ortalama_sicaklik"].mean()
) / yillik["ortalama_sicaklik"].std()

yillik["yagis_z"] = (
    yillik["toplam_yagis"] -
    yillik["toplam_yagis"].mean()
) / yillik["toplam_yagis"].std()


print("\nZ-SKORU > |2| OLAN SICAKLIK YILLARI")
print(
    yillik[abs(yillik["sicaklik_z"]) > 2]
)

print("\nZ-SKORU > |2| OLAN YAĞIŞ YILLARI")
print(
    yillik[abs(yillik["yagis_z"]) > 2]
)


# --------------------------------
# AYKIRI DEĞER BOXPLOT GRAFİKLERİ
# --------------------------------

# YILLIK SICAKLIK BOXPLOT
plt.figure(figsize=(8, 6))

plt.boxplot(
    yillik["ortalama_sicaklik"],
    tick_labels=["Yıllık Ortalama Sıcaklık"]
)

plt.title("Çanakkale Yıllık Ortalama Sıcaklık Boxplotu (2000-2025)")
plt.ylabel("Sıcaklık (°C)")
plt.grid(axis="y", alpha=0.3)

plt.tight_layout()

plt.savefig(
    r"C:\Users\ahmet\PycharmProjects\Turkiye_Iklim_Analizi\graphs\yillik_sicaklik_boxplot.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()


# YILLIK YAĞIŞ BOXPLOT
plt.figure(figsize=(8, 6))

plt.boxplot(
    yillik["toplam_yagis"],
    tick_labels=["Yıllık Toplam Yağış"]
)

plt.title("Çanakkale Yıllık Toplam Yağış Boxplotu (2000-2025)")
plt.ylabel("Yağış (mm)")
plt.grid(axis="y", alpha=0.3)

plt.tight_layout()

plt.savefig(
    r"C:\Users\ahmet\PycharmProjects\Turkiye_Iklim_Analizi\graphs\yillik_yagis_boxplot.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()

print("\nBoxplot grafikleri başarıyla kaydedildi.")


# --------------------------------
# SICAKLIK - YAĞIŞ KORELASYON ANALİZİ
# --------------------------------

from scipy.stats import pearsonr, spearmanr

# Pearson korelasyonu
r_pearson, p_pearson = pearsonr(
    yillik["ortalama_sicaklik"],
    yillik["toplam_yagis"]
)

print("\n--------------------------------")
print("SICAKLIK - YAĞIŞ KORELASYONU")
print("--------------------------------")

print(f"Pearson korelasyon katsayısı: {r_pearson:.4f}")
print(f"p-değeri: {p_pearson:.4f}")


# Spearman korelasyonu
r_spearman, p_spearman = spearmanr(
    yillik["ortalama_sicaklik"],
    yillik["toplam_yagis"]
)

print(f"Spearman korelasyon katsayısı: {r_spearman:.4f}")
print(f"Spearman p-değeri: {p_spearman:.4f}")


# --------------------------------
# SICAKLIK - YAĞIŞ SCATTER PLOT
# --------------------------------

plt.figure(figsize=(11, 7))

x = yillik["ortalama_sicaklik"]
y = yillik["toplam_yagis"]

# Noktaları çiz
plt.scatter(x, y)

# Her noktanın yanına yılını yaz
for _, satir in yillik.iterrows():
    plt.annotate(
        str(int(satir["yil"])),
        (satir["ortalama_sicaklik"], satir["toplam_yagis"]),
        xytext=(5, 5),
        textcoords="offset points",
        fontsize=8
    )

# Regresyon doğrusu
sonuc = linregress(x, y)

trend = sonuc.intercept + sonuc.slope * x

plt.plot(
    x,
    trend,
    linestyle="--",
    label="Regresyon doğrusu"
)

# Korelasyon bilgilerini grafiğe yaz
plt.text(
    0.05,
    0.95,
    f"Pearson r = {r_pearson:.4f}\np = {p_pearson:.4f}",
    transform=plt.gca().transAxes,
    verticalalignment="top"
)

plt.title(
    "Çanakkale Yıllık Ortalama Sıcaklık - Toplam Yağış İlişkisi (2000-2025)"
)

plt.xlabel("Yıllık Ortalama Sıcaklık (°C)")
plt.ylabel("Yıllık Toplam Yağış (mm)")

plt.legend()
plt.grid(True, alpha=0.3)

plt.tight_layout()

plt.savefig(
    r"C:\Users\ahmet\PycharmProjects\Turkiye_Iklim_Analizi\graphs\sicaklik_yagis_korelasyon.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()

print("\nSıcaklık-yağış korelasyon grafiği başarıyla kaydedildi.")


# --------------------------------
# 2010 DUYARLILIK ANALİZİ
# --------------------------------

# 2010 dahil korelasyon
r_dahil, p_dahil = pearsonr(
    yillik["ortalama_sicaklik"],
    yillik["toplam_yagis"]
)

# 2010 hariç veri
yillik_2010_haric = yillik[yillik["yil"] != 2010]

# 2010 hariç Pearson korelasyonu
r_haric, p_haric = pearsonr(
    yillik_2010_haric["ortalama_sicaklik"],
    yillik_2010_haric["toplam_yagis"]
)

# 2010 hariç Spearman korelasyonu
rho_haric, p_rho_haric = spearmanr(
    yillik_2010_haric["ortalama_sicaklik"],
    yillik_2010_haric["toplam_yagis"]
)

print("\n--------------------------------")
print("2010 DUYARLILIK ANALİZİ")
print("--------------------------------")

print("\n2010 DAHİL:")
print(f"Pearson r: {r_dahil:.4f}")
print(f"Pearson p: {p_dahil:.4f}")

print("\n2010 HARİÇ:")
print(f"Pearson r: {r_haric:.4f}")
print(f"Pearson p: {p_haric:.4f}")
print(f"Spearman rho: {rho_haric:.4f}")
print(f"Spearman p: {p_rho_haric:.4f}")


# --------------------------------
# 5 YILLIK HAREKETLİ ORTALAMA
# --------------------------------

yillik["sicaklik_5y_ortalama"] = (
    yillik["ortalama_sicaklik"]
    .rolling(window=5)
    .mean()
)

yillik["yagis_5y_ortalama"] = (
    yillik["toplam_yagis"]
    .rolling(window=5)
    .mean()
)

print("\n5 YILLIK HAREKETLİ ORTALAMA")
print(
    yillik[
        [
            "yil",
            "ortalama_sicaklik",
            "sicaklik_5y_ortalama",
            "toplam_yagis",
            "yagis_5y_ortalama"
        ]
    ].round(2)
)

# --------------------------------
# SICAKLIK 5 YILLIK HAREKETLİ ORTALAMA
# --------------------------------

plt.figure(figsize=(12, 7))

plt.plot(
    yillik["yil"],
    yillik["ortalama_sicaklik"],
    marker="o",
    alpha=0.5,
    label="Yıllık Ortalama Sıcaklık"
)

plt.plot(
    yillik["yil"],
    yillik["sicaklik_5y_ortalama"],
    linewidth=3,
    label="5 Yıllık Hareketli Ortalama"
)

plt.title(
    "Çanakkale Sıcaklık ve 5 Yıllık Hareketli Ortalama (2000-2025)"
)

plt.xlabel("Yıl")
plt.ylabel("Sıcaklık (°C)")

plt.legend()
plt.grid(True, alpha=0.3)

plt.tight_layout()

plt.savefig(
    r"C:\Users\ahmet\PycharmProjects\Turkiye_Iklim_Analizi\graphs\sicaklik_5y_hareketli_ortalama.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()

print("\nSıcaklık hareketli ortalama grafiği kaydedildi.")


# --------------------------------
# YAĞIŞ 5 YILLIK HAREKETLİ ORTALAMA
# --------------------------------

plt.figure(figsize=(12, 7))

plt.plot(
    yillik["yil"],
    yillik["toplam_yagis"],
    marker="o",
    alpha=0.5,
    label="Yıllık Toplam Yağış"
)

plt.plot(
    yillik["yil"],
    yillik["yagis_5y_ortalama"],
    linewidth=3,
    label="5 Yıllık Hareketli Ortalama"
)

plt.title(
    "Çanakkale Yağış ve 5 Yıllık Hareketli Ortalama (2000-2025)"
)

plt.xlabel("Yıl")
plt.ylabel("Yağış (mm)")

plt.legend()
plt.grid(True, alpha=0.3)

plt.tight_layout()

plt.savefig(
    r"C:\Users\ahmet\PycharmProjects\Turkiye_Iklim_Analizi\graphs\yagis_5y_hareketli_ortalama.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()

print("\nYağış hareketli ortalama grafiği kaydedildi.")


# --------------------------------
# DÖNEMSEL KARŞILAŞTIRMA
# --------------------------------

donemler = pd.cut(
    yillik["yil"],
    bins=[1999, 2010, 2020, 2025],
    labels=["2000-2010", "2011-2020", "2021-2025"]
)

donem_analizi = yillik.groupby(
    donemler,
    observed=False
).agg(
    ortalama_sicaklik=("ortalama_sicaklik", "mean"),
    ortalama_yagis=("toplam_yagis", "mean"),
    std_yagis=("toplam_yagis", "std"),
    min_yagis=("toplam_yagis", "min"),
    max_yagis=("toplam_yagis", "max")
)

print("\n--------------------------------")
print("DÖNEMSEL İKLİM KARŞILAŞTIRMASI")
print("--------------------------------")

print(donem_analizi.round(2))



from scipy.stats import mannwhitneyu

# --------------------------------
# 2021 SONRASI YAĞIŞ DÜŞÜŞÜ
# İSTATİSTİKSEL TEST
# --------------------------------

yagis_2011_2020 = yillik[
    (yillik["yil"] >= 2011) &
    (yillik["yil"] <= 2020)
]["toplam_yagis"]

yagis_2021_2025 = yillik[
    (yillik["yil"] >= 2021) &
    (yillik["yil"] <= 2025)
]["toplam_yagis"]

# Mann-Whitney U testi
u_stat, p_degeri = mannwhitneyu(
    yagis_2011_2020,
    yagis_2021_2025,
    alternative="two-sided"
)

print("\n--------------------------------")
print("2021 SONRASI YAĞIŞ DÜŞÜŞÜ TESTİ")
print("--------------------------------")

print(f"2011-2020 ortalama yağış: {yagis_2011_2020.mean():.2f} mm")
print(f"2021-2025 ortalama yağış: {yagis_2021_2025.mean():.2f} mm")

print(f"\nMann-Whitney U istatistiği: {u_stat:.2f}")
print(f"p-değeri: {p_degeri:.4f}")

if p_degeri < 0.05:
    print("Sonuç: İki dönem arasında istatistiksel olarak anlamlı fark vardır.")
else:
    print("Sonuç: İki dönem arasında istatistiksel olarak anlamlı fark bulunamamıştır.")



# --------------------------------
# MEVSİMSEL YAĞIŞ DÖNEM KARŞILAŞTIRMASI
# --------------------------------

from scipy.stats import mannwhitneyu

print("\n================================")
print("MEVSİMSEL YAĞIŞ DÖNEM KARŞILAŞTIRMASI")
print("================================")

mevsimler = ["Kış", "İlkbahar", "Yaz", "Sonbahar"]

for mevsim in mevsimler:

    veri = df[df["mevsim"] == mevsim]

    # 2000-2012
    donem_1 = veri[
        (veri["yil"] >= 2000) &
        (veri["yil"] <= 2012)
    ]["yagis_mm"]

    # 2013-2025
    donem_2 = veri[
        (veri["yil"] >= 2013) &
        (veri["yil"] <= 2025)
    ]["yagis_mm"]

    u, p = mannwhitneyu(
        donem_1,
        donem_2,
        alternative="two-sided"
    )

    ortalama_1 = donem_1.mean()
    ortalama_2 = donem_2.mean()

    degisim = ortalama_2 - ortalama_1

    print(f"\n{mevsim}")
    print("-" * 30)

    print(f"2000-2012 ortalaması: {ortalama_1:.2f} mm")
    print(f"2013-2025 ortalaması: {ortalama_2:.2f} mm")
    print(f"Değişim: {degisim:.2f} mm")

    print(f"Mann-Whitney U: {u:.2f}")
    print(f"p-değeri: {p:.4f}")

    if p < 0.05:
        print("Sonuç: İstatistiksel olarak anlamlı fark var.")
    else:
        print("Sonuç: İstatistiksel olarak anlamlı fark yok.")


# --------------------------------
# MEVSİMSEL SICAKLIK DÖNEM KARŞILAŞTIRMASI
# --------------------------------

print("\n================================")
print("MEVSİMSEL SICAKLIK DÖNEM KARŞILAŞTIRMASI")
print("================================")

mevsimler = ["Kış", "İlkbahar", "Yaz", "Sonbahar"]

for mevsim in mevsimler:

    veri = df[df["mevsim"] == mevsim]

    # 2000-2012
    donem_1 = veri[
        (veri["yil"] >= 2000) &
        (veri["yil"] <= 2012)
    ]["sicaklik_C"]

    # 2013-2025
    donem_2 = veri[
        (veri["yil"] >= 2013) &
        (veri["yil"] <= 2025)
    ]["sicaklik_C"]

    # Mann-Whitney U testi
    u, p = mannwhitneyu(
        donem_1,
        donem_2,
        alternative="two-sided"
    )

    ortalama_1 = donem_1.mean()
    ortalama_2 = donem_2.mean()

    degisim = ortalama_2 - ortalama_1

    print(f"\n{mevsim}")
    print("-" * 30)

    print(f"2000-2012 ortalaması: {ortalama_1:.2f} °C")
    print(f"2013-2025 ortalaması: {ortalama_2:.2f} °C")
    print(f"Değişim: {degisim:.2f} °C")

    print(f"Mann-Whitney U: {u:.2f}")
    print(f"p-değeri: {p:.4f}")

    if p < 0.05:
        print("Sonuç: İstatistiksel olarak anlamlı fark var.")
    else:
        print("Sonuç: İstatistiksel olarak anlamlı fark yok.")