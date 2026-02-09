#function & validasi data
def rata_rata(nilai):
    if len(nilai) == 0:
        return "data kosong"
    else:
        return sum(nilai) / len(nilai)
    
#panggil fungsi
dataNilai = [80, 75, 90, 60, 85]
hasil = rata_rata(dataNilai)

print(hasil)