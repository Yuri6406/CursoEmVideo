item = {1:4.00, 2:4.50, 3:5.00, 4:2.00, 5:1.50}

cod,cont = input().split()

cod = int(cod)
cont = int(cont)

prod = item[cod]
print(f'Total: R$ {prod * cont:.2f}')