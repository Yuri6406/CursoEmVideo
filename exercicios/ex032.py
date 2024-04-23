ano = int(input('Digite o ano: '))

bissexto = ano // 4

if bissexto * 4 == ano:
    print('{}O ano {} é bissexto!{}'.format('\033[4;30;45m' ,ano , '\033[m'))
else:
    print('{}O ano {} não é bissexto!{}'.format('\033[4;30;45m', ano, '\033[m'))