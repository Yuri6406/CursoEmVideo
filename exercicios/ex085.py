lista = [[],[]]

for c in range(1, 8):
    num = int(input(f'Digite {c}° valor: '))
    if num % 2 == 0:
        lista[0].append(num)
    elif num % 2 == 1:
        lista[1].append(num)
lista[0].sort()
lista[1].sort()
print(f'Todos os valores pares: {lista[0]}')
print(f'Todos os valores impares: {lista[1]}')
