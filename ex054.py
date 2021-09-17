from datetime import date

print('-=-' * 7)
print('GRUPO DA MAIORIDADE')
print('-=-' * 7)

ano_atual = date.today().year
menor = 0
maior = 0

for i in range(1, 8):
    ano_nasc = int(input(f'Digite o ano de nascimento da {i}° pessoa: '))
    idade = ano_atual - ano_nasc
    if idade < 18:
        menor += 1
    else:
        maior += 1

print(f'\nNeste gurpo de sete pessoas tem {menor} MENOR(ES) de idade e {maior} MAIOR(ES) de idade.')
