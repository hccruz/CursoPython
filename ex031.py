distancia = float(input('Digite a distância da viagem em km: '))

if (distancia <= 200):
    print('O preço da passagem é R${:.2f}.'.format(distancia * 0.5))
else:
    print('O preço da passagem é R${:.2f}.'.format(distancia * 0.45))
