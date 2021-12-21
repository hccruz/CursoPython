import datetime

dados_trabalhador = {}

dados_trabalhador['nome'] = input('Nome: ')

anoNasc = int(input('Ano de Nascimento: '))

dados_trabalhador['idade'] = datetime.datetime.now().year - anoNasc
dados_trabalhador['CTPS'] = input('Carteira de Trabalho (O não tem): ')

if dados_trabalhador['CTPS'] != '0':
    dados_trabalhador['contratacao'] = int(input('Ano de Contratação: '))
    dados_trabalhador['salario'] = float(input('Salário: R$'))
    dados_trabalhador['aposentadoria'] = (dados_trabalhador['contratacao'] - anoNasc) + 35

print('-=' * 30)

for k, v in dados_trabalhador.items():
    print(f'- {k} tem o valor {v}.')
