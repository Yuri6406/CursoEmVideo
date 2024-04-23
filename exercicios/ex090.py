situ = {}
situ['Nome'] = str(input('Digite o nome do aluno: '))
situ['Media'] = float(input('Qual a media de {}: '.format(situ['Nome'])))

print('-'*30)
if situ['Media'] < 5:
    print('Situação é igual a \033[41mReprovado\033[m')
elif situ['Media'] <7:
    print('Situação é em \033[43mrecuperação\033[m')
else:
    print('Situação é igual a \033[42mAprovado\033[m')
print('~'*30)
