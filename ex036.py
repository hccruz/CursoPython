print('Qual é o valor da casa? Em reais.')
casa = float(input())
print('Qual o salário do comprador? Em reais.')
salario = float(input())
print('Em quantos anos ele vai pagar?')
anos = int(input())

prestacao = casa / (anos * 12)

if prestacao >= salario * 0.3:
    print(f'Empréstimo negado!!! Consiga mais uma fonte de renda!!! '
          f'O valor da prestação será de R${prestacao:.2f}.')
else:
    print(f'Empréstimo concedido!!! Parabéns pelo financiamento!!! '
          f'O valor da prestação será de R${prestacao:.2f}.')
