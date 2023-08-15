# Funções são blocos de códigos identificados por nome  que podem receber uma lista de parâmetros. Esses parâmetros podem ou não ter valores padrão.

# def é a palavra reservada para declarar uma função. Assim como function em JS
# função identificador parâmetro
def exibir_mensagem(): # dois pontos abre o bloco da função
    print("Olá mundo!")

# quando retorna o recuo, já não faz mais parte da função. Se inicia uma nova função
def exibir_mensagem_2(nome):
    print(f"Seja bem vindo {nome}!")


def exibir_mensagem_3(nome="Anônimo"):
    print(f"Seja bem vindo {nome}!")


exibir_mensagem()
exibir_mensagem_2(nome="Guilherme")
exibir_mensagem_3()
exibir_mensagem_3(nome="Chappie")
