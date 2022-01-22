print('Exercício 007')
print('Tabela de Taxas')
#Criar uma tabela com taxas de cartões de crédito

valor = float(input('Valor a ser cobrado: R$ '))
qtdparcela = int(input('Em quantas vezes? '))

acréscimo = valor * 10/100
preço_final = valor + (acréscimo*qtdparcela)

print('Valor do Acréscimo: R$ {:.2f}'.format(acréscimo))
print('Em {} vezes o valor do produto ficará em R$ {:.2f}'.format(qtdparcela,preço_final))

print('--'*30)






