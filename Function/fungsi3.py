def total(array):
    jumlah = len(array)
    total = 0
    for index in range(0, jumlah):
        total = total + array[index]
    return total

angka = [1, 3, 5, 7, 9]
output = total(angka)
print("Totalnya adalah : " + str(output))

angka_2 = [2, 4, 6, 8, 10]
output2 = total(angka_2)
print("Totalnya adalah : " + str(output2))

angka_3 = [2, 4, 11, 512, 1]
output3 = total(angka_3)
print("Totalnya adalah : " + str(output3))