from datetime import date

anoAtual = date.today().year

anoNascimento = int(input("Informe seu ano de nascimento: "))

idade = anoAtual - anoNascimento


if idade ==1:
  print("Você tem apenas 1 ano de idade.")

elif idade <= 9: 

  print("Você tem {} anos, sua categoria é a Mirim.".format(idade))
  

elif idade <= 14:
  print("Você tem {} anos, sua categoria é a Infantil". format(idade))

elif idade <= 19:
  print("Você tem {} anos, sua categoria é a Júnior." .format(idade))

elif idade <=20:
  print("Você tem {} anos, sua categoria é a Sênior.".format(idade))

else:
  print("Você tem {} anos, sua categoria é a Master.".format(idade))