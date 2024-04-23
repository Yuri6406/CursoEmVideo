numero = int(input('Digite um numero:'))

print('\033[36;44m O dobro do numero digitado é: {}.\033[m\033[7;40m\n O triplo é: {}.\033[m\033[37;46m\n E o quadruplo é: {}.\033[m'.format(numero * 2, numero * 3, numero * 4))