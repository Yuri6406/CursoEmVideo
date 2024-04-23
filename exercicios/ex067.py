from time import sleep
while True:
    print('~'*20)
    num = int(input('Quer ver a tabuada de qual valor? '))
    if num <= 0:
        sleep(1)
        print('PROGRAMA ENCERRADO...')
        break
    print('~'*20)
    print('\033[46m{} do {}\033[m'.format('TABUADA', num))
    for c in range(0, 11):
        print('{} X {} = {}'.format(num, c, num * c ))