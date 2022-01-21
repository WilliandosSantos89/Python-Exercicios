print('Desafio 009')
print('>>> Reajuste Salarial <<<')

salário = float(input('Salário Atual: R$'))
novo = salário + (salário * 15/100)

print('O salário no valor de R$ {:.2f}, com um aumento de 15% ficará no valor de R$ {:.2f}'.format(salário, novo))