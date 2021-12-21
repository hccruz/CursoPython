valores = []

for i in range(0, 5):
    num = int(input('Digite um valor: '))
    if i == 0 or num > valores[-1]:
        valores.append(num)
        print('Adicionado no final da lista...')
    else:
        pos = 0
        while pos < len(valores):
            if num <= valores[pos]:
                valores.insert(pos, num)
                print(f'Adicionado na posição {pos} da lista...')
                break
            pos += 1

print('=-' * 30)
print(f'Os valores digitados em ordem foram {valores}')
