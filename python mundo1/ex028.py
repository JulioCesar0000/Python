from random import randint
from time import sleep
computador = randint(0,10)
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 10, tente advinhar...')
print('-=-' * 20)
jogador = int(input('Em que número pensei? '))#jogador tenta advinhar
print('PROCESSANDO...')
sleep(4)
if jogador == computador:
    print('PARABÉNS, vôce conseguiu me vencer! S2.')
else:
    print('GANHEI! Eu pensei no número {} e não no {}'.format(computador, jogador))

