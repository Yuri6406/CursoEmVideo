import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://pudim.com.br/')
except urllib.error.URLError:
    print('ERRO ao acessar o site.')
else:
    print('Site acessado com sucesso!')
    print(site.read())