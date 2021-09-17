from random import randint
from time import sleep

print('-=-' * 20)
print('Pensei em um número entre 0 e 5. Tente adivinhar!')
print('-=-' * 20)

# Faz o computador "pensar"
num = randint(0, 5)

# Jogador tenta adivinhar
num2 = int(input('\nDigite um número entre 0 e 5: '))

print('\nProcessando...')
sleep(3)

if (num == num2):
    print('\nVocê venceu. Parabéns!')
else:
    print('\nVocê perdeu. Tente outra vez!')
    print('\nO número que pensei foi {}.'.format(num))
