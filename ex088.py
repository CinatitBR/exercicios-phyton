from random import randint
from time import sleep
print('=' * 32)
print('GERADOR DE NÚMEROS - MEGA SENA')
print('=' * 32)
n = int(input('Quantos jogos você irá jogar? '))
jogos = [[] for i in range(n)]  # Cria os vetores internos
for v in range(len(jogos)):  # Representa cada vetor interno de 'jogos'
    for i in range(0, 6):  # Índice do vetor interno
        jogos[v].append(randint(1, 60))  # Sorteia 6 números
        if i >= 1:
            while jogos[v][i] == jogos[v][i - 1]:  # Enquanto houverem números iguais, número repetido será substituído
                jogos[v][i-1] = randint(1, 60)
print('-=' * 30)
for i, v in enumerate(jogos):  # Exibe todos os vetores
    print(f'{i+1}º JOGO: {v}')
    sleep(0.6)
print('-=' * 30)