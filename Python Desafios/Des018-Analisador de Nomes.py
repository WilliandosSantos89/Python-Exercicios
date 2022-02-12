print('>>> Desafio 18 <<<')
print('>>> Analisador de Nomes <<<')

nome = str(input('Digite seu nome completo: ')).strip()
separa = nome.split()

print('Verifique suas informações')

print('Seu nome completo é {}'.format(nome))
print('Seu nome em letras MAIÚSCULAS: {}'.format(nome.upper()))
print('Seu nome em letras minúsculas: {}'.format(nome.lower()))
print('Seu nome tem {} letras.'. format(len(nome)-nome.count(' ')))
#print(separa)
print('Seu primeiro nome é {} e tem {} letras.'.format(separa[0], len(separa[0])))


