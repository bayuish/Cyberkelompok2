def hitung_gaji(karyawan, golongan, jam_kerja):
    if golongan == "A":
        gaji_per_jam = 5000
    elif golongan == "B":
        gaji_per_jam = 7000
    elif golongan == "C":
        gaji_per_jam = 8000
    elif golongan == "D":
        gaji_per_jam = 10000
    else:
        return "Golongan yang dimasukkan tidak valid."

    if jam_kerja > 48:
        jam_lembur = jam_kerja - 48
        gaji = (48 * gaji_per_jam) + (jam_lembur * gaji_per_jam * 1.5)
    else:
        gaji = jam_kerja * gaji_per_jam

    return "Nama karyawan: {}\nGaji yang diterima: {}".format(karyawan, gaji)

# Input karyawan, golongan, dan jam kerja
nama_karyawan = input("Masukkan nama karyawan: ")
golongan = input("Masukkan golongan (A/B/C/D): ")
jam_kerja = float(input("Masukkan jumlah jam kerja: "))

# Memanggil fungsi hitung_gaji dan mencetak outputnya
print(hitung_gaji(nama_karyawan, golongan, jam_kerja))
print("aku")
