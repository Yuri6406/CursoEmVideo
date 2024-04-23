
print("Panificadora Pão de Ontem")
print('-'*15)
print('Tabela de preços')
print('-'*15)
preco = float(input("Preço do pão: "))
for c in range(1,51):
    print(f'{c:^4} - R$ {preco*c:.2f}')