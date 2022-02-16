print('>>> Desafio 021 <<<')
print('>>> Procurando uma string dentro de outra <<<')

nome = str(input('Digite seu nome completo: ')).strip()
print('Seu nome possui Silva: {}'.format(nome[:5].lower() == 'silva'))
#(cidade[:5].upper() == 'SANTO')

