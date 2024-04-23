n1 = int(input('primeiro número: '))
n2 = int(input('segundo número: '))
n3 = int(input('terceiro número: '))

lista = [n1, n2, n3]
menor = min(lista)
maior = max(lista)

print('Entre os numeros {} menor é {} e o mair é {}'.format(lista, menor, maior))