extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove',
           'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito',
           'dezenove', 'vinte')

resp = 'S'

while resp == 'S':
    numero = int(input('Digite um número entre 0 e 20: '))
    while numero < 0 or numero > 20:
        print('Número fora do intervalo pedido.')
        numero = int(input('Digite um número entre 0 e 20: '))
    print(f'O número digitado foi {extenso[numero]}')
    resp = input('Você quer continuar? (S or N): ').upper().strip()[0]
    while resp not in 'SN':
        print('Opção incorreta!!!')
        resp = input('Você quer continuar? (S or N): ').upper().strip()[0]

print('Programa finalizado!!!!')
