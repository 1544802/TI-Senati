
producto=Lista_producto[]
glag=True
while glag:
        try:
            nombreproducto=input("nombre del producto")
            marcaproducto=int(input("cantidad del producto")) 
            costoproducto=int(input("costo del producto"))
            cantidadproducto=int(input("cantidad del producto"))
        except ValueError:
            print("algodalio mal intentalo de nuevo")
        else:
            producto["nombre"]=nombreproducto
            producto["marca"]=marcaproducto
            producto["costo"]=costoproducto
            producto["cantidad"]=cantidadproducto
            lista_productos.append(producto)
            producto{}
            pregunta=input("desea agregar mas productos")
            if str(pregunta) != "si":
                flag=False

            print(lista_productos)
            

#menu
print("""
      supermercado
      elija la opcion
1. listar los productos
2. agregar mas productos
3. hacer la venta
    """  )