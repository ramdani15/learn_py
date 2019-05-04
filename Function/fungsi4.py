def cek_grade(nilai):
    if nilai >= 90:
        print("Grade A")
    elif nilai >= 80 and nilai < 90:
        print("Grade B+")
    elif nilai >= 70 and nilai < 80:
        print("Grade B")
    elif nilai >= 60 and nilai < 70:
        print("Grade C+")
    elif nilai >= 50 and nilai < 60:
        print("Grade C")
    elif nilai >= 40 and nilai < 50:
        print("Grade D")
    elif nilai >=30 and nilai < 40:
        print("Grade E")
    else:
        print("Anda DO")

angka = input("Masukkan nilai : ")
cek_angka = int(angka)
cek_grade(cek_angka)