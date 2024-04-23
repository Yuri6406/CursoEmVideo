import mode108

n = float(input('Digite o valor da compra: '))

print(f'A metadede {mode108.moeda(n)} é {mode108.moeda(mode108.metade(n))}')
print(f'O dobro de {mode108.moeda(n)} é {mode108.moeda(mode108.dobro(n))}')
print(f'Aumento 10%, temos {mode108.moeda(mode108.aumentar(n))}')
print(f'Reduzindo 13%, temos {mode108.moeda(mode108.diminuir(n))}')
