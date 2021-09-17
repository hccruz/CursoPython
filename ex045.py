from random import randint
from time import sleep

print('-=-' * 20)
print('JOGO JOKENPÔ')
print('-=-' * 20)
print('\n')

print('Vamos jogar um pouco de jokenpô. Faça a sua jogada.\n')
escolha_usario = int(input('Escolha um elemento do jokenpô, 1-pedra,' +
                           ' 2-papel, 3-tesoura: '))

print('Jo')
sleep(1)
print('Ken')
sleep(1)
print('Pô!!!!!')

if escolha_usario == 1:
    print('Você escolheu pedra.')
elif escolha_usario == 2:
    print('Você escolheu papel.')
elif escolha_usario == 3:
    print('Você escolheu tesoura.')

escolha_computador = randint(1, 3)

if escolha_computador == 1:
    print('Computador escolheu pedra.')
elif escolha_computador == 2:
    print('Computador escolheu papel.')
elif escolha_computador == 3:
    print('Computador escolheu tesoura.')

if escolha_usario == escolha_computador:
   print('Empate, jogue novamente.')
elif escolha_usario == 1 and escolha_computador == 2:
    print('Computador ganha.')
elif escolha_usario == 1 and escolha_computador == 3:
    print('Você ganha.')
elif escolha_usario == 2 and escolha_computador == 1:
    print('Você ganha.')
elif escolha_usario == 2 and escolha_computador == 3:
    print('Computador ganha.')
elif escolha_usario == 3 and escolha_computador == 1:
    print('Computador ganha.')
elif escolha_usario == 3 and escolha_computador == 2:
    print('Você ganha.')