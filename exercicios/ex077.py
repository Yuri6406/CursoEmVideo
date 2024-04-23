palavras = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRATIS', 'ESTUDAR', 'PRATICAR', 'TRABALHAR', 'MERCADO', 'PROGRAMADOR', 'FUTURO')

for p in palavras:
    print('\nNa palavra {}'.format(p), end=' ')
    for letra in p:
        if letra.upper() in 'AEIOU':
            print('{}'.format(letra),end=' ')
