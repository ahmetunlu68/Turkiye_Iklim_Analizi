# Çanakkale'nin 2000–2025 Dönemi İklim Verilerinin İstatistiksel Analizi

## 📌 Proje Hakkında

Bu proje, **Çanakkale'nin 2000–2025 yılları arasındaki sıcaklık ve yağış verilerinin istatistiksel yöntemler kullanılarak incelenmesini** amaçlamaktadır.

Çalışmada aylık iklim verileri kullanılarak yıllık ve mevsimsel değişimler, uzun dönemli trendler, hareketli ortalamalar, aykırı değerler ve sıcaklık ile yağış arasındaki ilişki analiz edilmiştir.

Projenin temel amacı, iklim verilerini yalnızca görselleştirmek yerine **istatistiksel yöntemlerle yorumlamak ve uzun dönemli değişimleri ortaya koymaktır.**

---

## 📊 Kullanılan Veri

Veriler **Copernicus Climate Change Service (C3S) – ERA5-Land** veri setinden elde edilmiştir.

* **Konum:** Çanakkale, Türkiye
* **Dönem:** 2000–2025
* **Gözlem sayısı:** 312 aylık gözlem
* **Değişkenler:**

  * Sıcaklık
  * Yağış
* **Sıcaklık birimi:** °C
* **Yağış birimi:** mm

---

## 🛠️ Kullanılan Teknolojiler

* **Python**
* **Pandas** – Veri işleme ve analiz
* **NumPy** – Sayısal hesaplamalar
* **Xarray** – NetCDF iklim verilerinin işlenmesi
* **Matplotlib** – Veri görselleştirme
* **SciPy** – İstatistiksel testler
* **Copernicus / ERA5-Land** – İklim verileri

---

## 🔎 Yapılan Analizler

### Tanımlayıcı İstatistikler

Sıcaklık ve yağış değişkenleri için:

* Ortalama
* Medyan
* Standart sapma
* Minimum
* Maksimum

değerleri hesaplanmıştır.

### 📈 Trend Analizi

Yıllık sıcaklık ve yağış değerlerinin zaman içerisindeki değişimi doğrusal regresyon kullanılarak incelenmiştir.

**Sıcaklık:**

* Trend eğimi: **+0.0504 °C/yıl**
* Yaklaşık değişim: **+0.504 °C/on yıl**
* R²: **0.4158**
* p-değeri: **0.0004**

Bu sonuç, incelenen dönem içerisinde sıcaklıkta istatistiksel olarak anlamlı bir artış eğilimi olduğunu göstermektedir.

**Yağış:**

* Trend eğimi: **−3.014 mm/yıl**
* Yaklaşık değişim: **−30.14 mm/on yıl**
* R²: **0.0231**
* p-değeri: **0.4581**

Yağışta azalış yönünde bir eğilim görülmesine rağmen bu trend istatistiksel olarak anlamlı değildir.

---

## 🌡️ Sıcaklık Analizi

2000–2025 dönemindeki genel sıcaklık istatistikleri:

| İstatistik     |    Değer |
| -------------- | -------: |
| Ortalama       | 15.86 °C |
| Medyan         | 15.33 °C |
| Standart Sapma |  6.97 °C |
| Minimum        |  2.20 °C |
| Maksimum       | 27.98 °C |

5 yıllık hareketli ortalama analizi, dönem içerisinde sıcaklıkların genel olarak yükselen bir eğilim gösterdiğini ortaya koymaktadır.

---

## 🌧️ Yağış Analizi

Yağış için hesaplanan temel istatistikler:

| İstatistik     |     Değer |
| -------------- | --------: |
| Ortalama       |  52.80 mm |
| Medyan         |  41.80 mm |
| Standart Sapma |  47.16 mm |
| Minimum        |   0.33 mm |
| Maksimum       | 298.32 mm |

Yağış değişkeninde özellikle **2010 yılı** belirgin bir aykırı değer olarak öne çıkmaktadır.

---

## 🍂 Mevsimsel Analiz

| Mevsim   | Ortalama Sıcaklık | Ortalama Yağış |
| -------- | ----------------: | -------------: |
| Kış      |           7.62 °C |       87.90 mm |
| İlkbahar |          13.80 °C |       53.30 mm |
| Yaz      |          25.00 °C |       14.51 mm |
| Sonbahar |          17.05 °C |       55.50 mm |

Mevsimsel trend analizinde özellikle **kış ve sonbahar sıcaklıklarında anlamlı artış eğilimleri** görülmüştür.

