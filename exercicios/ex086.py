lista0 = [[0 ,0 , 0] ,[0, 0, 0] ,[0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        lista0[l] [c] = int(input(f'Digite um valor: [{l},{c}] '))
print('-='*30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{lista0[l][c]:^5}]', end='')
    print()