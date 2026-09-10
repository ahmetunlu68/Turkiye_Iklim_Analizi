import xarray as xr

dosya = r"C:\Users\ahmet\PycharmProjects\Turkiye_Iklim_Analizi\data\canakkale_2000_2025.nc"

veri = xr.open_dataset(dosya)

print(veri)