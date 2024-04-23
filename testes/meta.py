
while True:
    meta = float(input('Qual a meta do mês: '))

    if meta > 4500:
        print('Foi batido a 3° meta')
    elif meta > 3000:
        print('foi batido a 2° meta')
    elif meta > 1000:
        print('foi batido a 1° meta')
    elif meta < 1000:
        print('A meta não foi alcançada')
        break