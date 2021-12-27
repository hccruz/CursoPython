from time import sleep

c = ('\033[m',          # 0 - sem cores
     '\033[0;30;41m',   # 1 - vermelho
     '\033[0;30;42m',   # 2 - verde
     '\033[0;30;43m',   # 3 - amarelo
     '\033[0;30;44m',   # 4 - azul
     '\033[0;30;45m',   # 5 - roxo
     '\033[7;40m'    # 6 - branco
     )


def escreva(msg, cor=0):
    tamanho = len(msg) + 4
    print(c[cor], end='')
    print('~' * tamanho)
    print(f'  {msg}')
    print('~' * tamanho)
    print(c[0], end='')
    sleep(1)


def ajuda(f):
    escreva(f"Acessando o manual do comando '{f}'", 4)
    print(c[6], end='')
    help(f)
    print(c[0], end='')
    sleep(2)


# Programa principal
while True:
    escreva('SISTEMA DE AJUDA PyHELP', 2)
    funcao = input('Função ou Biblioteca > ').lower().strip()
    if funcao == 'fim':
        escreva('ATÉ LOGO!', 1)
        break
    ajuda(funcao)

