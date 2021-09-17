escala = input('Digite C para converter gruas Celsisus em Fahrenheit' +
               ' ou digite F para converte graus Fahrenheit em Celsius: ')

while ((escala != 'C') and (escala != 'c') and
       (escala != 'F') and (escala != 'f')):
    escala = input('Digite C para converter gruas Celsisus em Fahrenheit' +
                   ' ou digite F para converte graus Fahrenheit em Celsius: ')

if (escala == 'C' or escala == 'c'):
    Fahr = float(input('Digite a temperatura em Fahrenheit: '))
    Cels = (Fahr - 32) * 5 / 9
    print('A temperatura de {}°F equivale a {}°C.'.format(Fahr, Cels))

if (escala == 'F' or escala == 'f'):
    Cels = float(input('Digite a temperatura em Celsius: '))
    Fahr = (Cels * 9 / 5) + 32
    print('A temperatura de {}°C equivale a {}°F.'.format(Cels, Fahr))
