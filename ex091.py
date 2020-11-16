from random import randint
from time import sleep

jogadores = {
    'jogador1': randint(1, 6),
    'jogador2': randint(1, 6),
    'jogador3': randint(1, 6),
    'jogador4': randint(1, 6)
}
print('-=' * 7, 'JOGANDO DADOS', '-=' * 7)
for key in jogadores:
    print(f'{key}: {jogadores[key]}')
    sleep(1)
print('-=' * 22)
for i, key in enumerate(sorted(jogadores, key=jogadores.get, reverse=True)):  # Organizo em ordem decrscente, e dou enumrate para usar o 'i'
    print(f'{i+1}º lugar: {key} tirou {jogadores[key]}')


