print('=' * 30)
print('{:^30}'.format('BANCO MONETÁRIO'))
print('=' * 30)

dinheiro = int(input('Qual valor você quer sacar? R$ '))

nota50 = nota20 = nota10 = nota1 = 0

nota50 = dinheiro // 50
nota20 = (dinheiro % 50) // 20
nota10 = ((dinheiro % 50) % 20) // 10
nota1 = dinheiro % 10

if nota50 != 0:
    print(f'Total de {nota50} cédulas de R$ 50.00')
if nota20 != 0:
    print(f'Total de {nota20} cédulas de R$ 20.00')
if nota10 != 0:
    print(f'Total de {nota10} cédulas de R$ 10.00')
if nota1 != 0:
    print(f'Total de {nota1} cédulas de R$ 1.00')

print('=' * 30)
print('Muito obrigado! Volte sempre ao Banco Monetário')