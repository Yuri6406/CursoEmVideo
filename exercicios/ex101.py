def voto(i):
    import datetime
    ano = datetime.date.today().strftime("%Y")
    anos = int(ano)
    idade = anos - i
    if idade > 65:
        return f'você tem {idade} anos e a votação é opcional'
    elif idade >= 18:
        return f'você tem {idade} anos e a votação é obrigatoria'
    else:
        return f'você tem {idade} anos e a votação ainda não é obrigatório'

print('-'*30)
print(voto(int(input('digite seu ano de nascimento: '))))