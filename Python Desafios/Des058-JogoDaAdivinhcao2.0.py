from random import randint
from time import sleep



computador = randint(0,10)

print ('Vou pensar em um número de 0 10, tente adivinhar qual é:')

acertou = False
palpites = 0

while not acertou:
    jogador = int(input('Qual o seu palpite? '))

    palpites += 1

    if jogador == computador:
        acertou = True

    else:
        if jogador < computador:
            print('Mais...')
        elif jogador > computador:
            print('Menos...')

print("Acertou na {}ª tentativa!".format(palpites))

finalização