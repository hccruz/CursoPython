listanum = []

resp = 'S'

while resp == 'S':
    listanum.append((int(input('Digite um valor: '))))
    resp = input('Quer continuar? [S/N]: ').upper().strip()[0]

print('-=' * 30)
print(f'Você digitou {len(listanum)} elementos.')

listanum.sort(reverse=True)
print(f'Os valores em ordem decrescente são {listanum}')

if 5 in listanum:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não faz parte da lista!')
