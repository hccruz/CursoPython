print('-=' * 12)
print('MAIOR OU MENOR VALORES')
print('-=' * 12)

continua = 'S'
contador = soma = 0

while continua not in 'Nn':
    n = int(input('Digite um número inteiro: '))
    if contador == 0:
        maior = menor = n
    if n > maior:
        maior = n
    if n < menor:
        menor = n
    soma += n
    continua = input('Quer digitar mais valores? [S ou N]').strip()[0]
    contador += 1

media = soma / (contador)

print(f'Você digitou {contador} números, a soma total é {soma}, sua média é {media},' +
      f'o menor número é {menor} e o maior número é {maior}.')