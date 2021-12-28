import uteis

preco = float(input('Digite o preço: R$'))
print(f'A metade de {uteis.trocar(preco)} é {uteis.metade(preco)}')
print(f'O dobro de {uteis.trocar(preco)} é {uteis.dobro(preco)}')
print(f'Aumentando 10%, temos {uteis.aumentar(preco, 10)}')
print(f'Diminuindo 20%, temos {uteis.diminuir(preco, 20)}')
