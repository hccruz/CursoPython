print('-=' * 13)
print('ANÁLISE DE DADOS DO GRUPO')
print('-=' * 13)

idade18 = homens = mulheres_20 = 0

while True:
    continuar = ' '
    sexo = ' '
    print('-' * 30)
    print('CADASTRO DE PESSOAS')
    print('-' * 30)
    idade = int(input('IDADE: '))
    while sexo not in 'MF':
        sexo = input('SEXO [M/F]: ').strip().upper()[0]
    if idade >= 18:
        idade18 += 1
    if sexo == 'M':
        homens += 1
    if idade < 20 and sexo == 'F':
        mulheres_20 += 1
    while continuar not in 'SN':
        continuar = input('Quer continuar? [S/N] ').strip().upper()[0]
    if continuar == 'N':
        break

print(f'Foram cadastradas {idade18} pessoas maiores de 18 anos.')
print(f'Foram cadastrados {homens} homens.')
print(f'Foram cadastradas {mulheres_20} mulheres com menos de 20 anos.')
