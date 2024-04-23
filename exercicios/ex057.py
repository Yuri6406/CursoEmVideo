
s = str(input('Informe seu sexo: [M/F] ')).upper().strip()[0]
while s not in 'MF':
    s = str(input('Dados inválidos. Por favor, informe seu sexo: ')).strip().upper()
print('Sexo {} registrado com sucesso'.format(s))