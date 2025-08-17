
# Lê números do usuário
lista = list(map(int, input("Digite pelo menos 4 números separados por espaço: ").split()))

print("Lista original:", lista)
print("3 primeiros elementos:", lista[:3])
print("2 últimos elementos:", lista[-2:])
print("Lista invertida:", lista[::-1])
print("Elementos de índice par:", lista[::2])
print("Elementos de índice ímpar:", lista[1::2])
