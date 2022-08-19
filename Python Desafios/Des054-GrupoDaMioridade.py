from datetime import date 


contador = 0
anoAtual = date.today().year
totalMaior = 0
totalMenor = 0

for pessoa in range (1,8):
    Nascimento = int(input('Em que ano a {}ª pessoa nasceu?: '.format(pessoa)))
    idade = anoAtual - Nascimento
    
    if idade >= 18:
        totalMaior += 1
    else: 
        totalMenor += 1

print('Ao todo tivemos {} pessoas maiores e {} manores.'.format(totalMaior, totalMenor))

