contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

# contatos["chave"]  # KeyError

resultado = contatos.get("chave")  # None
print(resultado)

resultado = contatos.get("chave", {})  # {} aqui se não localiza a chave, retorna um dicionário vazio
print(resultado)

resultado = contatos.get(
    "guilherme@gmail.com", {}
)  # {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}
print(resultado)

# se não tivermos certeza se uma chave existe ou não dentro de um dicionário, utilizamos o método get. Por exemplo, se quisermos acessar a chave conforme na linha 3, haverá um erro.