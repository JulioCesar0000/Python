larg = float(input('Largura de uma parede: '))
alt = float(input('Altura dessa parede: '))
area = larg * alt
print('a sua parede tem a dimensão de {}x{} e sua área é de {}m2'.format(larg, alt, area))
tinta = area / 2
print('Para pintar está parede você precisará de {}l de tinta.'.format(tinta))