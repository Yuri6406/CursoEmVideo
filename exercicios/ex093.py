jogador = {}
gols = []
jogador['nome'] = str(input('Nome do joador: '))
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou: '))
for c in range(0, partidas):
    gols.append(int(input(f'Quantos gols na partida {c+1}°: ')))
jogador['gol'] = gols[:]
jogador['total'] = sum(gols)

print('=-'*30)
print(jogador)
print('=-'*30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('=-'*30)
for i, v in enumerate(jogador['gol']):
    print(f'    => Na partida {i}, fez {v} gols.')
print(f'Foi um total de {jogador["total"]} gols')