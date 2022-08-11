soma = 0
contador = 0

for c in range (1,7):
    num = int(input('Digite o {}º número: '.format(c)))
    if num % 2 == 0:
        soma += num
        contador += 1
        
print('A soma do(s) {} número(s) pare(s) é {}'.format(contador, soma))
