peso = float(input('Por favor, informe o seu peso: '))
altura = float(input('Por favor, informe a sua altura: '))

IMC = peso / altura ** 2

if IMC < 18.5:
    print(f'Seu IMC é {IMC:.2f} e você está abaixo do peso.')
elif IMC < 25:
    print(f'Seu IMC é {IMC:.2f} e você está no peso ideal.')
elif IMC < 30:
    print(f'Seu IMC é {IMC:.2f} e você está com sobrepeso.')
elif IMC < 40:
    print(f'Seu IMC é {IMC:.2f} e você está com obesidade.')
else:
    print(f'Seu IMC é {IMC:.2f} e você está com obesidade mórbida.')
