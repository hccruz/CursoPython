from time import sleep


def contador(i, f, p):
    print('-=' * 20)
    p = abs(p)
    if p == 0:
        p = 1
    print(f'Contagem de {i} até {f} de {p} em {p}')
    if i < f:
        for n in range(i, f+1, p):
            print(n, end=' ')
            sleep(0.5)
    else:
        for n in range(i, f-1, -(p)):
            print(n, end=' ')
            sleep(0.5)
    print('FIM!')


# Programa principal
contador(1, 10, 1)
contador(10, 0, 2)
print('-=' * 20)
print('Agora é sua vez de  personalizar a contagem!')
ini = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(ini, fim, passo)
print('-=' * 20)
