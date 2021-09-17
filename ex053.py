print('-=-' * 7)
print('DETECTOR DE PALÍNDROMO')
print('-=-' * 7)

texto = input('Digite um texto: ').strip().upper()

palavras = texto.split()
junto = ''.join(palavras)
inverso = ''

for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]

if inverso == junto:
    print(f'O texto digitado: "{texto}", é um PALÍNDROMO.')
else:
    print(f'O texto digitado: "{texto}", não é um PALÍNDROMO.')
