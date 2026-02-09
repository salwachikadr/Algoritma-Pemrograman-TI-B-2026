#LAMBDA=================================================================
x = lambda a : a + 10
print(x(5))

x = lambda a, b, c : a + b + c
print(x(5, 6, 2))

#RECURSION=====================================================================
#fungsi memanggil dirinya sendiri
def countdown(n):
  if n <= 0:
    print("Done!")
  else:
    print(n)
    countdown(n - 1)    #disini memanggil dirinya sendiri

countdown(5)    #semacam hitung mundur

    #Fibonacci Sequence
def fibonacci(n):
  if n <= 1:
    return n
  else:
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(7))

    #factorial
def factorial(n):
  # Base case
  if n == 0 or n == 1:
    return 1
  # Recursive case
  else:
    return n * factorial(n - 1)

print(factorial(5))