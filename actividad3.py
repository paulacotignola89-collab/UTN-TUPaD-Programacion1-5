import random # Comenzamos con esta linea ya que es necesaria para trabajar con numeros al azar.

# Creamos la lista con 15 numeros.
numeros = []
for i in range(15):
    numeros.append(random.randint(1, 100))

# Armamos listas para pares e impares.
pares = []
impares = []
for n in numeros:
    if n % 2 == 0: 
        pares.append(n)
    else:
        impares.append(n)

# Mostramos cuantos numeros tiene cada lista usando len.
print("Cantidad de numeros pares:  ")
print(len(pares))

print("Cantidad de numeros impares: ")
print(len(impares))

print("Elementos pares: ")
for p in pares:
    print("-", p)

print("Elementos impares: ")
for imp in impares:
    print("-", imp)