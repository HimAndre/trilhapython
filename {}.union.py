conjunto_a = {1,2}
conjunto_b = {3,4}

conjunto_a.union(conjunto_b)

#pode usar o interseção para definir valor que estao em evidencia nos conjuntos relacionados
#{}.union

conjunto_a = {1,2,3}
conjunto_b = {2,3,4}

conjunto_a.intersection(conjunto_b)

print(conjunto_a.intersection(conjunto_b))
#printa o valor que existe entre os dois conjtos
#{}.intersection()

conjunto_a = {1,2,3}
conjunto_b = {2,3,4}

conjunto_a.difference(conjunto_b) #{1}
conjunto_b.difference(conjunto_a) #{4}

#exibe o valor que não existe no outro conjto

conjunto_a = {1,2,3}
conjunto_b = {2,3,4}

conjunto_a.symmetric_difference(conjunto_b) #{1,4}
#exibi o valor que não existe em ambos os conjtos vide o ex anterior

conjunto_a = {1,2,3}
conjunto_b = {4,1,2,5,6,3}

conjunto_a.issubset(conjunto_b) #true
conjunto_b.issubset(conjunto_a) #false
#retorna true or false se x é subconjnto de y 

conjunto_a = {1,2,3}
conjunto_b = {4,1,2,5,6,3}

conjunto_a.issuperset(conjunto_b) #False
conjunto_b.issuperset(conjunto_a) #True

#retorna true or false se x é subconjnto de y 

conjunto_a = {1,2,3,4,5,}
conjunto_b = {6,7,8,9}
conjunto_c = {1,0}

conjunto_a.isdisjoint(conjunto_b) #True
conjunto_a.isdisjoint(conjunto_c) #False

#indica T/F quando todos elementos do conjt ñ estao noutro 

sorteio = {1,23}

sorteio.add(25) # {1,23,25}
sorteio.add(42) #{1,23,25,42}
sorteio.add(25) #{1,23,25,42}

#adiciona valor a um conj

sorteio = {1,23}
sorteio  # {1,23}
sorteio.clear()
sorteio # {}

sorteio = {1,23}
sorteio  # {1,23}
sorteio.copy()
sorteio # {1,23}

numero = {1,2,3,4,5,6,7,8,9,0}

# numero = {1,2,3,4,5,6,7,8,9,0}
numero.discard(1)
numero.discard(45)
numero # numero = {2,3,4,5,6,7,8,9,0}



numeros = {0,1,2,3,4,5,6,7,8,9,0}
numeros #{1,2,3,4,5,6,7,8,9,0}
print(numeros.pop()) #0
print(numeros.pop()) #1
print(numeros.pop()) #2
print(numeros.pop()) #3
print(numeros.pop()) #4
print(numeros.pop()) #5


numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

print(numeros)  # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
print(numeros.remove(0))  # 0
print(numeros)  # {1, 2, 3, 4, 5, 6, 7, 8, 9}


numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

print(len(numeros))  # 10


numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

print(1 in numeros)  # True
print(10 in numeros)  # False

