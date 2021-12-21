num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
num3 = int(input('Digite mais um número: '))
num4 = int(input('Digite o último número: '))

numeros = (num1, num2, num3, num4)
print(f'Você digitou os valores {numeros}.')
print(f'O valor 9 apareceu {numeros.count(9)} vez(es).')
if 3 not in numeros:
    print('Não foi encontrado nenhum valor 3.')
else:
    print(f'O valor 3 foi digitado na {numeros.index(3) + 1}ª posição.')

print('Os valores pares digitados foram ', end='')
for n in numeros:
    if n % 2 == 0:
        print(n, end=' ')
