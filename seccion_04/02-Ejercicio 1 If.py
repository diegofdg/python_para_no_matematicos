n1 = int(input("Ingrese un número: "))
n2 = int(input("Ingrese otro número: "))

if n1 % 2 == 0 and n2 % 2 == 0:
    print("Ambos números son pares")
elif n1 % 2 == 0:
    print("El primer número es par")
elif n2 % 2 == 0:
    print("El segundo número es par")
else:
    print("Ambos numeros son impares")
