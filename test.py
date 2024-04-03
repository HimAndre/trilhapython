# Escreva um programa em Python que peça ao usuário 
# para digitar um número inteiro e, em seguida, determine 
# se esse número é par ou ímpar. Em seguida, imprima uma 
# mensagem indicando se o número é par ou ímpar.

# print('Descubra se o numero e par ou impar')

# numero = int(input('Escolha qualquer numero'))

# if numero % 2 == 0:
#     print('is par')
# else:       
#     print('is impar')
    
"""_summary_
    
Calculadora de Média:
Escreva um programa que peça ao usuário para digitar três 
notas e, em seguida, calcule e imprima a média dessas notas.

Contagem de Vogais:
Escreva um programa que conte o número de vogais 
(a, e, i, o, u) em uma frase fornecida pelo usuário.

Verificação de Palíndromo:
Escreva um programa que verifique se uma palavra fornecida 
pelo usuário é um palíndromo (ou seja, se pode ser lida da 
mesma forma da esquerda para a direita e vice-versa).

"""
# notas = input('Digite as notas que vc tirou')

# notas_lista = notas.split()

# nota1 = float(notas_lista[0])
# nota2 = float(notas_lista[1])
# notas3 = float(notas_lista[2])

# media = (nota1 + nota2 + notas3) / 3

# print(f'A media das notas e {media:.2f}')

# frase = input('digite uma frase:')

# contador_vogais = 0 
# for caractere in frase:
#     if caractere.lower() in 'aeiou':
#         contador_vogais += 1

# print('O numero de vogais na frase e:', contador_vogais)

# Passo 1: Pedir ao usuário para inserir uma palavra
palavra = input("Digite uma palavra: ")

# Passo 2: Verificar se a palavra é um palíndromo
# Inverter a palavra
palavra_invertida = palavra[::-1]

# Passo 3: Verificar se a palavra original é igual à palavra invertida
if palavra == palavra_invertida:
    print(f'A palavra "{palavra}" é um palíndromo.')
else:
    print(f'A palavra "{palavra}" não é um palíndromo.')