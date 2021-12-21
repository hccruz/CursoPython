import time
from random import randint

num = 0
jogo = []
temp = []

print('-' * 30)
print(f'{"JOGO DA MEGA SENA":^30}')
print('-' * 30)

quant_jogos = int(input('Quantos jogos você quer que eu sorteie? '))

for j in range(0, quant_jogos):
    for i in range(0, 6):
        num = randint(1, 60)
        while num in temp:
            num = randint(1, 60)
        temp.append(num)
    temp.sort()
    jogo.append(temp[:])
    temp.clear()

print('-=' * 3 + f'  SORTEANDO {quant_jogos} JOGOS  ' + '-=' * 3)

for i in range(0, quant_jogos):
    print(f'Jogo {i + 1}: {jogo[i]}')
    time.sleep(1)

print('-=' * 5 + f'{"< BOA SORTE! >":^16}' + '-=' * 5)
