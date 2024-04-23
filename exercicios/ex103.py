def jogador (n = 0, g = 0):
    if n == '':
        n = 'Desconhecido'
        print(f'O nome do jogador é {n}',end=' ')
        if g == '':
            g = '0'
        return f'fez {g} gol(s) no campeonato. '
    else:
        print(f'O nome do jogador é {n}',end=' ')
        return f'fez {g} gol(s) no campeonato. '


print(jogador(n = str(input('Nome do jogador: ')), g = input('Contidade de gols: ')))