import tkinter as tk
from PIL import Image, ImageTk

def create_empty_page():
    # Membuat jendela halaman kosong
    empty_window = tk.Toplevel(window)
    empty_window.title("Halaman Kosong")

    # Membuat input dan output
    input_label = tk.Label(empty_window, text="Total Belanja: ")
    input_label.pack()
    input_entry = tk.Entry(empty_window)
    input_entry.pack()

    def calculate_discount():
        total_belanja = int(input_entry.get())
        
        # Menghitung diskon
        if total_belanja < 100000:
            diskon = 0
        elif total_belanja <= 500000:
            diskon = 0.1
        elif total_belanja <= 1000000:
            diskon = 0.2
        else:
            diskon = 0.3

        x = total_belanja - (total_belanja * diskon)
        
        # Menampilkan hasil
        if diskon > 0:
            output_text = "Selamat, anda mendapatkan diskon {}%\n".format(diskon * 100)
        else:
            output_text = "Maaf, tidak ada diskon yang tersedia.\n"

        output_text += "Total bayar: Rp.{}".format(x)

        output_label = tk.Label(empty_window, text=output_text, pady=10)
        output_label.pack()

    # Tombol untuk menghitung diskon
    calculate_button = tk.Button(empty_window, text="Hitung Diskon", command=calculate_discount)
    calculate_button.pack()

def halamanbaru():
    empty_window = tk.Toplevel(window)
    empty_window.title("Halaman Kosong")

    # Membuat input dan output
    input_label = tk.Label(empty_window, text="Nama Karyawan: ")
    input_label.pack()
    input_entry_karyawan = tk.Entry(empty_window)
    input_entry_karyawan.pack()

    input_label = tk.Label(empty_window, text="Golongan A/B/C/D: ")
    input_label.pack()
    input_entry_golongan = tk.Entry(empty_window)
    input_entry_golongan.pack()

    input_label = tk.Label(empty_window, text="Jam Kerja: ")
    input_label.pack()
    input_entry_jam_kerja = tk.Entry(empty_window)
    input_entry_jam_kerja.pack()

    def calculate_salary():
        karyawan = input_entry_karyawan.get()
        golongan = input_entry_golongan.get()
        jam_kerja = float(input_entry_jam_kerja.get())
        
        if golongan == "A":
            gaji_per_jam = 5000
        elif golongan == "B":
            gaji_per_jam = 7000
        elif golongan == "C":
            gaji_per_jam = 8000
        elif golongan == "D":
            gaji_per_jam = 10000
        else:
            output_text = "Golongan yang dimasukkan tidak valid."
            output_label = tk.Label(empty_window, text=output_text, pady=10)
            output_label.pack()
            return

        if jam_kerja > 48:
            jam_lembur = jam_kerja - 48
            gaji = (48 * gaji_per_jam) + (jam_lembur * gaji_per_jam * 1.5)
        else:
            gaji = jam_kerja * gaji_per_jam

        output_text = "Nama karyawan: {}\nGaji yang diterima: {}".format(karyawan, gaji)

        output_label = tk.Label(empty_window, text=output_text, pady=10)
        output_label.pack()

    # Tombol untuk menghitung gaji
    calculate_button = tk.Button(empty_window, text="Hitung Gaji", command=calculate_salary)
    calculate_button.pack()


# Membuat jendela utama
window = tk.Tk()
window.title("Contoh GUI dengan Tkinter")

# Membuat elemen-elemen GUI
label = tk.Label(window, text="Hallo Abang Kaka Selamat Datang di TeamTwoCybersecurity!")
label.pack()

button = tk.Button(window, text="Our Team!")
button.pack()

entry = tk.Entry(window)
entry.pack()

# Menambahkan fungsi untuk event klik tombol
def button_clicked():
    input_text = entry.get()
    label.config(text="Team kami beranggotakan: " + input_text)
    button.destroy()  # Menghapus tombol
    entry.destroy()  # Menghapus kotak input

    # Membuka dan menampilkan gambar 1
    image1 = Image.open("bayu.jpg")
    image1 = image1.resize((100, 100))
    photo1 = ImageTk.PhotoImage(image1)
    photo_label1 = tk.Label(window, image=photo1)
    photo_label1.image = photo1
    label1 = tk.Label(window, text="Bayu Lesmana")
    photo_label1.pack(side=tk.LEFT)
    label1.pack(side=tk.LEFT)

    # Membuka dan menampilkan gambar 2
    image2 = Image.open("surya.jpg")
    image2 = image2.resize((100, 100))
    photo2 = ImageTk.PhotoImage(image2)
    photo_label2 = tk.Label(window, image=photo2)
    photo_label2.image = photo2
    label2 = tk.Label(window, text="Surya Pratama")
    photo_label2.pack(side=tk.LEFT)
    label2.pack(side=tk.LEFT)

    # Membuka dan menampilkan gambar 3
    image3 = Image.open("ikhsan.jpg")
    image3 = image3.resize((100, 100))
    photo3 = ImageTk.PhotoImage(image3)
    photo_label3 = tk.Label(window, image=photo3)
    photo_label3.image = photo3
    label3 = tk.Label(window, text="Ikhsan Siregar")
    photo_label3.pack(side=tk.LEFT)
    label3.pack(side=tk.LEFT)

    # Mengatur tata letak tombol 1 dan tombol 2
    button_frame = tk.Frame(window)
    button_frame.pack()
    button1 = tk.Button(button_frame, text="Tombol 1", command=create_empty_page)
    button1.pack()
    button2 = tk.Button(button_frame, text="Tombol 2", command=halamanbaru)
    button2.pack()

button.config(command=button_clicked)

# Menjalankan loop utama GUI
window.mainloop()
