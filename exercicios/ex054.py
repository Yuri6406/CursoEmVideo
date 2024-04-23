from datetime import date
atual = date.today().year
tot_maior = 0
tot_menor= 0
for c in range(1, 8):
    ano = int(input('Em que ano a {}° pessoa nasceu? '.format(c)))
    idade = atual - ano
    if idade >= 21:
        tot_maior += 1
        print('você tem {} anos !'.format(idade))
    else:
        tot_menor += 1
        print('você tem {} anos !'.format(idade))
print('{} pessoas atingiram a maior idade'.format(tot_maior))
print('{} pessoas não atingiram a maior idade'.format(tot_menor))