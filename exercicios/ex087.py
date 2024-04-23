lista = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]
par  = somaC = maior = 0
for l in range(0, 3):
    for c in range(0, 3):
        lista [l] [c] = int(input(f'Digite um valor: [{l}][{c}] '))

print('-='*30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{lista[l][c]:^5}]',end='')
        if lista[l][c] % 2 == 0:
            par += lista[l][c]
    print()
print('-='*30)
print(f'A soma dos valores par {par}')

for l in range(0, 3):
    somaC += lista[l][2]
print(f'A soma dos valores da terceira coluna é {somaC}')

for c in range(0,3):
    if c == 0:
        maior = lista[1][c]
    elif lista[1][c] > maior:
        maior = lista[1][c]
print(f'O maior valor da segunda linha é {maior}')
