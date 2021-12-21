numeros = []
numerospares = []
numerosimpares = []

resp = 'S'

while resp == 'S':
    numeros.append(int(input('Digite um número: ')))
    resp = input('Quer continuar? [S/N] ').upper().strip()[0]

for i in range(0, len(numeros)):
    if numeros[i] % 2 == 0:
        numerospares.append(numeros[i])
    else:
        numerosimpares.append(numeros[i])

print('-=' * 30)
print(f'Os números digitados foram {numeros}')
print(f'Os números pares digitados forma {numerospares}')
print(f'Os números impares digitados forma {numerosimpares}')
