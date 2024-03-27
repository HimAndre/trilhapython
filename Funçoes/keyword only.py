#em Python, uma função que aceita apenas argumentos de palavra-chave é conhecida como uma função de "keyword-only". Isso significa que todos os argumentos da função devem ser passados explicitamente por nome, e não por posição.

def descrever_carro(*, marca, modelo, ano_fabricaçao):
    # print(f'Marca: {marca}')
    # print(f'modelo: {modelo}')
    # print(f'ano de fabricação: {ano_fabricaçao}')
    print(marca,modelo,ano_fabricaçao)
    #chamamos a função com os arg nomeados

descrever_carro(marca= "FIAT" ,modelo = "palio", ano_fabricaçao= 2020)
