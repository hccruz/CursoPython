print('-=-' * 7)
print('Maior e menor da sequência')
print('-=-' * 7)

for i in range(1, 6):
    peso = float(input(f'Digite o peso da {i}° pessoa: '))
    if i == 1:
        maior = peso
        menor = peso
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso

print(f'\nO maior peso digitado foi {maior}kg e o menor peso digitado foi {menor}kg.')
