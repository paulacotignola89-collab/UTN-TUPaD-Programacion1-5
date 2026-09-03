# Armamos una lista original con 7 numeros.
numeros = [26, 4, 16, 30, 20, 10, 6]
print("Lista original: ", numeros)

# Creamos una variable para guardar el ultimo elemento de la lista original en base a su indice.
ultimo_elemento = numeros[6]

# Movemos los elemenmtos hacia la derecha.
for i in range(6, 0, -1):
    numeros[i] = numeros[i - 1]

numeros[0] = ultimo_elemento

print("Lista rotada: ", numeros)
