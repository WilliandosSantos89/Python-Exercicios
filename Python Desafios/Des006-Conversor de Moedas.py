print('Desafio 006')
print('Conversor de Moedasss')
real = float(input('Quanto de dinheiro você tem na cartera? R$'))
dolar = real / 5.39
euro = real / 6.11
print('Com R$ {:.2f}, você pode comprar US$ {:.2f} ou £ {:.2f}'.format(real, dolar, euro))

