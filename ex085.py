valores = [[], []]
v = 1

while v <= 7:
    num = (int(input(f'Digite o {v}º valor: ')))
    if num % 2 == 0:
        valores[0].append(num)
    else:
        valores[1].append(num)
    v += 1

print('-=' * 30)
valores[0].sort()
print(f'Os valores pares digitados foram: {valores[0]}')

valores[1].sort()
print(f'Os valores ímpares digitados foram: {valores[1]}')
