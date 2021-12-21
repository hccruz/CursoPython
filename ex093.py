dados_jogador = {}
gol = []

dados_jogador['nome'] = input('Nome do jogador: ')
jogos = int(input(f'Quantos partidas {dados_jogador["nome"]} jogou? '))

for i in range(0, jogos):
    gol.append(int(input(f'Quantos gols na partida {i +1}? ')))

dados_jogador['gols'] = gol
dados_jogador['total'] = sum(gol)

print('-=' * 30)
print(dados_jogador)
print('-=' * 30)

for k, v in dados_jogador.items():
    print(f'O campo {k} tem o valor {v}.')

print('-=' * 30)
print(f'O jogador {dados_jogador["nome"]} jogou {jogos} partidas.')
for i in range(0, jogos):
    print(f'    => Na partida {i + 1}, fez {dados_jogador["gols"][i]}.')
print(f'Foi um total de {dados_jogador["total"]} gols.')
