print ("## Program Python Diskon Potongan Harga ##")
print ("==========================================")

total_belanja = int(input("Total Belanja: "))

if total_belanja < 100000:
    diskon = 0
    x= total_belanja - (total_belanja * diskon) 
    print ("Selamat, anda mendapatkan diskon {}%".format(diskon))
    print ("Total bayar: Rp.{}".format(x))
elif total_belanja <= 500000:
    diskon = 0.1
    x= total_belanja - (total_belanja * diskon) 
    print ("Selamat, anda mendapatkan diskon 10%")
    print ("Total bayar: Rp.{}".format(x))
elif total_belanja <= 1000000:
    diskon = 0.2
    x= total_belanja - (total_belanja * diskon) 
    print ("Selamat, anda mendapatkan diskon 20%")
    print ("Total bayar: Rp.{}".format(x))
else:
    diskon = 0.3
    x = total_belanja - (total_belanja * diskon) 
    print ("Selamat, anda mendapatkan diskon 30%")
    print ("Total bayar: Rp.{}".format(x))



