# recebe listas do usuário
n1 = int(input("Digite a quantidade de elementos da lista 1: "))
lista1 = [int(input(f"Elemento {i+1} da lista 1: ")) for i in range(n1)]

n2 = int(input("Digite a quantidade de elementos da lista 2: "))
lista2 = [int(input(f"Elemento {i+1} da lista 2: ")) for i in range(n2)]

# intercalar listas
lista3 = []
for i in range(min(n1, n2)):
    lista3.append(lista1[i])
    lista3.append(lista2[i])

# adiciona elementos restantes
if n1 > n2:
    lista3.extend(lista1[n2:])
else:
    lista3.extend(lista2[n1:])

print("Lista intercalada:", lista3)
