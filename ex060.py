num = int(input('Digite um número: '))

aux = num
fat = 1

print(f'Calculando {num}! = ', end='')
while aux > 0:
    print(f'{aux}', end='')
    print(' x ' if aux > 1 else ' = ', end='')
    fat *= aux
    aux -= 1

print(f'{fat}')

