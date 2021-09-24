print('-=-' * 7)
print('PROGRESSÃO ARITMÉTICA')
print('-=-' * 7)

primeiro_termo = int(input('Digite o primeiro termo da P.A.: '))
razao = int(input('Digite a razão da P.A.: '))

contador = 1
PA = primeiro_termo

while contador <= 10:
    print(PA, end=' ')
    PA += razao
    contador += 1
