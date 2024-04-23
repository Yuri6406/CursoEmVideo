def metade (n, fomat = False):
    res = n / 2
    return res if format is False else moeda(res)


def dobro (n, format = False):
    res = n * 2
    return res if format is False else moeda(res)


def aumentar (n= 0, a = 10, format = False):
    aumento = (n/100 *a) + n
    return aumento if format is False else moeda(aumento)


def diminuir (n = 0, d = 15 , format = False):
    desconto = n - (n/100 *d)
    return desconto if format is False else moeda(desconto)


def resumo (n = 0, a = 10, r = 15, format = False):
    print('-'*30)
    print(f'RESUMO DO VALORER.')
    print('='*30)
    print()

    print(f'Preço analizado:     \t{moeda(n)}')
    print(f'Dobro do preço:      \t{dobro(n, True)}')
    print(f'Metade do preço:     \t{metade(n, True)}')
    print(f'{a}% de aumento:      \t{aumentar(n, a, True)}')
    print(f'{r}% de redução:      \t{diminuir(n, r, True)}')
    print('-'*30)


def moeda (n = 0, moeda = 'R$'):
    return (f'{moeda}{n:>.2f}'.replace('.', ','))


