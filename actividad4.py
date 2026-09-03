# Usamos los datos del ejercicio para la lista original.
datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]

# Creamos una nueva lista para guardar los elementos que no se repiten.
lista_unicos = []

# Recorremos la lista original de datos para pasar los elementos.
for numero in datos:
    if numero not in lista_unicos:
        lista_unicos.append(numero)

print("Lista original: ")
print(datos)

print("\nLista sin elementos repetidos: ")
for n in lista_unicos:
    print("-", n)
