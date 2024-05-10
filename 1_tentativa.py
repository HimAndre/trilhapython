class PessoaFisica():
    def __init__(self, cpf, nome, data_nascimento):
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento


class Cliente(PessoaFisica):
    def __init__(self, endereço, contas):
        self.endereço = endereço
        self.contas = contas
    

class Conta():
    def __init__(self, saldo, numero, agencia, cliente, historico):
        self.saldo = saldo
        self.saldo = numero      
        self.saldo = agencia
        self.saldo = cliente
        self.saldo = historico

class ContaCorrente():
    def __init__(self, limite, limite_saques):
        self.limite_saques = limite_saques
        