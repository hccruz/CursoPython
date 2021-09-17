salario = float(input('Informe o salário do funcionários em R$: '))

if salario > 1250:
    salario += salario * 0.1
    print('\nVocê recebeu um aumento de 10% e seu ' +
          'salário agora é R${:.2f}.\n'.format(salario))
else:
    salario += salario * 0.15
    print('\nVocê recebeu um aumento de 15% e seu ' +
          'salário agora é R${:.2f}.\n'.format(salario))
