pessoa = []
dados = []
maior = menor = 0
while True:
    opção = ' '
    while opção not in 'N':
        dados.append(str(input('Nome: ')))
        dados.append(float(input('Peso: ')))
        if len(pessoa) == 0:
            menor = maior = dados[1]
        else:
            if dados[1] > maior:
                maior = dados[1]

            if dados[1] < menor:
                menor = dados[1]
        pessoa.append(dados[:])
        dados.clear()
        opção = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    break

print('-='*40)
print(f'Ao todo, você cadastrou {len(pessoa)} pessoas')
print(f'O maior peso foi de {maior:.1f}kg peso de ',end='')
for p in pessoa:
    if p[1] == maior:
        print(f' {p[0]} ', end='')
print(f'  e menor peso foi de {menor:.1f}kg peso de ',end='')
for p in pessoa:
    if p[1] == menor:
        print(f' {p[0]} ', end='')
        