''' 
primeiro progama POO
Joao tem uma bicicleta e gostaria de registrar as
vendas de suas bicicletas. Crie um progama onde 
Joao informe: cor, modelo, ano e valor da bicicleta
vendida. Uma bicicleta pode: buzinar, parar e correr.
adicione esses comportamentos!!!! '''

class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo 
        self.ano = ano 
        self.valor = valor


    def buzina(self):
        print('BIIIIIIIIIIIIIIII')

    def parar(self):
        print('parou')

    def correr(self):
        print('eu sou o flash!')
        
    # def __str__(self):
    #     return f"Bicicleta: cor={self.cor}, modelo={self.modelo}, ano={self.ano},valor={self.valor}"
    
    def __str__(self):
         return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"
    
b1 = Bicicleta('vermelha','monark', 1999, 1500)
b1.buzina()
b1.parar()
b1.correr()
print(b1.cor, b1.modelo,b1.valor,b1.ano)

b2 = Bicicleta('Verder', 'monark',2000, 189)
print(b2)
b2.correr()


