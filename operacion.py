from producto import Producto




lista_productos =[]
p=Producto("laptop", "ASUS", 20000, 5)
lista_productos.append(p)
print(lista_productos)
producto=lista_productos[0]
print(producto.info())

nombre_p= input("nombre del producto:")
marca_p=input("marca del producto:")
precio_p=int(input("precio del producto:"))
cantidad_p=int(input("cantidad del producto:"))

t=Producto(nombre_p,marca_p,precio_p,cantidad_p)
print (t.info())
lista_productos.append(t)
