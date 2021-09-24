print('-=' * 12)
print('TRATANDO VÁRIOS VALORES')
print('-=' * 12)

n = int(input('Digite um número inteiro [999 para parar]: '))
contador = 0
total = 0

while n != 999:
    total += n
    contador += 1
    n = int(input('Digite um número inteiro [999 para parar]: '))

print(f'Você digitou {contador} números e a soma total é {total}.')