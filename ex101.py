def voto(ano):
    """
    Função para validar se uma pessoa deve votar conforme dado seu ano de nascimento.
    :param ano: Ano de nascimento da pessoa.
    :return: Situação da pessoa: NÃO VOTA, VOTO OPCIONAL, VOTO OBRIGATÓRIO.
    """
    import datetime
    ano_atual = datetime.datetime.now().year
    idade = ano_atual - ano
    if idade < 16:
        situacao = 'NÃO VOTA!'
    elif 18 <= idade <= 65:
        situacao = 'VOTO OBRIGATÓRIO!'
    else:
        situacao = 'VOTO OPCIONAL!'
    return f'Com {idade} anos: {situacao}'


# Programa principal
print('-' * 30)
ano_nasc = int(input('Em que ano você nasceu? '))
print(voto(ano_nasc))
