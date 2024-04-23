valor = float(input('Digite o valor da casa que deseja comprar: R$'))

salario = float(input('Digite o salário do comprador: R$'))

anos = int(input('Digite em quantos anos deseja finalciar: '))

parcela = valor / (anos * 12)
media_s = salario / 100 * 30

if parcela <= media_s:
    print('\033[30;42mO valo da parcela será: {:.2f} R$ em {} meses\033[m'.format(parcela, anos))
else:
    print('\033[30;41mInfelizmente não será posivel realizar o financiamento!!!\033[m')