def metade (n, fomat = False):
    res = n / 2
    return res if format is False else moeda(res)


def dobro (n, format = False):
    res = n * 2
    return res if format is False else moeda(res)


def aumentar (n, a, format = False):
    aumento = (n/100 *a) + n
    return aumento if format is False else moeda(aumento)


def diminuir (n, d , format = False):
    desconto = n - (n/100 *d)
    return desconto if format is False else moeda(desconto)


def resumo (n, a, r, format = False):
    print('-'*30)
    print('RESUMO DO VALORER')
    print('='*30)
    print()

    print(f'Preço analizado:     R${n:.2f}')
    print(f'Dobro do preço:      R${n*2:.2f}')
    print(f'Metade do preço:     R${n/2:.2f}')
    print(f'{a}% de aumento:      R${(n/100*a)+n:.2f}')
    print(f'{r}% de redução:      R${n-(n/100*r):.2f}')
    print('-'*30)


def moeda (n = 0, moeda = 'R$'):
    return (f'{moeda}{n:>.2f}'.replace('.', ','))
