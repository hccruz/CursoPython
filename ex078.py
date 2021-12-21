valores = []

for i in range(0, 5):
    valores.append(int(input(f'Digite um valor para a Posição {i}: ')))

print('=-' * 30)
print(f'Você digitou os valores {valores}.')

print(f'O maior valor digitado foi {max(valores)} nas posições ', end='')

for i in range(0, 5):
    if valores[i] == max(valores):
        print(f'{i}...', end=' ')

print(f'\nO menor valor digitado foi {min(valores)} nas posições ', end='')

for i in range(0, 5):
    if valores[i] == min(valores):
        print(f'{i}...', end=' ')
