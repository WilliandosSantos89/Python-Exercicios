import random



opções = ['Pedra', 'Papel', 'Tesoura']
computador = random.randint(0,2)

print('''Faça sua jogada:
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura''')

jogador = int(input("Qual é a sua jogada? "))

print("JO")
print("KEN")
print("PÔ!!!")

print('***---***'*5)

print("Computador jogou {}.".format(opções[computador]))
print("Jogador jogou {}.".format(opções[jogador]))

print('***---***'*5)

if computador == 0: #computador Pedra

  if jogador == 0:
    print("Empate!")

  elif jogador == 1:
    print("Jogado Vence!")

  elif jogador == 2:
    print("Computador Vence!")

  else:
    print("Joada Errada")

elif computador == 1: #computador Papel

  if jogador == 0:
    print("Computador Vence!")
  
  elif jogador == 1:
    print("Empate!")

  elif jogador == 2:
    print("Jogador Vence!")

  else: 
    print("Joada Errada")

elif computador == 2: #computador Tesoura
  if jogador == 0:
    print("Computador Vence!")
  
  elif jogador == 1:
    print("Jogador Vence!")

  elif jogador == 2:
    print("Empate!")

  else: 
    print("Joada Errada")

  