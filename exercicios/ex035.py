r1 = int(input('tamanho da primeira reta: '))
r2 = int(input('segunra reta: '))
r3 = int(input('terceira reta: '))



if r1< r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('\033[4;47mSim essas retas formam um triângulo\033[m')
else:
    print('\033[4;47mAs retas informada não formam um triângulo\033[m')