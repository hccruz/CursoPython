def leia_int(msg):
    while True:
        try:
            num = int(input(msg))
        except (ValueError, TypeError):
            print('\033[1;31mERRO! Digite um número inteiro válido.\033[0;0m')
        except KeyboardInterrupt:
            print('\n\033[31mEntrada de dados interrompida pelo usuário.\033[m')
            break
        else:
            return num


def leia_real(msg):
    while True:
        try:
            num = float(input(msg).replace(',', '.'))
        except (ValueError, TypeError):
            print('\033[1;31mERRO! Digite um número real válido.\033[0;0m')
        except KeyboardInterrupt:
            print('\n\033[31mEntrada de dados interrompida pelo usuário.\033[m')
            break
        else:
            return num


# Programa principal
n = leia_int('Digite um Inteiro: ')
r = leia_real('Digite um Real: ')
print(f'O valor inteiro digitado foi {n} e o real foi {r}.')
