def saudacao(nome):
    return f"Olá, {nome}!"

minha_funcao = saudacao
#tribui um número a uma variável, pode atribuir uma função também.

def aplicar_funcao(funcao, valor):
    return funcao(valor)

print(aplicar_funcao(len, "Python"))  # Isso irá imprimir 6
#passar funções como argumentos para outras funções:

def fabricar_saudacao():
    def saudacao():
        return "Olá!"
    return saudacao

minha_saudacao = fabricar_saudacao()
print(minha_saudacao())  # Isso irá imprimir "Olá!"
#Funções podem retornar outras funções: 

funcoes = [len, print, max]
print(funcoes[0]("Hello"))  # Isso irá imprimir 5

# Você pode armazenar funções em estruturas de dados