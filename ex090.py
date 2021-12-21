aluno = {}

aluno['nome'] = input('Nome: ')
aluno['media'] = float(input(f'Média do {aluno["nome"]}: '))

if aluno['media'] >= 7:
    aluno['situacao'] = 'Aprovado'
elif aluno['media'] > 3:
    aluno['situacao'] = 'Recuperação'
else:
    aluno['situacao'] = 'Reprovado'

print('-=' * 30)
for k, v in aluno.items():
    print(f'- {k} é igual a {v}.')
