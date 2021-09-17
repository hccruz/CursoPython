num1 = int(input('Primeiro valor: '))
num2 = int(input('Segundo valor: '))
num3 = int(input('Terceiro valor: '))

# Verificando o menor valor
menor = num1

if num2 < num1 and num2 < num3:
    menor = num2

if num3 < num1 and num3 < num2:
    menor = num3

# Verificando o maior valor
maior = num1

if num2 > num1 and num2 > num3:
    maior = num2

if num3 > num1 and num3 > num2:
    maior = num3

print('\nO maior valor digitado é {}.'.format(maior))
print('\nO menor valor digitado é {}.'.format(menor))
