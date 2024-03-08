menu = """

[s]  saque
[d]  deposito
[e]  extrato
[q]  Sair

"""
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
    
        if valor > 0:
            saldo += valor
            extrato += f"Deposito: r$ {valor:.2f}\n"
        else:
            print('Operação falhou! O valor informado é inválido!')
    elif opcao == "s":
        valor = float(input("Qual é o valor do saque: "))

        excedeu_saldo = valor > saldo
        
        excedeu_limite = valor > limite

        excedeu_saque = numero_saques >= LIMITE_SAQUES
        #caso falhe por motivos acima, será escrito o motivo de acordo com as opcoes
        if excedeu_saldo:
            print("Operaçao falou! saldo insuficiente")

        elif excedeu_limite:
            print("operaçao falhou! Limite excedido")

        elif excedeu_saque:
            print("Operaçao falou! número máximo de saques realizado!")

        elif valor > 0:
            saldo -= valor #retira do saldo
            extrato += f'Saque r$ {saldo:.2f}\n'
            numero_saques == 1 
            # elif valor é simbolica para que seja feito a consulta se o valor é negativo ou possitivo
            #elif valor > 0: é para números positivos
        else:
            print("Operação falhou! o valor inserido é inválido")
    elif opcao == "e":
        print("==============EXTRATO==============")
        print("Não foram realizada movimentações." if not extrato else extrato)
        #se a variavel extrato n esta vazia (quanto deposito/saque exibir o valor seguinte "extrato")
        #if ternário (estudar afinco)
        print(f'\nSaldo: r$ {saldo:.2f}')
        print("===================================")
    elif opcao == "q":
        break
    else:
        print("operaçao inválida! por favor realizar novamente a operação desejada.")
        #para que nao use um valor que n seja o desejado

