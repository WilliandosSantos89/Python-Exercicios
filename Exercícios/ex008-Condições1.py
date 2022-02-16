nome = str(input('Qual seu nome?')).strip()

if nome == 'Willian':
    print('Que nome lindo você tem!')
    print('Bom dia, {}'.format(nome))
else:
    print('Bom dia {}.'.format(nome))
    print('Seu nome é tão normal!')