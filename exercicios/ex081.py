lista = []
lista.append(int(input('Digite um valor: ')))
while True:
    opção = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    while opção == 'S':
        num = lista.append(int(input('Digite outro numero: ')))
        opção = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    if opção == 'N':
        print('~'*30)
        lista.sort(reverse=True)
    
        print(f'Você digitou {len(lista)} elementos.')
        print(f'Os valores em ordem decrescente são {lista}')
        if 5 in lista:
            print('O valor 5 faz parte da lista !')
        else:
            print('O valor 5 não faz parte da lista !')
        break
    else:
        print('Tente novamente',end='')