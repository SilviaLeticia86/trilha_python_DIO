# Listas em python, podem armazenar de maneira sequencial qualquer tipo de objeto. Podemos criar listas usando o construtor #list, a função #range ou colocando valores separados por vírgulas entre colchetes. As listas são objetos mutáveis, portanto podem ser alterados.

frutas = ["laranja", "maca", "uva"]
print(frutas)

frutas = [] #declarar lista vazia
print(frutas)

letras = list("python") #insere lista onde cada letra é um elemento
print(letras)

numeros = list(range(10)) # essa lista irá criar um elemento para cada número de 0 a 9
print(numeros)

carro = ["Ferrari", "F8", 4200000, 2020, 2900, "São Paulo", True] #lista com objeto de diferentes tipos
print(carro)
