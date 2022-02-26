print('>>> Desafio 025 <<<')
print('>>> Radar Eletrônico <<<')

from random import randint
from time import sleep
from colorama import Fore, Back, Style

print(20*'-=-')
print('Velocidade Máxima 80 KM')


velocidade = int(input('Qual sua velocidade? '))


print('Sua velocidade é de {} KM!'.format(velocidade))

if velocidade > 80:
    print(Fore.RED + 'Você foi multado. Você excedeu a velocidade máxima que é de 80 KM!')
    multa = (velocidade-80) * 7
    print('Você deve pagar uma multa de R${:.2f}!'.format(multa))
else:
    print('Tenha um bom dia.')





