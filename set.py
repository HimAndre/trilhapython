set([1,2,3,4,])

set("abacaxi")

set(("palio","gol","celta","palio"))

#para que um "set" seja acessivél deve-se convertelo para list

carros = {"gol", "palio","celta"}

for carro in carros:
    print(carro)

#ou

carros = {"gol", "palio","celta"}

for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")
