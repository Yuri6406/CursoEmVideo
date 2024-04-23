total = totmil = menor = cont = 0
barato = ''
while True:
    produto = str(input('Digite o Produto: '))
    preço = float(input('Preço: R$' ))
    cont +=1
    total += preço
    if preço > 100:
        totmil += 1
    if cont == 1 or preço < menor:
        menor = preço
        barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print('FIM DO PROGRAMA')
print('Total da compra foi {:.2f}'.format(total))
print('Total {} produtos custando mais de R$1000.00'.format(totmil))
print('O produto mais barato foi {} que custa R${}'.format(barato, menor))