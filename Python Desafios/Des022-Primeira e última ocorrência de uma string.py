print('>>> Desafio 022 <<<')
print('>>> Primeira e última ocorrência de uma string <<<')

frase = str(input('Digite uma frase para ser analisada: ')).upper().strip()

print('Nessa frase, a letra A aparece {} vezes!'.format(frase.count('A')))
print('Nessa frase, a letra A aparece pela primeira vez na posição {}!'.format(frase.find('A')+1))
print('Nessa frase, a letra A aparece por último na posição {}!'.format(frase.rfind('A')+1))
