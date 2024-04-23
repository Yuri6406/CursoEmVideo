def mensagem (msg):
    print(msg)
    print('-'*25)

def área(a, b):
    terreno = a * b
    print(f'A área de um terreno {a} x {b} é de {terreno}m².')

mensagem('CONTROLE DE TERRENOS')
área(
a = float(input('LARGURA(m): ')),
b = float(input('COMPRIMENTO (m):')))