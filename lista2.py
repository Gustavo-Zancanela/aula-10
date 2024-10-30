lista = [132,1045,0,32,22]
print(lista)

num = int(input("Digite um número: "))
lista[2] = num
del lista[4]

print('Valor da lista atual:', lista)
print("Comprimento da lista atual:",len(lista))
