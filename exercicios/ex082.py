lista = []
listaI = []
listaP = []

while True:
    num = int(input('Digite um número: '))
    lista.append(num)
    opção = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    if opção in 'N':
        break
for c in lista:
    if c % 2 == 0:
        listaP.append(c)
    elif c % 2 == 1:
            listaI.append(c)
print(f'A lista completa é {lista}')
print(f'A lista com os numeros pares {listaP}')
print(f'A lista com os numeros impares {listaI}')