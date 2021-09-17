print('-=-' * 7)
print('NÚMEROS PRIMOS')
print('-=-' * 7)

num = int(input('Digite um número: '))

cont = 1
for i in range(2, num+1):
    if num % i == 0:
        cont += 1

if cont == 2:
    print(f'O número {num} é um NÚMERO PRIMO.')
else:
    print(f'O número {num} não é um NÚMERO PRIMO.')
