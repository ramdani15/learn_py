def welcome(nama_anda):
    print("Selamat Datang " + nama_anda)

nama = input("Masukkan nama : ")
# welcome(nama)

def luas_persegi_panjang(panjang, lebar):
    luas = panjang * lebar
    print("Luas " + str(luas))
    return luas

l = input("Masukkan lebar : ")
p = input("Masukkan panjang : ")

l_kirim = int(l)
p_kirim = int(p)

hasil = luas_persegi_panjang(p_kirim, l_kirim)
total = hasil + 10

print("Luas persegi panjang adalah " + str(hasil))
print("Total adalah " + str(total))