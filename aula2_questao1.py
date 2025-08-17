import random

# gera lista com 20 números aleatórios entre -100 e 100
lista = [random.randint(-100, 100) for _ in range(20)]

# saída
print("Lista original:", lista)
print("Lista ordenada:", sorted(lista))
print("Maior valor:", max(lista))
print("Índice do maior valor:", lista.index(max(lista)))
print("Menor valor:", min(lista))
print("Índice do menor valor:", lista.index(min(lista)))
