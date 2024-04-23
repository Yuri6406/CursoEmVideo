import math

angulo = int(input('Digite um angulo qualquer: '))

seno = math.sin(angulo)
coseno = math.cos(angulo)
tangente = math.tan(angulo)

print('O angulo digitado foi {:.2f}°.'.format(angulo))
print('O seno é {:.2f}.'.format(seno))
print('O coseno é {:.2f}.'.format(coseno))
print('E a tangente é {:.2f}.'.format(tangente))