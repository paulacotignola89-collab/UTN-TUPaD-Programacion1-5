# Creamos una lista con las notas de 10 estudiantes.
notas = [2, 7, 8, 9, 4, 10, 6, 4, 6, 9]

# Mostramos la lista completa.
print("Lista de notas de los estudiantes: ")
for nota in notas:
    print(nota)

# Establecemos una variable acumuladora para calcular el promedio
suma_notas = 0
for nota in notas:
    suma_notas += nota

promedio = suma_notas / len(notas)     # Usamos len() para conocer cantidad de elementos
print(f"\nEl promedio de las notas es: {promedio}")

# Para indicar nota mas alta y mas baja usamos max y min
nota_maxima = max(notas)
nota_minima = min(notas)

print(f"La nota mas alta es: {nota_maxima}")
print(f"La nota mas baja es: {nota_minima}")

