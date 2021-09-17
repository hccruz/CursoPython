print('-=-' * 7)
print('PROGRESSÃO ARITMÉTICA')
print('-=-' * 7)

primeiro_termo = int(input('Digite o primeiro termo da P.A.: '))
razao = int(input('Digite a razão da P.A.: '))

for i in range(1, 11):
    if i == 1:
        PA = primeiro_termo
        print(PA, end=' ')
        continue
    PA = PA + razao
    print(PA, end=' ')
