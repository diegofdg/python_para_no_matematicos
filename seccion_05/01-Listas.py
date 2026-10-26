array1 = ["futbol", "pc", 18.6, 45, [6, 7, 8], True, False, "pc"]

print(len(array1)) # Número de elementos en la lista

array1.append(66) # Agrega un elemento al final de la lista
array1.insert(1, 88) # Inserta un elemento en la posición 2
array1.extend([2, 55, True, 100]) # Agrega varios elementos al final de la lista

print(array1)

array2 = [200, 250, "hola"]
array3 = array1 + array2 # Une dos listas
print(array3)

print("pc" in array1) # Verifica si un elemento está en la lista
print(array1.index(45)) # Devuelve el índice de un elemento en la lista
print(array1.count("pc")) # Devuelve el número de veces que un elemento aparece en la lista

array1.remove("pc") # Elimina un elemento de la lista
print(array1)

array2.clear() # Elimina todos los elementos de la lista
print(array2)

array1.reverse() # Invierte el orden de los elementos en la lista
print(array1)

array4 = [1, 5, 3, -2, 4]
array4.sort() # Ordena los elementos de la lista
print(array4)

array4.sort(reverse=True) # Ordena los elementos de la lista en orden descendente
print(array4)