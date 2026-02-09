'''
array : variabel untuk menyimpan beberapa data
'''

cars = ["Ford", "Volvo", "BMW"]

    #The Length of an Array
    #berapa banyak anggota dari variabel array
x = len(cars)

    #Looping Array Elements
    #menghasilkan output satu persatu bukan dalam satu baris
for x in cars:
  print(x)

    #Adding Array Elements
cars.append("Honda")

    #Removing Array
cars.pop(1)     #untuk hapus sesuai indeks
cars.remove("Volvo")        #untuk hapus sesuai valuenya langsung

