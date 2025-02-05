# Algoritma menghitung akar
# programmer : Eunra
# tanggal di buat : Rabu, 5 Februari 2025
# jenis variabel : tipe float

import math

# input angka dari user
angka: float = float(input("Masukkan angka: "))

# cek apakah angka nya negatif
if angka < 0:
    print("Error: Tidak bisa menghitung akar dari bilangan negatif.")
else:
    hasil: float = math.sqrt(angka)
    print(f"Akar dari {angka} adalah {hasil}")