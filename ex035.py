print('-=-' * 20)
print('ANALISADOR DE TRIÂNGULOS')
print('-=-' * 20)
print('\n')

a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))

if (a < (b + c)) and (b < (a + c)) and (c < (a + b)):
    print('\n\033[33mOs segmentos acima\033[m \033[1;31mPODEM ' +
          'FORMAR\033[m \033[33mum triângulo.\033[m\n')
else:
    print('\n\033[33mOs segmentos acima\033[m \033[1;31mNÃO PODEM ' +
          'FORMAR\033[m \033[33mum triângulo.\033[m\n')
