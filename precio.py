producto={}
while True:
    producto = input("ingresarel nombre del producto (o 'salir' para terminar):")
    if producto.lower()== 'salir':
        break

    if producto not in producto:
        producto[producto]=1
        print(f"producto '{producto}' agragado correctamente.")
    else:
        print(f"el producto '{producto}' ya existe en la lista y no sera agregado.")

lista_producto = list(producto.keys())
print("lista de producto sin repeticiones:", lista_producto)
