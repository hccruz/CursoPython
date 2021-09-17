nome = input('Digite seu nome completo: ')

lista = nome.split()

print('Analisando seu nome...')

print('Seu nome em maiúsculas é {}.'.format(nome.upper()))
print('Seu nome em minúsculas é {}.'.format(nome.lower()))
print('Seu nome tem ao todo {} letras.'.format(len(nome.replace(' ', ''))))
print('Seu primeiro nome é {} e ele tem {} letras.'.format(lista[0],
                                                           len(lista[0])))
