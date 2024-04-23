altura = float(input('Digite a altura da parede: '))
largura = float(input('Digite a largura da parede: '))

area = altura * largura

tinta = area / 2

print('Sua parede tem {} metro (s) de altura e {} metro (s) de largura, área total da parede é {} metro(s)'.format(altura, largura, area))
print('Para pintar toda a parede será necessário {} litros de tinta'.format(tinta))