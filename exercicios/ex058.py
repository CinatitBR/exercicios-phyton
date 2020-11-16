from random import randint
from time import sleep

print('\033[1;31m-=-\033[m' * 8, '\033[1;33mJOGO DA ADIVINHAÇÃO\033[m', '\033[1;31m-=-\033[m' * 8)
print('Irei pensar em um número entre 0 e 10. Tente advinhar qual é!')
tentativas = 1
pc = randint(0, 10)
usuario = int(input('Em que número você acha que pensei? '))

while usuario != pc:
    print('\033[1;34mProcessando...\033[m')
    sleep(0.3)
    if usuario < pc:
        usuario = int(input('\033[1;31mErrou, o número que pensei é maior! Tente novamente\033[m: '))
    else:
        usuario = int(input('\033[1;31mErrou, o número que pensei é menor! Tente novamente\033[m: '))
    tentativas += 1

sleep(0.3)
print('\033[1;34mProcessando...\033[m')

print(f'\033[1;32mAcertou!\033[m')
print(f'Você teve que tentar {tentativas} vezes antes de conseguir ganhar de mim...')