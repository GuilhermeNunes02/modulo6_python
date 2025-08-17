
import random

lista = [random.randint(-10, 10) for _ in range(20)]
print("Original:", lista)

# encontrar maior quantidade de negativos em sublistas de tamanho variável
# aqui, o exercício quer achar o intervalo com MAIS negativos e remover
# solução simplificada: achar sublista contínua com mais negativos
max_inicio, max_fim, max_negativos = 0, 0, 0

for i in range(len(lista)):
    for j in range(i+1, len(lista)+1):
        sublista = lista[i:j]
        qtd_neg = sum(1 for x in sublista if x < 0)
        if qtd_neg > max_negativos:
            max_negativos = qtd_neg
            max_inicio, max_fim = i, j

# deletando
del lista[max_inicio:max_fim]
print("Editada:", lista)
