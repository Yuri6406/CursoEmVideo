dia = int(input('Quantos dias alugados? '))
distancia = float(input('Quantos km rodados? '))

print('Você ultilizou o carro por {} dias e rodou {} Km. O valor total a ser pago é {:.2f} R$.'.format(dia, distancia, dia * 60 + distancia * 0.15))