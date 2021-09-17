from datetime import date

ano_nasc = int(input('Digite o ano de nascimento do nadador: '))

data = date.today()
ano_atual = data.year

idade = ano_atual - ano_nasc

if idade <= 9:
    print(f'A categoria deste nadador é MIRIM e ele tem {idade} anos.')
elif idade <= 14:
    print(f'A categoria deste nadador é INFANTIL e ele tem {idade} anos.')
elif idade <= 19:
    print(f'A categoria deste nadador é JUNIOR e ele tem {idade} anos.')
elif idade <= 30:
    print(f'A categoria deste nadador é SÊNIOR e ele tem {idade} anos.')
else:
    print(f'A categoria deste nadador é MASTER e ele tem {idade} anos.')
