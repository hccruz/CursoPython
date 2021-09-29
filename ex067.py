print('-=' * 7)
print(f'TABAUADA v3.0')
print('-=' * 7)

while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    print('-' * 10)
    if n <= 0:
        break
    for i in range (1, 11):
        print(f'{n} x {i} = {n * i}')
    print('-' * 10)
print('PROGRAMA ENCERRADO')
