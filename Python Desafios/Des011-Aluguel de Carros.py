print('Desafio 011')
print('>>> Aluguel de Carros <<<')

dias = int(input('Quantos dias ficou com o carro? '))
km = float(input('Quantos km foram rodados? '))
valor = (dias*60) + (km*0.15)

print('O total a pagar é R$ {:.2f}.'.format(valor))

