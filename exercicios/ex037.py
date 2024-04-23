num = int(input('Digite um numero: '))
print('''Escolha uma das bases para conversão
[1] binario
[2] octau
[3] hexadecimal''')
base = int(input('Qual opção: '))

if base == 1:
    print('{}'.format(bin(num)[2:]))
elif base == 2:
    print('{}'.format(oct(num)[2:]))
elif base == 3:
    print('{}'.format(hex(num)[2:]))
else:
    print('opção invalida. tente novamente.')