from random import randint
from time import sleep

dados = {}

print('Valores sorteados:')

for i in range (0, 4):
    dados[f'jogador {i + 1}'] = randint(1, 6)
    print(f'O jogador {i + 1} tirou {dados[f"jogador {i + 1}"]} no dado.')
    sleep(1)

print('-=' * 30)
print(f'{"== RANKING DOS JOGADORES ==":^31}')

n = 1
for i in sorted(dados, key=dados.get, reverse=True):
    print(f'{n}º lugar: {i} com {dados[i]}.')
    sleep(1)
    n += 1
