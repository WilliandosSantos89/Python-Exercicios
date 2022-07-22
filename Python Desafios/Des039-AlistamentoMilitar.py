from datetime import date

anoAtual = date.today().year

anoNascimento = int(input("Digite seu ano de nascimento com 4 dígitos: "))

print('''Informe seu sexo:
[ 1 ] Masculino
[ 2 ] Feminino''')

sexo = int(input("Informe seu sexo: "))

if sexo == 2:
  print("Você não precisa se alistar por ser mulher!")

else:

  idade = anoAtual - anoNascimento

  print("Quem nasceu em {}, tem {} anos em {}.".format(anoNascimento, idade, anoAtual))

  if idade == 18:
    print("Você tem {} anos, ja tem que se alistar!". format(idade))

  elif idade < 18:
    saldo = 18 - idade
    print("Ainda faltam {} anos para você se alistar.".format(saldo))

    ano = anoAtual + saldo
    print("Seu alistamento será em {}".format(ano))
    

  elif anoNascimento > idade:
    saldo = idade - 18
    print("Já passaram {} anos do prazo do seu alistamento.".format(saldo))

    ano = anoAtual - saldo
    print("Você deveria ter se alistado em {}.".format(ano))
    