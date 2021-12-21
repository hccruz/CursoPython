peso = []
dados = []
max_peso = []
min_peso = []
maior = menor = 0
resp = 'S'

while resp == 'S':
    dados.append(input('Nome: '))
    dados.append(float(input('Peso: ')))
    if len(peso) == 0:
        maior = menor = dados[1]
    else:
        if maior <= dados[1]:
            maior = dados[1]
            max_peso.append(dados[0])

        if menor >= dados[1]:
            menor = dados[1]
            min_peso.append(dados[0])

    peso.append(dados[:])
    dados.clear()
    resp = input('Quer continuar? [S/N] ').upper().strip()[0]

print('-=' * 30)
print(f'Ao todo, você cadastrou {len(peso)} pessoas.')

print(f'O maior peso foi de {maior}kg. Peso de {max_peso}')
print(f'O menor peso foi de {menor}kg. Peso de {min_peso}')

