t = int(input())
for c in range (0, t):
    caso1,caso2 = input().split()
    caso_1 = caso1
    caso_2 = caso2

    a = caso_1[-len(caso_2):]
    if a == caso_2:
        print('encaixa')
    else:
        print('nao encaixa')