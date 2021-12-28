def leiaDinheiro(msg='0'):
    while True:
        preco = input(msg).strip().replace(',', '.')
        if preco.replace('.', '').isnumeric():
            break
        print(f'\033[1;31mERRO: "{preco}" é um preço inválido!\033[m')
    return float(preco)
