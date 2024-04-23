print('GERADOR DE PA')
print('-='*20)
primeiro = int(input('Digite o primeiro termo: '))
razão = int(input('Digite a razão: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} ->'.format(termo), end='')
        termo += razão
        cont+=1
    print('PAUSA')
    mais = int(input('Quanto termos você quer mostrar á mais?'))
print('Progressão finalizada com {} termos mostrados'.format(total))