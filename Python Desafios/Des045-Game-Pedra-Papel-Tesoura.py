import random
import time


opções = ['Pedra', 'Papel', 'Tesoura']
computador = random.randint(0,2)

print('''Faça sua jogada:
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura''')

jogador = int(input("Qual é a sua jogada? "))

print("PEDRA \U0001F91C") 
time.sleep(1.5)

print("PAPEL \U0001270B")
time.sleep(1.5)

print("TESOURA \U0001FE0F")

print('***---***'*5)

print("Computador jogou {}.".format(opções[computador]))
print("Jogador jogou {}.".format(opções[jogador]))

print('***---***'*5)

if computador == 0: #computador Pedra

  if jogador == 0:
    print("Empate!")

  elif jogador == 1:
    print("Jogador Vence!")

  elif jogador == 2:
    print("Computador Vence!")


elif computador == 1: #computador Papel

  if jogador == 0:
    print("Computador Vence!")
  
  elif jogador == 1:
    print("Empate!")

  elif jogador == 2:
    print("Jogador Vence!")


elif computador == 2: #computador Tesoura
  if jogador == 0:
    print("Computador Vence!")
  
  elif jogador == 1:
    print("Jogador Vence!")

  elif jogador == 2:
    print("Empate!")


else: 
    print("Jogada Errada")

  