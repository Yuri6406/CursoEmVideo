Especificacao = {   'Produto':'Cachorro Quente', '100': 1.20,
                    'Produto':'BauruSimples', '101': 1.30,
                    'Produto':'Bauru com ovo', '102': 1.50,
                    'Produto':'Hambúrguer', '103': 1.20,
                    'Produto':'Cheeseburguer',   '104': 1.30,
                    'Produto':'Refrigerante', '105': 1.00}


print(f'Especificação   Código  Preço')
print()
print(f"Cachorro Quente 100     R$ 1,20 \nBauru Simples   101     R$ 1,30\nBauru com ovo   102     R$ 1,50\nHambúrguer      103     R$ 1,20\nCheeseburguer   104     R$ 1,30\nRefrigerante    105     R$ 1,00")
print()

total = 0
while True:
    cod = input("Digite qual produto deseja, ultilizando o Cod. ")
    quantidades = int(input("Digite a quantidades desejada: "))

    item = Especificacao[cod] * quantidades
    total += item

    opc = input("Deseja continuar [S/N]").upper()
    if opc == "N":
        print(f'Total do pedido foi {total:.2f}')
        break