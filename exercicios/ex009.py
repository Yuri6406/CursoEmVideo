num = int(input())

cores = {'verde':'\033[42m', 'amarelo':'\033[43m', 'vermelho':'\033[41m', 'limpo':'\033[m'}

print('TABUADA DO {}'.format(num))

print('{} 0 x {} = {}{}'.format(cores['verde'], num, num * 0, cores['limpo']))
print('{} 1 x {} = {}{}'.format(cores['amarelo'], num, num * 1,cores['limpo']))
print('{} 2 x {} = {}{}'.format(cores['vermelho'], num, num * 2, cores['limpo']))
print('{} 3 x {} = {}{}'.format(cores['verde'], num, num * 3, cores['limpo']))
print('{} 4 x {} = {}{}'.format(cores['amarelo'], num, num * 4, cores['limpo']))
print('{} 5 x {} = {}{}'.format(cores['vermelho'], num, num * 5, cores['limpo']))
print('{} 6 x {} = {}{}'.format(cores['verde'],num, num * 6, cores['limpo']))
print('{} 7 x {} = {}{}'.format(cores['amarelo'], num, num * 7, cores['limpo']))
print('{} 8 x {} = {}{}'.format(cores['vermelho'],num, num * 8, cores['limpo']))
print('{} 9 x {} = {}{}'.format(cores['verde'],num, num * 9, cores['limpo']))
print('{}10 x {} = {}{}'.format(cores['amarelo'],num, num * 10, cores['limpo']))