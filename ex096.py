def area(l, c):
    a = l * c
    print(f'A área de um terreno de {l}m x {c}m é {a}m².')


print(' Controle de Terrenos')
print('----------------------')

larg = float(input('LARGURA (m): '))
comp = float(input('COMPRIMENTO (m): '))

area(larg, comp)
