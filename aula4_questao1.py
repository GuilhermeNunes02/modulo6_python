
# a) Pares entre 20 e 50
pares = [x for x in range(20, 51) if x % 2 == 0]

# b) Quadrados
quadrados = [x**2 for x in [1,2,3,4,5,6,7,8,9]]

# c) Divisíveis por 7
div7 = [x for x in range(1, 101) if x % 7 == 0]

# d) Par ou ímpar
paridade = ["par" if x % 2 == 0 else "ímpar" for x in range(0, 30, 3)]

print(pares)
print(quadrados)
print(div7)
print(paridade)
