peso = float(input("Informe seu peso: "))
altura = float(input("Informe sua altura: "))
imc = peso / (altura * altura)

if imc > 18.5 and imc < 24.9:
  print("Seu IMC é {:.1f}".format(imc))
  print("Entre 18.5 e 24.9")
  print("Normal")

elif imc < 18.5:
  print("Seu IMC é {:.1f}".format(imc))
  print("Abaixo de 18.5")
  print("Abaixo do peso")
  print("Prucure um médico")

elif imc > 25.0 and imc < 29.9:
  print("Seu IMC é {:.1f}".format(imc))
  print("Entre 25.0 e 29.9")
  print("Sobrepeso")

elif imc > 30.0 and imc < 39.9:
  print("Seu IMC é {:.1f}".format(imc))
  print("Acima de 30.0")
  print("Obesidade")

else:
  print("Seu IMC é {:.1f}".format(imc))
  print("Acima de 40.0")
  print("Obesidade Grave")
  print("Procure um médico")



