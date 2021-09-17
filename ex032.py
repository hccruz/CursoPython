from datetime import date

print('-=-' * 20)
ano = int(input('Digite um ano ou coloque 0 para o ano atual: '))
print('-=-' * 20)

if ano == 0:
    ano = date.today().year

if (ano % 4 == 0) and (ano % 100 != 0 or ano % 400 == 0):
    print('\nO ano de {} é um ano Bissexto.\n'.format(ano))
else:
    print('\nO ano de {} não é um ano Bissexto.\n'.format(ano))
