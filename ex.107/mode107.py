def metade (n):
    return n / 2


def dobro (n):
    return n * 2


def aumentar (n):
    aumento = n/100 *10
    return aumento + n


def diminuir (n):
    desconto = n/100 *13
    return n - desconto

def resumo (n, a, r):
    print('-'*30)
    print('RESUMO DO VALORER')
    print('='*30)
    print()

    print(f'Preço analizado:     \t{n}')
    print(f'Dobro do preço:      \t{dobro(n, True)}')
    print(f'Metade do preço:     \t{metade(n), True}')
    print(f'{a}% de aumento:      \t{aumentar(n), True}')
    print(f'{r}% de redução:      \t{diminuir(n), True}')
    print('-'*30)