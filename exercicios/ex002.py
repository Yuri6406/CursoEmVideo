print('Óla digite á seguir sua data de nascimento:')
dia = input('Dia: ')
mes = input('Mês: ')
ano = input('Ano: ')
print('Sua data de nascimento é: \033[32m{}\033[m/\033[33m{}\033[m/\033[31m{}\033[m'.format(dia, mes, ano))
print('\033[7;31;40mObrigado!\033[m')