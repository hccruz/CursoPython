import random

print('-=' * 9)
print('JOGO PAR OU ÍMPAR')
print('-=' * 9)

vitoria = 0

while True:
    num_usuario = int(input('Digite um valor: '))
    while True:
        escolha_usuario = input('Par ou Ímpar? [P/I] ').upper().strip()[0]
        if escolha_usuario in 'PI':
            break
    num_computador = random.randint(1, 10)
    resultado = num_usuario + num_computador
    if resultado % 2 == 0:
        resultado2 = 'PAR'
    else:
        resultado2 = 'ÍMPAR'
    print('-' * 50)
    print(f'Você jogou {num_usuario} e o computador {num_computador}. Total de {resultado}, FOI {resultado2}')
    print('-' * 50)
    if (escolha_usuario == 'P' and resultado % 2 == 0) or (escolha_usuario == 'I' and resultado % 2 != 0):
        print('VOCÊ VENCEU!!!!!')
        print('-' * 50)
        vitoria += 1
    else:
        print('VOCÊ PERDEU!!!!!')
        print('-' * 50)
        break

print(f'GAME OVER. Você venceu {vitoria} partidas.')