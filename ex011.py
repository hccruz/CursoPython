largura = float(input('Digite o largura da parede: '))
altura = float(input('Digite a altura da parede: '))

area = largura * altura
tinta = area / 2

print('Para pintar a parede de {:.2f}m², precisa de {:.2f}l de tinta.'.format(
    area, tinta))
