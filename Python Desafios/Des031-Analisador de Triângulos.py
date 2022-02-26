print('>>> Desafio 032 <<<')
print('>>> Analisador de Triângulos <<<')

print('-=-' * 20)

seg1 = float(input('Digite o Primeiro seguimento: '))
seg2 = float(input('Digite o Segundo seguimento:'))
seg3 = float(input('Digite o Terceiro seguimento:'))

if seg1 < seg2 + seg3 and seg2 < seg1 + seg3 and seg3 < seg1 + seg2:
    print('Esses seguimentos formam um triângulo!')
else:
    print('Esses seguimentos não formam um triângulo! ')
