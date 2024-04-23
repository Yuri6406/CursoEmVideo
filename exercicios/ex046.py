from time import sleep
print('\033[45mCONTAGEM REGRESSIVA:\033[m')
for c in range(10, - 1, -1):
    sleep(1)
    print('{:=^20}'.format(c))

print('{:^13}'.format('BUuM!!!BUuM!!! POOW'))