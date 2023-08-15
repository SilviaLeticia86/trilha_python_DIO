# Dicionário é um conjunto não ordenado de pares chave: valor, onde as chaves são únicas em uma dada instância. São delimitados por {} e contém uma lista de pares de chave: valor separadas por vírgulas. Diferente das listas e tuplas, onde a estrutura de objetos é sequencial, e o set (conjuntos) que a estrutura é sequencial porém não repetida.

# Para ser uma chave válida para o dicionário, o objeto tem que ser imutável (tuplas, strings)

pessoa = {"nome": "Guilherme", "idade": 28}
print(pessoa)

pessoa = dict(nome="Guilherme", idade=28) # Podemos utilizar também o método dict e em seguida declarar os valores entre () separados por vírgulas
print(pessoa)

pessoa["telefone"] = "3333-1234"  # {"nome": "Guilherme", "idade": 28, "telefone": "3333-1234"}
print(pessoa) # aqui podemos utilizar os [] quando já temos dicionário criado e precisamos adicionar dados. No caso do exemplo acima, estamos adicionando o telefone ao objeto pessoa.

# Não podemos utilizar listas nos dicionários, visto que essas são objetos mutáveis
