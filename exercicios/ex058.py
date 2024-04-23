from random import randint

print('Sou seu computador...')
computador = randint(0, 11)
print('''\033[45mAcabei de pensar em um número entre 0 e 10.\033[m
\033[47;34mSerá que você consegue adivinhar qual foi?\033[m''')
jodador = 0
cont = 0
while jodador != computador:
    jodador = int(input('\033[47;34mQual é seu palpite?\033[m '))
    cont += 1
    if computador > jodador:
        print('Mais.. tente outra vez')
    elif computador < jodador:
        print('Menor... tente outra vez')
    else:
        print('Acertou com {}{}{} tentativas. Parabéns'.format('\033[45m',cont ,'\033[m'))
print('O PC pensou no numero {}{}{}'.format('\033[45m',computador ,'\033[m'))
