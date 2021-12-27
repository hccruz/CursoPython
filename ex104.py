def leiaInt(msg):
    print('-' * 20)
    while True:
        num = input(msg)
        if num.isnumeric():
            num = int(num)
            break
        else:
            print('\033[1;31mERRO! Digite um número inteiro válido.\033[0;0m')
    return num


# Programa principal
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}.')
