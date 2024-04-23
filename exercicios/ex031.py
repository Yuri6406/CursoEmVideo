dist = float(input(' Digite a distância da viagem em Km: '))

if dist <= 200:
    print('O valor da passagem é {}{:.2f}{}'.format('\033[47;34m',dist * 0.50, '\033[m'))
else:
    print('O valor da passagem é {}{:.2f}{}'.format('\033[47;34m',dist * 0.45, '\033[m'))