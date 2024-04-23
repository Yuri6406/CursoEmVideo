num = int(input('DIGITE O NUMERO QUE GOSTARI DE SABER A TABUADA:'))
print('=-'* 10)
print('\033[35;43mTABUADA DO NÚMERO {}:\033[m'.format(num))
print('-='* 10)
for c in range(0, 11):
    print('{:2} X {:2} = {}'.format(num, c, c * num))