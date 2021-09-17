from datetime import date

ano_nasc = int(input('Informe o ano de nascimento: '))
sexo = input('Informe o seu sexo.(M ou F): ')

data = date.today()
ano_atual = data.year

idade = ano_atual - ano_nasc

if sexo == 'M':
    if idade < 18:
        print(f'Você ainda vai se alistar, faltam {18 - idade} ano(s) para o prazo de alistamento.')
    elif idade == 18:
        print('Já é hora de se alistar. Dirija-se a um posto de alistamento.')
    elif idade > 18:
        print(f'Você passou do tempo de alistamento. Você passou {idade - 18} ano(s) do prazo de alistamento')
else:
    print('Você não tem alistamento obrigatório!!!!')