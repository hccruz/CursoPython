numero = int(input('Digite um número inteiro: '))

print('Escolha a base de conversão:')
conversao = input('Digite 1 para binário, 2 para octal e 3 para hexadecimal: ')

if conversao == '1':
    binario = bin(numero)[2:]
    print(f'O número {numero} na base binária é {binario}.')
elif conversao == '2':
    octal = oct(numero)[2:]
    print(f'O número {numero} na base octadecimal é {octal}.')
elif conversao == '3':
    hexa = hex(numero)[2:]
    print(f'O número {numero} na base hexadecimal é {hexa}.')

