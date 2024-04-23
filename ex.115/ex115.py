from mode115.lib.interface import*
from mode115.lib.arquivo import*
from time import sleep

arq = 'Cursoemvideo.txt'
if arquivoExiste(arq):
    print('Arquivo encontrado com sucesso')
else:
    print('Arquivo não encontrado')
    criarArquivo(arq)
        

while True:
    resposta = menu(['Ver Cadrastro de Pessoas','Cadastrar nova Pessoa', 'Sair do sistema'])
    if resposta == 1:
        cabeçalho('Opção 1')
    elif resposta == 2:
        cabeçalho('Opção 2')
    elif resposta == 3:
        cabeçalho('Saindo do sistema...   Até logo')
        break
    else:
        print('\033[;41mErro! Digite um opção valida!\033[m')
    sleep(2)