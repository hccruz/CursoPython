def notas(*n, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias).
    :param sit: valor opcional, indicando se deve ou não adicionar a situação.
    :return: dicionário com várias informações sobre a situação da turma.
    """
    aluno = {}
    aluno['total'] = len(n)
    aluno['maior'] = max(n)
    aluno['menor'] = min(n)
    media = sum(n) / len(n)
    aluno['media'] = f'{media:.2f}'
    if sit:
        if media >= 7:
            aluno['situacao'] = 'BOA'
        elif media >= 5:
            aluno['situacao'] = 'RAZOÁVEL'
        else:
            aluno['situacao'] = 'RUIM'

    return aluno


# Programa principal
resp = notas(3.5, 9.5, 7, 10, sit=True)
print(resp)
# help(notas)
