from utilidades import moeda
from utilidades import dado

preco = dado.leiaDinheiro('Digite o preço: R$')
moeda.resumo(preco, 15, 20)
