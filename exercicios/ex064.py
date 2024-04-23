cont = soma = 0
while True:
    n = int(input('Digite um número [999 para parar]:'))
    if n == 999:
        break
    cont += 1
    soma += n
print('Foram digitado {} numeros e a soma foi {}'.format(cont, soma))