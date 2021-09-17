sexo = input('Informe seu sexo: [M/F] ').upper().strip()[0]

while sexo != 'M' and sexo != 'F':
    sexo = input('Dados inválidos. Por favor, informe seu sexo: [M/F] ').upper().strip()[0]

print(f'Sexo {sexo} registrado com sucesso!!!')