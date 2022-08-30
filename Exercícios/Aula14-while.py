#contador = 1

'''while contador < 10:
    print(contador)
    contador += 1
print('fim')'''

#r = 1

'''while r != 0:
    r = int(input('digite um número:'))
print('fim')'''

#r = 'S'

'''while r == 'S':
    n = int(input('digite um valor:'))
    r = str(input('quer continuar? [S/N]')).upper()
print('fim')'''




n = 1
par = impar = 0

while n != 0:
    n = int(input('Dgite um número: '))
    if n != 0:
        if n % 2  == 0:
            par += 1
        else:
            impar += 1
print('Você digitou {} número(s) par(es) e {} numero(s) impar(es).'.format(par, impar))




