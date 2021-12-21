notas = []
nomes = []
temp = []

resp = 'S'
num = 0

while resp == 'S':
    nomes.append(input('Nome: '))
    for i in range(0, 2):
        temp.append(float(input(f'Nota {i + 1}: ')))
    nomes.append(temp[:])
    notas.append(nomes[:])
    temp.clear()
    nomes.clear()
    resp = input('Quer continuar? [S/N] ').upper().strip()[0]

print('-=' * 30)
print(f'{"No.":<4}{"NOME":<14}{"MÉDIA":>5}')
print('-' * 30)
for i, nome in enumerate(notas):
    print(f'{i + 1:<3}', end=' ')
    print(f'{nome[0]:<14}', end='')
    print(f'{(nome[1][0] + nome[1][1])/2:>5}')

print('_' * 30)

while True:
    num = int(input('Digite o número do aluno que você quer ver as notas (999 interrompe): '))
    if num == 999:
        break
    num -= 1
    print(f'Notas do {notas[num][0]} são {notas[num][1]}')

print('FINALIZANDO...')
print('<<< VOLTE SEMPRE >>>')




