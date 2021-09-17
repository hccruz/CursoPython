from random import randint
from time import sleep

print('-=-' * 20)
print('Pensei em um número entre 0 e 10. Tente adivinhar!')
print('-=-' * 20)

# Faz o computador "pensar"
num = randint(0, 10)

# Número de palpites
palpite = 1

# Jogador tenta adivinhar
num2 = int(input('\nDigite um número entre 0 e 10: '))

while num != num2:
    print('\nProcessando...')
    sleep(3)
    print('\nVocê perdeu. Tente outra vez!')
    palpite += 1
    num2 = int(input('\nDigite um número entre 0 e 10: '))

print(f'\nVocê venceu. Parabéns! Você acertou em {palpite} palpite(s).')