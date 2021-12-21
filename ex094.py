list_dados = []
dic_dados = {}
mulheres = []

soma = 0

while True:
    dic_dados['nome'] = input('Nome: ')
    dic_dados['sexo'] = input('Sexo: [M/F] ').upper().strip()[0]
    while dic_dados['sexo'] not in 'MF':
        print('ERRO! Responda apenas M ou F.')
        dic_dados['sexo'] = input('Sexo: [M/F] ').upper().strip()[0]
    dic_dados['idade'] = int(input('Idade: '))
    resp = input('Quer continuar? [S/N] ').upper().strip()[0]
    while resp not in 'SN':
        print('ERRO! Responda apenas S ou N.')
        resp = input('Quer continuar? [S/N] ').upper().strip()[0]
    list_dados.append(dic_dados.copy())
    if resp == 'N':
        break

print('-=' * 30)
print(f'A) Ao todo temos {len(list_dados)} pessoas cadastrados.')

for i in range(0, len(list_dados)):
    soma += list_dados[i]['idade']
    if list_dados[i]['sexo'] == 'F':
        mulheres.append(list_dados[i]['nome'])

media = soma / len(list_dados)

print(f'B) A média de idade é de {media:5.2f} anos.')
print('C) As mulheres cadastradas foram ', end='')

for m in mulheres:
    print(m, end=' ')

print()
print('D) Lista das pessoas que estão acima da média:')

for i in range(0, len(list_dados)):
    if list_dados[i]['idade'] > media:
        print('    ', end='')
        for k, v in list_dados[i].items():
            print(f'{k} = {v};', end=' ')
        print()

print('<< ENCERADO >>')
