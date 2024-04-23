preco = float(input('Qual o preço do produto: '))

desconto = (preco * 5) / 100

print('O valor do produto é: {} R$, seu novo preço com 5% de desconto é : {} R$'.format(preco, preco - desconto))