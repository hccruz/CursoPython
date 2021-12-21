palavras = ('aprender', 'programa', 'linguagem', 'python', 'curso', 'gratis', 'estudar', 'praticar',
            'trabalhar', 'mercado', 'programador', 'futuro')

for palavra in palavras:
    print(f'\nNa palavra {palavra.upper()} temos ', end='')
    for letra in palavra.lower():
        if letra in 'aeiou':
            print(f'{letra}', end=' ')



