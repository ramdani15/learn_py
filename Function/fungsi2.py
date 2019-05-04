# deklarasi print ganjil
def ganjil():
    print("Angka yang dimasukkan adalah Ganjil")

# deklarasi print genap
def genap():
    print("Angka yang dimasukkan adalah Genap")

def cek_ganjil_genap(angka):
    if angka % 2 == 0:
        genap()
    else:
        ganjil()

n = input("Masukkan nilai : ")
nilai = int(n)
cek_ganjil_genap(nilai)