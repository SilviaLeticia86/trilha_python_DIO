# como a lista é objeto mutável, podemos utilizar o copy para copiar o objeto porém apresentá-lo de uma maneira diferente
lista = [1, "Python", [40, 30, 20]]

list2 = lista.copy()

print(lista)  # [1, "Python", [40, 30, 20]]
print(id(list2), (id(lista))) #2650994044480 2650993961088

# Ou seja, o que eu fizer em list2 não refletirá na lista