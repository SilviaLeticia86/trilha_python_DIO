resultado = dict.fromkeys(["nome", "telefone"])  # {"nome": None, "telefone": None}
print(resultado)

resultado = dict.fromkeys(["nome", "telefone"], "vazio")  # {"nome": "vazio", "telefone": "vazio"}
print(resultado)

# fromkeys cria chaves em duas situações: 1. criar a chaves sem vincular valor 2. criar um conjunto de chaves e atribuir um valor padrão
