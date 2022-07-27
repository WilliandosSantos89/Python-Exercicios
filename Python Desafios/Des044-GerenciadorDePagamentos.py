preço = float(input("Informe o valor do produto: R$ "))
Avista = preço - (preço * 10/100)
AvistaCartao = preço - (preço * 5/100)
AvistaParcelado = preço + (preço * 20/100)

print('''Informe a forma de pagamento: 
[ 1 ] À vista em dinheiro
[ 2 ] À vista no cartão
[ 3 ] Em até 2x no cartão
[ 4 ] Em 3x ou mais no cartão''')

opção = int(input("Escolha uma opção: "))

if opção == 1:
  print("Você tem 10% de desconto.")
  print("O valor do produto ficará em R$ {:.2f}.".format(Avista))

elif opção == 2:
  print("Você tem 5% de desconto.")
  print("O valor do produto ficará em R$ {:.2f}.".format(AvistaCartao))

if opção == 3:
  print("Você não tem desconto.")
  parcela = preço / 2
  print("O valor do produto ficará em R$ {:.2f}".format(preço))
  print("A parcela ficará em R$ {:.2f}.".format(parcela))

if opção == 4:
  print("Você não tem desconto.")

  parcela3 = preço / 3
  parcela4 = preço / 4
  parcela5 = preço / 5
  parcela6 = preço / 6
  
  print('''Informe a quantidade de parcelas: 
  [ 3 ] 3x de R$ {:.2f}
  [ 4 ] 4x de R${:.2f}
  [ 5 ] 5x de R${:.2f}
  [ 6 ] 6x de R$ {:.2f}'''.format(parcela3, parcela4, parcela5, parcela6))

  opção = int(input("Escolha uma opção: "))

  if opção == 3:
    print("A parcela ficará em 3x de R$ {:.2f}.".format(parcela3))

  if opção == 4:
    print("A parcela ficará em 4x de R$ {:.2f}.".format(parcela4))
  
  if opção == 5:
    print("A parcela ficará em 5x de R$ {:.2f}.".format(parcela5))

  if opção == 6:
    print("A parcela ficará em 6x de R$ {:.2f}.".format(parcela6))

print("Obrigado pela compra.")
print("Volte sempre!")