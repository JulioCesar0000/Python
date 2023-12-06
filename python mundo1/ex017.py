import math
co = float(input('Comprimento do Cateto Oposto: '))
ca = float(input('Comprimento do Cateto Adjecente: '))
hi = math.hypot(co, ca)
print('A Hipotenusa vai medir {:.2f}'.format(hi))