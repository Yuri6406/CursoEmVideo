numero = (int(input('Digite um número: ')),
        int(input('Digite outro número: ')),
        int(input('Digite mais um número: ')),
        int(input('Digite o último número: ')))
                   

print('Você digitou os valores {}'.format(numero))
print('O valor 9 apareceu {} fezes'.format(numero.count(9)))
if 3 in numero:
    print('O valor 3 apareceu na {}° posição '.format(numero.index(3)+ 1))
else:
    print('O valor 3 não foi digitado em nem uma posição')
print('Os valores pares digitados foram',end= ' ')
for n in numero:
    if n % 2 == 0:
        print(n, end=' ')