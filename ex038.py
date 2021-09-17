num1 = int(input('Digite o primeiro valor inteiro: '))
num2 = int(input('Digite o segundo valor inteiro: '))

if num1 > num2:
    print('O PRIMEIRO valor é maior.')
elif num2 > num1:
    print('O SEGUNDO valor é o maior.')
elif num1 == num2:
    print('Não existe valor maior, os dois são IGUAIS.')
