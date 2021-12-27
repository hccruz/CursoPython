from time import sleep


def maior(* num):
    print('-=' * 30)
    print('Analisando os valores passados...')
    if len(num) > 0:
        m = num[0]
        for i in range(0, len(num)):
            print(num[i], end=' ')
            sleep(1)
            if m < num[i]:
                m = num[i]
        print('FIM!')
        print(f'Foram informados {len(num)} valores ao todo')
        print(f'O maior valor informado foi {m}.')
    else:
        print(f'Foram informados 0 valores ao todo')
        print(f'O maior valor informado foi 0.')


maior(6, 7, 5, 2, 8, 1)
maior(3, 9, 4)
maior(2, 5)
maior(6)
maior()
