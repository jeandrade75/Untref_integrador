# Escribir un programa que dado el ingreso de un número retorne si el mismo es primo o no.
# Algoritmo para saber si un numero es primo python

n = int(input("Ingrese un numero: "))
x = 1
c = 0

while x <= n:
    if n % x == 0:
        c = c + 1
    x = x + 1

if c == 2:
    print("El numero",n, " es primo")
else:
    print("El numero",n, " no es primo")
        