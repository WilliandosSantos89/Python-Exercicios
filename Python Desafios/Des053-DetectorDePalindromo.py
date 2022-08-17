frase = str(input("Digite uma frase: ")).strip().upper()
palavras = frase.split()
juntas = ''.join(palavras)
inverso = ''
for letra in range(len(juntas) -1, -1, -1):
    inverso += juntas[letra]

print('O inverso de {} é {}'.format(juntas, inverso))

if inverso == juntas:
    print('Esse frase é um Palíndromo!')
else:
    print('Essa frase não é um Palíndromo')




