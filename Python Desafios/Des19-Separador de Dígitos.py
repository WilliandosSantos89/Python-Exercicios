print('>>> Desafio 019 <<<')
print('>>> Separador de Dígitos <<<')

número = int(input('Digite um número: '))


unidade = número // 1 % 10
dezena = número // 10 % 10
centena = número // 100 % 10
milhar = número // 1000 % 10

print('Analizando o número {}...'.format(número))

print('Unidade: {} .'.format(unidade))
print('Dezena: {}.'.format(dezena))
print('Centena: {}.'.format(centena))
print('Milhar: {}.'.format(milhar))