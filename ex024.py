cidade = input('Em que cidade você nassceu? ').lower().strip()

num = cidade.find(' ')

print('santo' in cidade[:num])
