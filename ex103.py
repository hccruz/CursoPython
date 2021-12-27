def ficha(j='<desconhecido>', g=0):
    return f'O jogador {j} fez {g} gol(s) no campeonato.'


# Programa principal
jogador = input('Nome do Jogador: ')
gols = input('Número de Gols: ')
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if jogador.strip() == '':
    print(ficha(g=gols))
else:
    print(ficha(jogador, gols))
