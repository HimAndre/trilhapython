# Solução do desafio pelo código do amigo 
#https://github.com/renatosetubal?tab=overview&from=2023-12-01&to=2023-12-31


T = int(input())

for i in range(T):
    i = input()
    i = i.split()
    N = int(i[0])
    K = int(i[1])
    garrafas_cheias = N // K
    garrafas_vazias = N % K
    total = garrafas_vazias + garrafas_cheias
    print(total)