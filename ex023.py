num = int(input('Informe um número: '))

print('Analisando o número {}.'.format(num))
print('Unidade: {}'.format(num % 10))
print('Dezena: {}'.format((num % 100) // 10))
print('Centena: {}'.format((num % 1000) // 100))
print('Milhar: {}'.format(num // 1000))
