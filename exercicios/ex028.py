import random
n = random.randint(0, 5)
comp = n
num = int(input('Adivinhe qual foi o número escolhido pelo PC: '))

if num == comp:
    print('Você acertou!!! VENCEU O PC.')
else:
    print('Você errou!!! PERDEU TENTE NOVAMENTE...')
print(' O numero escolhido pelo PC foi {}'.format(comp))