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


def linha(tam=42):
    return '-' * tam


def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabecalho('MENU PRINCIPAL')
    for i, v in enumerate(lista):
        print(f'\033[33m{i+1} -\033[34m {v}\033[m')
    print(linha())
    opc = leia_int('\033[32mSua opção: \033[m')
    return opc
