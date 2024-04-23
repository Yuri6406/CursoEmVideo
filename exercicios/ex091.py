from random import randint
from time import sleep
from operator import itemgetter
jogo = {}
maior = menor = 0
jogo['jogado-1'] = randint(1, 6)
jogo['jogado-2'] = randint(1, 6)
jogo['jogado-3'] = randint(1, 6)
jogo['jogado-4'] = randint(1, 6)
ranking = ()
print('-='*15)
print(f' {"VALORES DO SORTEIO:":^30}')
print('-='*15)
for e, v in jogo.items():
    sleep(1)
    print(f'O {e} tirou {v}')
print('-'*40)

ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print(f'{"RANKING DOS JOGADORES:":^30} ')
for g, p in enumerate(ranking):
    sleep(1)
    print(f'{g+1}° lugar:  {p[0]} com {p[1]}')