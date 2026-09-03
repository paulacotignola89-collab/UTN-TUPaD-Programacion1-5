# Iniciamos creando una lista con nombres de 8 estudiantes presentes en clase.
estudiantes = ["Ramiro", "joaquin", "Paula", "Alberto", "Olga", "Jorge", "Luka", "Milo"]

# Preguntamos al usuario que quiere hacer y le damos las opciones.
print("¿Que accion desea hacer?")
opcion = input("Escriba 'agregar' para sumar un estudiante o 'eliminar' para quitar uno: ").lower() # Validamos mayusculas/minusculas

# Segun la opcion.
if opcion == "agregar":
    nuevo = input("Nombre del nuevo estudiante: ").capitalize() # Validamos para la mayuscula inicial
    estudiantes.append(nuevo)
    print("Agregado con exito.")
elif opcion == "eliminar":
    sacar = input("Nombre del estudiante a quitar: ").capitalize()
    if sacar in estudiantes:
        estudiantes.remove(sacar)
        print("Eliminado con exito.")
    else:
        print("El nombre no esta en la lista.")

else:
    print("Opcion invalida.")

# Mostramos lista final.
print("\nLista actualizada: ")
for estudiante in estudiantes:
    print(f"-{estudiante}")