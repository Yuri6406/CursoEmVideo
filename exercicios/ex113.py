def leiaInt (msg):
    while True:
        try:
            num = int(input(msg))
        except KeyboardInterrupt:
            print('\033[;41mO Usuário preferiu não digitar o esse número\033[m')
            return 0
        except:
            print('\033[;41mERRO. Digite um valor valido.\033[m')
        else:
            return num
def leiaReal (msg):
    while True:
        try:
            real = float(input(msg))
        except KeyboardInterrupt:
            print('\033[;41mO Usúario preferiu não digitas esse número')
            return 0
        except:
            print('\033[;41mERRO. Digite um valor valido.')
        else:
            return real

num = leiaInt("Digite um numero Interio:")
real = leiaReal("Digite um número Real: ")
print(f'O número Interio digitado foi {num} e o real {real}')