* Kış sıcaklık trendi: **+0.0866 °C/yıl**, p = 0.0011
* Sonbahar sıcaklık trendi: **+0.0616 °C/yıl**, p = 0.0093

---

## 📉 Korelasyon Analizi

Sıcaklık ve yağış arasındaki Pearson korelasyon katsayısı:

**r = −0.0169**

**p = 0.9348**

Bu sonuç, incelenen veri setinde sıcaklık ile yağış arasında anlamlı bir doğrusal ilişki bulunmadığını göstermektedir.

2010 yılındaki yağış aykırı değeri çıkarıldığında korelasyon:

**r = −0.1456**, p = 0.4873

olmuştur. Bu durumda da istatistiksel olarak anlamlı bir ilişki bulunmamıştır.

---

## 📌 Aykırı Değer Analizi

Yağış değişkeni için IQR yöntemi kullanılmıştır.

2010 yılı yağış değeri belirlenen üst sınırın üzerinde olduğu için **aykırı gözlem** olarak tespit edilmiştir.

Sıcaklık değişkeninde IQR yöntemine göre belirgin bir aykırı değer bulunmamıştır.

---

## 📊 Görselleştirmeler

Projede aşağıdaki grafikler oluşturulmuştur:

### Yıllık Sıcaklık

![Yıllık Sıcaklık](graphs/yillik_sicaklik_2000_2025.png)

### Yıllık Yağış

![Yıllık Yağış](graphs/yillik_yagis_2000_2025.png)

### Sıcaklık – 5 Yıllık Hareketli Ortalama

![Sıcaklık Hareketli Ortalama](graphs/sicaklik_5y_hareketli_ortalama.png)

### Yağış – 5 Yıllık Hareketli Ortalama

![Yağış Hareketli Ortalama](graphs/yagis_5y_hareketli_ortalama.png)

### Mevsimsel Sıcaklık Trendleri

![Mevsimsel Sıcaklık](graphs/mevsimsel_sicaklik_trendleri.png)

### Mevsimsel Yağış Trendleri

![Mevsimsel Yağış](graphs/mevsimsel_yagis_trendleri.png)

### Sıcaklık – Yağış Korelasyonu

![Sıcaklık Yağış Korelasyonu](graphs/sicaklik_yagis_korelasyon.png)

### Yıllık Sıcaklık Boxplot

![Sıcaklık Boxplot](graphs/yillik_sicaklik_boxplot.png)

### Yıllık Yağış Boxplot

![Yağış Boxplot](graphs/yillik_yagis_boxplot.png)

---

## 📁 Proje Yapısı

```text
Turkiye_Iklim_Analizi/
│
├── data/
│   └── canakkale_2000_2025.csv
│
├── graphs/
│   ├── mevsimsel_sicaklik_trendleri.png
│   ├── mevsimsel_yagis_trendleri.png
│   ├── sicaklik_5y_hareketli_ortalama.png
│   ├── sicaklik_yagis_korelasyon.png
│   ├── yagis_5y_hareketli_ortalama.png
│   ├── yillik_sicaklik_2000_2025.png
│   ├── yillik_sicaklik_boxplot.png
│   ├── yillik_yagis_2000_2025.png
│   └── yillik_yagis_boxplot.png
│
├── src/
│   ├── canakkale_csv_olustur.py
│   ├── canakkale_veri_topla.py
│   ├── istatistik_analizi.py
│   ├── mevsim_analizi.py
│   ├── test_copernicus.py
│   ├── veri_incele.py
│   └── veri_indir.py
│
└── README.md
```

---

## 🎯 Sonuç

2000–2025 dönemine ait Çanakkale iklim verilerinin incelenmesi sonucunda sıcaklıklarda **istatistiksel olarak anlamlı bir artış eğilimi** tespit edilmiştir.

Yağış miktarında azalış yönünde bir eğilim gözlenmesine rağmen bu değişim istatistiksel olarak anlamlı değildir. Mevsimsel analizler ise özellikle kış ve sonbahar sıcaklıklarında belirgin artışlar olduğunu göstermektedir.

Bu çalışma, Python kullanılarak gerçek iklim verileri üzerinde **veri temizleme, istatistiksel analiz, trend analizi, hipotez testi ve veri görselleştirme** süreçlerinin uygulanmasını içeren bir veri analizi projesidir.

---

## 👨‍💻 Geliştirici

**Ahmet Ünlü**

İstatistik Öğrencisi | Veri Analizi ve Veri Bilimi

GitHub: [@ahmetunlu68](https://github.com/ahmetunlu68)
