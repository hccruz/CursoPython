num1 = int(input('Digite o 1° número: '))
num2 = int(input('Digite o 2° número: '))

print('''Escolha a opção desejada:
[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa''')

opcao = input('Digite a opção desejada: ')

while opcao != '5':
    if opcao == '1':
        soma = num1 + num2
        print(f'\nA soma dos números {num1} e {num2} é {soma}.')
    elif opcao == '2':
        mult = num1 * num2
        print(f'\nA multiplicação dos números {num1} e {num2} é {mult}.')
    elif opcao == '3':
        if num1 > num2:
            print(f'\nO número {num1} é maior do que o número {num2}.')
        else:
            print(f'\nO número {num2} é maior do que o número {num1}.')
    elif opcao == '4':
        num1 = int(input('\nDigite o 1° número: '))
        num2 = int(input('Digite o 2° número: '))
    elif opcao != '5':
        print('Dados inválidos. Tente novamente!!!!')
    print('''\nEscolha a opção desejada:
    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa''')

    opcao = input('Digite a opção desejada: ')

print('\nVocê saiu do programa!!!!')