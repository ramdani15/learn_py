def cek_grade(nilai):
    grade = ""
    if nilai >= 90:
        grade = "A"
    elif nilai >=80 and nilai < 90:
        grade = 'B+'
    elif nilai >= 70 and nilai < 80:
        grade = 'B'
    elif nilai >= 60 and nilai < 70:
        grade = 'C+'
    elif nilai >= 50 and nilai < 60:
        grade = 'C'
    elif nilai >=40 and nilai < 50:
        grade = 'D'
    elif nilai >= 30 and nilai < 40:
        grade = 'E'
    else:
        grade = 'DO'
    return grade

def cek_nilai(nilai):
    n = len(nilai)
    hasil = []
    for index in range(0, n):
        kirim = cek_grade(nilai[index])
        hasil.append(kirim)
    return hasil

buku_nilai = [40, 20, 80, 98, 77, 69]
output = cek_nilai(buku_nilai)
print(output)
