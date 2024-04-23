altura = float(input('Digite sua altura: (m)'))
peso = float(input('Digite seu peso: (kg)'))

imc = peso / (altura * altura)
print('O IMC é {:.1f}'.format(imc))

if imc < 18.5:
    print('Abaixo do peso')
elif imc < 25:
    print('Peso ideal')
elif imc < 30:
    print('Sobre peso')
elif imc < 40:
    print('Obesidade')
else:
    print('Obesidade mórbida')