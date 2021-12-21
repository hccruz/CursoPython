brasileiro = ('Atlético-MG', 'Flamengo', 'Palmeiras', 'Corinthians', 'Fortaleza', 'Bragantino', 'Fluminense',
              'América-MG', 'Atlético-GO', 'Ceará', 'Santos', 'Internacional', 'São Paulo', 'Athletico-PR',
              'Cuiabá', 'Bahia', 'Juventude', 'Grêmio', 'Sport', 'Chapecoense')

print('-=' * 15)
print(f'Listar todos os times do Brasileirão: {brasileiro[-20:]}')

print('-=' * 15)
print(f'Listar os 5 primeiros times do Brasileirão: {brasileiro[:5]}')

print('-=' * 15)
print(f'Listar os 4 últimos times do Brasileirão: {brasileiro[-4:]}')

print('-=' * 15)
print(f'Os times do Brasileirão em ordem alfabética: {sorted(brasileiro)}')

print('-=' * 15)
print(f'A Chapecoense está na {brasileiro.index("Chapecoense") + 1}ª posição')
