nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

media = (nota1 + nota2) / 2

if media < 5:
    print(f'REPROVADO!!! Com nota média de {media:.1f}')
elif media < 7:
    print(f'EM RECUPERAÇÃO!!! Com nota média de {media:.1f}')
else:
    print(f'APROVADO!!! Com nota média de {media:.1f}')