class Veiculo:
    def __init__ (self, cor, placa , numero_rodas):
        self.cor = cor
        self.placa = placa 
        self.numero_rodas = numero_rodas

    def ligar_motor(self):
            print("ligando o MOTOR")


class Motocicleta(Veiculo):
    pass

class Carro(Veiculo):
    pass

class Caminhao(Veiculo):
    def __init__(self, carregado):
        self.carregado = carregado
    
    def esta_carregado(self):
        print(f'{"sim" if self.carregado else "nao" } estou carregado')

# moto = Motocicleta('preta','abc-123', 2)
# moto.ligar_motor()

# carro = Carro("branco", "acb-123", 4)
# carro.ligar_motor()                

caminhao = Caminhao('roxa', "das-123", 8, True)
caminhao.ligar_motor()
caminhao.esta_carregado()
