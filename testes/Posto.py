'''Um posto está vendendo combustíveis com a seguinte tabela de descontos:
Álcool:
até 20 litros, desconto de 3% por litro
acima de 20 litros, desconto de 5% por litro
Gasolina:
até 20 litros, desconto de 4% por litro
acima de 20 litros, desconto de 6% por litro Escreva um algoritmo que leia o número de litros vendidos,
 o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina),
calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.'''

litros = float(input("Digite a Contidade de Litros: "))
tipo = input("A-alcool / G-gasolina ").upper()[0]

precoA = 1.90
desconto3 = (precoA/100) * 3
desconto4 = (precoA/100) * 5

precoG = 2.50
desconto5 = (precoG/100) * 4
desconto6 = (precoG/100) * 6

if tipo == "A":
    tipo = "Álcool"
    if litros <= 20:
        preco = (precoA - desconto3) * litros
    elif litros > 20:
        preco = (precoA - desconto4) * litros
elif tipo == "G":
    tipo = "Gasolina"
    if litros <= 20:
        preco = (precoG - desconto5) * litros
    elif litros > 20:
        preco = (precoG - desconto6) * litros
print(f'O preço á ser pago pelo cliente referente {litros} lts de {tipo} é {preco:.2f} R$')