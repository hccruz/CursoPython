print('-=-' * 7)
print('SOMA MÚTLIPLOS DE 3')
print('-=-' * 7)

s = 0
for i in range(0, 501, 3):
    if i % 2 != 0:
        s += i

print(f'A soma dos números ímpares e múltiplos de 3 é {s}.')
