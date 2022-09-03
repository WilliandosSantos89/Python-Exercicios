print('>>> Desafio 024 <<<')
print('>>> Jogo da Adivinhação <<<')

from random import randint
from time import sleep


computador = randint(0,5) #PC pensando

print('Vou pensar em um número entre 0 e 5, tente adivinhar...')

print('-=-' * 20)

print('-=-' * 20)

jogador = int(input('Em que número eu pensei?')) #Jogador tentando adivinhar

print('Processando...')
sleep(3)

#Condições

if jogador == computador:
    print('Parabéns, você acertou!')
else:
    print('Que pena, você errou! Eu pensei no número {} e não no número {}'.format(computador, jogador))








