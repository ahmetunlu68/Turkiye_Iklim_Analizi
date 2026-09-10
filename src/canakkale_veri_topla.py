import os
import cdsapi

# --------------------------------
# 1. Copernicus ayar dosyası
# --------------------------------

os.environ["CDSAPI_RC"] = (
    r"C:\Users\ahmet\PycharmProjects\Turkiye_Iklim_Analizi\cds_config.txt"
)

# --------------------------------
# 2. Proje ve veri klasörü
# --------------------------------

project_folder = r"C:\Users\ahmet\PycharmProjects\Turkiye_Iklim_Analizi"

data_folder = os.path.join(project_folder, "data")

os.makedirs(data_folder, exist_ok=True)

# --------------------------------
# 3. Copernicus bağlantısı
# --------------------------------

client = cdsapi.Client()

# --------------------------------
# 4. Veri isteği
# --------------------------------

client.retrieve(
    "reanalysis-era5-land-monthly-means",
    {
        "product_type": "monthly_averaged_reanalysis",

        "variable": [
            "2m_temperature",
            "total_precipitation"
        ],

        "year": [
            str(yil) for yil in range(2000, 2026)
        ],

        "month": [
            "01", "02", "03", "04",
            "05", "06", "07", "08",
            "09", "10", "11", "12"
        ],

        "time": "00:00",

        # Çanakkale çevresi
        # Kuzey, Batı, Güney, Doğu
        "area": [
            40.5,
            26.0,
            39.8,
            26.8
        ],

        "data_format": "netcdf",

        "download_format": "unarchived"
    },

    os.path.join(data_folder, "canakkale_2000_2025.nc")
)

print("Çanakkale verileri başarıyla indirildi!")