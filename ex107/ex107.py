import uteis

preco = float(input('Digite o preço: R$'))
print(f'A metade de R${preco:.2f} é R${uteis.metade(preco):.2f}')
print(f'O dobro de R${preco:.2f} é R${uteis.dobro(preco):.2f}')
print(f'Aumentando 10%, temos R${uteis.aumentar(preco, 10):.2f}')
