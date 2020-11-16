from random import randint
v = 0
print('-=-' * 10)
print('        PAR OU ÍMPAR')
print('-=-' * 10)
while True:
    computador = randint(0, 10)
    user = int(input('Digite um número: '))
    soma = computador + user
    op = str(input('Par ou Ímpar [P/I]? ')).strip().upper()[0]
    while op not in 'PI':
        op = str(input('Par ou Ímpar [P/I]? ')).strip().upper()[0]
    if op in 'P' and soma % 2 == 0:  # Se o jogador GANHAR (PAR)
        print('-' * 30)
        print(f'Você escolheu {user} e o computador {computador}, a soma é: {soma}. Um número PAR.')
        print('Você GANHOU! Recomeçando...')
        print('-' * 30)
        v += 1
    elif op in 'I' and soma % 2 != 0:  # Se o jogador GANHAR (IMPAR)
        print('-' * 30)
        print(f'Você escolheu {user} e o computador {computador}, a soma é: {soma}. Um número IMPAR...')
        print('Você GANHOU! Recomeçando...')
        print('-' * 30)
        v += 1
    elif op in 'P':  # Se o jogador PERDER (PAR)
        print('*' * 43)
        print(f'Você escolheu {user} e o computador {computador}, a soma é: {soma}. Um número IMPAR.')
        print(f'Você PERDEU, com {v} vitórias consecutivas.')
        print('*' * 43)
        break
    elif op in 'I':  # Se o jogador PERDER (IMPAR)
        print('*' * 43)
        print(f'Você escolheu {user} e o computador {computador}, a soma é: {soma}. Um número PAR.')
        print(f'Você PERDEU, e teve {v} vitórias consecutivas.')
        print('*' * 43)
        break
