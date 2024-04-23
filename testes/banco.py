def notas():
    lista = [50, 20, 10, 1]
    for c in lista:
        print(f'Total de cédulas de R$ {c}')

print('='*30)
print('{:-^30}'.format('BANCO YURI'))
print('='*30)
valor = int(input('Que valor você quer sacar? R$ '))

nota50 = valor // 50
resto50 = valor % 50

nota20 = resto50 // 20
resto20 = resto50 % 20

nota10 = resto20 // 10
resto10 = resto20 % 10

nota1 = resto10 / 1

print('Total de {} cédulas de R$50'.format(nota50))
print('Total de {} cédulas de R$20'.format(nota20))
print('Total de {} cédulas de R$10'.format(nota10))
print('Total de {:.0f} cédulas de R$1'.format(nota1))
print('~'*30)
print('Volte sempre ao BANCO DO YURI! Tenha um bom dia!')

notas()