def trocar(p):
    return f'R${p:.2f}'.replace('.', ',')


def metade(p):
    return trocar(p / 2)


def dobro(p):
    return trocar(p * 2)


def aumentar(p, porcentagem):
    return trocar(p * (1 + (porcentagem / 100)))


def diminuir(p, porcentagem):
    return trocar(p * (1 - (porcentagem / 100)))



