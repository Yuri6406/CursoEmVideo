from datetime import date
atual = date.today().year

ano = int(input('Digite o ano do seu nascimento: '))

idade = atual - ano
print('\033[31;47mQuem nasceu em {} tem {} anos em {}.\033[m'.format(ano, idade, atual))

if idade < 17:
    print('Ainda não chegou o prazo para você se alistamento,\033[32;43m falta {} ano (s)\033[m'.format(17 - idade))
    print('Seu ano de alistamento será {}'.format((17 - idade) + atual))
elif idade == 18:
    print('\033[31;40mChegou o momento de se alistar\033[m')
else:
    print('\033[32;43mJa se passaram {} anos do prazo de alistamento'.format(idade - 18))
    print('Seu ano de alistamento foi {}\033[m'.format(atual - (idade - 18)))