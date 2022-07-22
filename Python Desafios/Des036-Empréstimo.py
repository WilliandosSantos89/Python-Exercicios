valorCasa = float(input("Qual o valor da casa? "))
salarioComprador = float(input("Qual o seu salário?"))
qtdAnos = int(input("Em quantos anos você deseja pagar?"))

if (valorCasa / qtdAnos) - salarioComprador:
  print("Empréstimo Aprovado!")

else:
  print("Empréstimo aprovado")
