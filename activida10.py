# Creamos la matriz 4x7. cada fila es un producto y cada columna es un dia de la semana
ventas = [[1, 3, 2, 7, 4, 1, 8], [3, 6, 9, 4, 8, 15, 20], [18, 15, 14, 19, 25, 30, 35], [9, 14, 6, 12, 15, 18, 25]]

# Definimos variables para guardar resultados.
totales_por_producto = []
totales_por_dia = [0] * 7

# Calculamos los totales por productos sumando filas.
for i in range(len(ventas)):
    suma_producto = 0
    for j in range(len(ventas[i])):
        suma_producto += ventas [i][j]
# Sumamos los totales por dia (columnas).
        totales_por_dia[j] += ventas [i][j]

    totales_por_producto.append(suma_producto)

print("--- TOTAL VENDIDO POR PRODUCTO---")
for i in range(len(totales_por_producto)):
    print(f"Producto{i+1}: {totales_por_producto[i]} unidades")

# Buscamos el dia con mayores ventas totales.
maximo_ventas_dia = 0
dia_ganador = 0
for d in range(len(totales_por_dia)):
    if totales_por_dia[d] > maximo_ventas_dia:
        maximo_ventas_dia = totales_por_dia[d]
        dia_ganador = d + 1

print(f"\nEl dia con mayores ventas totales fue el dia {dia_ganador} con {maximo_ventas_dia} ventas.")

# Indicamos el producto mas vendido en la semana.
maximo_ventas_productos = 0
producto_ganador = 0
for p in range(len(totales_por_producto)):
    if totales_por_producto[p] > maximo_ventas_productos:
        maximo_ventas_productos = totales_por_producto[p]
        producto_ganador = p + 1

print(f"El producto mas vendido fue el producto {producto_ganador} con {maximo_ventas_productos} ventas.")