expressao = []

string = input('Digite a espressão: ')

for l in string:
    expressao.append(l)

if expressao.count('(') == expressao.count(')'):
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')
