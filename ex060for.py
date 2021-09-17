num = int(input('Digite um número: '))

fat = 1

print(f'Calculando {num}! = ', end='')

for aux in range(num, 0, -1):
    print(f'{aux}', end='')
    print(' x ' if aux > 1 else ' = ', end='')
    fat *= aux
    aux -= 1

print(f'{fat}')
