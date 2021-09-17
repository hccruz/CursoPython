print('{:=^40}'.format('LOJAS AMERICANAS'))

preco_real = float(input('Digite o valor real do produto: R$'))
forma_pagamento = input('Digite a forma de pagamento, ' +
                            '1- dinheiro/cheque; 2- à vista no cartão; ' +
                            '3- 2x no cartão; 4- 3x ou mais no cartão: ')

if forma_pagamento == '1':
    preco_pagar = preco_real * 0.9
    print(f'O valor do produto à vista em dinheiro ou cheque é de R${preco_pagar:.2f}.')
elif forma_pagamento == '2':
    preco_pagar = preco_real * 0.95
    print(f'O valor do produto à vista no cartão é de R${preco_pagar:.2f}.')
elif forma_pagamento == '3':
    parcela = preco_real / 2
    print(f'O valor do produto em 2x no cartão é de R${preco_real:.2f}.')
    print(f'O valor da parcela será de R${parcela:.2f}.')
else:
    quant = int(input('Quantidade de parcelas: '))
    preco_pagar = preco_real * 1.2
    parcela = preco_pagar / quant
    print(f'O valor do produto em {quant}x no cartão é de R${preco_pagar:.2f}.')
    print(f'O valor da parcela será de R${parcela:.2f}.')
