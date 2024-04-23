from time import sleep
n1 = int(input(' Primeiro número: '))
n2 = int(input(' Segundo número: '))
opção = 0
while opção != 5:
    print('''
    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa''')

    opção = int(input('>>>> Qual é a sua opção? '))
    if opção == 1:
        print(' A soma entre {} + {} é {}'.format(n1, n2, n1 + n2))
    if opção == 2:
        print('A multiplicação entre {} X {} é {}'.format(n1, n2, n1 * n2))
    if opção == 3:
        print(' O maior entre {} e {} é {}'.format(n1, n2, max(n1, n2)))
    if opção == 4:
        print('Informe os numeros novamente: ') 
        n1 = int(input(' Primeiro número: '))
        n2 = int(input(' Segundo número: '))
    if opção > 5:
        print('Opção invalida tente novament')
print('Finalizando...')
sleep(2)
print('-='*20)
print('Fim do programa! Volte sempre')
