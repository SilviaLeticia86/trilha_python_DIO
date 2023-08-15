# alguns parãmetros podem ser passados por posição, sem o nome. Para identificá-los, utilizamos a /. Tudo o que vem antes da barra será passado por posição. O que vier após a barra poderá ser passado por posição e nome

def criar_carro(modelo, ano, placa, /, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)


criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")
criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")  # inválido
