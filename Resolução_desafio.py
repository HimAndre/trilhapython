class CLiente:
    def __init__(self, endereco):
        self.endereco = endereco 
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)     
    
    def adicionar_conta(self, conta):
        self.contas.append(conta)


class PessoaFisica(CLiente):
    def __init__(self, cpf, nome, data_nascimento, endereco):
        super().__init__(endereco) # Chama o construtor da superclasse Cliente, passando o parâmetro endereco.
        self.nome = nome 
        self.data_nascimento = data_nascimento
        self.cpf = cpf

class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()

@classmethod
def nova_conta(cls, cliente, numero):
    return cls(numero, cliente)

@property
def saldo(self):
    return self._saldo

@property
def numero(self):
    return self._numero

@property
def agencia(self):
    return self._agencia

@property
def cliente(self):
    return self._cliente

@property
def historico(self):
    return self._historico

def sacar(self, valor):
    saldo = self.saldo
    excedeu_saldo = valor > saldo

    if excedeu_saldo:
        print('\n@@@ Operacao falhou! vc n tem saldo suficiente ')