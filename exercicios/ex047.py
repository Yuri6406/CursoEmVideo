print('''\033[31;43mTODOS OS NUMEROS PAR
 ENTRE 1 E 50 SÃO : \033[m''')
for c in range(2, 51, 2):
    print('{}{:^20}{}'.format('\033[;35;42m', c, '\033[m'))
