nome = str(input("Digite seu nome completo: ")).strip()

print('nome todo em maiúsculo: {}'.format(nome.upper()))
print('nome todo em minúsculo: {}'.format(nome.lower()))
print('contidade de letras no nome: {}'.format(len(nome) - nome.count(' ')))
print(' seu primeiro nome tem: {}'.format(nome.find(' ')))