lista = []

t = int(input())
for c in range(0, t):
    num = int(input())
    lista.append(num)

som = 1
for c in lista:
    n = c
    if n == c:
        som +=1
    print(f'{c} aparece {som} vez(es)')