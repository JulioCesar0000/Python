from random import randint
from time import sleep
computador = randint(1, 10)
print('Sou seu computador... ')
sleep(1)
print('Acabei de pensar em um número de 0 a 10.')
print('Será que você consegue adivinhar? Qual foi o número? ')
print('-=' *10)

acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é o seu palpite? '))
    palpites += 1
    sleep(0.3)
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez.')
        elif jogador > computador:
            print('Menos... Tente mais uma vez.')
print('PARABÉNS. Você acertou com {} TENTATIVAS!'.format(palpites))