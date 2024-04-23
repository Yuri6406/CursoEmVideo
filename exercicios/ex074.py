from random import randint

numeros = (randint(0, 5), randint(0, 5), randint(0, 5), randint(0, 5), randint(0, 5))

print('Os valores sorteados foram {}'.format(numeros))
print('O menor valor sorteado foi {} e o maior  foi {}'.format(min(numeros), max(numeros)))