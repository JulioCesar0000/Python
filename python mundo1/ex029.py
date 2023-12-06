print('Olá, Vôce está em uma via que só permite 80km/h')
from time import sleep
velocidade = float(input('Qual é a velociade do carro? '))
if velocidade > 80:
    sleep(3)
    print('MULTADO! Vôce excedeu o limite permitido que é 80km/h')
    multa = (velocidade-80) * 7
    print('Vôce foi multado, deve pegar a quantia de {:.2f}!'.format(multa))
print('Tenha um Bom Dia, dirija com segurança! ')