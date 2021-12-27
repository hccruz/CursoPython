from random import randint
from time import sleep


def sorteia(num):
    num_lst = []
    print(f'Sorteando {num} valores da lista:', end=' ')
    for i in range(0, num):
        n = randint(0, 10)
        print(n, end=' ')
        num_lst.append(n)
        sleep(0.3)
    print('PRONTO!')
    somaPar(num_lst)


def somaPar(lst):
    s = 0
    for v in lst:
        if v % 2 == 0:
            s += v
    print(f'Somando os valores pars de {lst}, temos {s}.')


#Programa principal
sorteia(5)
