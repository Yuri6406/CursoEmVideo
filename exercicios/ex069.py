from time import sleep
print('-'*20)
print('{:^5}'.format('CADASTRE UMA PESSOA'))
print('-'*20)
cont = homem = mulher = 0
while True:
    idade = int(input('Digite a idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Qual o sexo [M/F]: ')).strip().upper()
        if sexo == 'M':
            homem += 1
        elif sexo == 'F':
            if idade < 20:
                mulher += 1
    print('-'*20)
    if idade >= 18:
        cont += 1
    sleep(1)
    opção = ' '
    while opção not in 'SN':
        opção = str(input('Gostaria de continuar [S/N]')).strip().upper()
    if opção == 'N':
        print('PROGRAMA ENCERRADO...')
        break
    print('-'*20)
    print('{:^5}'.format('CADASTRE MAIS UMA PESSOA'))
    print('-'*20)
print(f'Total de pessoas com mais de 18 anos: {cont}')
print(f'Ao todo temos {homem} homens cadastrados')
print(f'Cadastrou {mulher} mulher com menos de 20 anos')