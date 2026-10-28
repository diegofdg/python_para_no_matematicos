numero = 0
while numero < 20:
    print(numero)
    numero += 1

import math
numero = int(input("Ingrese un número: "))

while numero < 0:
    print("Por favor, ingrese un número positivo")
    numero = int(input("Vuelva a ingresar un número positivo: "))

print(f"El resultado de la raiz cuadrada del número ingresado es: {math.sqrt(numero):.2f}")
