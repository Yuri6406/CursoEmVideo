
lista = []

lista.append(int(input('Digite um valor: ')))
print('Numero cadastrado com susseso...')
while True:
    opção = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    while opção in 'S':
        num = int(input('Digite outro numero: '))
        if num in lista: 
            print('Valor duplicado. Não vou adicionar.')
        else:
            lista.append(num)
            print('Numero cadastrado com susseso...')
        opção = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    if opção == 'N':
        print('~'*40)
        print('Você digitou os valores {}'.format(sorted(lista)))
        break
    else:
        print('Tente novamente.',end='')