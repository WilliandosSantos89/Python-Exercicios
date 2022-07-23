nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

if media < 5.0:
  print("Nos vemos ano que vem; sua média foi {}.".format(media))
  print("Reprovado!")


elif media > 5 and media < 6.9:
  print("Você pode melhorar, sua média foi {}".format(media))
  print("Recuperação!")


elif media > 7:
  print("Parabéns, sua média foi {}.".format(media))
  print("Aprovado!")
