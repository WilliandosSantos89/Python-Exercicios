print('Desafio 007')
print('Pintando a Parede')

larg = float(input('Largura da Parede: '))
alt = float(input('Altura da parede: '))
área = larg * alt

print('Sua área tem a dimensão de {:.2f} x {:.2f} e a sua área é de {:.1f}m²'.format(larg, alt, área))
tinta = área / 2
print('Para pintar essa parede você precisará de {} litros de tinta'.format(tinta))



