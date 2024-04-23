nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

media = (nota1 + nota2) / 2

if media < 5:
    print('\033[30;41mREPROVADO\033[m')
elif media < 6.9:
    print('\033[34;40mRECULPERAÇÃO\033[m')
else:
    print('\033[;42mAPROVADO\033[m')