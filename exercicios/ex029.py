v = float(input('Qual a velocidade do veiculo: '))
multa = (v - 80) * 7
if v > 80:
    print('O limite da via é 80 Km/h e você excedeu o limite de velocidade')
    print('Sua velocidade foi {} km/h e por isso foi MULTADO!! '.format(v))
    print('O valor da multa é {:.2f} R$'.format(multa))