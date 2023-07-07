def cant_vc(n):
    cantidad_vocales=0
    cantidad_consonante=0
    n=n.lower()
    for letra in nombre:
        if letra=="a" or letra=="e" or letra="i" or letra=="o" or letra=="u":
            cantidad_vocales+=1
        else:
            cantidad_consonante+=1

    r=f"""nombre:{n.capitalize()}
          numero de vocales:{cantidad_vocales}
          numero de consonantes:{cantidad_consonantes}
          numero de letras.{len(n)}"""  
    return r 
    print(cant_vc("juan"))         

print(lent())
lista_nombres = []
flag=True
while flag:
    nombres = input("ingresar nombres o para terminar escriba x:")
    if nombres=="x": 
        flag=False
    else:
         cnombre=nombres.capitalize()
         if nombres in lista_nombres:
              pass
         else:    
           lista_nombres.append(cnombre)


lista_nombre.short()
print(lista_nombres)
print(f"la cantidad de nombres son {len(lista_nombres)}")

for i in lista_nombres
    print(cant_vc(i))