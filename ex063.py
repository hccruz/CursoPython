print('-=' * 11)
print('SEQUÊNCIA DE FIBONACCI')
print('-=' * 11)

N = int(input('Quantos termos você quer mostrar? '))

segundoTermo = 0
primeiroTermo = 0

contador = 1

while contador <= N:
    if contador == 2 or contador == 3:
        primeiroTermo = 1
        segundoTermo = 0
    fibonacci = primeiroTermo + segundoTermo
    print(f'{fibonacci} - ', end='')
    segundoTermo = primeiroTermo
    primeiroTermo = fibonacci
    contador += 1

print('FIM')
