print('-=-' * 7)
print('ANALISADOR COMPLETO')
print('-=-' * 7)

homem_velho = 0
contador = 0
media = 0

for i in range(1, 5):
    nome = input(f'Digite o nome da {i}° pessoa: ')
    idade = int(input(f'Digite a idade da {i}° pessoa: '))
    sexo = input(f'Digite o sexo da {i}° pessoa, (M) para homens ou (F) para mulheres: ')
    if sexo in 'Mm':
        if homem_velho < idade:
            nome_velho = nome
            homem_velho = idade
    else:
        nome_velho = 'não tem'

    if sexo in 'Ff' and idade < 20:
        contador += 1

    media += idade

print(f'\nA média de idade do grupo é {media/4:.1f} anos, o homem mais velho é o {nome_velho} e neste grupo tem {contador}' +
      ' mulher(es) com menos de 20 anos.')
