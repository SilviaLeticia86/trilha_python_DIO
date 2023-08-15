#tuplas são "irmãs" das listas. São estruturas muito parecidas com listas, porém são imutáveis. Podemos criá-las através da classe tuple ou colocando valores separados por vírgulas entre parenteses.
frutas = (
    "laranja",
    "pera",
    "uva", #inclusive utilizamos virgula no final, mesmo que não haja objeto após. Isso serve para o interpretador de python não confundir com precedência de operadores.
)
print(frutas)

letras = tuple("python")
print(letras)

numeros = tuple([1, 2, 3, 4]) # podemos passar uma lista para a tupla
print(numeros)

pais = ("Brasil",)
print(pais)

