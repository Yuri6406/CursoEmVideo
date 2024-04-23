print('{}'.format('10 TERMOS DE UMA PA'))
print('=-'*20)

num = int(input('Digite o Primeiro termo: '))
raz = int(input('Digite a Razão: '))
termo = num
cont = 1
while cont <= 10:
    print('{} ->'.format(termo), end='')
    termo += raz
    cont += 1
print('FIM')