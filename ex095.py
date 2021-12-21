list_jogador = []
dados_jogador = {}
gol = []

while True:
    dados_jogador['nome'] = input('Nome do jogador: ')
    jogos = int(input(f'Quantos partidas {dados_jogador["nome"]} jogou? '))

    for i in range(0, jogos):
        gol.append(int(input(f'Quantos gols na partida {i +1}? ')))

    dados_jogador['gols'] = gol[:]
    dados_jogador['total'] = sum(gol)
    gol.clear()
    while True:
        resp = input('Quer continuar? [S/N] ').upper().strip()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda S ou N.')
    list_jogador.append(dados_jogador.copy())
    if resp == 'N':
        break

print('-=' * 30)
print('cod', end=' ')

for i in dados_jogador.keys():
    print(f'{i:<15}', end='')
print()

print('-' * 50)

for i, j in enumerate(list_jogador):
    print(f'{i:>3}', end=' ')
    for d in j.values():
        print(f'{str(d):<15}', end='')
    print()

while True:
    print('-' * 50)
    busca = int(input('Mostrar os dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(list_jogador):
        print(f'ERRO! Não existe jogador com código {busca}!')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {list_jogador[busca]["nome"]}:')
        for i, g in enumerate(list_jogador[busca]["gols"]):
            print(f'    => Na partida {i + 1}, fez {g} gols.')

print('<< VOLTE SEMPRE >>')
