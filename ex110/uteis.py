def trocar(p):
    """
    Função que tansforma um número de ponto flutuante em formato de moeda brasileira.
    :param p: Valor em ponto flutuante.
    :return: Retorna o valor como string em formato de moeda.
    """
    return f'R${p:.2f}'.replace('.', ',')


def metade(p):
    """
    Função que retorna a metade de um valor dado
    :param p: Valor em ponto flutuante
    :return: Retorna a metade do valor dado como string em formato de moeda.
    """
    return trocar(p / 2)


def dobro(p):
    return trocar(p * 2)


def aumentar(p, porcentagem):
    return trocar(p * (1 + (porcentagem / 100)))


def diminuir(p, porcentagem):
    return trocar(p * (1 - (porcentagem / 100)))


def resumo(p: object, taxa_aumento: object = 10, taxa_reducao: object = 5) -> object:
    print('-' * 30)
    print(f'{"RESUMO DO VALOR":^30}')
    print('-' * 30)
    print(f'{"Preço analisado:":<20}{trocar(p):>10}')
    print(f'{"Dobro do preço:":<20}{dobro(p):>10}')
    print(f'{"Metade do preço:":<20}{metade(p):>10}')
    print(f'{taxa_aumento}{"% de aumento:":<18}{aumentar(p, taxa_aumento):>10}')
    print(f'{taxa_reducao}{"% de redução:":<18}{diminuir(p, taxa_reducao):>10}')
    print('-' * 30)
