print('-=' * 12)
print('VÁRIOS NÚMEROS COM FLAG')
print('-=' * 12)

cont = soma = 0

while True:
    n = int(input('Digite um número (999 para parar): '))
    if n == 999:
        break
    soma += n
    cont += 1

print(f'Foram digitados {cont} números e a soma total é {soma}.')
