salario = float(input('Digite o salario do funcionario: '))

aumento1 = salario // 100 * 10
aumento2 = salario // 100 * 15

if salario >= 1250:
    print('Você tera um aumento de {:.2f} R$ no seu salario, passara a receber {} R$'.format(aumento1, salario + aumento1))
else:
    print('Você tera o aumento de {:.2f} R$ no seu salario,  passara a receber {} R$'.format(aumento2, salario + aumento2))