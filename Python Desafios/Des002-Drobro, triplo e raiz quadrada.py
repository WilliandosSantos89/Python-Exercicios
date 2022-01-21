import math

print('=== Desafio 002 ===')
print('Dobro, triplo e raiz quadrada')

n1 = int(input('Digite um número: '))
dobro = n1 * 2
triplo = n1 * 3
raiz = n1**0.5 #pow (n1, (1/2)), n1*(1/2)

print('O dobro de {} é {}\no seu triplo é {} \ne a raiz quadrada é {:.2f}'.format(n1,dobro,triplo,raiz))


