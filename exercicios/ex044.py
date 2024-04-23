valor = float(input('Preço das compras: '))

print('{:=^40}'.format(' LOJÃO DO YURI '))
print('''FORMA DE PAGAMENTO
[1] Á vista dinheiro/cheque
[2] Á vista cartão
[3] 2x cartão
[4] 3x ou mais no cartão''')

op = int(input('Qual é a opção? '))

print('o valor da compra foi {:.2f}.'.format(valor))

if op == 1:
    print('Com desconto para pagamento á vista irá pagar {:.2f} R$'.format((valor - (valor / 100 * 10))))
elif op == 2:
    print('Com desconto para pagamento á  vista no cartão  irá pagar {:.2f} R$'.format(valor - (valor / 100 * 5)))
elif op == 3:
    print('Valor a ser pago até duas vezes no cartão {:.2f} R$'.format(valor))
elif op == 4:
    print('O valor parecelado em 3x ou mais ficará em {:.2f} R$'.format((valor / 100 * 20) + valor))
else:
    print('OPÇÃO INVALIDA. Tente novamente!!!')