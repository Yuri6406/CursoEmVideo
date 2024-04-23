num = int(input('Digite um numero: '))
print('O um numero digitado foi \033[7;31;43m{}\033[m \033[7;30;40m o sucessor do numero {} e o antecessor é {}\033[m'.format(num, num + 1, num - 1))