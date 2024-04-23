from random import randint
v = 0
while True:
    jogador = int(input('Digite um valor:'))
    computador = randint(0, 10)
    tot = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('PAR ou IMPAR : [P/I]')).strip().upper()
    print(f'você jogou {jogador} e o computador {computador}. Total de {tot} ',end='')
    print(' DEU PAR'if tot % 2 == 0 else ' DEU IMPAR')
    if tipo == 'P':
        if tot % 2 == 0:
            v += 1
            print('Você VENCEU!!!')
        else:
            print('Você PERDEU!!!')
            break
    elif tipo == 'I':
        if tot % 2 == 1:
            v +=1
            print('Você VENCEU!!!')
        else:
            print('Você PERDEU!!!')
            break
    print('VAMOS JOGAR NOVAMENTE!!!')
print(f'GAME OVER. Você venceu {v} vez (es)')
