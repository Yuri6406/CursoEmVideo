def fatorial(n, show = False):
    """
    -> Calcula o fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (opcional) Mostarr ou não a conta.
    :return: O valor do Fatorial de número n.
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *=c
    return f


print(fatorial(int(input('Calcule o fatorial de um numero: ')), show=True))
