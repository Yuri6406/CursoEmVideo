print('{}'.format('10 TERMOS DE UMA PA'))
print('='*20)

num = int(input('Digite o Primeiro termo: '))
raz = int(input('Digite a Razão: '))
decimo = num + (10 - 1) * raz
for c in range(num, decimo + raz, raz):
    print('{}'.format(c), end=' >>> ')
print('ACABOU')