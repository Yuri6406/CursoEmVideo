gols = []
jogador = {}
times = []
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do joador: '))
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou: '))
    gols.clear()
    for c in range(0, partidas):
        gols.append(int(input(f'Quantos gols na partida {c+1}°: ')))
    jogador['gol'] = gols[:]
    jogador['total'] = sum(gols)
    times.append(jogador.copy())
    while True:
        opção = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
        if opção in 'NnSs':
            break
        print('Opeção invalida. TENTE NOVAMENTE...')
    if opção == 'N':
        break

print('-='*40)
print('Cod.', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-'*40)
for k, v in enumerate(times):
    print(f' {k}',end=' ')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-='*40)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar)'))
    if busca == 999:
        break
    if busca >= len(gols):
        print(f'ERRO! Não existe jogador com código {busca}')
    else:
        print(f'  -- LEVANTAMENTO DO JOGADOR {times[busca]["nome"]}')
        for i, g in enumerate(times[busca]['gol']):
            print(f'    No jogo  {i+1} fez {g} gols.')
    print('-'*40)
print('<< VOLTE SEMPRE >>>')