# Listas podem armazenar todos os tipos de objetos, sendo assim, podemos ter listas que armazenam outras listas, criando estruturas bidimensionais(tabelas) para acessar índices e linhas de colunas.

matriz = [
    [1, "a", 2],
    ["b", 3, 4],
    [6, 5, "c"]
]
            # busca objeto da linha na posição zero    
print(matriz[0])  # para buscar somente dados da linha utilizamos somente o indice desejado entre UM colchete, sendo esse o dados da LINHA [1, "a", 2]
            #linha #coluna 
print(matriz[0][0])  # 1

print(matriz[0][-1])  # Busca na primeira linha o último objeto -2-

print(matriz[1][1])  # "c"
