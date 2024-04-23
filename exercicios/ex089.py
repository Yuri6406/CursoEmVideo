lista = []
dados = []

while True:
    opção = ' '
    while opção not in 'N':
        nome = str(input('Nome:'))
        nota1 = float(input('Nota 01: '))
        nota2 = float(input('Nota 02: '))

        dados.append(nome)
        dados.append(nota1)
        dados.append(nota2)
        media = (nota1 + nota2) / 2
        dados.append(media)
        lista.append(dados[:])
        dados.clear()
        opção = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    break
print('-='*30)
print(f'{"N0.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-'*26)
for i, a in enumerate(lista):
    print(f'{i + 1:<4}{a[0]:<10}{a[3]:>8.1f}')
while True:
    print('.'*35)
    opc = int(input('Mostrar notas de qual aluno? (999)'))
    if opc == 999:
        print('FINALIZADO...')  
        break
    if opc<= len(lista) - 1:
        print(f'Notas de {lista[opc - 1][0]} são {lista[opc - 1][1], lista[opc - 1][2]}')
    else:
        print('TENTE NOVAMENT...', end='')