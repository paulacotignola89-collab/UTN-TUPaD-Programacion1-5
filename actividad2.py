# Pedimos al usuraio que ingrese 5 productos en una lista.
productos = []

for i in range(5):
    item = input(f"Ingrese el producto {i+1}: ")
    productos.append(item)

# Para mostrar la lista ordenada en forma alfabetica usamos sorted.
productos_ordenados = sorted(productos)

print("\nLista de productos ordenados alfabeticamente: ")
for item in productos_ordenados:
    print("-", item)

# Preguntamos al usuario que producto quiere eliminar.
eliminar = input("¿Que producto desea eliminar de la lista?: ")
# Verificamos que el producto a eliminar este en la lista.
if eliminar in productos_ordenados:
    productos_ordenados.remove(eliminar)
    print(f"El producto {eliminar} ha sido eliminado.")
else:
    print("Ese producto no se encuentra en la lista.")

# Mostramos la lista final actualizada.
print("\nLista final de productos: ")
for item in productos_ordenados:
    print("-", item)
    