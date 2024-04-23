while True:
    print('-'*15)
    print('Lojas Tabajara')
    print('-'*15)

    total = 0
    c = 1
    while True:
        produto = float(input(f"Produto {c}: R$ "))
        total += produto
        c += 1
        if produto == 0:
            break
    print(f'Total: {total+1}')
    dinheiro = float(input("Dinheiro: R$ "))
    print(f'Troco: R$ {dinheiro - (total+1):.2f}')