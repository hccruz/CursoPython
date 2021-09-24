print('-=-' * 7)
print('PROGRESSÃO ARITMÉTICA')
print('-=-' * 7)

primeiro_termo = int(input('Digite o primeiro termo da P.A.: '))
razao = int(input('Digite a razão da P.A.: '))

contador = 1
PA = primeiro_termo
total = 0
mais_termos = 10

while mais_termos != 0:
    total += mais_termos
    while contador <= total:
        print(PA, end=' ')
        PA += razao
        contador += 1
    mais_termos = int(input('\nQuantos termos você quer mostrar mais? '))

print(f'\nProgressão finalizada com {total} termos mostrados.')