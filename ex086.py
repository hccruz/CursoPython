matriz = [[], [], []]
i = 0

for linha in matriz:
    for j in range(0, 3):
        linha.append(int(input(f'Digite um valor para [{i}, {j}]: ')))
    i += 1

print('-=' * 30)
for i in range(0, 3):
    for j in range(0, 3):
        print(f'[{matriz[i][j]:^5}]', end=' ')
    print()
