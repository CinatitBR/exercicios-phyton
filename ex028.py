from random import randint
from time import sleep

nPc = randint(0, 5)  # Computador escolhe um número
print('-=-' * 20)
print('Irei escolher um número de 0 a 5. Tente advinhar qual é...')
print('-=-' * 20)
nUser = int(input('Em que número você acha que eu pensei? '))  #Jogador tenta advinhar
print(5 * '*', 'PROCESSANDO...', 5 * '*')
sleep(2.5)

if nUser == nPc:
    print(f'Você disse {nUser}, eu escolhi o {nPc}. PARABÉNS, você GANHOU!')
else:
    print(f'EU GANHEI!!! Você disse {nUser}, eu escolhi {nPc}!')
