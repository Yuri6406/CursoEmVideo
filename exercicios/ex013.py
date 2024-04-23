salario = float(input(' Digite qual o seu salario atual: '))

aumento = (salario * 15) / 100

print('Você terá um aumento de 15% no seu salario e passará a receber {:.2f} R$'. format(salario + aumento))