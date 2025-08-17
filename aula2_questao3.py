import random

lista1 = [random.randint(0, 50) for _ in range(20)]
lista2 = [random.randint(0, 50) for _ in range(20)]

interseccao = sorted(list(set(lista1) & set(lista2)))

print("Lista 1:", lista1)
print("Lista 2:", lista2)
print("Interseção (sem duplicatas e ordenada):", interseccao)

# contar quantas vezes aparece
for num in interseccao:
    print(f"{num}: (lista1={lista1.count(num)}, lista2={lista2.count(num)})")
