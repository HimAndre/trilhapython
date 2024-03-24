def calcular_total(numero):
    return sum(numero)

def antecessor_e_sucessor(numero):
    antecessor = numero -1
    sucessor = numero + 1
    return antecessor, sucessor

print(calcular_total([10,30,34])) #chamamos o comando junto do "numero"

print(antecessor_e_sucessor(10)) 

