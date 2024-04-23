import mode109

n = float(input('Digite o valor da compra: '))

print(f'A metadede {mode109.moeda(n)} é {mode109.metade(n, True)}')
print(f'O dobro de {mode109.moeda(n)} é {mode109.dobro(n, True)}')
print(f'Aumento 10%, temos {mode109.aumentar(n, 10, True)}')
print(f'Reduzindo 13%, temos {mode109.diminuir(n, 13, True)}')
