print('Exercício 006')
print('Sistemas de descontos e acréscimos')
#Criar um programa que dá desconto nas compras à vista e acréscimos
#nas compras à prazo.

valor = float(input('Valor do produto: R$'))
desconto = valor - (valor * 5/100)
acréscimo = valor + (valor * 5/100)

print('Valor nas compras à vista: R$ {:.2f}'.format(desconto))
print('Valor nas compras à prazo: R$ {:.2f}'.format(acréscimo))

