time = ('Botafogo', 'Palmeiras', 'São Paulo', 'Atletico Mineiro',
'Gremio', 'Cruzeiro','Flamengo','Fluminense', 'Fortaleza',
'Red Bull Bragantino', 'Paranaense', 'Santos', 'Internacional',
'Corinthians', 'Cuiabá', 'Bahia', 'Goiás', 'Vasco Gama', 'América', 'Coritiba')

print(f'Lista de times do Brasileirão: {time}')
print('~=~'*30)
print(f'Os 5 primeiros são {time[0:6]}')
print('~=~'*30)
print(f'Os 4 útimos são {time[-4:]}')
print('~=~'*30)
ordem = sorted(time)
print(f'Times em ordem alfabética: {ordem}')
print('~=~'*30)
encontra = time.index('Fluminense')
print('O Fluminense está na {}° posição'.format(encontra + 1))