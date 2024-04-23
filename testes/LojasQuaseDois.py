
print("Lojas Quase Dois")
print('-'*15)
print('Tabela de preços')
print('-'*15)
preco = 1.99
for c in range(1,51):
    print(f'{c:^4} - R$ {preco*c}')