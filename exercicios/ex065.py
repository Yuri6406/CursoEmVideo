cont = soma = maior = menor = 0
resp = 'S'
while resp in 'S':
    num = int(input('Digite um número: '))
    cont += 1
    soma = soma + num
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()
print('Você digitou {} números e a média foi {:.2f}'.format(cont, soma / cont))
print('O maior foi {} e o menor foi {}'.format(maior, menor))