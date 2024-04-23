valor = float(input('Qual o valor que você tem na carteira?'))
dolar = float(3.27)


print('Você tem {:.2f} R$ na carteira, com esse valor consegue comprar {:.0f} dolar'.format(valor, valor // dolar))
