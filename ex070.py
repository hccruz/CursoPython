print('-' * 30)
print('{:^30}'.format('LOJA HIPER BARATO'))
print('-' * 30)

total = produto1000 = 0
cont = 1

while True:
    produto = input('Nome do Produto: ').strip()
    preco = float(input('Preço: R$ '))
    total += preco
    if preco > 1000:
        produto1000 += 1
    if cont == 1 or menorpreco > preco:
        menorpreco = preco
        menorproduto = produto
    resp = ' '
    while resp not in 'SN':
        resp = input('Quer continuar? [S/N] ').strip().upper()[0]
    if resp == 'N':
        break
    cont += 1

print('-' * 30)
print('{:^30}'.format('FIM DO PROGRAMA'))
print('-' * 30)

print(f'O total da compra foi R$ {total:.2f}.')
print(f'{produto1000} produtos custam mais de R$ 1000.00.')
print(f'O produto mais barato é {menorproduto} e custa R$ {menorpreco:.2f}.')
