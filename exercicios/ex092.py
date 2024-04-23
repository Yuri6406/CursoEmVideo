from datetime import datetime
carteira = {}

while True:
    carteira['Nome'] = str(input('Nome: '))
    nasc = int(input('Ano de nascimento: '))
    carteira['idade'] = datetime.now().year - nasc
    carteira['ctps'] = int(input('Carteira de trabalho (0 não tem):'))
    if carteira['ctps'] == 0:
        break
    carteira['contratação'] = int(input('Ano de Contratação: '))
    carteira['Salário'] = float(input('Salário: R$ '))
    carteira['Aposentadoria'] = carteira['contratação'] + 35 - datetime.now().year
    print('-='*30)
    for k, v in carteira.items():
        print(f' - {k} tem o valor {v}')
    opção = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    if opção != 'S':
        break