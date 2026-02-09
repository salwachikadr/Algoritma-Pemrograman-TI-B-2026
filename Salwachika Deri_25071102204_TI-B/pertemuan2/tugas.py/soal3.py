#rekursi - penjumlahan digit
def jumlah_digit(n):
    if n == 0:          #Fungsi memanggil dirinya sendiri sampai n == 0 (rekursi)            
        return 0
    else:
        return n % 10 + jumlah_digit(n // 10)       #n % 10 → mengambil digit terakhir
                                                    #n // 10 → menghilangkan digit terakhir

#panggil fungsi
hasil = jumlah_digit(1234)
print(hasil)