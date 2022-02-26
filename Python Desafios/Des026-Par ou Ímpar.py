print('>>> Desafio 026 <<<')
print('>>> Par ou Ímpar <<<')

número = int(input('Digite um número: '))

resultado = número % 2 #Resto do divisão

if resultado == 0:
    print('O número {} é PAR!'.format(número))
else:
    print('O número {} é ÍMPAR'.format(número))