def descrever_carro(marca,modelo, /, ano_fabricacao, *, cor):
    print(marca,modelo,ano_fabricacao,cor)

descrever_carro("Toyota", "Corolla", 2020, cor="Preto")
