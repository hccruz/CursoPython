matriz = [[], [], []]
i = somapares = tot3col = 0

for l in matriz:
    for j in range(0, 3):
        l.append(int(input(f'Digite um valor para [{i}, {j}]: ')))
    i += 1

print('-=' * 30)
for i in range(0, 3):
    for j in range(0, 3):
        if matriz[i][j] % 2 == 0:
            somapares += matriz[i][j]
        print(f'[{matriz[i][j]:^5}]', end=' ')
    tot3col += matriz[i][2]
    print()

print('-=' * 30)
print(f'A soma dos valores pares é {somapares}.')
print(f'A soma dos valores da terceira coluna é {tot3col}.')
print(f'O maior valor da segunda linha é {max(matriz[1])}.')
