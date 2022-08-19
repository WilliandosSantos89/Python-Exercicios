
somaIdade = 0
mediaIdade = 0
maiorIdadeHomem = 0
nomeVelho = ''
qtdMulher20 = 0
nomeMulher = ''


for pessoa in range (1,5):
    print('==='*20)

    print('Dados da {}ª pessoa'.format(pessoa))
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M / F]: '))

    somaIdade += idade

    if pessoa == 1 and sexo == 'Mm':
        maiorIdadeHomem = idade
        nomeVelho = nome

    
    if sexo in 'Mm' and idade > maiorIdadeHomem:
        maiorIdadeHomem = idade
        nomeVelho = nome

    if sexo in 'Ff' and idade < 20:
        qtdMulher20 += 1
        nomeMulher = nome

        

    print('==='*20)
    print('\n')

mediaIdade = somaIdade / 4

print('A média da idade do grupo é {}'.format(mediaIdade))
print('O homem mais velho tem {} anos e se chama {}'.format(maiorIdadeHomem, nomeVelho))
print('Temos {} nulher com menos de 20 anos e ela se chama {}'.format(qtdMulher20, nomeMulher))



   