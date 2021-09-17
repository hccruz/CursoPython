print('-=-' * 5)
print('SOMA DOS PARES')
print('-=-' * 5)

s = 0
for i in range(1, 7):
    num = int(input(f'Digite o {i}° número: '))
    if num % 2 == 0:
        s += num

print(f'A soma dos números pares digitados é {s}.')
