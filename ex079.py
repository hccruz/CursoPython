valores = []

resp = 'S'

while resp == 'S':
    num = int(input('Digite um valor: '))
    if num not in valores:
        valores.append(num)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    resp = input('Quer continuar? [S/N]: ').upper()

valores.sort()
print('=-' * 30)
print(f'Você digitou os valores {valores}')
