from datetime import date
atual = date.today().year
ano = int(input('Digite o ano de nascimento do atléta:'))

idade = atual - ano
print('A idade do atléta é {} anos.'.format(idade))
if idade <= 9:
    print('\033[34;42mAtléta MIRIM\033[m')
elif idade <= 14:
    print('\033[34;42mAtléta INFANTIL\033[m')
elif idade <=19:
    print('\033[34;42mAtléta JUNIOR\033[m')
elif idade <= 25:
    print('\033[34;42mAtléta SENIOR\033[m')
else:
    print('\033[34;42mAtléta MASTER\033[m')