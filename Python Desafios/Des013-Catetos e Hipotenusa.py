import math
print('Desafio 013')
print('>>> Catetos e Hipotenusa <<<')

cateto_oposto = float(input('Digite o cateto oposto: '))
cateto_adjascente = float(input("Digite o cateto adjascente: "))
#hipotenusa = (cateto_oposto **2 + cateto_adjascente **2) ** (1/2)
hipotenusa = math.hypot(cateto_oposto,cateto_adjascente)

print('A hipotenusa vai medir {:.2f}.'.format(hipotenusa))
