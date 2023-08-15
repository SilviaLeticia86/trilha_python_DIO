#para percorrer listas utilizamos o for

carros = ["gol", "celta", "palio"]

for carro in carros:
    print(carro)


for indice, carro in enumerate(carros): # utilizamos o enumerate para enumerar os objetos da lista. No exemplo abaixo a lista retornará para indice gol, celta e palio e para carro 0: gol 1: celta e 2: palio
    print(f"{indice}: {carro}")
