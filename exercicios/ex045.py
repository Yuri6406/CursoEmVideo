from random import randint
from time import sleep
itens = ('Pedra', 'Papel' , 'Tesoura')
computador = randint (0, 2)
print(''' Sua opção:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual sua jogada? '))
print('JÔ')
sleep(1)
print('keEN')
sleep(1)
print('PÔôH!!!')
sleep(1)
print('-=' * 11)
print('computador jogou {}'.format(itens[computador]))
print('{:^20}'.format('X'))
print('jogador jogou {}'.format(itens[jogador]))
print('-=' * 11)
if computador == 0:
    if jogador == 0:
        print('{:^20}'.format('EMPATE'))
    elif jogador == 1:
        print('{:^20}'.format('JOGADOR VENCE'))
    elif jogador == 2:
        print('{:^20}'.format('COMPUTADOR VENCE'))
    else:
        print('{:^20}'.format('Jogada Inválida!'))
elif computador == 1:
    if jogador == 0:
        print('{:^20}'.format('COMPUTADOR VENCE'))
    elif jogador == 1:
        print('{:^20}'.format('EMPATE'))
    elif jogador == 2:
        print('{:^20}'.format('JOGADOR VENCE'))
    else:
        print('{:^20}'.format('Jogada Inválida!'))
elif computador == 2:
    if jogador == 0:
        print('{:^20}'.format('JOGADOR VENCE'))
    elif jogador == 1:
        print('{:^20}'.format('JOGADOR VENCE'))
    elif jogador == 2:
        print('{:^20}'.format('EMPATE'))
    else:
        print('{:^20}'.format('Jogada Inválida!'))