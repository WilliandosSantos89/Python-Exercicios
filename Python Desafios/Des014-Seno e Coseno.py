print('>>> Desafio 014 <<<')
print('>>> Seno e Coseno <<<')

import math

ângulo = float(input('Dgite um ângulo: '))

seno = math.sin(math.radians(ângulo))
print('O ângulo de {} tem o SENO de {:.2}.'.format(ângulo, seno))

coseno = math.cos(math.radians(ângulo))
print('O ângulo de {} tem o COSENO de {:.2f}.'.format(ângulo, coseno))

tangente = math.tan(math.radians(ângulo))
print('O ângulo de {} tem a TANGENTE de {:.2f}.'.format(ângulo, tangente))




