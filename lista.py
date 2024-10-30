
lista = [10,5,7,2,1]
print(lista)

lista[0] = 111
print(lista)

lista[1] = lista[4]
print(lista)
print(lista[0])
print(len(lista))

del lista[1]
print(lista)
print(len(lista))

listas = [111,7,2,9]
print(listas[-1])
print(listas[-3])