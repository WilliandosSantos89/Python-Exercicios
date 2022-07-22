valorCasa = float(input("Qual o valor da casa? "))
salarioComprador = float(input("Qual o seu salário? "))
qtdAnos = int(input("Em quantos anos você deseja pagar? "))
prestacao = valorCasa / (qtdAnos * 12)
minimo = salarioComprador * 30/100


print ("Para comprar um casa de  R$ {:.2f} em {} anos". format(valorCasa, qtdAnos))
print ("Você pagará uma prestação de R$ {:.2f}.".format(prestacao))

if prestacao <= minimo:
  print("Financimento Aprovado!")

else:
  print("Finacimento Negado!")
