import os
import cdsapi

os.environ["CDSAPI_RC"] = r"C:\Users\ahmet\PycharmProjects\Turkiye_Iklim_Analizi\cds_config.txt"

client = cdsapi.Client()

print("Copernicus bağlantısı başarılı!")