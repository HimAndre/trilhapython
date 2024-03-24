def salvar_carro(marca, modelo, ano ,placa):
    #salvar carrp no banco de dados 
    print(f'Carro inserido com sucesso!{marca}/{modelo}/{ano}/{placa}')

# salvar_carro("fiat", "palio", 1990, "ABC-1234") #forma de atribuir os valores

# salvar_carro(marca="fiat", modelo="palio", ano= 1999, placa= "ABC-1345")

salvar_carro(**{"marca":"Fiat", "modelo": "palio", "ano": 1999, "placa":"ABC-1234"})


          