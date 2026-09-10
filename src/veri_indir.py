import os
import cdsapi

# Copernicus ayar dosyası
os.environ["CDSAPI_RC"] = (
    r"C:\Users\ahmet\PycharmProjects\Turkiye_Iklim_Analizi\cds_config.txt"
)

# Proje klasörü
project_folder = r"C:\Users\ahmet\PycharmProjects\Turkiye_Iklim_Analizi"

# Veri klasörünü oluştur
data_folder = os.path.join(project_folder, "data")
os.makedirs(data_folder, exist_ok=True)

# Dosyanın kaydedileceği yer
output_file = os.path.join(data_folder, "test_2025_01.nc")

client = cdsapi.Client()

client.retrieve(
    "reanalysis-era5-land-monthly-means",
    {
        "product_type": "monthly_averaged_reanalysis",
        "variable": [
            "2m_temperature",
            "total_precipitation"
        ],
        "year": "2025",
        "month": "01",
        "time": "00:00",
        "data_format": "netcdf",
        "download_format": "unarchived"
    },
    output_file
)

print("Veri başarıyla indirildi!")
print("Dosya:", output_file)