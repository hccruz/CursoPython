velocidade = float(input('Digite a velocidade do carro: '))

if (velocidade > 80):
    multa = (velocidade - 80) * 7
    print('\nVocê foi multado e pagará um valor de R${:.2f}.\n'.format(multa))
else:
    print('\nTenha um bom dia! Dirija com segurança!\n')
