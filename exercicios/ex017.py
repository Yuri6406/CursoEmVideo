from math import sqrt

cat_O = float(input('Digite o comprimento do cateto oposto de um triângulo: '))
cat_A = float(input('Digite o comprimento do cateto adjacente de um triângulo:'))


print('O comprimento da hipotenusa é {:.2f}'.format(sqrt(cat_A**2 + cat_O**2)))