menu = """"
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
        opcao = input(menu) 
        
        if opcao == "d":
           valor = float(input("Informe o valor a ser depositado: "))
            
        if valor > 0:
                        saldo += valor
                        extrato += f"Deposito : R${valor:.2f}\n"
        else:
                   print('Operação falhou! O valor informado é invalido para deposito ')

        if opcao == "s":
                valor = float(input("Informe o valor do saque"))
                excedeu_saldo = valor > saldo
                excedeu_limite = valor > limite    
                excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
                print("Operação falhou, não há saldo sificiente")

        elif excedeu_limite:
                print('Operaão falhou! O valor do saque superou o limite')

        elif excedeu_saques:
                print('Operação falhou! Número de saques excedeu o limite')

        elif valor > 0:
                saldo -= valor 
                extrato += f'Saque: r$ {valor:.2f}\n'
                numero_saques += 1
        
        else:
                print('Operação falhou! O valor informado é inválido!')

        if opcao == "e":
                print('\n ========== EXTRATO========')
                print("nao foram realizados." if not extrato else extrato)
                print(f'\nSaldo: r$ {saldo:.2f}')
                print("----------------------------")

        elif opcao == "q":
                break

        else:
                print("Operação invalida ")

