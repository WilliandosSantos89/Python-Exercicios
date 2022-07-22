num = int(input("Digite um número inteiro: "))

print('''Escolha uma das opções para conversão:
[ 1 ]Converter para Binário
[ 2 ]Converter para Ocatal
[ 3 ]Converter para Hexadecimal''')

opcao = int(input("Sua opção: "))

if opcao == 1:
  print("{} convertido para Binário é {}.".format(num, bin(num)[2:]))

elif opcao == 2:
  print("{} convertidoem Octal é {}.".format(num, oct(num)[2:]))

elif opcao == 3:
  print("{} convertido em Hexadecimal é {}.".format(num, hex(num)[2:]))

else:
  print("Opção inválida, tente novamente!")