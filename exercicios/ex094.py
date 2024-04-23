dados = []
cadastro = {}
soma = média = 0
while True:
    cadastro.clear()
    cadastro['nome'] = str(input('Nome: '))
    while True:
        cadastro['sexo'] = str(input('Sexo: [M/F]')).strip().upper()[0]
        if cadastro['sexo'] in 'MF':
            break
        print('Informação invalida. Tente novamente...')
    cadastro['idade'] = int(input('Idade: '))
    soma += cadastro['idade']
    dados.append(cadastro.copy())

    while True:
        opção = str(input('Quer continuar? [S/N]')).strip().upper()[0]
        if opção in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if opção == 'N':
        break
print('-='*30)
print(f'Ao todo temos {len(dados)} pessoas cadastradas')
média = soma / len(dados)
print(f' A média de idade é de {média:5.2f} anos')
print('As mulheres cadastradas foram' ,end=' ')
for p in dados:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]} ',end=' ')
print()
print(' Lista das pessoas que estão acima da média')
for m in dados:
    if m ['idade'] >= média:
        for k, v in m.items():
            print(f'{k} = {v}; ' , end=' ')
        print()
print(F'{"<< ENCERRADO >>":>20}')
