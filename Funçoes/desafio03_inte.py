a = input() 
b = input() 
c = input() 

if a == 'vertebrado':
    if b == 'ave' and c == 'carnivoro':
        print('aguia')
    elif b == 'ave' and c == 'onivoro':
        print('Pomba')
    elif b == 'mamifero' and c == 'onivoro':
        print('homem')
    elif b == 'mamifero' and c == 'herbívoro':
        print('vaca')
elif a == 'invertebrado':
    if b == 'inseto' and c == 'hematofago':
        print('pulga')
    elif b == 'inseto' and c == 'herbivoro':
        print('lagarta')
    elif b == 'anelideo' and c == 'hematofago':
        print('sanguessuga')
    elif b == 'anelideo' and c == ':onivoro':
        print('minhoca')

# Foi utilizado um codigo do git como base 
# https://github.com/renatosetubal?tab=overview&from=2023-12-01&to=2023-12-31

