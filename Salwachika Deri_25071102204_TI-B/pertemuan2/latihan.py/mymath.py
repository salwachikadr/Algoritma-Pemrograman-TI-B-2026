    #penambahan(a, b)
def tambah(a, b):
  return a + b

    #pengurangan
def kurang(a, b):
  return a - b

    #perkalian
def kali(a, b):
  return a * b

    #pembagian
def bagi (a, b):
    if b == 0:
        print ("Pembagian tidak dapat dilakukan karena pembagi bernilai 0")
    return a / b

    #modulus
def modulus (a, b):
   return a % b

    #fibonacci
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

